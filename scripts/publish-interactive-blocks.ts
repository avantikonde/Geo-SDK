/**
 * Publish Interactive TextBlocks to Geo Knowledge Graph Pages
 * 
 * Attaches rich in-app entity mentions (`graph://<entityId>`) to:
 * 1. PocketOS Incident Entity (a33d1cfb8f4941e8a3d398e43c13b85e)
 * 2. Cursor AI Coding Agent Entity (3ce8532d390c455f99c7d86f3e7b7e97)
 * 3. involves agent Relation Entity (c0010001000000000000000000000001)
 * 4. resulted in Relation Entity (c0010001000000000000000000000003)
 * 5. Claude Opus 4.6 Model Entity (e0010001000000000000000000000001)
 * 6. Critical Severity Entity (d0010001000000000000000000000001)
 */

import {
  TextBlock,
  Position,
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
const FAILURE_ID = 'b1d76f03eabe4ed4b9843053cf008ece';
const LOSS_ID = 'ec4f740ddac84b26b9eefb42e93dd542';
const MITIGATION_ID = 'cb6c242944b04332b851b47be27f917b';

const INVOLVES_AGENT_REL_ID = 'c0010001000000000000000000000001';
const RESULTED_IN_REL_ID = 'c0010001000000000000000000000003';

const geo = createGeoClient({ network: GeoTestnetConfig });
const allOps: Op[] = [];

console.log('--- Step 1: Building Interactive TextBlock Ops ---');

// 1. Block on Incident Page
const incidentMarkdown = `### 🔗 Incident Knowledge Graph Relations

* **Involves Agent**: [Cursor AI Coding Agent](graph://${AGENT_ID})
* **Underlying Model**: [Claude Opus 4.6](graph://${MODEL_ID})
* **Severity Classification**: [Critical Severity](graph://${SEVERITY_ID})
* **Failure Mode**: [Unconstrained Infrastructure Mutation & Permissive Token Misuse](graph://${FAILURE_ID})
* **Economic Impact**: [PocketOS Production Outage Loss ($1.45M)](graph://${LOSS_ID})
* **Architectural Mitigation**: [Independent Backup Plane & Runtime Boundary Enforcement](graph://${MITIGATION_ID})

---
*Verified Incident Dossier · [AI Incident Database #1469](https://incidentdatabase.ai/cite/1469/)*`;

const incidentBlockOps = TextBlock.make({
  fromId: INCIDENT_ID,
  text: incidentMarkdown,
  position: Position.generateBetween(null, null),
});
allOps.push(...incidentBlockOps);

// 2. Block on Agent Page
const agentMarkdown = `### 🤖 Autonomous Agent Specification

* **Reasoning Model**: [Claude Opus 4.6](graph://${MODEL_ID})
* **Architecture**: Autonomous IDE Agent with Railway GraphQL API Tool Calling
* **Associated Incident**: [PocketOS Production Database & Volume Deletion Incident](graph://${INCIDENT_ID})`;

const agentBlockOps = TextBlock.make({
  fromId: AGENT_ID,
  text: agentMarkdown,
  position: Position.generateBetween(null, null),
});
allOps.push(...agentBlockOps);

// 3. Block on "involves agent" Schema Page (so it's not empty!)
const involvesAgentMarkdown = `### 📋 Relation Usage in this Space

This relation connects an Incident to the specific autonomous agent implicated in the failure.

* **Incident**: [PocketOS Production Database & Volume Deletion Incident](graph://${INCIDENT_ID})
* **Involved Agent**: [Cursor AI Coding Agent](graph://${AGENT_ID})
* **Reasoning Model**: [Claude Opus 4.6](graph://${MODEL_ID})`;

const involvesAgentBlockOps = TextBlock.make({
  fromId: INVOLVES_AGENT_REL_ID,
  text: involvesAgentMarkdown,
  position: Position.generateBetween(null, null),
});
allOps.push(...involvesAgentBlockOps);

// 4. Block on "resulted in" Schema Page (so it's not empty!)
const resultedInMarkdown = `### 📋 Relation Usage in this Space

This relation connects an Incident to the quantifiable financial damages or economic loss incurred.

* **Incident**: [PocketOS Production Database & Volume Deletion Incident](graph://${INCIDENT_ID})
* **Financial Loss**: [PocketOS Production Outage Loss ($1.45M)](graph://${LOSS_ID})`;

const resultedInBlockOps = TextBlock.make({
  fromId: RESULTED_IN_REL_ID,
  text: resultedInMarkdown,
  position: Position.generateBetween(null, null),
});
allOps.push(...resultedInBlockOps);

// 5. Block on Foundation Model Page
const modelMarkdown = `### 🧠 Foundation Model Overview

* **Developer**: Anthropic
* **Model Family**: Claude
* **Autonomous Agent Powered**: [Cursor AI Coding Agent](graph://${AGENT_ID})
* **Incident Record**: [PocketOS Production Database & Volume Deletion Incident](graph://${INCIDENT_ID})`;

const modelBlockOps = TextBlock.make({
  fromId: MODEL_ID,
  text: modelMarkdown,
  position: Position.generateBetween(null, null),
});
allOps.push(...modelBlockOps);

// 6. Block on Severity Page
const severityMarkdown = `### 🚨 Severity Classification Level

* **Risk Level**: Critical
* **Definition**: Catastrophic damage, total data loss, severe financial impact, or critical regulatory violation.
* **Classified Incidents**: [PocketOS Production Database & Volume Deletion Incident](graph://${INCIDENT_ID})`;

const severityBlockOps = TextBlock.make({
  fromId: SEVERITY_ID,
  text: severityMarkdown,
  position: Position.generateBetween(null, null),
});
allOps.push(...severityBlockOps);

console.log(`\n======================================================`);
console.log(`Total Interactive Blocks Configured: 6`);
console.log(`Total Operations Generated: ${allOps.length}`);
console.log(`Target Space ID: ${SPACE_ID}`);
console.log(`======================================================\n`);

if (DRY_RUN) {
  console.log('[DRY RUN COMPLETE] Operations successfully generated.');
} else {
  if (!privateKey) {
    throw new Error('Cannot publish: GEO_PRIVATE_KEY environment variable is missing.');
  }

  console.log('[PUBLISHING INTERACTIVE BLOCKS TO GEO TESTNET]...');
  const wallet = await createGeoWalletClient({
    signer: privateKeyToAccount(privateKey),
    network: GeoTestnetConfig,
  });

  const { to, calldata, editId } = await geo.personalSpaces.publishEdit({
    name: 'Add Interactive Knowledge Graph Navigation Blocks',
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
  console.log(`Agent Explorer:    https://www.geobrowser.io/space/${SPACE_ID}/${AGENT_ID}`);
  console.log(`Involves Agent:    https://www.geobrowser.io/space/${SPACE_ID}/${INVOLVES_AGENT_REL_ID}`);
  console.log(`======================================================\n`);
}
