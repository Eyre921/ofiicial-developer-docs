---
title: "Hours and booking rules"
source: https://elevenlabs.io/docs/reception-ai/scheduling/hours-and-booking-rules.md
path: docs/reception-ai/scheduling/hours-and-booking-rules
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Hours and booking rules

Opening hours define when each location accepts bookings. Booking rules control how and when customers can book within those hours. Both are configured in **Business** → **Overview**.

## Opening hours

Hours are set per [location](/docs/reception-ai/scheduling/locations). Open the **Opening hours** card, choose a location, and set open and close times for each day. You can add multiple time blocks per day (for example 9:00–12:00 and 14:00–18:00 for a lunch break), mark days as closed, or keep a location open until midnight. Use **Copy to…** to apply one day's hours to weekdays, the weekend, or all days.

Staff members and assets follow their location's hours by default. You can give them custom hours instead. See [Staff](/docs/reception-ai/scheduling/staff).

If you change hours and existing bookings fall outside the new hours, Reception.ai warns you. Select **Save anyway** to keep the bookings and apply the new hours.

### Time zones

Each workspace has a time zone, set in the business profile. To give individual locations, staff, or assets their own time zone, turn on per-resource time zones in the time zone settings.

## Closures and time off

Open **Closures** to add exceptions to your regular hours: public holidays, vacations, maintenance, or extended hours for an event.

| Type                  | Applies to                    | Example                    |
| --------------------- | ----------------------------- | -------------------------- |
| **Location closure**  | One location or all locations | Public holiday, renovation |
| **Staff leave**       | One staff member              | Vacation, sick day         |
| **Asset maintenance** | One asset                     | Equipment repair           |

Each exception is either **Closed all day** or **Change hours** to set custom hours for those dates. Staff and asset time off can also be added from the **Time off** tab in their settings.

### Conflicts with existing bookings

Time off cannot be saved while bookings exist during that period. Reception.ai lists the affected bookings. Cancel or reschedule them, then save the time off again. Time off never removes bookings silently.

> **Tip**
>
> Add all known holidays at the start of the year so your receptionist never books during a closure.

## Booking rules

The **Booking rules** card applies to both your receptionist and your booking page. Bookings you create from the dashboard are not restricted by these rules.

| Rule                            | Options                                               | Default    |
| ------------------------------- | ----------------------------------------------------- | ---------- |
| **Slot length**                 | 10, 15, 20, 30, or 60 minutes                         | 15 minutes |
| **Book up to**                  | 7, 14, 30, 60, 90, or 365 days ahead                  | 14 days    |
| **Minimum notice**              | None, 15 or 30 minutes, 1, 2, or 4 hours, 1 or 2 days | None       |
| **Reschedule or cancel notice** | Same options as minimum notice                        | None       |
| **Overlapping**                 | Limit overlapping appointments per location           | Off        |

* **Minimum notice** is the soonest a new booking can start.
* **Reschedule or cancel notice** is the latest a client can reschedule or cancel before the appointment starts.
* **Overlapping** caps how many appointments can run at the same time at one location.

> **Note**
>
> When Calendly or Cal.com is connected, that tool's own scheduling settings apply instead.

## How availability is calculated

A time slot is bookable only when **all** of the following are true:

1. The location is open, with no closure.
2. The service is offered at that location.
3. At least one qualified staff member is working there and has no time off.
4. Required assets are free and not under maintenance.
5. No conflicting appointment exists, including buffer and travel time.
6. The overlapping-appointment limit is not reached.
7. The slot respects minimum notice and the book-up-to window.
8. Google Calendar, if connected, shows the staff member as free.

If any condition fails, the slot is not offered by phone or on the booking page.
