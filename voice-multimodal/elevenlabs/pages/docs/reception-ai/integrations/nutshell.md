---
title: "Nutshell"
source: https://elevenlabs.io/docs/reception-ai/integrations/nutshell.md
path: docs/reception-ai/integrations/nutshell
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Nutshell

Your receptionist can recognize callers who are already in Nutshell, and add new callers as people with a lead for your team to follow up. Looking up callers uses a [webhook tool](/docs/reception-ai/integrations/webhooks). Adding people and leads goes through [Zapier](/docs/reception-ai/integrations/zapier), because Nutshell's API needs lists and nested values to create records, which webhook tools can't send.

## Look up callers

### Create an API key

In Nutshell, select **Settings** in the lower-left corner, then **API keys** under **Connections**. Select **Add API key** and choose **API + user impersonation**, which Zapier needs too. Copy the key.

### Build the authorization header

Nutshell's API uses your Nutshell email address as the username and the API key as the password. Encode them in a terminal, replacing both values and keeping the colon between them:

```bash
printf 'YOUR_EMAIL:YOUR_API_KEY' | base64
```

The header value is `Basic ` followed by the output.

> **Warning**
>
> Don't paste your API key into an online encoder. Anyone with the key or the encoded header can
> read and change your Nutshell data.

### Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                    |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `find_nutshell_person`                                                                                                                   |
| **Description**      | "Find the caller in our CRM by phone number, name, or email. Use it at the start of a call to check whether they're an existing client." |
| **Method**           | GET                                                                                                                                      |
| **URL**              | `https://app.nutshell.com/rest/contacts`                                                                                                 |
| **Request Headers**  | `Authorization`: `Basic ` followed by the encoded value                                                                                  |
| **Query Parameters** | `q` (string, required): "The caller's phone number, full name, or email address."                                                        |
| **Assign to agents** | **Receptionist**                                                                                                                         |

Select **Enable**.

## Add people and leads

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Nutshell actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), connect your Nutshell account with the API key and add these actions:

* **Create Person**: let the AI fill in the caller's name, phone number, and email address.
* **Create Lead**: set the source, pipeline, and assignee as fixed values, and let the AI fill in a description of what the caller wants and the person it's for.

> **Tip**
>
> To record the call on the person's timeline, also add **Log Activity** and let the AI fill in a
> short summary.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign the Nutshell actions to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) with a call from a number saved on a Nutshell person, then as a new caller who wants a quote. The new person and their lead appear in Nutshell.

## Limitations

* Zapier's Nutshell app has no action to create a follow-up task. The lead's assignee sees new leads in Nutshell instead.
* Zapier's Nutshell app can't check anyone's availability, so your receptionist can't book meetings in Nutshell. Use Reception's own booking with [Google Calendar](/docs/reception-ai/integrations/google-calendar).
* Each Zapier action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                          | What to check                                                                                          |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| 401 from Nutshell                                | Encode your Nutshell email address, a colon, and the key, and start the header value with `Basic `.    |
| Known callers aren't found                       | Try a test call from a number saved on a person in Nutshell, or ask the caller for their name instead. |
| The receptionist creates duplicate people        | Tell it in the lookup tool's description to add a person only when the caller wasn't found.            |
| A Nutshell action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.                     |
| Zapier can't connect to Nutshell                 | Use an API key with **API + user impersonation**.                                                      |
