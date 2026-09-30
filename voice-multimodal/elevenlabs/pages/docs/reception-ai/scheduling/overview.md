---
title: "Scheduling"
source: https://elevenlabs.io/docs/reception-ai/scheduling/overview.md
path: docs/reception-ai/scheduling/overview
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Scheduling

Reception.ai includes a full scheduling system. Your receptionist uses it to book appointments over the phone, and customers can book directly on your [booking page](/docs/reception-ai/features/booking-page).

## How scheduling works

The scheduling system connects:

1. **Services**: what you offer, such as a haircut, consultation, or equipment rental.
2. **Locations**: where you offer it, each with its own opening hours.
3. **Staff**: who provides the service.
4. **Assets**: resources the service needs, such as rooms, chairs, or equipment.
5. **Booking rules**: slot length, notice periods, and how far ahead customers can book.

A time slot is only offered when the location is open, a qualified staff member is free, required assets are available, the booking rules allow it, and no conflicts exist. See [How availability is calculated](/docs/reception-ai/scheduling/hours-and-booking-rules#how-availability-is-calculated).

## Booking channels

Appointments from every channel go into the same calendar:

* **Phone**: booked by your receptionist during a call.
* **Text message**: booked through SMS.
* **Website**: self-scheduled on your booking page or through the web widget.
* **Dashboard**: created by you or your team.

## Calendar

Open **Calendar** in the sidebar to see and manage bookings.

* **Views**: Month, Week, 3 days, or Day. Turn on **Show weekends** to include Saturday and Sunday.
* **Group by**: staff, assets, services, channel, or a timeline.
* **Location**: view one location or **All locations**.
* **New appointment** and **New time off**: create bookings and closures directly.

When you change or cancel a booking, Reception.ai asks whether to notify the client by email or SMS: send to everyone affected, send to selected clients, or don't send. [Orders](/docs/reception-ai/features/orders) also appear on the calendar.

## Assets

Assets represent physical resources required for appointments: rooms, chairs, courts, or equipment. Use them when a service needs a resource with limited availability.

Assets follow their location's hours by default, and can have custom hours and maintenance time off. They are only bookable when not already reserved.

For rental businesses, the asset *is* the service. Create a rental-type service and link it to the asset.

## Turning scheduling features off

Go to **Settings** → **Features** to turn off parts of scheduling you don't use: services, clients, staff, assets, availability, the online booking page, or individual service types (appointments, home and mobile, group sessions, rentals). Turned-off features are hidden from the dashboard, the receptionist, and the booking page.

For example, with **Staff** turned off, your receptionist books with whoever is free and never mentions team members by name.

## Using Calendly or Cal.com

If you connect [Calendly](/docs/reception-ai/integrations/calendly) or [Cal.com](/docs/reception-ai/integrations/cal-com), that tool manages availability and bookings instead. Reception.ai's own staff, assets, availability, and booking page are hidden while it is connected. Existing data is kept.

#### [Services](/docs/reception-ai/scheduling/services)

Service types, pricing, variants, and add-ons.

#### [Hours and booking rules](/docs/reception-ai/scheduling/hours-and-booking-rules)

Opening hours, closures, and booking rules.

#### [Staff](/docs/reception-ai/scheduling/staff)

Staff schedules, assignments, and calendar sync.

#### [Locations](/docs/reception-ai/scheduling/locations)

Addresses, hours, and what each location offers.
