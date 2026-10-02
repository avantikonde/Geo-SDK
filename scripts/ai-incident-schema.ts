/**
 * AI Agent Incident Knowledge Graph — Schema & Example Publication Script
 * 
 * Target Platform: Geo Knowledge Graph (GRC-20 / @geoprotocol/geo-sdk v0.20+)
 *
 * This script defines the core ontology for tracking AI agent failures, their
 * architectural root causes, real-world impacts, and mitigations.
 *
 * It creates:
 *   1. Meta Types: Incident, Agent, FailureMode, Mitigation, FinancialLoss
 *   2. Property Definitions (Attributes & Relation Types)
 *   3. Example Incident Instance linking the complete graph
 */

import {
  Graph,
  createGeoClient,
  createGeoWalletClient,
  GeoTestnetConfig,
  SystemIds,
  Id,
  type Op,
} from '@geoprotocol/geo-sdk';
import { privateKeyToAccount } from 'viem/accounts';

// ============================================================================
// CONFIGURATION & CREDENTIALS
// ============================================================================

// Set TRIAL_MODE to false to allow live Geo publication
const TRIAL_MODE = false;

// Two-phase execution flag (defaults to true for safety)
const DRY_RUN = process.env.DRY_RUN !== 'false';

const rawKey = process.env.GEO_PRIVATE_KEY ?? process.env.PK_SW;
const privateKey = rawKey
  ? ((rawKey.startsWith('0x') ? rawKey : `0x${rawKey}`) as `0x${string}`)
  : undefined;

// Target Space (Personal space or DAO space ID)
const SPACE_ID = process.env.DEMO_SPACE_ID ?? 'a19c345ab9866679b001d7d2138d88a1';

// Initialize Geo Client (SDK v0.20+ with GeoTestnetConfig)
const geo = createGeoClient({ network: GeoTestnetConfig });

const allOps: Op[] = [];

// ============================================================================
// SAFEGUARD HELPER (Geo Hard Rule: No typeless entities)
// ============================================================================
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

// ============================================================================
// ONTOLOGY IDS (Deterministic 32-char hex UUIDs for reproducibility)
// ============================================================================

// Core Types (Classes)
export const OntologyTypes = {
  INCIDENT: 'a0010001000000000000000000000001',
  AGENT: 'a0010001000000000000000000000002',
  FAILURE_MODE: 'a0010001000000000000000000000003',
  MITIGATION: 'a0010001000000000000000000000004',
  FINANCIAL_LOSS: 'a0010001000000000000000000000005',
};

// Attributes (Value Properties)
export const OntologyProperties = {
  DATE: 'b0010001000000000000000000000001', // Date (YYYY-MM-DD)
  SEVERITY: 'b0010001000000000000000000000002', // Text ('Low' | 'Medium' | 'High' | 'Critical')
  SOURCE_EVIDENCE_LINK: 'b0010001000000000000000000000003', // Text (URL)
  AGENT_NAME: 'b0010001000000000000000000000004', // Text
  ARCHITECTURE: 'b0010001000000000000000000000005', // Text (e.g. 'ReAct with Tool Execution')
  LOSS_AMOUNT: 'b0010001000000000000000000000006', // Float / Decimal
  CURRENCY: 'b0010001000000000000000000000007', // Text ('USD', 'EUR', 'ETH', etc.)
  MITIGATION_STRATEGY: 'b0010001000000000000000000000008', // Text (e.g. 'Human-in-the-Loop Guardrail')
};

// Relation Types (Predicates / Graph Edges)
export const OntologyRelations = {
  INVOLVES_AGENT: 'c0010001000000000000000000000001', // Incident -> Agent
  EXHIBITS: 'c0010001000000000000000000000002', // Incident -> FailureMode
  RESULTED_IN: 'c0010001000000000000000000000003', // Incident -> FinancialLoss
  MITIGATED_BY: 'c0010001000000000000000000000004', // FailureMode -> Mitigation
};

// ============================================================================
// 1. DEFINE SCHEMA TYPES (Entities typed with SystemIds.SCHEMA_TYPE)
// ============================================================================
console.log('--- Step 1: Defining Core Entity Types ---');

// Meta-type ID for "Type" in Geo
const TYPE_META = SystemIds.SCHEMA_TYPE ?? 'e7d737c536764c609fa16aa64a8c90ad';
const PROP_META = SystemIds.PROPERTY_TYPE ?? '808a04ceb21c4d888ad12e240613e5ca';

const typeDefinitions = [
  {
    id: OntologyTypes.INCIDENT,
    name: 'Incident',
    description: 'An observable failure or security compromise involving an autonomous AI agent in a real-world environment.',
  },
  {
    id: OntologyTypes.AGENT,
    name: 'Agent',
    description: 'The autonomous AI system or multi-agent pipeline implicated in the incident.',
  },
  {
    id: OntologyTypes.FAILURE_MODE,
    name: 'Failure Mode',
    description: 'The categorical root cause, cognitive flaw, or vulnerability pattern exhibited during the failure.',
  },
  {
    id: OntologyTypes.MITIGATION,
    name: 'Mitigation',
    description: 'Architectural guardrails, verification gates, or engineering controls designed to prevent or contain the failure mode.',
  },
  {
    id: OntologyTypes.FINANCIAL_LOSS,
    name: 'Financial Loss',
    description: 'Quantifiable monetary or economic damage directly or indirectly resulting from the incident.',
  },
];

for (const t of typeDefinitions) {
  const { ops } = createTypedEntity({
    id: t.id,
    name: t.name,
    description: t.description,
    types: [TYPE_META],
    values: [],
  });
  allOps.push(...ops);
}

// ============================================================================
// 2. DEFINE ATTRIBUTE PROPERTIES (Entities typed with SystemIds.PROPERTY_TYPE)
// ============================================================================
console.log('--- Step 2: Defining Attribute Properties ---');

const attributeDefinitions = [
  {
    id: OntologyProperties.DATE,
    name: 'Date',
    description: 'The calendar date on which the incident took place or was publicly disclosed.',
  },
  {
    id: OntologyProperties.SEVERITY,
    name: 'Severity',
    description: 'The severity classification level (e.g., Low, Medium, High, Critical).',
  },
  {
    id: OntologyProperties.SOURCE_EVIDENCE_LINK,
    name: 'Source Evidence Link',
    description: 'Cryptographic proof, post-mortem URL, or public repository citing the incident.',
  },
  {
    id: OntologyProperties.AGENT_NAME,
    name: 'Agent Name',
    description: 'The operational moniker or release identifier of the agent.',
  },
  {
    id: OntologyProperties.ARCHITECTURE,
    name: 'Architecture',
    description: 'The agent reasoning framework, harness, or tool execution pipeline (e.g., ReAct, Reflexion, Swarm).',
  },
  {
    id: OntologyProperties.LOSS_AMOUNT,
    name: 'Loss Amount',
    description: 'The numerical monetary quantification of the loss incurred.',
  },
  {
    id: OntologyProperties.CURRENCY,
    name: 'Currency',
    description: 'Standard three-letter currency code or cryptocurrency asset symbol (e.g., USD, ETH).',
  },
  {
    id: OntologyProperties.MITIGATION_STRATEGY,
    name: 'Mitigation Strategy',
    description: 'The defensive pattern applied to mitigate the failure mode (e.g., Human-in-the-Loop, Rate Limit).',
  },
];

for (const prop of attributeDefinitions) {
  const { ops } = createTypedEntity({
    id: prop.id,
    name: prop.name,
    description: prop.description,
    types: [PROP_META],
    values: [],
  });
  allOps.push(...ops);
}

// ============================================================================
// 3. DEFINE RELATIONSHIP PROPERTIES (Predicates)
// ============================================================================
console.log('--- Step 3: Defining Relationship Properties ---');

const relationshipDefinitions = [
  {
    id: OntologyRelations.INVOLVES_AGENT,
    name: 'involves agent',
    description: 'Links an Incident to the specific Agent architecture that failed.',
  },
  {
    id: OntologyRelations.EXHIBITS,
    name: 'exhibits',
    description: 'Relates an Incident to the Failure Mode(s) demonstrated.',
  },
  {
    id: OntologyRelations.RESULTED_IN,
    name: 'resulted in',
    description: 'Connects an Incident to its Financial Loss or economic damages.',
  },
  {
    id: OntologyRelations.MITIGATED_BY,
    name: 'mitigated by',
    description: 'Maps a known Failure Mode to an effective architectural Mitigation.',
  },
];

for (const rel of relationshipDefinitions) {
  const { ops } = createTypedEntity({
    id: rel.id,
    name: rel.name,
    description: rel.description,
    types: [PROP_META], // In Geo, relation types are properties of type Relation
    values: [],
  });
  allOps.push(...ops);
}

// ============================================================================
// 4. INSTANCE SEEDING: COMPLETE AI INCIDENT GRAPH TRIPLE EXAMPLE
// ============================================================================
console.log('--- Step 4: Instantiating Example Incident Triples ---');

// Instance A: Agent
const agentEntity = createTypedEntity({
  name: 'DevOps-Automator-v2',
  description: 'Autonomous cloud infrastructure deployment agent powered by an unconstrained ReAct loop.',
  types: [OntologyTypes.AGENT],
  values: [
    { property: OntologyProperties.AGENT_NAME, type: 'text', value: 'DevOps-Automator-v2' },
    { property: OntologyProperties.ARCHITECTURE, type: 'text', value: 'ReAct Agent with Direct AWS SDK Tool Access' },
  ],
});
allOps.push(...agentEntity.ops);

// Instance B: Failure Mode
const failureModeEntity = createTypedEntity({
  name: 'Unconstrained Tool Execution Loop',
  description: 'Agent autonomously executes destructive API calls without idempotency checks or human verification.',
  types: [OntologyTypes.FAILURE_MODE],
  values: [],
});
allOps.push(...failureModeEntity.ops);

// Instance C: Mitigation
const mitigationEntity = createTypedEntity({
  name: 'Cryptographic Policy Gate & Human Approval',
  description: 'Pre-flight dry-run policy interceptor requiring multi-party human sign-off on non-idempotent ops.',
  types: [OntologyTypes.MITIGATION],
  values: [
    { property: OntologyProperties.MITIGATION_STRATEGY, type: 'text', value: 'Deterministic Approval Interceptor' },
  ],
});
allOps.push(...mitigationEntity.ops);

// Instance D: Financial Loss
const financialLossEntity = createTypedEntity({
  name: 'Production Outage Cloud Teardown Loss',
  description: 'Accidental database drop and 6-hour cluster outage during automated migration.',
  types: [OntologyTypes.FINANCIAL_LOSS],
  values: [
    { property: OntologyProperties.LOSS_AMOUNT, type: 'float', value: 450000.0 },
    { property: OntologyProperties.CURRENCY, type: 'text', value: 'USD' },
  ],
});
allOps.push(...financialLossEntity.ops);

// Instance E: Incident (The root anchor)
const incidentEntity = createTypedEntity({
  name: 'AutoDevOps Production Database Deletion Incident',
  description: 'Autonomous deployment agent mistakenly issued unverified DROP DATABASE during CI/CD maintenance.',
  types: [OntologyTypes.INCIDENT],
  values: [
    { property: OntologyProperties.DATE, type: 'date', value: '2026-04-18' },
    { property: OntologyProperties.SEVERITY, type: 'text', value: 'Critical' },
    {
      property: OntologyProperties.SOURCE_EVIDENCE_LINK,
      type: 'text',
      value: 'https://postmortems.security-ai.org/reports/2026-autodevops-drop',
    },
  ],
});
allOps.push(...incidentEntity.ops);

// ============================================================================
// 5. WIRE RELATIONSHIPS (Triples: Entity -> Relation -> Entity)
// ============================================================================
console.log('--- Step 5: Connecting Relations ---');

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

// ============================================================================
// SUMMARY & PUBLISH DISPATCH
// ============================================================================
console.log(`\n======================================================`);
console.log(`Entities Registered: ${registeredEntities.length}`);
console.log(`Total Operations Generated: ${allOps.length}`);
console.log(`======================================================`);

for (const ent of registeredEntities) {
  console.log(` - [${ent.id.slice(0, 8)}...] ${ent.name} (Types: ${ent.types.length})`);
}

if (TRIAL_MODE) {
  console.log('\n[TRIAL MODE ACTIVE] 🛡️');
  console.log('All entities, triples, and operations were generated and verified locally.');
  console.log('Zero data was broadcast to Geo Testnet or the blockchain.');
  console.log('To view and interact with this graph visually, open: http://localhost:3333');
} else if (DRY_RUN) {
  console.log('\n[DRY RUN COMPLETE] Set DRY_RUN=false with valid GEO_PRIVATE_KEY to publish to Geo.');
} else {
  if (!privateKey) {
    throw new Error('Cannot publish: GEO_PRIVATE_KEY environment variable is missing.');
  }

  console.log('\n[PUBLISHING TO GEO TESTNET]...');
  const wallet = await createGeoWalletClient({
    signer: privateKeyToAccount(privateKey),
    network: GeoTestnetConfig,
  });

  const { to, calldata, editId } = await geo.personalSpaces.publishEdit({
    name: 'Publish AI Agent Incident Ontology & Instance',
    spaceId: SPACE_ID,
    ops: allOps,
    author: SPACE_ID,
  });

  const tx = await wallet.sendTransaction({
    account: wallet.account,
    to,
    data: calldata,
  });

  console.log(`Publish Successful!`);
  console.log(`Edit ID: ${editId}`);
  console.log(`Transaction Hash: ${tx}`);
  console.log(`Explorer Link: https://www.geobrowser.io/space/${SPACE_ID}/${incidentEntity.id}`);
}
