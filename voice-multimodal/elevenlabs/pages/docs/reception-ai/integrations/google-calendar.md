---
title: "Google Calendar"
source: https://elevenlabs.io/docs/reception-ai/integrations/google-calendar.md
path: docs/reception-ai/integrations/google-calendar
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Google Calendar

The Google Calendar integration lets your receptionist check staff availability in real time. When a staff member has an event on their Google Calendar, that time is blocked for bookings. Reception.ai bookings can also be added to their calendar.

## How it works

1. Each staff member connects their Google Calendar.
2. Reception.ai reads free and busy times from the calendars you choose.
3. Busy times are excluded when offering appointment slots.
4. New bookings can be added to one of the staff member's calendars.

## Connecting a staff member's calendar

### Enable the integration

Go to **Integrations**, select **Add integration**, and enable **Google Calendar**. The **Staff** feature must be on in **Settings** → **Features**.

### Open the staff member

Go to **Staff**, select the staff member, and open **Calendars**. Select **Connect**.

### Authorize with Google

The staff member signs in with their Google account. To let them connect from their own device, use the QR code, **Copy link**, or **Open in browser**.

On the Google consent screen, leave every permission selected. Reception.ai needs to:

* See free and busy times
* View the calendar list
* Manage events it creates

If any permission is unchecked, the connection fails and must be retried.

### Choose calendars

Choose which calendars to check for availability and where to sync bookings.

## Sync settings

| Setting                     | Description                                                                                                                  |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Check availability from** | Calendars whose events block availability. You can select several.                                                           |
| **Sync new bookings to**    | The calendar where new bookings are added, or **Do not sync bookings**. Only calendars the staff member can edit are listed. |

When a booking is cancelled, its Google Calendar event stays with a "\[Cancelled]" prefix and is marked as free, so the time becomes available again.

## Troubleshooting

If a connection expires or access is revoked, the staff member's calendar shows that it needs reconnecting. Go to **Staff**, select the staff member, open **Calendars**, and select **Reconnect**.

> **Warning**
>
> While a connection needs reconnecting, availability won't include Google Calendar events. This may
> lead to double-bookings until it is restored.

> **Note**
>
> Google Calendar works with Reception.ai's own scheduling. It is not available while Calendly or
> Cal.com is connected.
