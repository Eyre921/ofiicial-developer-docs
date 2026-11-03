---
title: "HighLevel"
source: https://elevenlabs.io/docs/reception-ai/integrations/highlevel.md
path: docs/reception-ai/integrations/highlevel
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# HighLevel

HighLevel is also known as GoHighLevel, and its API runs under the LeadConnector name. With a [webhook tool](/docs/reception-ai/integrations/webhooks), your receptionist can save each caller as a contact in your HighLevel sub-account. If the caller is already a contact, HighLevel updates the existing record instead of creating a duplicate.

## Setup

### Create a private integration token

In your HighLevel sub-account, open **Settings** → **Private Integrations** and select **Create New Integration**. Give it a name, select only the scopes to view and edit contacts, and create it. Copy the token right away: HighLevel only shows it once.

If **Private Integrations** isn't in your settings, ask your agency admin to give you access to it.

### Find your location ID

Open **Settings** → **Business Profile** in the same sub-account and copy the **Location ID**.

### Create the webhook tool

In Reception.ai, go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `save_highlevel_contact`                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Description**      | "Save the caller as a contact in our CRM once you know their name and phone number. Use it on every call from a new or returning customer."                                                                                                                                                                                                                                                                                                                           |
| **Method**           | POST                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **URL**              | `https://services.leadconnectorhq.com/contacts/upsert`                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Request Headers**  | `Authorization`: `Bearer ` followed by your token  `Version`: `2021-07-28`                                                                                                                                                                                                                                                                                                                                                                                            |
| **Body Parameters**  | `locationId` (string, required): "Always the exact value `LOCATION_ID`."  `firstName` (string, required): "The caller's first name."  `lastName` (string): "The caller's last name, if they gave it."  `phone` (string, required): "The caller's phone number in international format, for example +14155550123."  `email` (string): "The caller's email address, if they gave it."  `source` (string, required): "Always the exact value `Reception.ai phone call`." |
| **Assign to agents** | **Receptionist**                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

Replace `LOCATION_ID` with the ID you copied. Select **Enable**.

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) with a call where you give your name and number. The contact appears in HighLevel under **Contacts**. Call again with the same number: HighLevel updates that contact rather than adding a new one.

> **Warning**
>
> The token can read and change your contacts. Keep it out of shared documents, and delete the
> private integration in HighLevel if it leaks.

HighLevel decides whether a caller is already a contact using the sub-account's **Allow Duplicate Contact** setting. If that setting matches on both email and phone, it checks them in the order the setting lists.

> **Tip**
>
> To do more after a call, such as opening an opportunity or alerting your team, build a HighLevel
> workflow that starts with the **Inbound Webhook** trigger. Point a second webhook tool at the
> workflow's URL with the fields you need, then map those fields inside the workflow. Treat the
> workflow URL as a secret. HighLevel lists Inbound Webhook as a premium trigger, so check your plan
> for usage charges.

## Limitations

* HighLevel's MCP server requires an OAuth sign-in, which Reception.ai doesn't support, so use the webhook tool.
* Tags and custom fields are lists in HighLevel's API, and webhook tools send flat values. Set them with a workflow instead.
* Adding notes or tasks needs the contact's ID in the URL, which a webhook tool can't fill in during a call. Use an **Inbound Webhook** workflow for these.

## Troubleshooting

| Problem                          | What to check                                                                                                     |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 401 from HighLevel               | The `Authorization` header must be `Bearer ` followed by the token, with a space after `Bearer`.                  |
| 403 from HighLevel               | The token needs the contact scopes, and `locationId` must be the sub-account the token was created in.            |
| HighLevel rejects the version    | The `Version` header must be exactly `2021-07-28`. If HighLevel's API docs list a newer required value, use that. |
| Returning callers are duplicated | Check the **Allow Duplicate Contact** setting, and that phone numbers are saved in the same international format. |
| The contact has no name          | Make the tool's description tell the receptionist to ask for the caller's name before saving them.                |
