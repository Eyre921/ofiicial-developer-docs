---
title: "Monday.com"
source: https://elevenlabs.io/docs/reception-ai/integrations/monday.md
path: docs/reception-ai/integrations/monday
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Monday.com

Your receptionist can add an item to a Monday.com board, such as a new lead or a callback request, and find an item by name. Monday.com's API is GraphQL: every request is a `POST` with one `query` field, so each tool gives your receptionist a query template to fill in.

## Before you start

| Value         | Where to find it                                        |
| ------------- | ------------------------------------------------------- |
| **API token** | Profile picture → **Developers** → **My access tokens** |
| **Board ID**  | The number after `/boards/` in the board's URL          |

The token acts as you, with your access to every board.

## Create an item

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| **Name**             | `create_monday_item`                                                                              |
| **Description**      | "Add a callback request to the team's board. Use it whenever you promise the caller a follow-up." |
| **Method**           | POST                                                                                              |
| **URL**              | `https://api.monday.com/v2`                                                                       |
| **Request Headers**  | `Authorization`: your API token, without `Bearer`                                                 |
| **Body Parameters**  | `query` (string, required), with the description below                                            |
| **Assign to agents** | **Receptionist**                                                                                  |

Use this description for `query`, with your board ID in place of `1234567890`:

```text
A GraphQL mutation in exactly this form, changing only ITEM_NAME:
mutation { create_item(board_id: 1234567890, item_name: "ITEM_NAME") { id } }
ITEM_NAME is the caller's name, phone number, and request, without double quotes.
```

Select **Enable**.

## Find an item

Create a second webhook tool with the same method, URL, and header.

| Field               | Value                                                                                                     |
| ------------------- | --------------------------------------------------------------------------------------------------------- |
| **Name**            | `find_monday_item`                                                                                        |
| **Description**     | "Find the caller's item on the board by its exact name. Use it when a caller asks about an existing job." |
| **Body Parameters** | `query` (string, required), with the description below                                                    |

```text
A GraphQL query in exactly this form, changing only ITEM_NAME:
query { items_page_by_column_values(board_id: 1234567890, limit: 5, columns: [{column_id: "name", column_values: ["ITEM_NAME"]}]) { items { name column_values { text column { title } } } } }
```

[Test your receptionist](/docs/reception-ai/receptionist/testing) with a callback request, then ask about it in a second conversation.

## Limitations

The create tool only sets the item name. Filling status, date, or people columns needs a JSON value inside the GraphQL query, which is hard for your receptionist to write reliably. To set columns, use Monday.com's **Create Item** action through [Zapier](/docs/reception-ai/integrations/zapier).

## Troubleshooting

| Problem              | What to check                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------------- |
| `Not Authenticated`  | The header must hold the token on its own, without `Bearer`.                                              |
| `Parse error on ...` | The receptionist changed the query's shape. Make the `query` description stricter, or shorten item names. |
| Items aren't found   | The lookup matches the full item name exactly.                                                            |
| `Board not found`    | Check the board ID and that the token's owner can see the board.                                          |
