---
title: "Reusable Agent Configurations"
source: https://developers.deepgram.com/docs/reusable-agent-configurations.md
path: docs/reusable-agent-configurations
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Reusable Agent Configurations

Reusable Agent Configurations allow you to define and persist the `agent` block of your [Settings](/docs/voice-agent-settings) message using the Deepgram API. Once created, you receive a UUID that can be passed in place of the full `agent` object—simplifying your client code and enabling consistent agent behavior across sessions.

Reusable Agent Configurations are managed via the API. UI support is not yet available.

## Overview

When using the Voice Agent API, you typically send a full `agent` configuration object inside every `Settings` message. With Reusable Agent Configurations, you can:

* **Store** a reusable `agent` block using the Console API and receive a unique UUID.
* **Reference** that UUID in your `Settings` message instead of repeating the full configuration.
* **Use template variables** to define reusable values that can be shared across multiple agent configurations.

All agent configurations and template variables are visible to every member of your Deepgram project—including members, admins, and owners. Do not store secrets such as API keys or passwords in agent configurations or template variables.

### Common use cases

* **Per-customer configurations** — Platforms that resell agent functionality can give each customer a distinct voice, persona, or model without maintaining separate codebases.
* **Regional and regulatory compliance** — Maintain separate configurations for different markets (for example, EU vs. US) to enforce data-handling, language, or disclosure requirements without code branching.
* **A/B testing voices or prompts** — Run two configurations in parallel and measure conversion, CSAT, or containment rate to pick a winner—no code deploy required.
* **Multi-agent architectures** — Store and manage all of the agents used in your [multi-agent architecture](/docs/multi-agent-architecture) from a single project.

***

## Using a reusable agent configuration

Once you've created an agent configuration (see [Create an Agent Configuration](#create-an-agent-configuration) below), pass its UUID as the value of the `agent` field in your `Settings` message:

```json
{
  "type": "Settings",
  "audio": {
    "input": {
      "encoding": "linear16",
      "sample_rate": 24000
    },
    "output": {
      "encoding": "linear16",
      "sample_rate": 24000,
      "container": "none"
    }
  },
  "agent": "your-agent-config-uuid"
}
```

Deepgram will look up the reusable configuration by UUID, interpolate any [template variables](#template-variables), and apply the resulting `agent` block to your session.

***

## Agent Configuration API

The base URL for all Agent Configuration endpoints is:

```
https://api.deepgram.com/v1
```

### Create an Agent Configuration

```bash
POST /projects/{project_id}/agents
```

**Request body:**

| Parameter     | Type    | Description                                                                                      |
| ------------- | ------- | ------------------------------------------------------------------------------------------------ |
| `config`      | String  | A valid JSON string representing the `agent` block of a `Settings` message                       |
| `metadata`    | Object  | Optional. A map of arbitrary key-value pairs for labeling or organizing your agent configuration |
| `api_version` | Integer | Optional. API version. Defaults to `1`                                                           |

**Example request:**

```bash
curl -X POST https://api.deepgram.com/v1/projects/{project_id}/agents \
  -H "Authorization: Token YOUR_DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "config": "{\"language\": \"en\", \"listen\": {\"provider\": {\"type\": \"deepgram\", \"model\": \"nova-3\"}}, \"think\": {\"provider\": {\"type\": \"open_ai\", \"model\": \"gpt-4o-mini\"}, \"prompt\": \"You are a helpful customer service agent.\"}, \"speak\": {\"provider\": {\"type\": \"deepgram\", \"model\": \"aura-2-thalia-en\"}}}",
    "metadata": {
      "name": "customer-service-agent",
      "environment": "production"
    }
  }'
```

**Response:**

```json
{
  "agent_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "config": { ... },
  "metadata": {
    "name": "customer-service-agent",
    "environment": "production"
  }
}
```

The returned `agent_id` is the UUID you'll pass in place of the `agent` block in future `Settings` messages.

***

### List Agent Configurations

```bash
GET /projects/{project_id}/agents
```

Returns all agent configurations for the specified project. Configurations are returned in their uninterpolated form—template variable placeholders will appear as-is rather than with their substituted values.

**Example request:**

```bash
curl https://api.deepgram.com/v1/projects/{project_id}/agents \
  -H "Authorization: Token YOUR_DEEPGRAM_API_KEY"
```

***

### Get an Agent Configuration

```bash
GET /projects/{project_id}/agents/{agent_id}
```

Returns the specified agent configuration in its uninterpolated form.

**Example request:**

```bash
curl https://api.deepgram.com/v1/projects/{project_id}/agents/{agent_id} \
  -H "Authorization: Token YOUR_DEEPGRAM_API_KEY"
```

***

### Update Agent Metadata

```bash
PUT /projects/{project_id}/agents/{agent_id}
```

Updates the metadata associated with an agent configuration. The `config` itself is immutable—to change the configuration, delete the existing agent and create a new one.

**Request body:**

| Parameter  | Type   | Description                                                                |
| ---------- | ------ | -------------------------------------------------------------------------- |
| `metadata` | Object | A map of string key-value pairs to associate with this agent configuration |

**Example request:**

```bash
curl -X PUT https://api.deepgram.com/v1/projects/{project_id}/agents/{agent_id} \
  -H "Authorization: Token YOUR_DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "metadata": {
      "name": "customer-service-agent-v2",
      "environment": "production"
    }
  }'
```

***

### Delete an Agent Configuration

```bash
DELETE /projects/{project_id}/agents/{agent_id}
```

Deletes the specified agent configuration.

Deleting an agent configuration can cause a production outage if your service references this agent UUID. Migrate all active sessions to a new configuration before deleting.

**Example request:**

```bash
curl -X DELETE https://api.deepgram.com/v1/projects/{project_id}/agents/{agent_id} \
  -H "Authorization: Token YOUR_DEEPGRAM_API_KEY"
```

***

## Template Variables

Template variables let you define reusable values that can be referenced across agent configurations. When an agent configuration is used in a `Settings` message, Deepgram automatically interpolates the variable values before applying the configuration.

Template variable values are stored as plain text and are visible to all members, admins, and owners of your Deepgram project. Do not store secrets such as API keys or passwords in template variables.

Template variables follow the format `DG_<VARIABLE_NAME>`, where `<VARIABLE_NAME>` must consist of uppercase alphanumeric characters, underscores, or hyphens (e.g., `DG_MY_MODEL`, `DG_DEFAULT_LANGUAGE`).

### Using Template Variables in a Configuration

Template variables can substitute any JSON value—a string, number, boolean, or even an entire object. For example:

```json
{
  "language": "en",
  "listen": {
    "provider": {
      "type": "deepgram",
      "model": DG_LISTEN_MODEL,
      "smart_format": false
    }
  },
  "think": {
    "provider": {
      "type": "open_ai",
      "model": DG_THINK_MODEL
    },
    "prompt": "You are a helpful agent."
  },
  "speak": {
    "provider": DG_SPEAK_PROVIDER
  }
}
```

In this example, `DG_LISTEN_MODEL`, `DG_THINK_MODEL`, and `DG_SPEAK_PROVIDER` are all template variables. `DG_SPEAK_PROVIDER` resolves to an entire provider object, while the others resolve to strings.

### Agent Variable API

#### List Agent Variables

```bash
GET /projects/{project_id}/agent-variables
```

#### Create an Agent Variable

```bash
POST /projects/{project_id}/agent-variables
```

**Request body:**

| Parameter      | Type    | Description                                                                                    |
| -------------- | ------- | ---------------------------------------------------------------------------------------------- |
| `key`          | String  | The variable name, following the `DG_<VARIABLE_NAME>` format                                   |
| `value`        | Any     | The value to substitute. Can be any valid JSON type: string, number, boolean, object, or array |
| `is_sensitive` | Boolean | Required. Must be `false`                                                                      |
| `api_version`  | Integer | Optional. API version. Defaults to `1`                                                         |

The `is_sensitive` field currently only accepts `false`. Support for sensitive variables is on our roadmap and will be available in the future.

**Example request:**

```bash
curl -X POST https://api.deepgram.com/v1/projects/{project_id}/agent-variables \
  -H "Authorization: Token YOUR_DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "key": "DG_LISTEN_MODEL",
    "value": "nova-3",
    "is_sensitive": false
  }'
```

#### Get an Agent Variable

```bash
GET /projects/{project_id}/agent-variables/{variable_id}
```

#### Update an Agent Variable

```bash
PATCH /projects/{project_id}/agent-variables/{variable_id}
```

**Request body:**

| Parameter | Type | Description                 |
| --------- | ---- | --------------------------- |
| `value`   | Any  | The new value to substitute |

#### Delete an Agent Variable

```bash
DELETE /projects/{project_id}/agent-variables/{variable_id}
```

***

## Full Example

The following example walks through creating an agent configuration with template variables and using it in a Voice Agent session.

**Step 1: Create a template variable**

```bash
curl -X POST https://api.deepgram.com/v1/projects/{project_id}/agent-variables \
  -H "Authorization: Token YOUR_DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "key": "DG_SYSTEM_PROMPT",
    "value": "You are a helpful customer service agent for Acme Corp.",
    "is_sensitive": false
  }'
```

**Step 2: Create an agent configuration referencing the variable**

```bash
curl -X POST https://api.deepgram.com/v1/projects/{project_id}/agents \
  -H "Authorization: Token YOUR_DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "config": "{\"language\": \"en\", \"listen\": {\"provider\": {\"type\": \"deepgram\", \"model\": \"nova-3\"}}, \"think\": {\"provider\": {\"type\": \"open_ai\", \"model\": \"gpt-4o-mini\"}, \"prompt\": DG_SYSTEM_PROMPT}, \"speak\": {\"provider\": {\"type\": \"deepgram\", \"model\": \"aura-2-thalia-en\"}}, \"greeting\": \"Hello! How can I help you today?\"}",
    "metadata": {
      "name": "acme-support-agent"
    }
  }'
```

This returns an `agent_id`, for example: `a1b2c3d4-e5f6-7890-abcd-ef1234567890`.

**Step 3: Use the UUID in your Settings message**

```json
{
  "type": "Settings",
  "audio": {
    "input": {
      "encoding": "linear16",
      "sample_rate": 24000
    },
    "output": {
      "encoding": "linear16",
      "sample_rate": 24000,
      "container": "none"
    }
  },
  "agent": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

Deepgram resolves the UUID to the reusable configuration, substitutes `DG_SYSTEM_PROMPT` with its value, and applies the fully resolved `agent` block to your session.

***

## Next Steps

* [Configure the Voice Agent](/docs/configure-voice-agent) — see all available `agent` configuration options.
* [Voice Agent Settings](/docs/voice-agent-settings) — learn about the full `Settings` message format.
* [Voice Agent Message Flow](/docs/voice-agent-message-flow) — understand the correct message flow for building a Voice Agent client.
