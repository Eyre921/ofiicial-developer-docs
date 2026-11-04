---
title: "JobNimbus"
source: https://elevenlabs.io/docs/reception-ai/integrations/jobnimbus.md
path: docs/reception-ai/integrations/jobnimbus
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# JobNimbus

With the [webhook tool](/docs/reception-ai/integrations/webhooks) below, your receptionist can add a new caller to JobNimbus as a contact in your lead workflow, with their phone number, address, and what they need, so your team can follow up.

## Before you start

1. In JobNimbus, select your profile icon in the top-right corner, then **Settings** → **API**, and create a new API key.
2. Choose an **Access Profile** that can create contacts and nothing more than you need. The key keeps the permissions the profile had when you created it.
3. Copy the full API key, not the **Key ID**. JobNimbus only shows it once.

The tool sends the key in the `Authorization` request header as `Bearer YOUR_API_KEY`.

> **Warning**
>
> The API key gives access to your JobNimbus data. Store it safely and don't share it. New keys
> expire after one year, so create a replacement before then.

You also need the exact names of the contact workflow and status new leads should land in, as they appear in your JobNimbus settings, for example `Customer` and `Lead`.

## Create the tool

Go to **Integrations**, select **Add integration**, choose **Webhook Tool**, and fill in the fields below.

| Field                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `create_jobnimbus_contact`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Description**      | "Add the caller to our CRM as a new lead when they need work done and haven't used us before."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Method**           | POST                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **URL**              | `https://app.jobnimbus.com/api1/contacts`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Request Headers**  | `Authorization`: `Bearer YOUR_API_KEY`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Body Parameters**  | `first_name` (string, required): "The caller's first name."  `last_name` (string, required): "The caller's last name."  `record_type_name` (string, required): "Always the exact value `Customer`."  `status_name` (string, required): "Always the exact value `Lead`."  `mobile_phone` (string, required): "The caller's phone number, digits only."  `email` (string): "The caller's email address, if they gave one."  `address_line1` (string): "The street address where the work is needed."  `city` (string): "The city of that address."  `state_text` (string): "The state, as a two-letter code."  `zip` (string): "The ZIP code."  `description` (string, required): "What the caller needs, when they're available, and anything else they told you." |
| **Assign to agents** | **Receptionist**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

Replace `Customer` and `Lead` with your own workflow and status names.

Select **Enable**, then [test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller who needs a roof inspection. The contact appears in JobNimbus in your lead status.

> **Tip**
>
> Add a [procedure](/docs/reception-ai/receptionist/rules-and-procedures) telling your receptionist
> to collect the full address before it adds the caller.

## Limitations

* Searching JobNimbus contacts needs a JSON search filter, so this tool can't look callers up. A returning caller can be added twice.
* Jobs, tasks, and notes link to a contact through nested fields, which webhook tools can't send. The contact's description holds the call details instead.

To look callers up by email and create jobs linked to their contact, use JobNimbus's **Find Contact by Email**, **Create Contact**, and **Create Job** actions through [Zapier](/docs/reception-ai/integrations/zapier).

## Troubleshooting

| Problem                            | What to check                                                                                                     |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 401 or 403 from JobNimbus          | The header value must be `Bearer` followed by the full API key, not the **Key ID**. Check the key hasn't expired. |
| Error about the workflow or status | `record_type_name` and `status_name` must match a contact workflow and one of its statuses exactly.               |
| 403 with a permissions message     | The key's **Access Profile** can't create contacts. Create a new key with a profile that can.                     |
| Contacts have no address           | Make the description tell the receptionist to ask for the full address before adding the caller.                  |
