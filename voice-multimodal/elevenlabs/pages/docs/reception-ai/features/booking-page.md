---
title: "Booking page"
source: https://elevenlabs.io/docs/reception-ai/features/booking-page.md
path: docs/reception-ai/features/booking-page
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Booking page

Your booking page is a hosted page where customers can browse services and book appointments without calling. The web widget adds your receptionist to your own website. Both are managed in **Your own website** in the sidebar.

## Turning the booking page on

The booking page is controlled by **Online booking page** in **Settings** → **Features**. When it is off, the page is unavailable and confirmation messages don't include a link to manage the booking.

Your booking page URL looks like:

```
https://app.reception.ai/smb-public/book/your-business-slug
```

Change the slug under **Booking page URL**, then select **Save**. Use **Copy** or **Open** to share or preview it.

> **Warning**
>
> Changing your slug breaks existing links. Update any published URLs after changing it.

## How customers book

1. Optionally filter by location, staff, or resource.
2. Choose a service and variant.
3. Choose add-ons.
4. Pick a date and time.
5. Enter their details: full name and phone number are required, email and notes are optional. Home services also ask for an address, and services with [intake questions](/docs/reception-ai/scheduling/services#intake-questions) show them here.
6. Review and confirm.

Customers receive a confirmation by email and/or SMS, depending on your [notification settings](/docs/reception-ai/features/notifications), with a confirmation number and a link to manage the booking.

Availability follows your [booking rules](/docs/reception-ai/scheduling/hours-and-booking-rules#booking-rules), the same as phone bookings.

## Self-service booking management

The management link is unique per booking and needs no login. Customers can:

* **Reschedule** to another available time
* **Cancel** the appointment
* **View details** of the date, time, service, and staff

Rescheduling and cancelling are limited by your **Reschedule or cancel notice** rule. If appointment reminders ask clients to confirm, the reminder includes links to confirm or decline.

Your receptionist can also help callers manage existing bookings by phone number or confirmation number.

## Customizing the booking page

Open **Your own website** → **Booking page** to customize the page with a live preview on desktop and mobile. Start from a template or select **Start fresh**.

| Area                    | What you can change                                                       |
| ----------------------- | ------------------------------------------------------------------------- |
| **Setup**               | Which steps and filters appear, including **Show staff member selection** |
| **Page and typography** | Colors, fonts, and layout                                                 |
| **Header and landing**  | Cover image, header, and introduction text                                |
| **Steps**               | Text on the date and time, personal details, confirm, and success steps   |
| **Receptionist**        | Show your receptionist on the booking page                                |

The confirm step can show **Payment instructions** (up to 500 characters) and a **Cancellation policy** (up to 2,000 characters). The cancellation policy is also included in confirmation emails.

### Receptionist on the booking page

Turn on **Show receptionist on booking page** to let visitors talk to your receptionist while they book. Select **Receptionist only** to replace the booking flow with the receptionist.

## Embedding the booking page

To embed the booking page on your website, open the embed options and copy the code. Choose **Full page** or set a height in pixels.

## Web widget

The **Web widget** tab adds a button to your website that starts a conversation with your receptionist.

| Setting         | Options                                  |
| --------------- | ---------------------------------------- |
| **Variant**     | Tiny, Compact, or Full                   |
| **Placement**   | One of six positions on the page         |
| **Colors**      | Two orb colors                           |
| **Text**        | Prompt text and call button label        |
| **Collapsible** | Whether visitors can minimize the widget |

Copy the embed code and add it to your website. Widget conversations use web minutes. See [Usage and limits](/docs/reception-ai/billing/usage-and-limits).

## Orders and quotes

When [orders](/docs/reception-ai/features/orders) are enabled, the booking page lets customers choose between **Book an appointment** and **Order**. Quote-only services show **We'll quote you** and open a [quote request](/docs/reception-ai/features/quote-requests) form instead of a calendar.

## Group events

Group sessions let multiple customers attend the same session, such as a yoga class or workshop:

* **Fixed schedule**: the session happens at a set date and time.
* **Capacity**: 2–200 participants.
* **Seats per registration**: customers can book up to 50 seats, for example to bring friends.
* **Add-ons**: optional extras per participant that add price, not duration.

To set up group events, create a service with the type **Group session**, set the capacity and add-ons, then create sessions in the calendar.

Customers see upcoming sessions with available spots and the price per person. After registering, they receive a link to cancel, change seats, modify add-ons, or switch sessions. The same client cannot register twice for one session.

## Sharing your booking page

Link to your booking page from:

* Your website (a "Book now" button)
* Google Business Profile
* Social media bios
* Email signatures
