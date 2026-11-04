---
title: "FieldPulse"
source: https://elevenlabs.io/docs/reception-ai/integrations/fieldpulse.md
path: docs/reception-ai/integrations/fieldpulse
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# FieldPulse

With the [webhook tools](/docs/reception-ai/integrations/webhooks) below, your receptionist can recognize callers who are already in FieldPulse, add new callers as leads, and leave a comment on the customer with what they need, so your team can follow up.

## Before you start

FieldPulse issues API keys on request. Contact FieldPulse support at [support@fieldpulse.com](mailto:support@fieldpulse.com) or through the in-app chat and ask for an API key. Every tool below sends it in the `x-api-key` request header.

> **Warning**
>
> The API key can read and change your FieldPulse data. Store it safely and don't share it.

## Create the tools

For each tool, go to **Integrations**, select **Add integration**, choose **Webhook Tool**, and set **Assign to agents** to **Receptionist**.

### Find a caller

| Field                | Value                                                                                                     |
| -------------------- | --------------------------------------------------------------------------------------------------------- |
| **Name**             | `find_fieldpulse_customer`                                                                                |
| **Description**      | "Find the caller in our customer list by name or phone number. Use it at the start of a call about work." |
| **Method**           | GET                                                                                                       |
| **URL**              | `https://ywe3crmpll.execute-api.us-east-2.amazonaws.com/stage/customers`                                  |
| **Request Headers**  | `x-api-key`: your API key                                                                                 |
| **Query Parameters** | `search` (string, required): "The caller's full name or phone number."                                    |

### Add a new customer

| Field               | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**            | `create_fieldpulse_customer`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Description**     | "Add the caller as a new customer when `find_fieldpulse_customer` didn't find them."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Method**          | POST                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **URL**             | `https://ywe3crmpll.execute-api.us-east-2.amazonaws.com/stage/customers`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Request Headers** | `x-api-key`: your API key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Body Parameters** | `first_name` (string, required): "The caller's first name."  `last_name` (string, required): "The caller's last name."  `phone` (string, required): "The caller's phone number, including the area code."  `email` (string): "The caller's email address, if they gave one."  `status` (string, required): "Always the exact value `lead`."  `service_address_1` (string): "The street address where the work is needed."  `service_address_city` (string): "The city of that address."  `service_address_state` (string): "The state."  `service_address_zip_code` (string): "The ZIP code." |

### Log the call details

| Field               | Value                                                                                                                                                                                                                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**            | `add_fieldpulse_comment`                                                                                                                                                                                                                                                                                    |
| **Description**     | "Leave a comment on the caller's customer record with what they need. Use it once you have their customer id."                                                                                                                                                                                              |
| **Method**          | POST                                                                                                                                                                                                                                                                                                        |
| **URL**             | `https://ywe3crmpll.execute-api.us-east-2.amazonaws.com/stage/comments`                                                                                                                                                                                                                                     |
| **Request Headers** | `x-api-key`: your API key                                                                                                                                                                                                                                                                                   |
| **Body Parameters** | `commentable_type` (string, required): "Always the exact value `customer`."  `commentable_id` (number, required): "The customer's id, from `find_fieldpulse_customer` or `create_fieldpulse_customer`."  `text` (string, required): "What the caller needs, when they're available, and how to reach them." |

Select **Enable** on each tool, then [test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller who needs a repair. The customer appears in FieldPulse as a lead, with your receptionist's comment.

> **Tip**
>
> Add a [procedure](/docs/reception-ai/receptionist/rules-and-procedures) for new work: find the
> caller, add them if they aren't found, then log the call details.

## Limitations

* Jobs need a job type, a status, and billing details from your FieldPulse account, so your receptionist doesn't create them. Your team turns the lead into a job.
* Your receptionist can't check technician availability or book a time.
* Webhook tools can't send lists, so these tools can't add tags or custom fields to a customer.

## Troubleshooting

| Problem                    | What to check                                                                                          |
| -------------------------- | ------------------------------------------------------------------------------------------------------ |
| 401 from FieldPulse        | The header must be named `x-api-key` and hold a current key.                                           |
| 400 from FieldPulse        | Read the error list in the response. `status` must be exactly `lead`, and phone numbers must be valid. |
| Known callers aren't found | FieldPulse matches what's stored. Try the caller's name as well as their phone number.                 |
| The comment isn't added    | `commentable_id` must be the id of an existing customer. Check the find or create tool ran first.      |
| 429 from FieldPulse        | You've hit FieldPulse's request limit. Wait and try again.                                             |
