---
title: "Staff"
source: https://elevenlabs.io/docs/reception-ai/scheduling/staff.md
path: docs/reception-ai/scheduling/staff
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Staff

Staff members represent the people who deliver your services. The scheduling system uses their hours, service assignments, and calendar data to decide which time slots to offer.

> **Note**
>
> Staff members are the people you schedule. They do not get access to the Reception.ai dashboard.

## How staff affect availability

When a customer wants to book a service, the system:

1. Identifies which staff members can perform that service.
2. Checks who is working at the requested time and location.
3. Excludes anyone with a conflicting appointment, time off, or a busy Google Calendar event.
4. Offers the remaining open slots.

If no qualified staff member is available, the slot is not offered, even if the location is open.

## Staff settings

Open **Staff** in the sidebar and select a staff member. Settings are grouped into:

| Section           | What it contains                                                                      |
| ----------------- | ------------------------------------------------------------------------------------- |
| **Basic info**    | Full name, display name (the name customers see), groups, email, phone, and location  |
| **Working hours** | Location hours or a custom schedule                                                   |
| **Services**      | Services this person is individually assigned to, and services available to all staff |
| **Time off**      | Vacation, sick days, and other leave                                                  |
| **Calendars**     | Google Calendar connection                                                            |

Additional options:

* **Active (available for bookings)**: turn off to stop booking this person without deleting them.
* **Display on public booking page**: turn off to make this person bookable by phone only.
* **Opted in to receive SMS booking notifications**: allows SMS notifications to this person. This is turned off automatically if they reply STOP.

## Working hours

Each staff member belongs to one location, or to all locations. Their working hours are either:

* **Follow location hours**: the staff member works whenever their location is open. Changes to location hours apply automatically.
* **Custom schedule**: per-day time blocks, for part-time employees or staggered shifts.

## Service assignments

Services use **Any staff can do it** by default, so every active staff member can be booked for them. To restrict a service to certain people, turn this off on the service and assign staff individually. Assignments update both the staff profile and the service.

## Booking notifications

Staff can be notified by email or SMS when a booking assigned to them is created, updated, or cancelled. See [Notifications and SMS](/docs/reception-ai/features/notifications).

## Google Calendar sync

Connect a staff member's Google Calendar from the **Calendars** section:

* **Check availability from**: calendars whose busy times block Reception.ai availability. You can select several.
* **Sync new bookings to**: the calendar where Reception.ai adds new bookings, or **Do not sync bookings**.

See [Google Calendar](/docs/reception-ai/integrations/google-calendar) for setup.

> **Info**
>
> If a staff member's Google Calendar connection needs reconnecting, their availability won't
> reflect external events. This may lead to double-bookings until the connection is restored.

## Staff on the booking page

On your booking page, customers can choose a specific person when **Show staff member selection** is on in the booking page setup. Staff with **Display on public booking page** turned off are hidden. Customers can also select **Any staff** to see all available times.
