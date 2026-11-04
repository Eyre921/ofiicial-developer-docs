---
title: "Editing tools safely"
source: https://elevenlabs.io/docs/eleven-agents/customization/tools/tool-configuration/editing-tools.md
path: docs/eleven-agents/customization/tools/tool-configuration/editing-tools
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Editing tools safely

This guide shows you how to change a tool used by a production agent without affecting live conversations. It explains what [agent versioning](/docs/eleven-agents/operate/versioning) tracks for tools, what [environment variables](/docs/eleven-agents/integrate/environment-variables) can change, how to find everything that uses a tool, and a workflow for testing a tool change on a branch.

## How tools relate to branches and versions

Custom tools and system tools are stored in different places, so versioning treats them differently.

### Custom tools are shared workspace records

Webhook, client and code tools are workspace records. You create them with [Create tool](/docs/eleven-agents/api-reference/tools/create) or in the dashboard, then attach them to an agent by ID in `conversation_config.agent.prompt.tool_ids`. Workflow tool nodes also reference tools by ID.

A branch version stores only these tool IDs, not the tool's definition. The definition lives on the tool record, and [Update tool](/docs/eleven-agents/api-reference/tools/update) takes no branch or version parameter. Editing a custom tool therefore has these effects:

* The change applies right away to every agent, branch and version that uses the tool, including the main branch.
* Going back to an earlier version doesn't undo the edit, because that version references the same tool ID.
* A branch can add or remove tools, but it can't hold its own copy of a tool's definition.

> **Warning**
>
> Editing a custom tool from a non-main branch doesn't keep main untouched. To test a change in
> isolation, follow the [testing workflow](#test-a-tool-change-without-affecting-production) below.

### What a branch versions

| Item                                                                         | Stored on                       | Versioned per branch |
| ---------------------------------------------------------------------------- | ------------------------------- | -------------------- |
| Which custom tools are attached (`tool_ids`)                                 | Agent configuration             | Yes                  |
| Tool references in workflow nodes                                            | Agent workflow                  | Yes                  |
| System tool configuration (`built_in_tools`)                                 | Agent configuration             | Yes                  |
| Custom tool definition: name, description, parameters, URL, `execution_mode` | Tool record                     | No                   |
| Tool mock responses (`response_mocks`)                                       | Tool record                     | No                   |
| Tool references in tests                                                     | Test record (`referenced_tool`) | No                   |

The **tools configuration** listed under [versioned settings](/docs/eleven-agents/operate/versioning#versioned-settings) refers to which tools are attached and to system tool settings. It doesn't cover the definitions of custom tools.

### System tools are part of the agent configuration

[System tools](/docs/eleven-agents/customization/tools/system-tools) such as `transfer_to_number` and `end_call` are configured inside each agent's own configuration, under `conversation_config.agent.prompt.built_in_tools`. They aren't shared records, so they're versioned with the branch like the rest of the agent configuration.

Two agents, or two branches of the same agent, can have different system tool settings, such as different transfer numbers and conditions. To change a system tool safely, edit it on a non-main branch and merge the branch when you've tested it.

## What environment variables can change

[Environment variables](/docs/eleven-agents/integrate/environment-variables) resolve different values for the same tool depending on the conversation's environment. For a webhook tool, they can change:

* The URL, with `{{system__env_<label>}}` templates.
* Request header values, with secret variables.
* The auth connection, with auth connection variables.

Environment variables only swap values. They can't change a tool's name, description, parameters or execution mode. Those fields are the same in every environment.

If your change only points a tool at a different endpoint or credential, use environment variables instead of duplicating the tool. If it changes the tool's description, parameters or behavior, use the workflow below.

> **Note**
>
> The environment is chosen when a conversation starts and applies to the whole conversation. To
> route test traffic, pass `environment` when starting the conversation, select an environment in a
> Simulation test, or [pin a phone number](/docs/eleven-agents/integrate/environment-variables#telephony-twilio-and-sip-trunk) to an
> environment and a branch.

## Check what uses a tool before editing it

Before you edit a tool, find the agents and branches that depend on it.

#### Dashboard

Open the tool from your tools list. The tool's page lists the agents that depend on it.

#### CLI

Call [Get dependent agents](/docs/eleven-agents/api-reference/tools/get-dependent-agents) from
the [ElevenLabs CLI](/docs/eleven-agents/operate/cli):

```bash
elevenlabs agents tools get-dependent-agents --tool-id tool_5201k6m3q8vxhd2ftc9wpj4bn7se --page-size 100
```

`agents graph --uses` also lists the agents in your local project that reference a tool, by ID or
name:

```bash
elevenlabs agents pull --all-branches
elevenlabs agents graph --uses tool_5201k6m3q8vxhd2ftc9wpj4bn7se
```

`agents graph` follows tools in `prompt.tool_ids`, workflow tool nodes and `additional_tool_ids`
across every agent in `agents.json`, branches included. It reads local files only and needs no
API key, so it only sees the agents and branches you've pulled. Tool IDs that aren't registered
in the project, such as tools created in the dashboard, are shown as external.

#### SDK

Call [Get dependent agents](/docs/eleven-agents/api-reference/tools/get-dependent-agents):

```python
import os

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

dependents = elevenlabs.conversational_ai.tools.get_dependent_agents(
    tool_id="tool_5201k6m3q8vxhd2ftc9wpj4bn7se",
    page_size=100,
)

for agent in dependents.agents:
    print(f"Agent: {agent.id}")

for branch in dependents.branches or []:
    print(f"Branch: {branch.agent_name} / {branch.branch_name} (main: {branch.is_main})")
```

```typescript
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';

const elevenlabs = new ElevenLabsClient({ apiKey: process.env.ELEVENLABS_API_KEY });

const dependents = await elevenlabs.conversationalAi.tools.getDependentAgents(
  'tool_5201k6m3q8vxhd2ftc9wpj4bn7se',
  { pageSize: 100 }
);

for (const agent of dependents.agents) {
  console.log(`Agent: ${agent.id}`);
}

for (const branch of dependents.branches ?? []) {
  console.log(`Branch: ${branch.agentName} / ${branch.branchName} (main: ${branch.isMain})`);
}
```

The Get dependent agents response contains:

* `agents`: agents whose main configuration uses the tool, either in `tool_ids` or in a workflow node.
* `branches`: non-archived branches whose latest version lists the tool in `tool_ids`, with `agent_id`, `agent_name`, `branch_id`, `branch_name` and `is_main`.
* `has_more` and `next_cursor`: pass `next_cursor` as `cursor` to fetch the next page. `page_size` defaults to `30` and can't exceed `100`.

> **Warning**
>
> Treat the result as a minimum, not a complete list. It can miss a tool that is used only in a
> workflow node on a non-main branch, or only in a
> [procedure](/docs/eleven-agents/customization/procedures). It also doesn't report earlier
> versions, archived branches, or tests that reference the tool.

## Test a tool change without affecting production

Because a branch can swap which tool it uses but can't hold its own tool definition, test a change on a copy of the tool. This example changes a tool that the main branch uses.

#### Check dependencies and capture current behavior

[Check what uses the tool](#check-what-uses-a-tool-before-editing-it) so you know which agents
and branches rely on the current definition. Create
[tests](/docs/eleven-agents/customization/agent-testing) that capture the expected behavior
before you branch.

#### Duplicate the tool

Create a copy of the tool, then make your changes to the copy, not the original.

#### Dashboard

In your tools list, open the actions menu for the tool and select **Duplicate tool**. This is
available for webhook and client tools. It creates a copy named `copy_<original-name>` that
includes the original's mock responses.

#### CLI

Pull the original tool's configuration, then create a new tool to hold the copy:

```bash
elevenlabs tools pull --tool tool_5201k6m3q8vxhd2ftc9wpj4bn7se
elevenlabs tools add copy_lookup_order --type webhook
```

`tools add` prints the new tool's ID and writes its configuration to `tool_configs/`. Copy the
contents of the original's configuration file into the new file, keep the new `name`, make
your changes, and push the copy:

```bash
elevenlabs tools push --tool tool_6401k6m7rbt9fe3qhw2nzs8kd5ya
```

The CLI only syncs `tool_config`, so the copy doesn't include the original's mock responses.
Add them to the copy in the dashboard if your tests rely on them.

#### SDK

Read the original with [Get tool](/docs/eleven-agents/api-reference/tools/get) and create the
copy with [Create tool](/docs/eleven-agents/api-reference/tools/create), passing the same
`tool_config` and `response_mocks`. There's no dedicated duplicate endpoint.

```python
import os

from dotenv import load_dotenv
from elevenlabs import ToolRequestModel
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

original = elevenlabs.conversational_ai.tools.get(
    tool_id="tool_5201k6m3q8vxhd2ftc9wpj4bn7se",
)

tool_config = original.tool_config.dict()
tool_config["name"] = f"copy_{tool_config['name']}"

copy = elevenlabs.conversational_ai.tools.create(
    request=ToolRequestModel(
        tool_config=tool_config,
        response_mocks=[mock.dict() for mock in original.response_mocks or []],
    ),
)

print(f"Copy: {copy.id}")
```

```typescript
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';

const elevenlabs = new ElevenLabsClient({ apiKey: process.env.ELEVENLABS_API_KEY });

const original = await elevenlabs.conversationalAi.tools.get('tool_5201k6m3q8vxhd2ftc9wpj4bn7se');
const { toolConfig } = original;

if (toolConfig.type !== 'webhook' && toolConfig.type !== 'client') {
  throw new Error('This example duplicates webhook and client tools');
}

const copy = await elevenlabs.conversationalAi.tools.create({
  toolConfig: { ...toolConfig, name: `copy_${toolConfig.name}` },
  responseMocks: original.responseMocks,
});

console.log(`Copy: ${copy.id}`);
```

The copy has a different name, and the name is what the LLM sees when it decides to call the
tool. If your system prompt refers to the tool by name, update the prompt on the dev branch in
the next step as well.

#### Attach the copy on a dev branch

[Create a branch](/docs/eleven-agents/operate/versioning#creating-a-branch) from the main
branch's current version. On that branch, replace the original tool's ID with the copy's ID in
`tool_ids`.

#### Dashboard

1. Open the agent, select the menu next to **Publish**, and select **View all branches**.
2. Click **Create branch**, create the branch from main, and switch the agent to the new branch.
3. In the **Tools** section, remove the original tool, then click **Add tool** and select the copy.
4. Click **Publish** to save a new version on the dev branch.

If you've already made the swap on main without publishing, select **Publish to a new branch**
from the menu next to **Publish** instead. Your unpublished changes go to the new branch and
main stays unchanged.

#### CLI

Read the main branch's current `version_id`, then create the branch from that version:

```bash
elevenlabs agents get --agent-id agent_7101k5zvyjhmfg983brhmhkd98n6 --format json
elevenlabs agents branches create --agent-id agent_7101k5zvyjhmfg983brhmhkd98n6 --json '{
  "parent_version_id": "agtvrsn_3901k6kz2c4ep8vm7tq5hd1xw9fb",
  "name": "copy-lookup-order",
  "description": "Test the updated lookup_order tool"
}'
```

Pull the branch's configuration into your project:

```bash
elevenlabs agents pull --agent agent_7101k5zvyjhmfg983brhmhkd98n6 --branch copy-lookup-order
```

In the branch's configuration file, replace the original tool's ID with the copy's ID in
`conversation_config.agent.prompt.tool_ids`, then push the branch:

```bash
elevenlabs agents push --agent agent_7101k5zvyjhmfg983brhmhkd98n6 --branch copy-lookup-order
```

#### SDK

```python
agent = elevenlabs.conversational_ai.agents.get(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
)

branch = elevenlabs.conversational_ai.agents.branches.create(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    parent_version_id=agent.version_id,
    name="copy-lookup-order",
    description="Test the updated lookup_order tool",
)

tool_ids = [
    "tool_6401k6m7rbt9fe3qhw2nzs8kd5ya" if tool_id == "tool_5201k6m3q8vxhd2ftc9wpj4bn7se" else tool_id
    for tool_id in agent.conversation_config.agent.prompt.tool_ids
]

elevenlabs.conversational_ai.agents.update(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    branch_id=branch.created_branch_id,
    conversation_config={"agent": {"prompt": {"tool_ids": tool_ids}}},
)
```

```typescript
const agent = await elevenlabs.conversationalAi.agents.get('agent_7101k5zvyjhmfg983brhmhkd98n6');

const branch = await elevenlabs.conversationalAi.agents.branches.create(
  'agent_7101k5zvyjhmfg983brhmhkd98n6',
  {
    parentVersionId: agent.versionId!,
    name: 'copy-lookup-order',
    description: 'Test the updated lookup_order tool',
  }
);

const toolIds = (agent.conversationConfig.agent?.prompt?.toolIds ?? []).map((toolId) =>
  toolId === 'tool_5201k6m3q8vxhd2ftc9wpj4bn7se' ? 'tool_6401k6m7rbt9fe3qhw2nzs8kd5ya' : toolId
);

await elevenlabs.conversationalAi.agents.update('agent_7101k5zvyjhmfg983brhmhkd98n6', {
  branchId: branch.createdBranchId,
  conversationConfig: { agent: { prompt: { toolIds } } },
});
```

If a workflow node on the branch references the original tool, update that node to use the copy
as well.

#### Test the branch with mocked tools

Run [Simulation tests](/docs/eleven-agents/customization/agent-testing#simulation-testing)
against the dev branch. Use [tool mocking](/docs/eleven-agents/customization/agent-testing#tool-mocking)
so the copy returns controlled responses instead of calling live systems, and set the fallback
behavior to **Finish with error** if a test must never reach the real tool. System tools and
workflow tools are never mocked.

#### Dashboard

Switch the agent to the dev branch and open its **Tests** tab. Tests you run there run
against the selected branch.

#### CLI

Pass the branch's ID to `agents run-tests`. Without `branch_id`, tests run on the main
branch:

```bash
elevenlabs agents run-tests --agent-id agent_7101k5zvyjhmfg983brhmhkd98n6 --json '{
  "branch_id": "agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
  "tests": [{"test_id": "test_4501k6n2wq7hfz3dbv8mt1sk6pcr"}]
}'
```

#### SDK

Pass the branch's ID to [Run tests on agent](/docs/eleven-agents/api-reference/tests/run-tests).
Without `branch_id`, tests run on the main branch:

```python
elevenlabs.conversational_ai.agents.run_tests(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
    tests=[{"test_id": "test_4501k6n2wq7hfz3dbv8mt1sk6pcr"}],
)
```

```typescript
await elevenlabs.conversationalAi.agents.runTests('agent_7101k5zvyjhmfg983brhmhkd98n6', {
  branchId: 'agtbrch_8901k4t9z5defmb8vh3e9361y7nj',
  tests: [{ testId: 'test_4501k6n2wq7hfz3dbv8mt1sk6pcr' }],
});
```

To test with live calls, [pin a test phone number](/docs/eleven-agents/integrate/environment-variables#telephony-twilio-and-sip-trunk) to
the dev branch and a non-production environment. To try the change on a share of real traffic,
[deploy](/docs/eleven-agents/operate/versioning#deploying-traffic) a small percentage to the
branch.

#### Merge the branch

[Preview the merge](/docs/eleven-agents/operate/versioning#resolving-merge-conflicts) and
confirm that `tool_ids` on the main branch will contain the copy's ID. Then merge the branch.

#### Dashboard

On the agent's branches page, open the actions menu for the dev branch and select **Merge
branch**. Choose main as the target and review the result before you confirm.

#### CLI

Use the main branch's ID, shown as `main_branch_id` in the `agents get` output, as the target:

```bash
elevenlabs agents branches preview-merge --agent-id agent_7101k5zvyjhmfg983brhmhkd98n6 \
  --source-branch-id agtbrch_8901k4t9z5defmb8vh3e9361y7nj \
  --target-branch-id agtbrch_2301k5zvyjj0e8k3t4qm9xw6r1hb

elevenlabs agents branches merge --agent-id agent_7101k5zvyjhmfg983brhmhkd98n6 \
  --source-branch-id agtbrch_8901k4t9z5defmb8vh3e9361y7nj \
  --target-branch-id agtbrch_2301k5zvyjj0e8k3t4qm9xw6r1hb
```

#### SDK

```python
preview = elevenlabs.conversational_ai.agents.branches.preview_merge(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    source_branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
    target_branch_id=agent.main_branch_id,
)

print(f"Tools after merge: {preview.conversation_config.agent.prompt.tool_ids}")

elevenlabs.conversational_ai.agents.branches.merge(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    source_branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
    target_branch_id=agent.main_branch_id,
)
```

```typescript
const preview = await elevenlabs.conversationalAi.agents.branches.previewMerge(
  'agent_7101k5zvyjhmfg983brhmhkd98n6',
  'agtbrch_8901k4t9z5defmb8vh3e9361y7nj',
  { targetBranchId: agent.mainBranchId! }
);

console.log(`Tools after merge: ${preview.conversationConfig.agent?.prompt?.toolIds}`);

await elevenlabs.conversationalAi.agents.branches.merge(
  'agent_7101k5zvyjhmfg983brhmhkd98n6',
  'agtbrch_8901k4t9z5defmb8vh3e9361y7nj',
  { targetBranchId: agent.mainBranchId! }
);
```

The main branch now uses the copy, and the original tool is unchanged. Earlier versions of the
main branch still reference the original tool, so going back to one of them restores the old
tool definition as well.

#### Update the remaining references by hand

Merging only changes this agent's configuration. Update these references manually:

* Workflow nodes on other branches, and other agents, that should move to the copy.
* Tool Call tests whose `referenced_tool` points at the original tool's ID.

Keep the original tool while anything still depends on it. Once nothing does, you can delete it.

## Next steps

#### [Versioning](/docs/eleven-agents/operate/versioning)

Create branches, deploy traffic and merge changes

#### [Environment variables](/docs/eleven-agents/integrate/environment-variables)

Resolve tool URLs, headers and auth connections per environment

#### [Testing](/docs/eleven-agents/customization/agent-testing)

Run Simulation tests with mocked tools

#### [Get dependent agents](/docs/eleven-agents/api-reference/tools/get-dependent-agents)

List the agents and branches that use a tool
