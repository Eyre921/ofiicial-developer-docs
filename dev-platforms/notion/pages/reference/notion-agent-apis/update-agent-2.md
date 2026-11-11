---
title: "Update an agent"
source: https://developers.notion.com/reference/notion-agent-apis/update-agent
path: reference/notion-agent-apis/update-agent
---

patch /v1/agents/{agent_id}
Change a Custom Agent's or the personal agent's name, model, status, and other settings in one request.

Send only the fields you want to change. Every body field is optional, but the request needs at least one, and an empty body returns a `400` `validation_error`. A field set to its current value usually changes nothing. The exception is `status`: sending `"disabled"` for an agent that's already disabled, other than through the API, returns a `403` `restricted_resource` and rejects the whole request. Leave `status` out when you only want to change other fields. All the fields in one request save together, so either every change applies or none does.

The response is the updated [agent object](/reference/notion-agent-apis/retrieve-agent), without `instructions`.

```bash theme={null}
curl --request PATCH "https://api.notion.com/v1/agents/$AGENT_ID" \
  --header "Authorization: Bearer $NOTION_TOKEN" \
  --header "Notion-Version: 2026-03-11" \
  --header "Content-Type: application/json" \
  --data '{"name":"Weekly report writer","status":"disabled"}'
```

### Which fields each agent and token can change

| Field | Custom Agent | Personal agent (`notion_ai`) |
| - | - | - |
| `name` | Edit access | Yes |
| `description` | Edit access. Send `""` to clear it. | No |
| `model` | Edit access | Yes |
| `status` | Edit access | No |
| `is_favorited` | Read access, personal access token only | No |

A [personal access token](/guides/connections-and-tokens/personal-access-tokens) acts as its user, so its user's role on the agent decides which fields it can change. A connection needs the Edit selected agents capability and edit access to the agent. Sending a field the token can't change returns a `403` `restricted_resource`. The exception is `is_favorited`: a connection that sends it gets a `400` `validation_error`, because only a personal access token can change it.

For `notion_ai`, you can change `name` and `model`. `name` sets the token user's name for their personal agent. Sending any other field returns a `400` `validation_error`. Only a personal access token can update `notion_ai`.

To change a Custom Agent's credit limit, use [Update an agent credit limit](/reference/notion-agent-apis/update-agent-credit-limit). Sending `credit_limit` to this endpoint returns a `400` `validation_error`.

### Set the model

Set `model` to `{"mode": "auto"}` to let Notion choose, or to `{"mode": "pinned", "id": "<model-id>"}` to use one model. The model ID has to be one the token's user can use, or the request returns a `400` `validation_error`. Changing a Custom Agent's model also updates its published version.

### Enable or disable a Custom Agent

Set `status` to `"disabled"` to turn off a running agent, or `"active"` to turn it back on. You can re-enable an agent only if an editor disabled it, through the API or in agent settings. An agent paused for another reason, such as reaching its credit limit, returns a `403` `restricted_resource`. So does re-enabling an agent while the workspace doesn't allow Custom Agents.

This replaces [Update agent status](/reference/notion-agent-apis/update-agent-status), which is deprecated.
