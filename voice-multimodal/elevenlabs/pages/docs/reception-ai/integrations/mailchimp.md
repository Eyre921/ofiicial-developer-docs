---
title: "Mailchimp"
source: https://elevenlabs.io/docs/reception-ai/integrations/mailchimp.md
path: docs/reception-ai/integrations/mailchimp
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Mailchimp

Your receptionist can sign callers up to your mailing list. It confirms their email address, then adds them to your Mailchimp audience through Mailchimp's Marketing API. Mailchimp sends each new contact a confirmation email before they're subscribed.

## Before you start

You need these values from Mailchimp:

| Value             | Where to find it                                                                |
| ----------------- | ------------------------------------------------------------------------------- |
| **API key**       | Profile → **Extras** → **API keys** → **Create A Key**                          |
| **Server prefix** | The end of the API key after the dash, for example `us21`                       |
| **Audience ID**   | **Audience** → **All contacts** → **Settings** → **Audience name and defaults** |

Mailchimp authenticates API keys with HTTP basic auth. Build the header value on your computer:

```bash
printf 'reception:YOUR_API_KEY' | base64
```

## Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                        |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `add_to_mailing_list`                                                                                                                        |
| **Description**      | "Add the caller to the mailing list. Only use it after the caller has asked to join and has confirmed their email address letter by letter." |
| **Method**           | POST                                                                                                                                         |
| **URL**              | `https://SERVER_PREFIX.api.mailchimp.com/3.0/lists/AUDIENCE_ID/members`                                                                      |
| **Request Headers**  | `Authorization` set to `Basic ` followed by the encoded value                                                                                |
| **Body Parameters**  | `email_address` (string, required): "The caller's email address."  `status` (string, required): "Always the exact value `pending`."          |
| **Assign to agents** | **Receptionist**                                                                                                                             |

Select **Enable**, then [test your receptionist](/docs/reception-ai/receptionist/testing) by asking to join the mailing list. The contact appears in your audience as **Pending** until they confirm the email.

> **Warning**
>
> `pending` sends Mailchimp's opt-in confirmation email. A caller saying yes on the phone is not
> written consent in every country, so keep double opt-in unless you're sure you don't need it.

The tool sends only top-level fields, so it can't fill merge fields such as first name, which Mailchimp nests under `merge_fields`. To add them, route the signup through [Zapier](/docs/reception-ai/integrations/zapier) instead.

## Troubleshooting

| Problem            | What to check                                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------------------------- |
| 401 from Mailchimp | Re-encode the header value and check that the server prefix in the URL matches the API key.                 |
| 404 from Mailchimp | Check the audience ID in the URL.                                                                           |
| `Member Exists`    | The address is already on the list. Your receptionist can tell the caller they're already subscribed.       |
| `Invalid Resource` | The email address is malformed. Ask your receptionist to spell addresses back to callers before submitting. |
