/**
 * Clean Schema Definition for "involves agent"
 * 
 * Removes the hardcoded Cursor AI Agent and Claude Opus model values from the shared
 * schema relation definition `c0010001000000000000000000000001`.
 * 
 * Preserves the canonical ontology definition:
 * - Data type -> Relation
 * - To entity types -> Agent
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

const INVOLVES_AGENT_REL_ID = 'c0010001000000000000000000000001';
const AGENT_NAME_PROP_ID = 'b0010001000000000000000000000004';
const MODEL_PROP_ID = 'c0010001000000000000000000000006';

// Relation edge from involves agent -> Cursor AI Coding Agent
const HARDCODED_AGENT_REL_EDGE_ID = '4c8553e9683d46de975822a63fef070e';

const geo = createGeoClient({ network: GeoTestnetConfig });
const allOps: Op[] = [];

console.log('--- Step 1: Unsetting hardcoded Agent Name & Model from "involves agent" ---');
const unsetOp = Graph.updateEntity({
  id: INVOLVES_AGENT_REL_ID,
  unset: [
    { property: AGENT_NAME_PROP_ID },
    { property: MODEL_PROP_ID },
  ],
});
allOps.push(...unsetOp.ops);

console.log('--- Step 2: Deleting hardcoded Cursor AI Agent relation edge ---');
const deleteRelOp = Graph.deleteRelation({
  id: HARDCODED_AGENT_REL_EDGE_ID,
});
allOps.push(...deleteRelOp.ops);

console.log(`\n======================================================`);
console.log(`Total Operations Generated: ${allOps.length}`);
console.log(`Target Space ID: ${SPACE_ID}`);
console.log(`Target Schema ID: ${INVOLVES_AGENT_REL_ID}`);
console.log(`======================================================\n`);

if (DRY_RUN) {
  console.log('[DRY RUN COMPLETE] Operations successfully generated.');
} else {
  if (!privateKey) {
    throw new Error('Cannot publish: GEO_PRIVATE_KEY environment variable is missing.');
  }

  console.log('[PUBLISHING CLEAN-UP TO GEO TESTNET]...');
  const wallet = await createGeoWalletClient({
    signer: privateKeyToAccount(privateKey),
    network: GeoTestnetConfig,
  });

  const { to, calldata, editId } = await geo.personalSpaces.publishEdit({
    name: 'Clean shared "involves agent" relation definition (remove hardcoded agent/model)',
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
  console.log(`Clean-up Successful! 🎉`);
  console.log(`Edit ID: ${editId}`);
  console.log(`Transaction Hash: ${tx}`);
  console.log(`Involves Agent Explorer: https://www.geobrowser.io/space/${SPACE_ID}/${INVOLVES_AGENT_REL_ID}`);
  console.log(`======================================================\n`);
}
