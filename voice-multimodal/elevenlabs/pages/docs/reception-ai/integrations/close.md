---
title: "Close"
source: https://elevenlabs.io/docs/reception-ai/integrations/close.md
path: docs/reception-ai/integrations/close
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Close

Connect Close's hosted [MCP server](/docs/reception-ai/integrations/mcp-server) so your receptionist can recognize callers who are already in Close, add new callers as leads, and leave notes and follow-up tasks for your team.

## Setup

### Create an API key

In Close, open **Settings** → **Developer** → **API Keys** and create a new key. The key acts as your user, so it can see and change what you can.

### Add the MCP server

In Reception.ai, go to **Integrations**, select **Add integration**, and choose **MCP Server**.

| Field            | Value                                                          |
| ---------------- | -------------------------------------------------------------- |
| **Name**         | Close                                                          |
| **Server type**  | Streamable HTTP                                                |
| **Server URL**   | `https://mcp.close.com/mcp`                                    |
| **HTTP Headers** | `Close-API-Key`: your API key  `Close-Scope`: `mcp.write_safe` |

Leave **Secret Token** empty. Select **Enable**.

The `Close-Scope` header limits which tools Close offers:

| Scope                   | Allows                                    |
| ----------------------- | ----------------------------------------- |
| `mcp.read`              | Looking up data only                      |
| `mcp.write_safe`        | Looking up and creating data              |
| `mcp.write_destructive` | Also updating, merging, and deleting data |

Use `mcp.write_safe` so your receptionist can add leads and notes but can't change or delete existing records. Use `mcp.read` if it should only look callers up.

### Assign tools

Open the **Tools** tab and assign these to the **Client** (receptionist):

* `find_contacts`: finds the caller by phone number, email, or name.
* `create_lead`: adds a new caller as a lead.
* `create_note`: logs what the caller needed on their lead.
* `create_task`: creates a follow-up task for your team.

Leave the other tools unassigned. The `mcp.write_safe` scope also includes tools that create workflows, templates, and lead statuses, which your receptionist doesn't need.

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) with a call from a number that's saved on a contact in Close, then from a new number. The new caller appears as a lead.

> **Warning**
>
> Anyone with the API key can use your Close account. Keep it out of shared documents, and delete
> the key in Close if it leaks.

## Troubleshooting

| Problem                          | What to check                                                                                                   |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| No tools are listed              | Close doesn't support SSE. Use the **Streamable HTTP** server type, and check both headers are spelled exactly. |
| Create tools are missing         | The `Close-Scope` header is set to `mcp.read`. Change it to `mcp.write_safe` and select **Refresh tools**.      |
| Known callers aren't found       | `find_contacts` matches the complete number, not the last digits. Save numbers in Close with the area code.     |
| A tool shows a **Changed** badge | Close updated the tool. Review it in the **Tools** tab and select **Update**.                                   |
