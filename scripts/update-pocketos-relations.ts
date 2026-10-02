/**
 * PocketOS Incident Relations Upgrade
 * 
 * Target Incident: a33d1cfb8f4941e8a3d398e43c13b85e
 * Target Space:    fb47f7907b4cc91be446bbf9fb51ccad
 * Target Agent:    3ce8532d390c455f99c7d86f3e7b7e97
 * 
 * Implements Mentor Recommendations:
 * 1. `has severity` as a Relation (Incident -> Critical Severity)
 * 2. `model` as a Relation (Agent -> Claude Opus 4.6)
 * 3. Keeps existing `involves agent` relation on the Incident pointing to the Agent.
 */

import {
  Graph,
  createGeoClient,
  createGeoWalletClient,
  GeoTestnetConfig,
  SystemIds,
  type Op,
} from '@geoprotocol/geo-sdk';
import { privateKeyToAccount } from 'viem/accounts';

const DRY_RUN = process.env.DRY_RUN !== 'false';

const rawKey = process.env.GEO_PRIVATE_KEY ?? process.env.PK_SW;
const privateKey = rawKey
  ? ((rawKey.startsWith('0x') ? rawKey : `0x${rawKey}`) as `0x${string}`)
  : undefined;

const SPACE_ID = process.env.DEMO_SPACE_ID ?? 'fb47f7907b4cc91be446bbf9fb51ccad';
const INCIDENT_ID = 'a33d1cfb8f4941e8a3d398e43c13b85e';
const AGENT_ID = '3ce8532d390c455f99c7d86f3e7b7e97';

const geo = createGeoClient({ network: GeoTestnetConfig });
const allOps: Op[] = [];

// Schema & Relation IDs
export const OntologyTypes = {
  SEVERITY_LEVEL: 'a0010001000000000000000000000006',
  MODEL: 'a0010001000000000000000000000007',
};

export const OntologyRelations = {
  HAS_SEVERITY: 'c0010001000000000000000000000005',
  MODEL: 'c0010001000000000000000000000006',
};

export const SeverityEntities = {
  CRITICAL: 'd0010001000000000000000000000001',
};

export const ModelEntities = {
  CLAUDE_OPUS_4_6: 'e0010001000000000000000000000001',
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

const TYPE_META = SystemIds.SCHEMA_TYPE ?? 'e7d737c536764c609fa16aa64a8c90ad';
const PROP_META = SystemIds.PROPERTY_TYPE ?? '808a04ceb21c4d888ad12e240613e5ca';

console.log('--- Step 1: Registering Schema & Relation Types ---');

// 1. Severity Level Type
const severityLevelType = createTypedEntity({
  id: OntologyTypes.SEVERITY_LEVEL,
  name: 'Severity Level',
  description: 'Standardized risk and failure impact classification level for autonomous AI incidents.',
  types: [TYPE_META],
  values: [],
});
allOps.push(...severityLevelType.ops);

// 2. Foundation Model Type
const modelType = createTypedEntity({
  id: OntologyTypes.MODEL,
  name: 'Foundation Model',
  description: 'The underlying large language or multimodal foundation model powering an autonomous agent.',
  types: [TYPE_META],
  values: [],
});
allOps.push(...modelType.ops);

// 3. Relation Type: has severity
const relTypeSeverity = createTypedEntity({
  id: OntologyRelations.HAS_SEVERITY,
  name: 'has severity',
  description: 'Links an Incident to its standardized Severity Level classification.',
  types: [PROP_META],
  values: [],
});
allOps.push(...relTypeSeverity.ops);

// 4. Relation Type: model
const relTypeModel = createTypedEntity({
  id: OntologyRelations.MODEL,
  name: 'model',
  description: 'Connects an autonomous Agent to the underlying Foundation Model driving its reasoning loop.',
  types: [PROP_META],
  values: [],
});
allOps.push(...relTypeModel.ops);

console.log('--- Step 2: Instantiating Critical Severity & Claude Opus 4.6 Nodes ---');

// 5. Critical Severity Node
const criticalSeverityNode = createTypedEntity({
  id: SeverityEntities.CRITICAL,
  name: 'Critical Severity',
  description: 'Catastrophic damage, total data loss, severe financial impact, or critical regulatory violation.',
  types: [OntologyTypes.SEVERITY_LEVEL],
  values: [],
});
allOps.push(...criticalSeverityNode.ops);

// 6. Foundation Model Node: Claude Opus 4.6
const claudeOpusNode = createTypedEntity({
  id: ModelEntities.CLAUDE_OPUS_4_6,
  name: 'Claude Opus 4.6',
  description: 'Anthropic frontier reasoning and autonomous software engineering model.',
  types: [OntologyTypes.MODEL],
  values: [],
});
allOps.push(...claudeOpusNode.ops);

console.log('--- Step 3: Connecting Relations to Existing Incident & Agent ---');

// 7. Incident (a33d1cfb...) -> has severity -> Critical Severity (d0010001...)
const relIncidentSeverity = Graph.createRelation({
  fromEntity: INCIDENT_ID,
  toEntity: SeverityEntities.CRITICAL,
  type: OntologyRelations.HAS_SEVERITY,
});
allOps.push(...relIncidentSeverity.ops);

// 8. Agent (3ce8532d...) -> model -> Claude Opus 4.6 (e0010001...)
const relAgentModel = Graph.createRelation({
  fromEntity: AGENT_ID,
  toEntity: ModelEntities.CLAUDE_OPUS_4_6,
  type: OntologyRelations.MODEL,
});
allOps.push(...relAgentModel.ops);

// 9. Update Agent Name to cleanly decouple the model name from the agent title
const updateAgent = Graph.updateEntity({
  id: AGENT_ID,
  name: 'Cursor AI Coding Agent',
});
allOps.push(...updateAgent.ops);

console.log(`\n======================================================`);
console.log(`Entities Registered: ${registeredEntities.length}`);
console.log(`Total Operations Generated: ${allOps.length}`);
console.log(`Target Incident ID: ${INCIDENT_ID}`);
console.log(`Target Agent ID: ${AGENT_ID}`);
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

  console.log('\n[PUBLISHING POCKETOS RELATIONS UPGRADE TO GEO TESTNET]...');
  const wallet = await createGeoWalletClient({
    signer: privateKeyToAccount(privateKey),
    network: GeoTestnetConfig,
  });

  const { to, calldata, editId } = await geo.personalSpaces.publishEdit({
    name: 'Upgrade PocketOS Incident Relations (has_severity, model)',
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
  console.log(`Explorer Link: https://www.geobrowser.io/space/${SPACE_ID}/${INCIDENT_ID}`);
  console.log(`======================================================\n`);
}

