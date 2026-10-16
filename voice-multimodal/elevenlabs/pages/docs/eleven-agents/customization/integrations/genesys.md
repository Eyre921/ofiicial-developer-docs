---
title: "Genesys"
source: https://elevenlabs.io/docs/eleven-agents/customization/integrations/genesys.md
path: docs/eleven-agents/customization/integrations/genesys
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Genesys

## Overview

Integrate ElevenLabs conversational AI with Genesys Cloud to power your contact center with natural-sounding voice and text agents. The integration works in two directions, and you choose the direction with the credential you connect with.

With the **OAuth2 Client** credential, Genesys Cloud routes conversations to your agent: voice calls through the Audio Connector and chats through the Bot Connector, both called from an Architect flow.

With the **OAuth2 Client + Open Messaging** credential, your agent hands a chat that started in ElevenLabs, for example on WhatsApp, over to a human agent in Genesys Cloud. The human agent replies from Genesys Cloud, and the chat history stays in ElevenLabs.

## Capabilities

| Capability                   | Support                                                 |
| ---------------------------- | ------------------------------------------------------- |
| Zero retention mode (ZRM)    | Not supported                                           |
| Attachments in conversations | Not supported — conversations carry audio and text only |
| Attachments in tools         | Not supported — tools operate on text only              |

## Setup

This integration uses **OAuth 2.0 Client Credentials** for authentication. Both credentials use the same OAuth client fields and differ only in what the connection is for.

| Credential                     | Use it when                                                                 | Available in ElevenLabs                    |
| ------------------------------ | --------------------------------------------------------------------------- | ------------------------------------------ |
| OAuth2 Client                  | Genesys Cloud calls your agent from an Architect flow.                      | Bot Connector and Audio Connector triggers |
| OAuth2 Client + Open Messaging | Your agent hands an ElevenLabs chat over to a human agent in Genesys Cloud. | Transfer to Open Messaging tool            |

A connection serves one direction. To use both, create two connections, one per credential.

#### Create OAuth client in Genesys Cloud

In Genesys Cloud Admin Center, navigate to **Admin > Integrations > OAuth** and click **Add Client**.

#### Configure the OAuth client

* Set **Grant Type** to **Client Credentials**
* Assign the admin role for your Division(s)
* Save the client configuration

#### Copy client credentials

After creating the OAuth client, copy the **Client ID** and **Client Secret** immediately — the secret will not be shown again.

#### Select region

Identify your Genesys Cloud region (e.g., `mypurecloud.com` for US, `mypurecloud.de` for Europe, etc.).

#### Connect to ElevenLabs

In the ElevenLabs dashboard, go to **Agents > Integrations**, click **Add Integration** and select **Genesys**.
Under the **Configure** tab, select the credential, then enter your **region**, **Client ID**, and **Client Secret**. The **OAuth2 Client + Open Messaging** credential also takes an optional **Integration Name** of up to 100 characters.

> **Note**
>
> Connecting with the **OAuth2 Client + Open Messaging** credential creates an Open Messaging
> integration with the Integration Name you enter in your Genesys Cloud organization. Choose a name
> you can recognize when you assign a message route to it. If you leave it empty, ElevenLabs picks a
> random name such as `ElevenLabs - Fierce Tiger`. The OAuth client needs permission to create Open
> Messaging integrations, or the connection fails with a permission error.

## Triggers

### Audio Connector

For voice-based agents, configure the Genesys Audio Connector to connect phone numbers to your ElevenLabs conversational AI agents.

For step-by-step setup instructions including authentication, phone number configuration, and call routing, see the [Genesys Audio Connector documentation](https://elevenlabs.io/docs/eleven-agents/phone-numbers/c-caa-s-integrations/genesys).

### Bot Connector

For text-based agents, use the Genesys Bot Connector trigger to enable chat and messaging interactions. The Bot Connector automatically creates and configures the integration in your Genesys Cloud environment.

#### Configure trigger

#### Add a Bot Connector trigger

On the Integrations page in the ElevenAgents dashboard, open the Genesys integration, and navigate to the **Triggers** tab. Select **Genesys Bot Connector**.

#### Configure the trigger fields

Fill in the required fields:

* **Agent**: the ElevenLabs agent that will handle incoming conversations.
* **Integration Name**: name for the Bot Connector integration to be created in Genesys Cloud (e.g., "ElevenLabs Support Bot"). This name is used to derive the bot integration and bot name referenced in Architect flows.

#### Activate the trigger

Save and activate the trigger. ElevenLabs automatically creates a Bot Connector integration in your Genesys Cloud environment with the intents `success` and `escalate`. Deactivating the trigger removes the integration from Genesys Cloud.

#### Configure inbound message flow

In Architect, open the Inbound Message Flow you want to use.

1. Add a **Call Bot Connector** node and point it at your bot integration and bot name (both derived from the **Integration Name** you set in the trigger configuration).
2. Handle the returned intents:
   * **success** → send the agent's response back to the user
   * **escalate** → transfer to a support queue
   * **failure** → transfer to a fallback queue

![Genesys Bot Connector flow configuration](/docs/_fern-img/49cf1993f9e6978e75af83e28ac8de1256198630f3c06b9e850c1ce3f4486cb2.webp)

#### Configure escalation

To enable your agent to escalate conversations to human support, configure the following in ElevenLabs:

#### Add the Update state tool

In your agent configuration, add the **Update state** system tool. Configure it to set the `genesys_should_escalate` dynamic variable to `true`.

#### Configure the system prompt

Add escalation instructions to your agent's system prompt:

```text
### Escalation

When escalating, ALWAYS ask first if the user would like to talk to another client services team member. If they say yes, use the update_state tool to set the genesys_should_escalate dynamic variable to true.
```

#### Add business rules

Include escalation scenarios in your agent's business rules. For example:

```text
- If a question is partially covered, answer what you can and then escalate
- If a question is not covered in the knowledge base, respond: "I'm not able to help with that here". Then escalate to a client services team member.
```

When the agent sets `genesys_should_escalate` to `true`, the Bot Connector will return the `escalate` intent, triggering the escalation flow you configured in Architect.

## Chat handover with Open Messaging

Use the **Transfer to Open Messaging** tool when a chat starts in ElevenLabs and your agent needs to hand it over to a human agent in Genesys Cloud. The tool requires a connection made with the **OAuth2 Client + Open Messaging** credential.

### How it works

When the agent calls the tool, ElevenLabs opens a conversation on the Open Messaging integration that the connection created. Genesys Cloud routes it through the inbound message flow assigned to that integration, so it reaches a queue and a human agent. The human agent sees a summary and the chat so far. Messages from the human agent reach the customer on the original channel, and the customer's replies reach the human agent, until the human agent ends the conversation in Genesys Cloud. The ElevenLabs agent then takes the chat back. The chat history stays in ElevenLabs.

Open Messaging handover is available in text conversations only.

### Configure the handover

#### Connect with the OAuth2 Client + Open Messaging credential

Follow the [Setup](#setup) steps, select **OAuth2 Client + Open Messaging** as the credential, and optionally enter an **Integration Name**. ElevenLabs creates an Open Messaging integration with that name, or a random one, in your Genesys Cloud organization.

#### Assign an inbound message flow in Genesys Cloud

In Genesys Cloud, create an inbound message flow in Architect that transfers the message to a queue, then add a message route that uses the new integration as the inbound address for that flow. See [Add an inbound message route](https://help.genesys.cloud/articles/add-inbound-message-route/) in the Genesys Cloud documentation. Without a route, a handed-over chat reaches no human agent.

#### Add the tool to your agent

In your agent configuration, open **Tools**, click **Add tool**, and select **Transfer to Open Messaging** from the Genesys integration. Pick the connection you created with the OAuth2 Client + Open Messaging credential.

#### Tell the agent when to hand over

Add handover instructions to your agent's system prompt, for example:

```text
### Handover

If the user asks to speak to a human, or you cannot resolve the request, call the transfer_to_open_messaging tool with a short reason. Do not ask follow-up questions first.
```

### Removing the connection

Deleting the connection in ElevenLabs also deletes the Open Messaging integration it created in Genesys Cloud. Genesys Cloud refuses to delete an integration that still has an inbound message flow assigned. Remove the flow from the integration first, then delete the connection.

## FAQ

### Can one Genesys connection use both the triggers and the handover tool?

No. A connection made with the OAuth2 Client credential offers the triggers, and a connection made with the OAuth2 Client + Open Messaging credential offers the Transfer to Open Messaging tool. Create one connection per credential, with the same OAuth client if you prefer.

### Why did my Bot Connector trigger setup fail?

Setting up a Bot Connector involves multiple steps that need to propagate through Genesys internal systems. If propagation is slow, the setup can fail. Retrying after a couple of minutes usually succeeds. If the problem persists, reach out to ElevenLabs support.

### Will agents see conversation history after escalation?

Yes, past messages will appear as bot messages in the Genesys interface, so the agent can see the full conversation history.

### My Bot Connector is failing, how do I debug it?

In ElevenLabs, check for past conversations on your agent that originate from Genesys. These will have conversation IDs with a suffix `gn_xxxxxx` where the last six characters are the first characters of the connected Genesys conversation.
If there are errors in the transcript, for example failed tool calls, address these.

Also check if the agent takes longer than 10 seconds to reply, as Genesys only gives it a 10 second timeout.

If there are no past conversations, the error might be on the Genesys side.
In the Genesys Architect, check the execution history of your flow. Find it in the drop-down menu of the save button.

## Useful links

* [Genesys Cloud OAuth documentation](https://developer.genesys.cloud/authorization/platform-auth/use-client-credentials)
* [Genesys Architect overview](https://help.mypurecloud.com/articles/architect-overview/)
* [Genesys Bot Connector documentation](https://help.genesys.cloud/articles/about-genesys-bot-connector/)
* [Genesys Open Messaging documentation](https://help.genesys.cloud/articles/about-open-messaging/)
* [ElevenLabs Audio Connector for Genesys](https://elevenlabs.io/docs/eleven-agents/phone-numbers/c-caa-s-integrations/genesys)
