---
title: "Workflows"
source: https://elevenlabs.io/docs/eleven-agents/customization/agent-workflows.md
path: docs/eleven-agents/customization/agent-workflows
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Workflows

## Overview

Agent Workflows provide a powerful visual interface for designing complex conversation flows in ElevenAgents. Instead of relying on linear conversation paths, workflows enable you to create sophisticated, branching conversation graphs that adapt dynamically to user needs.

![Workflow Overview](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/0b5b2cf9754c67ef469c08af5d13786f70ca8e0018d10e92595861abb4ed32cb/assets/images/conversational-ai/workflow-overview.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T092658Z&X-Amz-Expires=604800&X-Amz-Signature=2ef8e077d6e5d9c4246fe132050628cedadb777d4a54c457999077ada2098edd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Building workflows

The dashboard is the recommended way to design workflows because of the visual graph editor. Workflows are stored as part of the agent's `conversation_config.workflow`, so you can also pull, edit, and push the JSON via the CLI or update it via the SDK — useful for version control and CI/CD.

#### Build via the dashboard

Open your agent in the dashboard, navigate to the **Workflow** tab, and use the visual editor to add nodes, configure subagent behavior, and connect edges. Save your changes.

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent "<agent-name>"
```

#### Edit \`agent\_configs/\<agent-name>.json\`

The workflow graph lives under `conversation_config.workflow`. `nodes` and `edges` are objects keyed by ID. Below is a minimal three-node workflow that routes the start node into a support subagent and then to an end node:

```json
{
  "conversation_config": {
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
    conversation_config={
        "workflow": {
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
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  conversationConfig: {
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
  },
});
```

## Node types

Workflows are composed of different node types, each serving a specific purpose in your conversation flow.

![Node Types](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/d638a84e1a6dc584a812be436f5da5e665b103b6cb5b6c53840705723bbb5a8f/assets/images/conversational-ai/workflow-node-types.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T092658Z&X-Amz-Expires=604800&X-Amz-Signature=c04e901dca76c4c299119ca641bcca4d7f5aa8f690ae5027cfd4b02d12955f2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Subagent nodes

Subagent nodes allow you to modify agent behavior at specific points in your workflow. These modifications are applied on top of the base agent configuration, or can override the current agent's config completely, giving you fine-grained control over each conversation phase.
Any of an agent's configuration, tools available, and attached knowledge base items can be updated/overwitten.

#### General

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/8ca72df8768a03adc0064281c906ab0f5710153249d17f7e7d51f465da7e9e94/assets/images/conversational-ai/workflow-subagent-extra-agent-config.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T092658Z&X-Amz-Expires=604800&X-Amz-Signature=45bf118e88e85d40bb088ab466cd7725fecf1464e7b5198f9329efd24b806f75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Subagent Extra Agent Config" />

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

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/168a56fc316596983275999c53bbbe391c4c30a05abedc17cb6a4566eff7773f/assets/images/conversational-ai/workflow-subagent-node-extra-kb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T092658Z&X-Amz-Expires=604800&X-Amz-Signature=e44c92e197d0ecffc2d8cf11a14d3d1003d6093a9257e5d0170b22fd08564602&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Subagent Extra Knowledge Base" />

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

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9af53c3227661fd88bec57cb21197eb289760d33a874b56152d507373e51bac1/assets/images/conversational-ai/workflow-sub-agent-config-extra-tools.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T092658Z&X-Amz-Expires=604800&X-Amz-Signature=61b4711a62dd57fa933c8eb1097b6f5b5e990753ab2844dc3dc30399e58247c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Subagent Extra Tools" />

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

### Dispatch tool node

Tool nodes execute a specific tool call during conversation flow. Unlike tools within subagents, tool nodes are dedicated execution points that guarantee the tool is called.

![Tool Node Result Edges](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/6b60603e56dfb25e89cdfe4223826f635af874e034af8936d74d3b428611e17b/assets/images/conversational-ai/workflow-tool-node-result-edges.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T092658Z&X-Amz-Expires=604800&X-Amz-Signature=02c2c45a71ae1af670d37ce0ba1d56b63365c66ed5f87b2b89d785bcbe7615e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Special Edge Configuration:**
Tool nodes have a unique edge type that allows routing to a new node based on the tool execution result. You can define:

* **Success path**: Where to route when the tool executes successfully
* **Failure path**: Where to route when the tool fails or returns an error

In future, futher branching conditions will be provided.

### Agent transfer node

Agent transfer node facilitate handoffs the conversation between different conversational agents, learn more [here](/docs/eleven-agents/customization/tools/system-tools/agent-transfer).

### Transfer to number node

Transfer to number nodes transitions from a conversation with an AI agent to a human agent via phone systems, learn more [here](/docs/eleven-agents/customization/tools/system-tools/transfer-to-number)

### End node

End call nodes terminate the conversation flow gracefully, learn more [here](/docs/eleven-agents/customization/tools/system-tools/transfer-to-number#:~:text=System%20tools-,End%20call,-Language%20detection)

## Edges and flow control

Edges define how conversations flow between nodes in your workflow. They support sophisticated routing logic that enables dynamic, context-aware conversation paths.

![Workflow Edges](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/02d664c9211bb8cf5452b80ab865f26b8d0b723a6acff75141ea1e9c43f7dbab/assets/images/conversational-ai/workflow-edges.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T092658Z&X-Amz-Expires=604800&X-Amz-Signature=6a88d9e5d3b193b0cb683f5080ea56df8f04f74fe548d76afe81791b52426b8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Forward Edges

Forward edges move the conversation to subsequent nodes in the workflow. They represent the primary flow of your conversation.

![Forward Edge Configuration](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/2400c66bf6f60b0d4262ecd828dea93847197f7cc00d9c8964e6486419bc90be/assets/images/conversational-ai/workflow-edge-forward.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T092658Z&X-Amz-Expires=604800&X-Amz-Signature=a0dfc2b81548918ce60e25679109bc406080bb7f1d53e0dcd6a792f5bffff617&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Backward Edges

Backward edges allow conversations to loop back to previous nodes, enabling iterative interactions and retry logic.

![Backward Edge Configuration](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e211da75e56c826fd763ae4d8149604a866d3ec63271c572e177d52bb9a80e14/assets/images/conversational-ai/workflow-edge-backward.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T092658Z&X-Amz-Expires=604800&X-Amz-Signature=8ac95e7f407bbe74841c65c1032c3ad9ebff81d221b2755c813db0284cd58642&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Use Cases:**

* Retry failed authentication attempts
* Loop back for additional information gathering
* Re-qualification after changes in user requirements
* Iterative troubleshooting processes

#### LLM Condition

Use LLM conditions to create dynamic conversation flows based on natural language evaluation. The LLM evaluates conditions in real-time to determine the appropriate path.

![LLM Condition Agent Transfer](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/507885879d781f291ab35b7dda84e760767a5544ffb6bf7b455e7a1cc19b78b7/assets/images/conversational-ai/workflow-agent-transfer-llm-condition.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T092658Z&X-Amz-Expires=604800&X-Amz-Signature=027e7714fb9c2e64e91fc0be8579b4531d3e2e0a7a6f1bc4b9a5d3aefb4ba590&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Configuration Options:**

* **Label**: Human-readable description of the edge condition (not processed by LLM)
* **LLM Condition**: Natural language condition evaluated by the LLM

#### Expression

Use expressions to create conditional logic based on variables and structured data.

![Expression Agent Transfer](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/712fc40d707906a7c6ccb4b0a76f0fd3857278176606d441bfb5245f5f6e0ffe/assets/images/conversational-ai/workflow-agent-transfer-expression.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T092658Z&X-Amz-Expires=604800&X-Amz-Signature=5c4e7ffebe1e3aec9ea8682de32105ad900f386b96b208abd81da7b90bd61b5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Configuration Options:**

* **Label**: Human-readable description of the edge condition (not processed by LLM)
* **Expression**: Deterministic evaluation criteria based on data structure

#### None

Unconditional transitions automatically move the conversation to the next node without any conditions.

![Unconditional Agent Transfer](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/73b70ce7c783277e64ba533f6d69c84e2ed3120f1fd03dbdebcd4d4f5358eb5b/assets/images/conversational-ai/workflow-agent-transfer-none.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T092658Z&X-Amz-Expires=604800&X-Amz-Signature=295ddf552273fe080766731c9204b47c8131b92eaf34feeaf343dcd21e01898d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Use Cases:**

* Sequential steps that always follow one another
* Automatic progression after completing an action
* Default fallback paths

## Analytics

![Workflow analytics tab showing per-node entries, durations, terminations, and edge flow overlaid
on the workflow graph](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/a758029a005f0327c1e6319708577efd617399c72cec63d5c342d3af2f0db2a3/assets/images/conversational-ai/workflow-analytics.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T092658Z&X-Amz-Expires=604800&X-Amz-Signature=d46f434386961224b4cfe7ddb37cacf23401d350b2f1041e5c6063e69f0d23b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Once a workflow is live, the **Workflow** tab in the [analytics dashboard](/docs/eleven-agents/dashboard#workflow-analytics) overlays usage data on the graph: per-node entries, average time spent, and terminations, plus the incoming and outgoing edge distribution for each node. From the node inspector you can also jump straight to the matching conversations in history via the **Node entered** filter.
