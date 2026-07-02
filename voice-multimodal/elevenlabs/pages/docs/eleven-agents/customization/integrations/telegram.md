---
title: "Telegram"
source: https://elevenlabs.io/docs/eleven-agents/customization/integrations/telegram.md
path: docs/eleven-agents/customization/integrations/telegram
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Telegram

## Overview

Connect your ElevenLabs AI agents with Telegram to respond to messages sent to your bot. This integration enables your agents to receive incoming messages in private chats and groups, look up chat information, send replies, and react to messages through the Telegram Bot API.

## Setup

Open Telegram and start a conversation with [@BotFather](https://t.me/BotFather). Send `/newbot` and follow the prompts to choose a name and username for your bot. BotFather will reply with a bot token.

In the ElevenLabs integration setup, click **Connect** and paste the bot token from BotFather.

After connecting, enable the **Telegram Message** trigger and select the agent that should handle incoming messages. ElevenLabs will automatically register a webhook with Telegram so your bot starts receiving messages.

## Using the bot in groups

The bot does **not** need to be an admin of the group, and you do **not** need to disable Telegram's [privacy mode](https://core.telegram.org/bots/features#privacy-mode). With privacy mode on (the default), Telegram delivers messages that explicitly address the bot, which is exactly what this integration listens for:

* **`@`-mentions** of the bot's username, for example `@my_bot what's the status?`.
* **Replies to the bot's own messages**, including follow-up turns inside the same back-and-forth.

Messages that don't address the bot are ignored by design. The bot also ignores messages from other bots and does not act on edited or deleted messages.

Telegram applies privacy-mode and admin-role changes only to groups the bot joins **after** the
change. If you previously toggled privacy mode in [@BotFather](https://t.me/BotFather), or made
the bot a group admin to "fix" mentions, remove the bot from the group and add it back so the new
setting takes effect — that's typically what makes mentions start working, not the admin role
itself.

In group and supergroup chats the agent's reply is sent as a quote-reply to the triggering message, so the response stays visually anchored to the question even when the chat is busy. In private 1:1 chats the quote-reply is suppressed because it would be redundant.

## Agent tools

When you add Telegram tools to an agent, the following built-in tools are available:

| Tool                        | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `telegram_get_chat`         | Looks up metadata about the current chat (such as type, title, username, and description). The `chat_id` is bound to the current conversation and cannot be retargeted.                                                                                                                                                                                                                                     |
| `telegram_send_message`     | Sends a text message to the current chat. `chat_id` is bound; the model controls `text` and the optional `parse_mode` (`HTML`, `Markdown`, or `MarkdownV2`).                                                                                                                                                                                                                                                |
| `telegram_react_to_message` | Reacts to the triggering message with a single emoji from Telegram's bot-allowed [reaction set](https://core.telegram.org/bots/api#reactiontypeemoji) — useful when a short acknowledgment (`👍`, `🎉`, `❤`) is more natural than a text reply. Both `chat_id` and `message_id` are bound to the originating turn. Setting a new reaction replaces any reaction the bot previously set on the same message. |

Some chats restrict which emoji are allowed via Telegram's **Available reactions** setting. If a
reaction call is rejected, instruct the agent to fall back to a text reply.

## Dynamic variables

When an agent runs from Telegram, the following dynamic variables are available in prompts and tools:

| Variable                              | Description                                                                      |
| ------------------------------------- | -------------------------------------------------------------------------------- |
| `integration__telegram_chat_id`       | Telegram chat ID where the conversation is taking place.                         |
| `integration__telegram_message_id`    | Telegram `message_id` of the user message that triggered the current agent turn. |
| `integration__telegram_connection_id` | ElevenLabs integration connection ID.                                            |

See [dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables) for how to reference these in prompts and tool calls.

## Useful links

* [Telegram Bot API documentation](https://core.telegram.org/bots/api)
* [Privacy mode](https://core.telegram.org/bots/features#privacy-mode)
* [BotFather — create and manage bots](https://t.me/BotFather)
