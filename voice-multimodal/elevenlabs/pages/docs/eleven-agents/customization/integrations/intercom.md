---
title: "Intercom"
source: https://elevenlabs.io/docs/eleven-agents/customization/integrations/intercom.md
path: docs/eleven-agents/customization/integrations/intercom
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Intercom

## Overview

Connect your ElevenLabs AI agents with Intercom to manage contacts, conversations, tickets, and notes. The integration supports two flows:

* **Tools**: let an agent look up and update contacts, search and reply to conversations, manage conversation lifecycle (close, reopen, assign), tag conversations, create and reply to tickets, and add internal notes — all from inside a running ElevenLabs conversation.
* **Triggers**: have an agent automatically respond to new Intercom conversations and replies from contacts, posting back as an Intercom admin.

## How the trigger works

When you enable the **Intercom Conversation** trigger, ElevenLabs subscribes to two Intercom webhook topics — one for new conversations created by a contact, and one for follow-up replies from a contact. Whenever Intercom delivers a notification:

1. ElevenLabs verifies the webhook signature against your app's client secret.
2. It fetches the full conversation from Intercom and maps the message history to the configured agent.
3. The agent generates a reply, which ElevenLabs posts back to the conversation as the configured admin.

Because Intercom only sends notifications for end-user activity (not admin replies), the agent never responds to its own messages.

## Setup

In Intercom, open **Settings → Integrations → Developer Hub** and create a new app for ElevenLabs (or open an existing one).

Under **Authentication**, copy the **Access token** — this is the token labeled for accessing your own workspace data. You'll also need the **Client secret** from the **Basic information** page; ElevenLabs uses it to verify the authenticity of every webhook delivery.

The agent posts replies as an Intercom admin (typically a dedicated teammate seat). Open **Settings → Teammates** in Intercom and select the teammate the agent should post as. The admin ID is a numeric value (for example `1234567`) — you can also retrieve it programmatically via Intercom's [List all admins](https://developers.intercom.com/intercom-api-reference/reference/listadmins) API.

In the ElevenLabs Intercom integration page, click **Connect** and paste the **Access token** from Developer Hub.

Open the **Triggers** tab of the Intercom integration and enable **Intercom Conversation**. Fill in:

* **Agent** — the ElevenLabs agent that should handle incoming Intercom conversations.
* **Client secret** — the value from Developer Hub → Basic information. Used to verify webhook signatures.
* **Admin ID** — the numeric admin ID the agent should post replies as.
* **Team inbox ID** *(optional)* — restrict the agent to a single Intercom team inbox. When set, the agent only responds to conversations currently assigned to that team; leave blank to respond to all conversations. See the next step for how to scope the agent to a dedicated inbox.

If you only want the agent to handle a specific subset of conversations, route those conversations into a dedicated **team inbox** and point the trigger at it:

1. In Intercom, create a **Team** for the agent (**Settings → Teammates & Teams → Teams**), e.g. "AI Agent".
2. Build a **Workflow** (**Fin AI Agent → Workflows**) that assigns the conversations you want handled to that team using an **Assign → Team** action (Workflows require an Advanced/Expert plan). To escalate, move the conversation out of the team to a human team.
3. Retrieve the team's numeric ID via Intercom's [List all teams](https://developers.intercom.com/intercom-api-reference/reference/listteams) API and paste it into the **Team inbox ID** field on the trigger.

With a team inbox configured, the agent ignores any conversation that is not assigned to that team.

Intercom assigns the team via your Workflow at the start of a conversation. If a
`conversation.user.created` webhook is delivered before the assignment lands, that first message
may be skipped; the agent picks up on the contact's next reply. Account for this when testing.

In Intercom Developer Hub, open your app's **Webhooks** section and add a new subscription pointing at this URL:

```
https://api.elevenlabs.io/v1/convai/api-integrations/intercom/triggers/conversation
```

Subscribe to both of the following topics:

* `conversation.user.created` — fires when an end-user starts a new conversation.
* `conversation.user.replied` — fires when an end-user replies to an existing conversation.

Intercom signs every webhook with your client secret; ElevenLabs verifies the `X-Hub-Signature` header on every delivery. Deliveries with an invalid or missing signature are silently dropped.

Open the Intercom Messenger as a test contact (or use Intercom's own preview), send a message to your workspace, and confirm that the configured agent replies as the admin you selected. You can review the resulting conversation transcript in the ElevenLabs **Conversations** view.

If no reply arrives, double-check the webhook URL and topic subscription in Developer Hub, and confirm the **Access token** and **Client secret** match the same Intercom app.

### CLI

CLI documentation for this integration is coming soon.

### SDK

SDK documentation for this integration is coming soon.

## Useful links

* [Intercom REST API reference](https://developers.intercom.com/docs/references/rest-api/api.intercom.io)
* [Intercom webhooks overview](https://developers.intercom.com/docs/webhooks)
* [Intercom webhook topics](https://developers.intercom.com/docs/references/webhooks/webhook-models)
* [Intercom Developer Hub](https://app.intercom.com/a/apps/_/developer-hub)
