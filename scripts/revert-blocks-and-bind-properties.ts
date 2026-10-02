/**
 * Revert Blocks & Populate Native GeoBrowser Card Properties
 * 
 * 1. Deletes the markdown TextBlock relations from Incident, Agent, and Schema pages
 *    to restore the original clean GeoBrowser card layout ("make it like before").
 * 2. Populates `Cursor AI Coding Agent` on the `involves agent` page so it is not empty.
 * 3. Populates `Claude Opus 4.6` on the `Cursor AI Coding Agent` page so it displays the model.
 * 4. Links `involves agent` to the `Agent` type via `To entity types` and `Data type` = `Relation`.
 */

import {
  Graph,
  createGeoClient,
  createGeoWalletClient,
  GeoTestnetConfig,
  type Op,
} from '@geoprotocol/geo-sdk';
import { privateKeyToAccount } from 'viem/accounts';

const DRY_RUN = process.env.DRY_RUN === 'true';

const rawKey = process.env.GEO_PRIVATE_KEY ?? process.env.PK_SW;
const privateKey = rawKey
  ? ((rawKey.startsWith('0x') ? rawKey : `0x${rawKey}`) as `0x${string}`)
  : undefined;

const SPACE_ID = process.env.DEMO_SPACE_ID ?? 'fb47f7907b4cc91be446bbf9fb51ccad';

const INCIDENT_ID = 'a33d1cfb8f4941e8a3d398e43c13b85e';
const AGENT_ID = '3ce8532d390c455f99c7d86f3e7b7e97';
const MODEL_ID = 'e0010001000000000000000000000001';
const SEVERITY_ID = 'd0010001000000000000000000000001';

const INVOLVES_AGENT_REL_ID = 'c0010001000000000000000000000001';
const HAS_SEVERITY_REL_ID = 'c0010001000000000000000000000005';
const MODEL_REL_ID = 'c0010001000000000000000000000006';

const AGENT_TYPE_ID = 'a0010001000000000000000000000002';
const MODEL_TYPE_ID = 'a0010001000000000000000000000007';

const AGENT_NAME_PROP_ID = 'b0010001000000000000000000000004';

// System IDs
const TO_ENTITY_TYPES_REL = '9eea393f17dd4971a62ea603e8bfec20';
const DATA_TYPE_PROP = '6d29d57849bb4959baf72cc696b1671a';
const RELATION_TYPE_TARGET = '4b6d9fc1fbfe474c861c83398e1b50d9';

// Block relation edge IDs to remove
const BLOCK_EDGES_TO_DELETE = [
  '038d190134fa45559adcfea0e9edd611', // Incident block
  '0eeb7fbe6aa4427ab32007f3bef54a34', // Agent block
  'ce1984a906f44d3d8f0825e5d5cd4638', // Involves agent block
  '35b33a9b55834970a04b3ceb2a506c81', // Resulted in block
  'f7b3712bda2c4eabafb07843a11b8349', // Model block
  '220b6a59d57f4c64aa29d7a20e9dfb3c', // Severity block
];

const geo = createGeoClient({ network: GeoTestnetConfig });
const allOps: Op[] = [];

console.log('--- Step 1: Removing TextBlock relations ("make it like before") ---');
for (const edgeId of BLOCK_EDGES_TO_DELETE) {
  const op = Graph.deleteRelation({ id: edgeId });
  allOps.push(...op.ops);
}

console.log('--- Step 2: Configuring "involves agent" so it is NOT empty ---');
// Set Data type -> Relation
const relDataType = Graph.createRelation({
  fromEntity: INVOLVES_AGENT_REL_ID,
  toEntity: RELATION_TYPE_TARGET,
  type: DATA_TYPE_PROP,
});
allOps.push(...relDataType.ops);

// Set To entity types -> Agent
const relToTypes = Graph.createRelation({
  fromEntity: INVOLVES_AGENT_REL_ID,
  toEntity: AGENT_TYPE_ID,
  type: TO_ENTITY_TYPES_REL,
});
allOps.push(...relToTypes.ops);

// Point involves agent to Cursor AI Coding Agent
const relInvolvesToAgent = Graph.createRelation({
  fromEntity: INVOLVES_AGENT_REL_ID,
  toEntity: AGENT_ID,
  type: AGENT_TYPE_ID,
});
allOps.push(...relInvolvesToAgent.ops);

// Set properties on involves agent page
const updateInvolvesAgent = Graph.updateEntity({
  id: INVOLVES_AGENT_REL_ID,
  values: [
    { property: AGENT_NAME_PROP_ID, type: 'text', value: 'Cursor AI Coding Agent' },
    { property: MODEL_REL_ID, type: 'text', value: 'Claude Opus 4.6' },
  ],
});
allOps.push(...updateInvolvesAgent.ops);

console.log('--- Step 3: Configuring "Cursor AI Coding Agent" to show the Model ---');
// Set model property on Agent page so it renders in the table
const updateAgent = Graph.updateEntity({
  id: AGENT_ID,
  name: 'Cursor AI Coding Agent',
  values: [
    { property: MODEL_REL_ID, type: 'text', value: 'Claude Opus 4.6' },
    { property: AGENT_NAME_PROP_ID, type: 'text', value: 'Cursor AI Coding Agent' },
  ],
});
allOps.push(...updateAgent.ops);

console.log('--- Step 4: Configuring Incident table card values ---');
const updateIncident = Graph.updateEntity({
  id: INCIDENT_ID,
  values: [
    { property: INVOLVES_AGENT_REL_ID, type: 'text', value: 'Cursor AI Coding Agent' },
    { property: HAS_SEVERITY_REL_ID, type: 'text', value: 'Critical Severity' },
  ],
});
allOps.push(...updateIncident.ops);

console.log(`\n======================================================`);
console.log(`Total Operations Generated: ${allOps.length}`);
console.log(`Blocks Being Deleted: ${BLOCK_EDGES_TO_DELETE.length}`);
console.log(`Target Space ID: ${SPACE_ID}`);
console.log(`======================================================\n`);

if (DRY_RUN) {
  console.log('[DRY RUN COMPLETE] Set DRY_RUN=false to publish.');
} else {
  if (!privateKey) {
    throw new Error('Cannot publish: GEO_PRIVATE_KEY environment variable is missing.');
  }

  console.log('[PUBLISHING CLEAN-UP & PROPERTY UPDATES TO GEO TESTNET]...');
  const wallet = await createGeoWalletClient({
    signer: privateKeyToAccount(privateKey),
    network: GeoTestnetConfig,
  });

  const { to, calldata, editId } = await geo.personalSpaces.publishEdit({
    name: 'Revert TextBlocks and Bind Native Table Properties (involves_agent, model)',
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
  console.log(`Incident Explorer: https://www.geobrowser.io/space/${SPACE_ID}/${INCIDENT_ID}`);
  console.log(`Involves Agent:    https://www.geobrowser.io/space/${SPACE_ID}/${INVOLVES_AGENT_REL_ID}`);
  console.log(`Agent Explorer:    https://www.geobrowser.io/space/${SPACE_ID}/${AGENT_ID}`);
  console.log(`======================================================\n`);
}
