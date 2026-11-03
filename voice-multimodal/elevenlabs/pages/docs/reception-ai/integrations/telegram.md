---
title: "Telegram"
source: https://elevenlabs.io/docs/reception-ai/integrations/telegram.md
path: docs/reception-ai/integrations/telegram
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Telegram

A Telegram bot lets your receptionist message you or your team's group during a call, for example when a caller asks for a callback or reports something urgent. The [webhook tool](/docs/reception-ai/integrations/webhooks) calls Telegram's Bot API `sendMessage` method.

## Create a bot and find the chat ID

### Create the bot

In Telegram, open a chat with [@BotFather](https://t.me/BotFather), send `/newbot`, and follow the prompts to name it. BotFather replies with a bot token, such as `123456789:AA...`. Treat it as a secret: anyone who has it controls the bot.

### Start a chat with the bot

Bots can only message chats they're in.

* **To message yourself:** open a chat with your new bot and select **Start**.
* **To message a group:** add the bot to the group, then send a message that mentions it, such as `/start@YOUR_BOT_NAME`.

### Find the chat ID

In a browser, open `https://api.telegram.org/botBOT_TOKEN/getUpdates`, with your bot token in place of `BOT_TOKEN`. Find your message in the response and copy the number after `"chat":{"id":`. A group's ID is negative, for example `-1001234567890`; keep the minus sign.

If the response is empty, send the bot another message and reload the page.

## Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                                             |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `notify_team_in_telegram`                                                                                                                                         |
| **Description**      | "Message the team on Telegram. Use it when a caller asks for a callback, wants to speak to a person, or reports an urgent problem."                               |
| **Method**           | POST                                                                                                                                                              |
| **URL**              | `https://api.telegram.org/botBOT_TOKEN/sendMessage`, with your bot token in place of `BOT_TOKEN`                                                                  |
| **Body Parameters**  | `chat_id` (string, required): "Always the exact value `CHAT_ID`."  `text` (string, required): "The message: the caller's name, phone number, and what they need." |
| **Assign to agents** | **Receptionist**                                                                                                                                                  |

Replace `CHAT_ID` in the description with your chat ID. The URL contains your bot token, so treat it as a secret too.

Select **Enable**, then [test your receptionist](/docs/reception-ai/receptionist/testing) by asking for a callback. The bot posts the message in the chat.

> **Tip**
>
> To message several chats, create one tool per chat ID. The same bot can post to all of them.

## Troubleshooting

| Problem                       | What to check                                                                                                              |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Telegram returns 401          | The bot token in the URL is wrong or was revoked in BotFather. The URL must have `bot` right before the token.             |
| `Bad Request: chat not found` | Check the chat ID, including the minus sign for groups, and that you started a chat with the bot or added it to the group. |
| `Forbidden: bot was kicked`   | The bot was removed from the group. Add it back.                                                                           |
| `getUpdates` shows nothing    | In groups, bots only see messages that mention them. Send `/start@YOUR_BOT_NAME` and reload.                               |
| The receptionist never posts  | Make the tool's description name the situations where it should post.                                                      |
