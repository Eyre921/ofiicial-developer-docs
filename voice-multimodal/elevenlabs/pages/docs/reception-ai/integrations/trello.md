---
title: "Trello"
source: https://elevenlabs.io/docs/reception-ai/integrations/trello.md
path: docs/reception-ai/integrations/trello
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Trello

Your receptionist can add a card to a Trello list when a caller asks for a callback, a quote, or anything else your team should follow up on. A [webhook tool](/docs/reception-ai/integrations/webhooks) creates the card through Trello's REST API.

## Before you start

### Get an API key

Go to the [Power-Up admin portal](https://trello.com/apps/admin), create a Power-Up for your workspace (the name doesn't matter), open its **Trello Auth** tab, and select **Generate a new API key**.

### Generate a token

Select the **Token** link next to your API key, or open this URL in a browser with your API key in place of `API_KEY`:

```
https://trello.com/1/authorize?expiration=never&scope=read,write&response_type=token&name=Reception&key=API_KEY
```

Select **Allow** and copy the token. It can read and change every board you can, so consider generating it from an account that's only a member of the board you need.

### Find the list ID

Open the board in your browser, add `.json` to the end of its URL, and load the page. Search for the list's name; the `id` value next to it is the list ID.

## Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                                                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `create_trello_card`                                                                                                                                                                                                                |
| **Description**      | "Create a card for the team whenever you promise the caller a follow-up, or the caller asks for something the team must handle."                                                                                                    |
| **Method**           | POST                                                                                                                                                                                                                                |
| **URL**              | `https://api.trello.com/1/cards?idList=LIST_ID`                                                                                                                                                                                     |
| **Request Headers**  | `Authorization`: `OAuth oauth_consumer_key="API_KEY", oauth_token="TOKEN"`                                                                                                                                                          |
| **Body Parameters**  | `name` (string, required): "Short title with the caller's name and what they need, for example: Call back Jane Doe about a quote."  `desc` (string, required): "The caller's name, phone number, and the details of their request." |
| **Assign to agents** | **Receptionist**                                                                                                                                                                                                                    |

Type `?idList=LIST_ID` into the URL field itself, with your list ID. Don't add `idList` as a query parameter: query parameters are filled in by the AI, while text in the URL is sent exactly as written.

> **Note**
>
> Trello also accepts the key and token in the URL, as `&key=API_KEY&token=TOKEN`. That works too,
> but the header keeps them out of the URL. If you put them in the URL, treat the whole URL as a
> secret.

Select **Enable**, then [test your receptionist](/docs/reception-ai/receptionist/testing) by asking for a callback. The card appears at the bottom of the list.

## Troubleshooting

| Problem                              | What to check                                                                                                                                |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Trello returns 401                   | Check the header: the key and token must each be in double quotes, separated by a comma and a space. Regenerate the token if it was revoked. |
| `invalid value for idList`           | The list ID in the URL is wrong. Use the list's `id`, not the board's.                                                                       |
| Trello returns 404 or no access      | The token's user must be a member of the board.                                                                                              |
| The receptionist never creates cards | Make the tool's description name the situations where it should create one.                                                                  |
