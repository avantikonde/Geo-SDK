/**
 * PocketOS Autonomous AI Agent Database Deletion Incident (Incident #1469)
 * 
 * Publication Script for Geo Knowledge Graph (GRC-20)
 * Reference: https://incidentdatabase.ai/cite/1469/
 */

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

const geo = createGeoClient({ network: GeoTestnetConfig });
const allOps: Op[] = [];

// Existing Ontology IDs from ai-incident-schema.ts
export const OntologyTypes = {
  INCIDENT: 'a0010001000000000000000000000001',
  AGENT: 'a0010001000000000000000000000002',
  FAILURE_MODE: 'a0010001000000000000000000000003',
  MITIGATION: 'a0010001000000000000000000000004',
  FINANCIAL_LOSS: 'a0010001000000000000000000000005',
};

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

export const OntologyRelations = {
  INVOLVES_AGENT: 'c0010001000000000000000000000001',
  EXHIBITS: 'c0010001000000000000000000000002',
  RESULTED_IN: 'c0010001000000000000000000000003',
  MITIGATED_BY: 'c0010001000000000000000000000004',
};

const registeredEntities: { id: string; name: string; types: string[] }[] = [];

function createTypedEntity(params: Parameters<typeof Graph.createEntity>[0]) {
  if (!params.types || params.types.length === 0) {
    throw new Error(`[Ontology Error] Entity "${params.name ?? '(unnamed)'}" must carry at least one type.`);
  }
  const result = Graph.createEntity(params);
  registeredEntities.push({
    id: result.id,
    name: params.name ?? '(unnamed)',
    types: params.types,
  });
  return result;
}

console.log('--- Step 1: Instantiating PocketOS Agent ---');
const agentEntity = createTypedEntity({
  name: 'Cursor AI Coding Agent (Claude Opus 4.6)',
  description: 'Autonomous software engineering agent embedded in Cursor IDE with shell execution and GraphQL tool calling capabilities.',
  types: [OntologyTypes.AGENT],
  values: [
    { property: OntologyProperties.AGENT_NAME, type: 'text', value: 'Cursor AI Coding Agent (Claude Opus 4.6)' },
    { property: OntologyProperties.ARCHITECTURE, type: 'text', value: 'Autonomous IDE Agent with Railway GraphQL API Tool Calling' },
  ],
});
allOps.push(...agentEntity.ops);

console.log('--- Step 2: Instantiating Failure Mode ---');
const failureModeEntity = createTypedEntity({
  name: 'Unconstrained Infrastructure Mutation & Permissive Token Misuse',
  description: 'Autonomous agent encountered staging credential mismatch, scanned repository for ambient API tokens, and executed unverified volume deletion mutation.',
  types: [OntologyTypes.FAILURE_MODE],
  values: [],
});
allOps.push(...failureModeEntity.ops);

console.log('--- Step 3: Instantiating Mitigation ---');
const mitigationEntity = createTypedEntity({
  name: 'Independent Backup Plane & Runtime Boundary Enforcement',
  description: 'Enforce Policy-as-Code requiring out-of-band human sign-off on non-idempotent operations, with logically air-gapped immutable backup storage.',
  types: [OntologyTypes.MITIGATION],
  values: [
    { property: OntologyProperties.MITIGATION_STRATEGY, type: 'text', value: 'Policy-as-Code Boundary & Immutable Air-Gapped Backups' },
  ],
});
allOps.push(...mitigationEntity.ops);

console.log('--- Step 4: Instantiating Financial Loss ---');
const financialLossEntity = createTypedEntity({
  name: 'PocketOS Production Outage & Data Reconstruction Loss',
  description: 'Loss of critical car rental bookings and manual data reconstruction spanning Stripe, calendar, and email sources.',
  types: [OntologyTypes.FINANCIAL_LOSS],
  values: [
    { property: OntologyProperties.LOSS_AMOUNT, type: 'float', value: 1450000 },
    { property: OntologyProperties.CURRENCY, type: 'text', value: 'USD' },
  ],
});
allOps.push(...financialLossEntity.ops);

console.log('--- Step 5: Instantiating Incident Entity (With all Table Values) ---');
const incidentEntity = createTypedEntity({
  name: 'PocketOS Production Database & Volume Deletion Incident',
  description: 'Autonomous AI coding agent in Cursor IDE deleted live production database and backup volumes during staging maintenance (AI Incident Database #1469).',
  types: [OntologyTypes.INCIDENT],
  values: [
    { property: OntologyProperties.DATE, type: 'text', value: '2026-04-25' },
    { property: OntologyProperties.SEVERITY, type: 'text', value: 'Critical' },
    {
      property: OntologyProperties.SOURCE_EVIDENCE_LINK,
      type: 'text',
      value: 'https://incidentdatabase.ai/cite/1469/',
    },
    // Populate relation properties as readable text values for the GeoBrowser card table:
    {
      property: OntologyRelations.INVOLVES_AGENT,
      type: 'text',
      value: 'Cursor AI Coding Agent (Claude Opus 4.6)',
    },
    {
      property: OntologyRelations.EXHIBITS,
      type: 'text',
      value: 'Unconstrained Infrastructure Mutation & Permissive Token Misuse',
    },
    {
      property: OntologyRelations.RESULTED_IN,
      type: 'text',
      value: 'PocketOS Production Outage & Data Reconstruction Loss ($1.45M)',
    },
  ],
});
allOps.push(...incidentEntity.ops);

console.log('--- Step 6: Connecting 3D Graph Relations ---');
// 1. Incident -> involves agent -> Agent
const relIncidentAgent = Graph.createRelation({
  fromEntity: incidentEntity.id,
  toEntity: agentEntity.id,
  type: OntologyRelations.INVOLVES_AGENT,
});
allOps.push(...relIncidentAgent.ops);

// 2. Incident -> exhibits -> FailureMode
const relIncidentFailure = Graph.createRelation({
  fromEntity: incidentEntity.id,
  toEntity: failureModeEntity.id,
  type: OntologyRelations.EXHIBITS,
});
allOps.push(...relIncidentFailure.ops);

// 3. Incident -> resulted in -> FinancialLoss
const relIncidentLoss = Graph.createRelation({
  fromEntity: incidentEntity.id,
  toEntity: financialLossEntity.id,
  type: OntologyRelations.RESULTED_IN,
});
allOps.push(...relIncidentLoss.ops);

// 4. FailureMode -> mitigated by -> Mitigation
const relFailureMitigation = Graph.createRelation({
  fromEntity: failureModeEntity.id,
  toEntity: mitigationEntity.id,
  type: OntologyRelations.MITIGATED_BY,
});
allOps.push(...relFailureMitigation.ops);

console.log(`\n======================================================`);
console.log(`Entities Registered: ${registeredEntities.length}`);
console.log(`Total Operations Generated: ${allOps.length}`);
console.log(`======================================================`);

for (const ent of registeredEntities) {
  console.log(` - [${ent.id.slice(0, 8)}...] ${ent.name}`);
}

if (DRY_RUN) {
  console.log('\n[DRY RUN COMPLETE] Set DRY_RUN=false to publish to Geo Testnet.');
} else {
  if (!privateKey) {
    throw new Error('Cannot publish: GEO_PRIVATE_KEY environment variable is missing.');
  }

  console.log('\n[PUBLISHING POCKETOS INCIDENT TO GEO TESTNET]...');
  const wallet = await createGeoWalletClient({
    signer: privateKeyToAccount(privateKey),
    network: GeoTestnetConfig,
  });

  const { to, calldata, editId } = await geo.personalSpaces.publishEdit({
    name: 'Publish PocketOS Incident (Incident #1469)',
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
  console.log(`Publish Successful! 🎉`);
  console.log(`Edit ID: ${editId}`);
  console.log(`Transaction Hash: ${tx}`);
  console.log(`Explorer Link: https://www.geobrowser.io/space/${SPACE_ID}/${incidentEntity.id}`);
  console.log(`======================================================\n`);
}
