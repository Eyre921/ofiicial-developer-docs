---
title: "Workflows"
source: https://elevenlabs.io/docs/eleven-agents/customization/agent-workflows.md
path: docs/eleven-agents/customization/agent-workflows
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Workflows

## Overview

Agent Workflows provide a powerful visual interface for designing complex conversation flows in ElevenAgents. Instead of relying on linear conversation paths, workflows enable you to create sophisticated, branching conversation graphs that adapt dynamically to user needs.

![Workflow Overview](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/0b5b2cf9754c67ef469c08af5d13786f70ca8e0018d10e92595861abb4ed32cb/assets/images/conversational-ai/workflow-overview.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T180107Z&X-Amz-Expires=604800&X-Amz-Signature=6e8419d8bc64302dfbaaa32fb87d3531aaffc966340cc94d9118b40f7452425f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Building workflows

The dashboard is the recommended way to design workflows because of the visual graph editor. Workflows are stored in the agent's top-level `workflow` field, so you can also pull, edit, and push the JSON via the CLI or update it via the SDK — useful for version control and CI/CD.

#### Build via the dashboard

Open your agent in the dashboard, navigate to the **Workflow** tab, and use the visual editor to add nodes, configure subagent behavior, and connect edges. Save your changes.

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent "<agent-name>"
```

#### Edit \`agent\_configs/\<agent-name>.json\`

The workflow graph lives under the top-level `workflow` key. `nodes` and `edges` are objects keyed by ID. Below is a minimal three-node workflow that routes the start node into a support subagent and then to an end node:

```json
{
  "workflow": {
    "nodes": {
      "start_node": {
        "type": "start",
        "edge_order": ["start_to_support"]
      },
      "support_agent": {
        "type": "override_agent",
        "label": "Support agent",
        "additional_prompt": "Help the user with their support request, then transition to the end node when resolved.",
        "edge_order": ["support_to_end"]
      },
      "end_node": {
        "type": "end"
      }
    },
    "edges": {
      "start_to_support": {
        "source": "start_node",
        "target": "support_agent",
        "forward_condition": { "type": "unconditional" }
      },
      "support_to_end": {
        "source": "support_agent",
        "target": "end_node",
        "forward_condition": {
          "type": "llm",
          "condition": "The support request has been resolved."
        }
      }
    }
  }
}
```

Most teams design workflows in the dashboard first, then commit the resulting JSON to version control.

#### Push your changes

```bash
elevenlabs agents push --agent "<agent-name>"
```

#### Update via the API

```python
from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs()

elevenlabs.conversational_ai.agents.update(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    workflow={
        "nodes": {
            "start_node": {
                "type": "start",
                "edge_order": ["start_to_support"],
            },
            "support_agent": {
                "type": "override_agent",
                "label": "Support agent",
                "additional_prompt": "Help the user with their support request, then transition to the end node when resolved.",
                "edge_order": ["support_to_end"],
            },
            "end_node": {"type": "end"},
        },
        "edges": {
            "start_to_support": {
                "source": "start_node",
                "target": "support_agent",
                "forward_condition": {"type": "unconditional"},
            },
            "support_to_end": {
                "source": "support_agent",
                "target": "end_node",
                "forward_condition": {
                    "type": "llm",
                    "condition": "The support request has been resolved.",
                },
            },
        },
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  workflow: {
    nodes: {
      start_node: {
        type: "start",
        edgeOrder: ["start_to_support"],
      },
      support_agent: {
        type: "override_agent",
        label: "Support agent",
        additionalPrompt:
          "Help the user with their support request, then transition to the end node when resolved.",
        edgeOrder: ["support_to_end"],
      },
      end_node: { type: "end" },
    },
    edges: {
      start_to_support: {
        source: "start_node",
        target: "support_agent",
        forwardCondition: { type: "unconditional" },
      },
      support_to_end: {
        source: "support_agent",
        target: "end_node",
        forwardCondition: {
          type: "llm",
          condition: "The support request has been resolved.",
        },
      },
    },
  },
});
```

## Node types

Workflows are composed of different node types, each serving a specific purpose in your conversation flow.

![Node Types](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/b169065e0f229623a4cd57861802fa30ecd463a142599f5fd60f6fc1b8a6223e/assets/images/conversational-ai/workflow-node-types.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T180107Z&X-Amz-Expires=604800&X-Amz-Signature=36397ba004b199bf82ebd377f4da65001e23ef8b27b9833de17bd5a3d9a4eb26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Subagent nodes

Subagent nodes allow you to modify agent behavior at specific points in your workflow. These modifications are applied on top of the base agent configuration, or can override the current agent's config completely, giving you fine-grained control over each conversation phase.
Any of an agent's configuration, tools available, and attached knowledge base items can be updated/overwitten.

#### General

![Subagent Extra Agent Config](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/8ca72df8768a03adc0064281c906ab0f5710153249d17f7e7d51f465da7e9e94/assets/images/conversational-ai/workflow-subagent-extra-agent-config.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T180107Z&X-Amz-Expires=604800&X-Amz-Signature=bdf7bff8434df2dab13120e3981d905953d2079d25b4e453462601a47961afbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Modify core agent settings for this specific node:

* **System Prompt**: Append or override system instructions to guide agent behavior
* **LLM Selection**: Choose a different language model (e.g., switch from Gemini 2.0 Flash to a more powerful model for complex reasoning tasks)
* **Voice Configuration**: Change voice settings including speed, tone, or even switch to a different voice

**Use Cases:**

* Use a more powerful LLM for complex decision-making nodes
* Apply stricter conversation guidelines during sensitive information gathering
* Change voice characteristics for different conversation phases
* Modify agent personality for specific interaction types

#### Knowledge Base

![Subagent Extra Knowledge Base](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/168a56fc316596983275999c53bbbe391c4c30a05abedc17cb6a4566eff7773f/assets/images/conversational-ai/workflow-subagent-node-extra-kb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T180107Z&X-Amz-Expires=604800&X-Amz-Signature=df69980ad97fa81c6e2cd069e374b9c45e5657f50995bda5c7aa966cd61b45a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Add node-specific knowledge without affecting the global knowledge base:

* **Include Global Knowledge Base**: Toggle whether to include the agent's main knowledge base
* **Additional Documents**: Add documents specific to this conversation phase
* **Dynamic Knowledge**: Inject contextual information based on workflow state

**Use Cases:**

* Add product-specific documentation during sales conversations
* Include compliance guidelines during authentication
* Provide troubleshooting guides for support flows
* Add pricing information only after qualification

#### Tools

![Subagent Extra Tools](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9af53c3227661fd88bec57cb21197eb289760d33a874b56152d507373e51bac1/assets/images/conversational-ai/workflow-sub-agent-config-extra-tools.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T180107Z&X-Amz-Expires=604800&X-Amz-Signature=0c109580505e0e6ddbff35f4f608979cc3ba72db04cb7443cb16b9e78c1c087c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Manage which tools are available to the agent at this node:

* **Include Global Tools**: Toggle whether to include tools from the main agent configuration
* **Additional Tools**: Add tools specific to this workflow node (e.g., webhook tools like `book_meeting`)
* **Tool Type**: Specify whether tools are webhooks, API calls, or other integrations

**Use Cases:**

* Add authentication tools only after initial qualification
* Enable payment processing tools at checkout nodes
* Provide CRM access after user verification
* Add scheduling tools for appointment booking phases
* Include webhook tools for specific actions like booking meetings

### Say node

A say node makes the agent speak one message at a specific point in the workflow, then moves on along its outgoing edges. Use it when the wording of a message matters and should not be left to a subagent, for example a greeting, a legal disclosure, or a confirmation read back to the user.

Each say node sends its message in one of two modes:

* **Literal**: the agent speaks the exact text you enter, with an optional translation per configured language.
* **Prompt**: the LLM generates the message from a description you write.

### Dispatch tool node

Tool nodes execute a specific tool call during conversation flow. Unlike tools within subagents, tool nodes are dedicated execution points that guarantee the tool is called.

![Tool Node Result Edges](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/6b60603e56dfb25e89cdfe4223826f635af874e034af8936d74d3b428611e17b/assets/images/conversational-ai/workflow-tool-node-result-edges.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T180107Z&X-Amz-Expires=604800&X-Amz-Signature=80d06a301c1653036285266c9844d9efe6c39a15d7f137e7eb3ad267c914cba3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Special Edge Configuration:**
Tool nodes have a unique edge type that allows routing to a new node based on the tool execution result. You can define:

* **Success path**: Where to route when the tool executes successfully
* **Failure path**: Where to route when the tool fails or returns an error

In future, futher branching conditions will be provided.

### Update state node

An update state node assigns one or more [dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables) every time the workflow passes through it, using the same expressions as the Update state tool. Unlike the tool, which runs when the LLM decides to call it, the node always applies its updates at that point in the graph and then continues along its outgoing edges.

Learn more [here](/docs/eleven-agents/customization/tools/system-tools/update-state).

### Agent transfer node

Agent transfer node facilitate handoffs the conversation between different conversational agents, learn more [here](/docs/eleven-agents/customization/tools/system-tools/agent-transfer).

### Transfer to number node

Transfer to number nodes transitions from a conversation with an AI agent to a human agent via phone systems, learn more [here](/docs/eleven-agents/customization/tools/system-tools/transfer-to-number)

### End node

End call nodes terminate the conversation flow gracefully, learn more [here](/docs/eleven-agents/customization/tools/system-tools/transfer-to-number#:~:text=System%20tools-,End%20call,-Language%20detection)

## Edges and flow control

Edges define how conversations flow between nodes in your workflow. They support sophisticated routing logic that enables dynamic, context-aware conversation paths.

![Workflow Edges](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/02d664c9211bb8cf5452b80ab865f26b8d0b723a6acff75141ea1e9c43f7dbab/assets/images/conversational-ai/workflow-edges.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T180107Z&X-Amz-Expires=604800&X-Amz-Signature=0d531a52595f10384ff72ca3bc24952a8fa236fdc005dd7c14c0fa7b2d1d099c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Forward Edges

Forward edges move the conversation to subsequent nodes in the workflow. They represent the primary flow of your conversation.

![Forward Edge Configuration](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/2400c66bf6f60b0d4262ecd828dea93847197f7cc00d9c8964e6486419bc90be/assets/images/conversational-ai/workflow-edge-forward.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T180107Z&X-Amz-Expires=604800&X-Amz-Signature=27a5bffcb37a0ce91e7e497bb14c080a8ac23ff6e9ad9d000e9dc78224a3352a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Backward Edges

Backward edges allow conversations to loop back to previous nodes, enabling iterative interactions and retry logic.

![Backward Edge Configuration](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e211da75e56c826fd763ae4d8149604a866d3ec63271c572e177d52bb9a80e14/assets/images/conversational-ai/workflow-edge-backward.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T180107Z&X-Amz-Expires=604800&X-Amz-Signature=066192c2a79bb760773902b664e49d9f983d8000376aa56915890e45aef72217&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Use Cases:**

* Retry failed authentication attempts
* Loop back for additional information gathering
* Re-qualification after changes in user requirements
* Iterative troubleshooting processes

#### LLM Condition

Use LLM conditions to create dynamic conversation flows based on natural language evaluation. The LLM evaluates conditions in real-time to determine the appropriate path.

![LLM Condition Agent Transfer](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/507885879d781f291ab35b7dda84e760767a5544ffb6bf7b455e7a1cc19b78b7/assets/images/conversational-ai/workflow-agent-transfer-llm-condition.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T180107Z&X-Amz-Expires=604800&X-Amz-Signature=ef52b686f13676983753e07836f678b4f7689ae90bf9d653ed433bc1de9e2a0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Configuration Options:**

* **Label**: Human-readable description of the edge condition (not processed by LLM)
* **LLM Condition**: Natural language condition evaluated by the LLM

#### Expression

Use expressions to create conditional logic based on variables and structured data.

![Expression Agent Transfer](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/712fc40d707906a7c6ccb4b0a76f0fd3857278176606d441bfb5245f5f6e0ffe/assets/images/conversational-ai/workflow-agent-transfer-expression.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T180107Z&X-Amz-Expires=604800&X-Amz-Signature=a85f0b2e26da7b4c0837508dd3feff5c0d78a1aaffd2865a17fe63eb883ce0b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Configuration Options:**

* **Label**: Human-readable description of the edge condition (not processed by LLM)
* **Expression**: Deterministic evaluation criteria based on data structure

#### None

Unconditional transitions automatically move the conversation to the next node without any conditions.

![Unconditional Agent Transfer](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/73b70ce7c783277e64ba533f6d69c84e2ed3120f1fd03dbdebcd4d4f5358eb5b/assets/images/conversational-ai/workflow-agent-transfer-none.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T180107Z&X-Amz-Expires=604800&X-Amz-Signature=09f486e9f255b2f3a7d4c7b7a7eef0528c626e00568d45803668b49a0a3e9116&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Use Cases:**

* Sequential steps that always follow one another
* Automatic progression after completing an action
* Default fallback paths

## Analytics

![Workflow analytics tab showing per-node entries, durations, terminations, and edge flow overlaid
on the workflow graph](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/a758029a005f0327c1e6319708577efd617399c72cec63d5c342d3af2f0db2a3/assets/images/conversational-ai/workflow-analytics.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T180107Z&X-Amz-Expires=604800&X-Amz-Signature=b98931969d444895a6020b58b6084a59f823fbf5b811217ef7b773d7e60a8273&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Once a workflow is live, the **Workflow** tab in the [analytics dashboard](/docs/eleven-agents/dashboard#workflow-analytics) overlays usage data on the graph: per-node entries, average time spent, and terminations, plus the incoming and outgoing edge distribution for each node. From the node inspector you can also jump straight to the matching conversations in history via the **Node entered** filter.
