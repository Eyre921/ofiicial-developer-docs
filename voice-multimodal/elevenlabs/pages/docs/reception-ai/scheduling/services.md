---
title: "Services"
source: https://elevenlabs.io/docs/reception-ai/scheduling/services.md
path: docs/reception-ai/scheduling/services
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Services

Services define what your customers can book. Manage them in **Business** → **Services**. Each service has a type that determines who performs it, where it happens, and what resources it needs.

## Service types

Choose a type when you create a service. The type is permanent and cannot be changed later.

| Type              | How it works                                                      | Example                            |
| ----------------- | ----------------------------------------------------------------- | ---------------------------------- |
| **Appointment**   | One client books a time slot with a staff member at your location | Haircut, consultation, massage     |
| **Home / mobile** | You travel to the client's location, with travel time blocked     | Plumber, cleaning, mobile grooming |
| **Group session** | Multiple clients register for a scheduled session                 | Yoga class, workshop, tour         |
| **Rental**        | Clients book an asset for a time period                           | Court, kayak, studio, vehicle      |

Each type changes the available options. Rentals use assets instead of staff. Home and mobile services include travel time. Group sessions allow multiple registrants per slot.

## Variants

Every service needs at least one variant: a duration and price combination. Use variants to offer the same service at different lengths:

| Variant  | Duration | Price |
| -------- | -------- | ----- |
| Short    | 30 min   | \$50  |
| Standard | 60 min   | \$90  |
| Extended | 90 min   | \$125 |

You can have up to 20 variants per service, each with a unique duration. Variants can be activated or deactivated without deleting them.

Price is optional. Leave it empty if the price varies. The booking page then shows the service as "Price on request".

When you change a price, Reception.ai asks whether to update the price of existing appointments or keep the old prices.

## Quote-only services

Turn on **Price set later (requires a quote)** for jobs you can't price up front, such as a roof repair. Price fields are hidden, and instead of booking, the receptionist and booking page collect a [quote request](/docs/reception-ai/features/quote-requests) for you to review.

Group sessions cannot be quote-only.

## Intake questions

Use the **Intake questions** tab to collect details when a customer books or requests a quote, for example "How many rooms need cleaning?".

* **Types**: text, number, or choice (up to 20 options).
* **Required**: enforced on the booking page. On calls, the receptionist is instructed to ask it.
* **Limit**: up to 10 questions per service.

Answers appear on the booking, order, or quote request.

## Buffer and travel time

**Buffer** blocks extra minutes after each appointment for cleanup or transition. A 60-minute massage with a 15-minute buffer blocks 75 minutes. For rentals this is labeled time between rentals; for group sessions, cleanup time after each session.

**Travel time** (home and mobile services only) blocks time before and/or after the appointment for travel, up to 480 minutes.

## Staff and asset assignment

Each service needs staff, assets, or both:

* **Staff**: **Any staff can do it** is on by default, so any staff member can be booked. Turn it off to choose specific people.
* **Assets**: if the service needs a physical resource, assign it. The service is only bookable when the asset is free.

Rental services skip staff assignment. The asset itself is booked.

## Locations

Choose which [locations](/docs/reception-ai/scheduling/locations) offer the service. Leave it empty to offer the service everywhere.

## Add-ons

Add-ons are optional extras customers can include when booking. Each add-on can extend the duration, add cost, or both. Up to 10 per service.

For group sessions, add-ons only affect price, since all participants share the same time slot.

## Promotions

Time-limited discounts on a service, a specific variant, or a specific add-on. Each promotion has a date range and optional active days of the week. Up to 10 per service. Your receptionist mentions active promotions when booking.

## Groups and display order

Organize services into groups, and order them within each group. This order determines how services appear on your booking page and how your receptionist lists them to callers. Turn off **Display on booking page** to offer a service by phone only.
