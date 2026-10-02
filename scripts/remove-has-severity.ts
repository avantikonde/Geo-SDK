/**
 * Remove "has severity" from Incident Entity
 * 
 * 1. Unsets property `c0010001000000000000000000000005` (has severity) on Incident (a33d1cfb8f4941e8a3d398e43c13b85e)
 * 2. Deletes relation edge `3f79c9f977624f45a6087f25d931677c` (Incident -> has severity -> Critical Severity)
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
const HAS_SEVERITY_PROP_ID = 'c0010001000000000000000000000005';
const HAS_SEVERITY_EDGE_ID = '3f79c9f977624f45a6087f25d931677c';

const geo = createGeoClient({ network: GeoTestnetConfig });
const allOps: Op[] = [];

console.log('--- Step 1: Unsetting "has severity" property on Incident ---');
const unsetOp = Graph.updateEntity({
  id: INCIDENT_ID,
  unset: [{ property: HAS_SEVERITY_PROP_ID }],
});
allOps.push(...unsetOp.ops);

console.log('--- Step 2: Deleting "has severity" relation edge ---');
const deleteRelOp = Graph.deleteRelation({
  id: HAS_SEVERITY_EDGE_ID,
});
allOps.push(...deleteRelOp.ops);

console.log(`\n======================================================`);
console.log(`Total Operations Generated: ${allOps.length}`);
console.log(`Target Space ID: ${SPACE_ID}`);
console.log(`Target Incident ID: ${INCIDENT_ID}`);
console.log(`======================================================\n`);

if (DRY_RUN) {
  console.log('[DRY RUN COMPLETE] Operations successfully generated.');
} else {
  if (!privateKey) {
    throw new Error('Cannot publish: GEO_PRIVATE_KEY environment variable is missing.');
  }

  console.log('[PUBLISHING "HAS SEVERITY" REMOVAL TO GEO TESTNET]...');
  const wallet = await createGeoWalletClient({
    signer: privateKeyToAccount(privateKey),
    network: GeoTestnetConfig,
  });

  const { to, calldata, editId } = await geo.personalSpaces.publishEdit({
    name: 'Remove "has severity" property and relation from PocketOS Incident',
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
  console.log(`Removal Successful! 🎉`);
  console.log(`Edit ID: ${editId}`);
  console.log(`Transaction Hash: ${tx}`);
  console.log(`Incident Explorer: https://www.geobrowser.io/space/${SPACE_ID}/${INCIDENT_ID}`);
  console.log(`======================================================\n`);
}
