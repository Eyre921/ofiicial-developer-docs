---
title: "Shopmonkey"
source: https://elevenlabs.io/docs/reception-ai/integrations/shopmonkey.md
path: docs/reception-ai/integrations/shopmonkey
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Shopmonkey

With a [webhook tool](/docs/reception-ai/integrations/webhooks), your receptionist can add an appointment to your Shopmonkey calendar when a caller wants to bring their vehicle in.

> **Warning**
>
> Shopmonkey doesn't check for conflicts when an appointment is created this way, so your
> receptionist can double-book a slot. Tell callers the time is a request that your shop will
> confirm, or give your receptionist your open hours and bay limits in its instructions.

## Setup

### Create an API key

In Shopmonkey, an admin opens **Settings** → **Integration** → **API Keys** and selects **Get Started** or **Add New Key**. Select **Create API Key** and copy the key right away: Shopmonkey only shows it once. The key has the same permissions as the user who creates it.

### Create the webhook tool

In Reception.ai, go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `create_shopmonkey_appointment`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Description**      | "Add an appointment to the shop calendar once the caller has chosen a day and time. Confirm the time with them first."                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Method**           | POST                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **URL**              | `https://api.shopmonkey.cloud/v3/appointment`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Request Headers**  | `Authorization`: `Bearer ` followed by your API key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Body Parameters**  | `name` (string, required): "The service and the caller's name, for example: Oil change - Jane Doe."  `startDate` (string, required): "The start time in UTC, in ISO 8601 format, for example 2026-11-04T15:00:00.000Z."  `endDate` (string, required): "The end time in the same format. Use one hour after the start unless the caller's service takes longer."  `color` (string, required): "Always the exact value `blue`."  `note` (string, required): "The caller's name, phone number, vehicle year, make and model, and what they need." |
| **Assign to agents** | **Receptionist**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

Select **Enable**.

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) by booking an oil change. Check that the appointment appears on your Shopmonkey calendar at the right local time.

`color` must be one of `aqua`, `black`, `blue`, `brown`, `gray`, `green`, `orange`, `purple`, `red`, or `yellow`. Use a color your team doesn't use for other appointments, so phone bookings stand out.

## Limitations

* Shopmonkey's customer search takes a list of phone numbers, which webhook tools can't send. So your receptionist can't look up callers or link the appointment to a customer or vehicle record. The note holds the caller's details instead.
* The tool can't reschedule or cancel appointments. Those need the appointment ID in the URL.

## Troubleshooting

| Problem                                 | What to check                                                                                                |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| 401 from Shopmonkey                     | The header must be `Bearer ` followed by a current key, with a space after `Bearer`.                         |
| Appointments are at the wrong time      | Times must be in UTC. Add your shop's time zone to the receptionist's instructions so it converts correctly. |
| 400 about `color`                       | Use one of Shopmonkey's color names, in lowercase.                                                           |
| The appointment has no customer details | Make the description tell the receptionist to collect the caller's name, number, and vehicle first.          |
