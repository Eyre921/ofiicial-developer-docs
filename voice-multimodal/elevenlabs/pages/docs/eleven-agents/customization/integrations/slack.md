---
title: "Slack"
source: https://elevenlabs.io/docs/eleven-agents/customization/integrations/slack.md
path: docs/eleven-agents/customization/integrations/slack
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Slack

## Overview

The Slack integration lets an ElevenLabs agent send and receive messages in Slack. Once connected, the agent replies in a thread when mentioned in a channel and maintains separate conversation context per thread.

## Setup

The integration offers two ways to connect:

* **OAuth** — install the shared ElevenLabs Slack app into your workspace. A single Slack workspace maps to a single ElevenLabs connection. Fastest setup, no Slack app management required.
* **Bring your own app** — connect using a Slack app you create and own. Use this when you need the bot to appear under your brand or when your workspace policies require apps to be installed by an admin.

### Option A — OAuth

The user installing the app must have permission to add apps to the target Slack workspace.

#### Open the integrations page

In the ElevenLabs dashboard, go to **Agents** > **Integrations** and select **Slack**.

#### Click Connect

Pick the **OAuth** credential and click **Connect**. You are redirected to Slack to choose which workspace to install the ElevenLabs app into and to approve the requested scopes.

#### Complete the redirect

After approval, Slack redirects you back to ElevenLabs and the connection is created. The Slack workspace ID is recorded automatically and used when configuring triggers.

### Option B — Bring your own Slack app

Use this if you want the bot to show up under your own app name and icon, or if your workspace requires apps to be reviewed and installed by your admin.

#### Create a Slack app

Go to [Slack API: Your Apps](https://api.slack.com/apps) and click **Create New App** > **From scratch**. Name the app and pick the Slack workspace to install it into.

#### Add bot scopes

Open **OAuth & Permissions** and add the following Bot Token Scopes:

`app_mentions:read`, `channels:history`, `channels:join`, `channels:manage`, `chat:write`, `files:read`, `groups:history`, `groups:write`, `im:history`, `reactions:write`.

Then click **Install to Workspace** and approve. Copy the **Bot User OAuth Token** (starts with `xoxb-`).

#### Copy the signing secret

Open **Basic Information** > **App Credentials** and copy the **Signing Secret**.

#### Create the connection in ElevenLabs

In the ElevenLabs dashboard, go to **Integrations**, click the **Add integration** button and choose **Slack**. Pick the **Bring your own app** credential. Paste the bot token and signing secret, then save. ElevenLabs verifies the token against Slack and records your workspace id.

After the connection is created, the connection page shows two webhook URLs derived from your Slack app's identity. The same Slack app, reconnected from the same ElevenLabs workspace, always produces the same URLs — so you can delete and recreate the connection without re-updating your Slack app's configuration. Keep that page open for the next steps.

#### Configure Event Subscriptions

In your Slack app, open **Event Subscriptions**, enable events, and paste the **Events URL** from the ElevenLabs connection page into **Request URL**. Slack will verify the URL using the signing secret you provided.

Subscribe to bot events based on how you want the agent to behave in channels:

* **Mention-only** — subscribe to `app_mention`. The agent responds only when a user `@`-mentions the bot.
* **All messages** — subscribe to `message.channels` and `message.groups`. The agent responds to every message in channels the bot is in, without requiring a mention.

If you use the **SlackDirectMessage** trigger, also subscribe to `message.im`.

Do not subscribe to both `app_mention` and the `message.*` channel events unless you intend to handle duplicate deliveries. When a user `@`-mentions the bot, Slack can send both an `app_mention` event and a `message` event for the same message, which causes the agent to respond twice.

#### Configure Interactivity

Open **Interactivity & Shortcuts**, enable interactivity, and paste the **Interactivity URL** from the ElevenLabs connection page into **Request URL**.

#### Reinstall if prompted

If Slack prompts you to reinstall the app after changing scopes or events, do so to apply the changes.

A Slack workspace can only be connected once via the shared ElevenLabs OAuth app. Reinstalling
from a different ElevenLabs workspace returns a `duplicate Slack workspace` error — remove the
existing connection first. Bring-your-own-app connections are independent and do not conflict.

## OAuth scopes

The ElevenLabs Slack app requests the following scopes:

| Scope               | Purpose                                                                                |
| ------------------- | -------------------------------------------------------------------------------------- |
| `app_mentions:read` | Receive messages where the bot is `@`-mentioned.                                       |
| `channels:history`  | Read messages in public channels the bot is in.                                        |
| `channels:join`     | Allow the bot to auto-join public channels when a trigger is created.                  |
| `channels:manage`   | Perform channel management actions.                                                    |
| `chat:write`        | Post messages in channels and threads.                                                 |
| `files:read`        | Download files attached to messages so the agent can read images and PDFs.             |
| `groups:history`    | Read messages in private channels the bot is in.                                       |
| `groups:write`      | Operate in private channels.                                                           |
| `im:history`        | Read messages in direct message channels with the bot.                                 |
| `reactions:write`   | Add and remove reactions, used for the thinking indicator on messages and agent tools. |

## Agent tools

When you add Slack tools to an agent, the following built-in tools are available:

| Tool                    | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `slack_add_reaction`    | Adds an emoji reaction. By default, channel and message `ts` are filled from `integration__slack_channel_id` and `integration__slack_trigger_message_ts`; the model only chooses the emoji shortcode (no colons), for example `thumbsup`. Outside Slack-triggered conversations those variables are absent unless you set them—adjust the tool schema if the model must pass channel and `ts` explicitly. |
| `slack_remove_reaction` | Removes an emoji reaction (same defaults as add). Per Slack, the calling bot may only remove reactions it originally added; see [reactions.remove](https://docs.slack.dev/reference/methods/reactions.remove).                                                                                                                                                                                            |

## Removing the connection

Removing the connection from the **Integrations** page uninstalls the ElevenLabs Slack app from the Slack workspace. After removal, the bot is no longer present in any channel.

For bring-your-own-app connections, ElevenLabs cannot uninstall an app it does not own — removing the connection only deletes the local mapping. To fully remove the bot from your Slack workspace, uninstall the app from your Slack admin settings.

## Configure the trigger

The integration exposes a single trigger, **SlackMessage**. It fires when the bot sees a new user message in a configured channel.

#### Add a SlackMessage trigger

On your agent's configuration page, add a new trigger and select **SlackMessage**.

#### Pick the agent and channel

Configure the trigger fields:

* **Agent**: the agent that handles the conversation.
* **Channel ID**: the Slack channel ID, for example `C0123456789`. The UI provides a deep link to open the channel in Slack.

#### Save the trigger

Save the trigger. ElevenLabs automatically invites the bot to public channels. Removing the trigger later causes the bot to leave that channel.

Slack does not allow apps to auto-join private channels. For a private channel, run `/invite
  @Eleven` in that channel after saving the trigger so the bot can see messages.

Only one trigger is allowed per `(Slack workspace, channel)` pair. Edit the existing trigger
instead of creating a duplicate.

## Configure the DM trigger

The **SlackDirectMessage** trigger lets any Slack user chat with the agent by sending a direct message to the bot. Unlike the channel trigger, no `@` mention is needed — every message a user sends in a DM with the bot is processed.

#### Add a SlackDirectMessage trigger

On your agent's configuration page, add a new trigger and select **SlackDirectMessage**.

#### Pick the agent

Select the **Agent** that handles DM conversations.

#### Save the trigger

Save the trigger. Any Slack user in the workspace can now open a DM with the bot and start a
conversation.

For BYO apps, make sure you have subscribed to the `message.im` bot event and added the
`im:history` bot scope. Reinstall the app if prompted after adding these.

Only one DM trigger is allowed per Slack connection. To change the agent, edit the existing
trigger.

## Talking to the bot in Slack

Once the trigger is active and the bot is in the channel, start a conversation in a channel thread. How you continue the thread depends on your Slack app's event subscriptions (OAuth uses mention-only behavior).

### Mention-only (`app_mention`)

#### Start a thread with a mention

Mention the bot in a channel to start a new thread, for example `@Eleven what's the status of
    order 1234?`. The bot replies in a thread under that message.

#### Continue the thread

Mention the bot again on every message you want it to respond to, including follow-ups inside
the same thread. Messages without a mention are ignored.

### All messages (`message.channels`, `message.groups`)

#### Start a thread

Send any message in a channel where the bot is present. The bot replies in a thread under that
message. You do not need to `@`-mention the bot.

#### Continue the thread

Reply in the same thread without mentioning the bot. Every new message in the thread is
processed.

While the bot is generating a response, it adds a `:eyes:` reaction to the user's triggering message and removes it once the reply is posted.

The **Respond to messages from** setting on the Channel Message trigger controls who can trigger the agent:

* **Only humans** (default): messages from other bots and from Slack workflows are ignored. This is the safe default and preserves the behavior of existing triggers.
* **Humans and bots**: messages from other bots and workflow-posted messages (including legacy `bot_message` events) also trigger the agent.

The bot always ignores its own messages — using the bot-user and app identity in Slack's signed webhook — under either setting, so it never replies to itself even when self-mentioned. It also continues to ignore edited messages (`message_changed`) and deleted messages (`message_deleted`). It handles `message` and `app_mention` events and works in both public and private channels.

Legacy bot events that contain only a `bot_id` identify the sender but not the receiving app. They
are treated as messages from another bot; self-loop detection for this Slack app uses the bot-user
or app identity included in modern Slack event payloads.

If your Slack app subscribes to both `app_mention` and `message.channels` / `message.groups`, a
single `@`-mention can trigger two agent responses. Subscribe to one mode or the other.

## Conversation model

The conversation ID is deterministic per `(agent_id, channel_id, thread_ts)`:

* A new Slack thread maps to a new ElevenLabs conversation.
* Continuing the same thread continues the same conversation, including transcript history and dynamic variables.

When constructing chat history, the bot reads the Slack thread directly. Messages from Slack members and other bots are treated as user turns, while the bot's own messages are treated as agent turns. Mentions of the bot user (`<@BOT_USER_ID>`) are rewritten to `@<agent_name>` before the agent processes them.

### Dynamic variables

When an agent runs from Slack, the following dynamic variables are available in prompts and tools:

| Variable                                | Description                                                                                  |
| --------------------------------------- | -------------------------------------------------------------------------------------------- |
| `integration__slack_channel_id`         | Slack channel ID.                                                                            |
| `integration__slack_thread_ts`          | Slack thread timestamp.                                                                      |
| `integration__slack_user_id`            | Slack sender ID. This is a user ID, or a bot ID for legacy bot events without a user.        |
| `integration__slack_team_id`            | Slack workspace (team) ID.                                                                   |
| `integration__slack_connection_id`      | ElevenLabs integration connection ID.                                                        |
| `integration__slack_trigger_message_ts` | Slack `ts` of the message that triggered this agent turn (unique message ID in the channel). |

See [dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables) for how to reference these in prompts and tool calls.

## Troubleshooting

### File attachments not working

When a user attaches an image or PDF in Slack but the agent does not process it (or behaves as if no file was sent), work through the checks below.

#### Confirm the Slack app has files:read

The bot needs the `files:read` bot scope to download attachments from Slack.

* **Bring your own app** — open your app at [Slack API: Your Apps](https://api.slack.com/apps), go to **OAuth & Permissions**, and verify `files:read` is listed under **Bot Token Scopes**. If you added it recently, reinstall the app to your workspace so the token picks up the new scope.

#### Confirm the agent model supports file input

File attachments are only forwarded when the agent's LLM supports multimodal input — image input and/or document (PDF) input, depending on the file type. In the agent configuration, open the **Agent** tab and check the selected model. If the model does not support the attachment type, switch to a model that does.

#### Enable Allow file attachments in agent settings

On the agent's configuration page, open **Settings** > **Advanced**. Under **Multimodal input**, turn on **Allow file attachments**. See [file input](/docs/eleven-agents/customization/multimodal-input#file-input) for the full setup. Without this setting, Slack attachments are ignored even when the Slack app and model support files.

## Useful links

* [Slack API documentation](https://api.slack.com/docs)
* [Slack App permissions](https://api.slack.com/scopes)
