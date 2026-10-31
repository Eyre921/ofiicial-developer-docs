---
title: "Airtable"
source: https://elevenlabs.io/docs/reception-ai/integrations/airtable.md
path: docs/reception-ai/integrations/airtable
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Airtable

Your receptionist can look up a caller in an Airtable table and add a new record, such as a lead or a callback request. Lookups use Airtable's API. New records go through an Airtable automation, because the API expects fields nested in a way webhook tools can't send.

## Look up records

### Create a personal access token

Go to [airtable.com/create/tokens](https://airtable.com/create/tokens) and create a token with the `data.records:read` scope. Under **Access**, add only the base your receptionist needs.

### Find the base and table IDs

Open the table in your browser. The URL contains the base ID, which starts with `app`, and the table ID, which starts with `tbl`.

### Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                                                                                          |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `find_airtable_record`                                                                                                                                                                                         |
| **Description**      | "Look up the caller in our customer table. Use it when a caller asks about an existing booking, order, or account."                                                                                            |
| **Method**           | GET                                                                                                                                                                                                            |
| **URL**              | `https://api.airtable.com/v0/BASE_ID/TABLE_ID`                                                                                                                                                                 |
| **Request Headers**  | `Authorization`: `Bearer ` followed by your token                                                                                                                                                              |
| **Query Parameters** | `filterByFormula` (string, required): "An Airtable formula that matches the caller, for example `{Phone} = '+14155550123'`. Use the field names Phone and Name."  `maxRecords` (number, required): "Always 5." |
| **Assign to agents** | **Receptionist**                                                                                                                                                                                               |

Select **Enable**.

Replace `Phone` and `Name` in the description with your table's field names, so your receptionist writes formulas that match.

## Add records

### Create an automation

In your base, open **Automations**, select **Create automation**, and choose the **When webhook received** trigger. Copy the webhook URL. Webhook triggers aren't on every Airtable plan.

### Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                     |
| -------------------- | ----------------------------------------------------------------------------------------- |
| **Name**             | `add_airtable_record`                                                                     |
| **Description**      | "Save a new lead when a caller wants a quote or a callback."                              |
| **Method**           | POST                                                                                      |
| **URL**              | The automation's webhook URL                                                              |
| **Body Parameters**  | One per field to fill, for example `name`, `phone`, and `request` (all strings, required) |
| **Assign to agents** | **Receptionist**                                                                          |

### Send a sample and map fields

[Test your receptionist](/docs/reception-ai/receptionist/testing) with a conversation that triggers the tool. In the automation, select **Test trigger** to load the request, then add a **Create record** action and map each body parameter to a field.

### Turn on the automation

Turn the automation on.

## Troubleshooting

| Problem                         | What to check                                                                                    |
| ------------------------------- | ------------------------------------------------------------------------------------------------ |
| 401 or 403 on lookups           | The token needs the `data.records:read` scope and access to this base.                           |
| 422 `INVALID_FILTER_BY_FORMULA` | The field names in the tool's description must match the table exactly, including case.          |
| Lookups return nothing          | Phone numbers must be stored in the same format your receptionist sends, such as `+14155550123`. |
| No records are added            | The automation must be on, and **Create record** must map fields from the webhook trigger.       |
| 429 from Airtable               | Airtable allows 5 requests per second per base. Reduce other API traffic on the base.            |
