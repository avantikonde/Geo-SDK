/**
 * Publish Remaining Real-World Incidents to Geo Knowledge Graph
 * 
 * Reads `data/incidents.json` at runtime and publishes 15 verified AI failure case studies.
 * Target Space: fb47f7907b4cc91be446bbf9fb51ccad
 */

import fs from 'fs';
import path from 'path';
import {
  Graph,
  createGeoClient,
  createGeoWalletClient,
  GeoTestnetConfig,
  type Op,
} from '@geoprotocol/geo-sdk';
import { privateKeyToAccount } from 'viem/accounts';

const DRY_RUN = process.env.DRY_RUN !== 'false';

const rawKey = process.env.GEO_PRIVATE_KEY ?? process.env.PK_SW;
const privateKey = rawKey
  ? ((rawKey.startsWith('0x') ? rawKey : `0x${rawKey}`) as `0x${string}`)
  : undefined;

const SPACE_ID = process.env.DEMO_SPACE_ID ?? 'fb47f7907b4cc91be446bbf9fb51ccad';

// Ontology Type IDs
export const OntologyTypes = {
  INCIDENT: 'a0010001000000000000000000000001',
  AGENT: 'a0010001000000000000000000000002',
  FAILURE_MODE: 'a0010001000000000000000000000003',
  MITIGATION: 'a0010001000000000000000000000004',
  FINANCIAL_LOSS: 'a0010001000000000000000000000005',
};

// Ontology Property IDs
export const OntologyProperties = {
  DATE: 'b0010001000000000000000000000001',
  SEVERITY: 'b0010001000000000000000000000002',
  SOURCE_EVIDENCE_LINK: 'b0010001000000000000000000000003',
  AGENT_NAME: 'b0010001000000000000000000000004',
  ARCHITECTURE: 'b0010001000000000000000000000005',
  LOSS_AMOUNT: 'b0010001000000000000000000000006',
  CURRENCY: 'b0010001000000000000000000000007',
  MITIGATION_STRATEGY: 'b0010001000000000000000000000008',
};

// Ontology Relation IDs
export const OntologyRelations = {
  INVOLVES_AGENT: 'c0010001000000000000000000000001',
  EXHIBITS: 'c0010001000000000000000000000002',
  RESULTED_IN: 'c0010001000000000000000000000003',
  MITIGATED_BY: 'c0010001000000000000000000000004',
};

interface IncidentRecord {
  id: string;
  name: string;
  description: string;
  date: string;
  severity: string;
  sourceName: string;
  sourceEvidenceLink: string;
  agent: {
    name: string;
    architecture: string;
    description: string;
  };
  failureMode: {
    name: string;
    description: string;
  };
  mitigation: {
    name: string;
    strategy: string;
    description: string;
  };
  financialLoss: {
    amount: number;
    currency: string;
    description: string;
  };
}

const dataPath = path.resolve(process.cwd(), 'data/incidents.json');
if (!fs.existsSync(dataPath)) {
  throw new Error(`Dataset not found at ${dataPath}. Please ensure data/incidents.json exists.`);
}

const incidents: IncidentRecord[] = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
console.log(`Loaded ${incidents.length} incident records from data/incidents.json.`);

const geo = createGeoClient({ network: GeoTestnetConfig });
const allOps: Op[] = [];
const createdEntities: { id: string; name: string; type: string }[] = [];
const createdRelations: { from: string; relation: string; to: string }[] = [];

function createTypedEntity(params: Parameters<typeof Graph.createEntity>[0]) {
  if (!params.types || params.types.length === 0) {
    throw new Error(`[Gate 4 Error] Entity "${params.name ?? '(unnamed)'}" must carry at least one type.`);
  }
  const result = Graph.createEntity(params);
  createdEntities.push({
    id: result.id,
    name: params.name ?? '(unnamed)',
    type: params.types[0],
  });
  return result;
}

// Build graph nodes and edges for each incident
for (let i = 0; i < incidents.length; i++) {
  const inc = incidents[i];

  // 1. Agent Entity
  const agent = createTypedEntity({
    name: inc.agent.name,
    description: inc.agent.description,
    types: [OntologyTypes.AGENT],
    values: [
      { property: OntologyProperties.AGENT_NAME, type: 'text', value: inc.agent.name },
      { property: OntologyProperties.ARCHITECTURE, type: 'text', value: inc.agent.architecture },
    ],
  });
  allOps.push(...agent.ops);

  // 2. Failure Mode Entity
  const failureMode = createTypedEntity({
    name: inc.failureMode.name,
    description: inc.failureMode.description,
    types: [OntologyTypes.FAILURE_MODE],
    values: [],
  });
  allOps.push(...failureMode.ops);

  // 3. Mitigation Entity
  const mitigation = createTypedEntity({
    name: inc.mitigation.name,
    description: inc.mitigation.description,
    types: [OntologyTypes.MITIGATION],
    values: [
      { property: OntologyProperties.MITIGATION_STRATEGY, type: 'text', value: inc.mitigation.strategy },
    ],
  });
  allOps.push(...mitigation.ops);

  // 4. Financial Loss Entity
  const loss = createTypedEntity({
    name: `${inc.name} Financial Loss`,
    description: inc.financialLoss.description,
    types: [OntologyTypes.FINANCIAL_LOSS],
    values: [
      { property: OntologyProperties.LOSS_AMOUNT, type: 'float', value: inc.financialLoss.amount },
      { property: OntologyProperties.CURRENCY, type: 'text', value: inc.financialLoss.currency },
    ],
  });
  allOps.push(...loss.ops);

  // 5. Incident Entity
  const incident = createTypedEntity({
    name: inc.name,
    description: inc.description,
    types: [OntologyTypes.INCIDENT],
    values: [
      { property: OntologyProperties.DATE, type: 'text', value: inc.date },
      { property: OntologyProperties.SEVERITY, type: 'text', value: inc.severity },
      { property: OntologyProperties.SOURCE_EVIDENCE_LINK, type: 'text', value: inc.sourceEvidenceLink },
      { property: OntologyRelations.INVOLVES_AGENT, type: 'text', value: inc.agent.name },
      { property: OntologyRelations.EXHIBITS, type: 'text', value: inc.failureMode.name },
      {
        property: OntologyRelations.RESULTED_IN,
        type: 'text',
        value: `${inc.financialLoss.description} ($${inc.financialLoss.amount.toLocaleString()} ${inc.financialLoss.currency})`,
      },
    ],
  });
  allOps.push(...incident.ops);

  // Relations:
  // Incident -> involves agent -> Agent
  const relInvolves = Graph.createRelation({
    fromEntity: incident.id,
    toEntity: agent.id,
    type: OntologyRelations.INVOLVES_AGENT,
  });
  allOps.push(...relInvolves.ops);
  createdRelations.push({ from: inc.name, relation: 'involves agent', to: inc.agent.name });

  // Incident -> exhibits -> Failure Mode
  const relExhibits = Graph.createRelation({
    fromEntity: incident.id,
    toEntity: failureMode.id,
    type: OntologyRelations.EXHIBITS,
  });
  allOps.push(...relExhibits.ops);
  createdRelations.push({ from: inc.name, relation: 'exhibits', to: inc.failureMode.name });

  // Incident -> resulted in -> Financial Loss
  const relResulted = Graph.createRelation({
    fromEntity: incident.id,
    toEntity: loss.id,
    type: OntologyRelations.RESULTED_IN,
  });
  allOps.push(...relResulted.ops);
  createdRelations.push({ from: inc.name, relation: 'resulted in', to: `${inc.financialLoss.amount} ${inc.financialLoss.currency}` });

  // Failure Mode -> mitigated by -> Mitigation
  const relMitigated = Graph.createRelation({
    fromEntity: failureMode.id,
    toEntity: mitigation.id,
    type: OntologyRelations.MITIGATED_BY,
  });
  allOps.push(...relMitigated.ops);
  createdRelations.push({ from: inc.failureMode.name, relation: 'mitigated by', to: inc.mitigation.name });
}

console.log(`\n======================================================`);
console.log(`Incidents Processed: ${incidents.length}`);
console.log(`Entities Registered: ${createdEntities.length}`);
console.log(`Relations Registered: ${createdRelations.length}`);
console.log(`Total Operations Generated: ${allOps.length}`);
console.log(`Target Space ID: ${SPACE_ID}`);
console.log(`======================================================\n`);

if (DRY_RUN) {
  console.log('[DRY RUN COMPLETE] Set DRY_RUN=false to publish to Geo Testnet.');
} else {
  if (!privateKey) {
    throw new Error('Cannot publish: GEO_PRIVATE_KEY environment variable is missing.');
  }

  console.log('[PUBLISHING 15 INCIDENTS TO GEO TESTNET]...');
  const wallet = await createGeoWalletClient({
    signer: privateKeyToAccount(privateKey),
    network: GeoTestnetConfig,
  });

  const { to, calldata, editId } = await geo.personalSpaces.publishEdit({
    name: 'Publish 15 Real-World Autonomous AI Incidents Catalog',
    spaceId: SPACE_ID,
    ops: allOps,
    author: SPACE_ID,
  });

  const tx = await wallet.sendTransaction({
    account: wallet.account,
    to,
    data: calldata,
  });

  console.log(`\n======================================================`);
  console.log(`Batch Publish Successful! 🎉`);
  console.log(`Edit ID: ${editId}`);
  console.log(`Transaction Hash: ${tx}`);
  console.log(`Explorer Link: https://www.geobrowser.io/space/${SPACE_ID}`);
  console.log(`======================================================\n`);
}
