---
title: "Google Sheets"
source: https://elevenlabs.io/docs/reception-ai/integrations/google-sheets.md
path: docs/reception-ai/integrations/google-sheets
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Google Sheets

Your receptionist can add a row to a Google Sheet for every call or lead, and look up a caller in a customer list you keep in a sheet. Google Sheets' API only accepts OAuth sign-ins, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

## Before you start

Give each sheet a header row. Zapier shows the headers as fields, so name them clearly:

* **Call log**, for example: `Date`, `Name`, `Phone`, `Email`, `Reason`, `Outcome`.
* **Customer list**, for example: `Phone`, `Name`, `Customer since`, `Notes`.

> **Warning**
>
> The sheets hold your callers' personal details. Share them only with people who need them, and
> connect a Google account that can only reach the sheets your receptionist uses, if you can.

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Google Sheets actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) and sign in to Google when Zapier asks. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action as listed.

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) with a short call. A new row appears in the call log.

## Actions

### Log the call

| Field                  | Value                                                                         |
| ---------------------- | ----------------------------------------------------------------------------- |
| **Zapier action**      | **Create Spreadsheet Row**                                                    |
| **Set in Zapier**      | **Spreadsheet** and **Worksheet**: your call log.                             |
| **Let the AI fill in** | Every column, such as the date, the caller's name and number, and the reason. |
| **Assign to**          | **Client**                                                                    |

> **Tip**
>
> Add a [procedure](/docs/reception-ai/receptionist/rules-and-procedures) so your receptionist logs
> the call before it ends.

### Look up the caller

| Field                  | Value                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------- |
| **Zapier action**      | **Lookup Spreadsheet Row**                                                         |
| **Set in Zapier**      | **Spreadsheet** and **Worksheet**: your customer list. **Lookup column**: `Phone`. |
| **Let the AI fill in** | **Lookup value**: the caller's phone number.                                       |
| **Assign to**          | **Client**                                                                         |

### Review calls from the dashboard

| Field                  | Value                                                             |
| ---------------------- | ----------------------------------------------------------------- |
| **Zapier action**      | **Lookup Spreadsheet Rows (Advanced)**                            |
| **Set in Zapier**      | **Spreadsheet** and **Worksheet**: your call log.                 |
| **Let the AI fill in** | The lookup column and value, for example `Date` and today's date. |
| **Assign to**          | **Assistant**                                                     |

Your assistant can then answer questions like "Who called about a quote today?".

## Limitations

* **Lookup Spreadsheet Row** returns the first matching row and only matches values exactly as written in the sheet.
* Your receptionist adds rows; it doesn't edit or delete them.
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                               | What to check                                                                                         |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| A Google Sheets action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.                    |
| An action shows **Changed** and isn't used            | You edited it in Zapier. Select **Update** in the **Tools** tab, for example after renaming a column. |
| Known callers aren't found                            | Store phone numbers in one format, such as `+14155550123`, and check the lookup column.               |
| Values land in the wrong columns                      | Check the header row, then edit the action in Zapier so its fields match the headers.                 |
