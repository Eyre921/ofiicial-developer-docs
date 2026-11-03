---
title: "Acuity Scheduling"
source: https://elevenlabs.io/docs/reception-ai/integrations/acuity-scheduling.md
path: docs/reception-ai/integrations/acuity-scheduling
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Acuity Scheduling

With the [webhook tools](/docs/reception-ai/integrations/webhooks) below, your receptionist can check when an appointment type is free and book the caller into an open slot. Acuity sends the client its usual confirmation email.

## Before you start

### Check your plan

Acuity only includes API access on its top plan (Premium, previously called Powerhouse). On other plans, the tools below fail with a 403 error.

### Get your API credentials

In Acuity, open **Integrations**, find **API**, and copy your **User ID** and **API Key**.

### Build the authorization header

Acuity uses your User ID as the username and the API key as the password. Encode them in a terminal, replacing both placeholders:

```bash
printf 'USER_ID:API_KEY' | base64
```

The header value is `Basic ` followed by the output.

> **Warning**
>
> Don't paste your API key into an online encoder. Anyone with it can read and change your
> appointments and client details.

### Find the appointment type ID

Copy the direct scheduling link for the appointment type you want your receptionist to book. The number after `appointmentType=` in the link is its ID. The tools below use it in place of `APPOINTMENT_TYPE_ID`.

## Create the tools

For each tool, go to **Integrations**, select **Add integration**, choose **Webhook Tool**, and set **Assign to agents** to **Receptionist**.

### Check open times

| Field                | Value                                                                                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `check_acuity_availability`                                                                                                                             |
| **Description**      | "List the open appointment times on one date. Use it before offering the caller a time."                                                                |
| **Method**           | GET                                                                                                                                                     |
| **URL**              | `https://acuityscheduling.com/api/v1/availability/times`                                                                                                |
| **Request Headers**  | `Authorization`: `Basic ` followed by the encoded credentials                                                                                           |
| **Query Parameters** | `appointmentTypeID` (number, required): "Always the exact value `APPOINTMENT_TYPE_ID`."  `date` (string, required): "The date to check, as YYYY-MM-DD." |

### Book an appointment

| Field               | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**            | `book_acuity_appointment`                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Description**     | "Book the caller into an open time once they have chosen one. Confirm the date and time with them first."                                                                                                                                                                                                                                                                                                                                                               |
| **Method**          | POST                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **URL**             | `https://acuityscheduling.com/api/v1/appointments`                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Request Headers** | `Authorization`: `Basic ` followed by the encoded credentials                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Body Parameters** | `datetime` (string, required): "The chosen time, exactly as returned in a `time` value by `check_acuity_availability`."  `appointmentTypeID` (number, required): "Always the exact value `APPOINTMENT_TYPE_ID`."  `firstName` (string, required): "The caller's first name."  `lastName` (string, required): "The caller's last name."  `email` (string, required): "The caller's email address. Ask them to spell it."  `phone` (string): "The caller's phone number." |

Select **Enable** on each tool, then [test your receptionist](/docs/reception-ai/receptionist/testing) by asking for an appointment. The booking appears in your Acuity calendar.

> **Tip**
>
> To book several appointment types, replace "Always the exact value" in both tools with a list, for
> example: "Use `111` for a 30-minute consultation and `222` for a 60-minute session."

## Limitations

* Acuity requires an email address for every booking, so your receptionist asks callers to spell theirs.
* Intake form answers are sent as a list, which webhook tools can't send. Booking notes can only be set by an admin booking, which skips Acuity's availability checks, so the tools above don't set either.
* The tools can't cancel or reschedule appointments. Those need the appointment ID in the URL.

## Troubleshooting

| Problem                                  | What to check                                                                                     |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------- |
| 401 from Acuity                          | Encode `USER_ID:API_KEY` with the colon, and start the header value with `Basic ` and a space.    |
| 403 from Acuity                          | Your plan doesn't include API access.                                                             |
| No times are returned                    | Check the appointment type ID, and that the type has open hours on that date.                     |
| Booking fails with `not_available`       | The time was taken or isn't open. Tell the receptionist to check open times again before booking. |
| Booking fails because a field is missing | Your account may require a phone number. Make `phone` required in the booking tool.               |
