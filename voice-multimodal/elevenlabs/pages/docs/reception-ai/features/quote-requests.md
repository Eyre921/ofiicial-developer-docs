---
title: "Quote requests"
source: https://elevenlabs.io/docs/reception-ai/features/quote-requests.md
path: docs/reception-ai/features/quote-requests
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Quote requests

Quote requests let your receptionist and booking page handle jobs without a fixed price, such as repairs, custom work, or large orders. Instead of booking, the receptionist collects the details you need and files a request for you to price.

Quotes are on by default. To turn them off, go to **Settings** → **Features** → **Quotes**. Before turning quotes off, set a price on every quote-only service and product.

## Setting up quote-only items

1. Open a service or product and turn on **Price set later (requires a quote)**.
2. Add [intake questions](/docs/reception-ai/scheduling/services#intake-questions) for the details you need, for example the size of the job or the type of material.

Group sessions cannot be quote-only.

## How customers request a quote

**By phone**: when a caller asks for a quote-only item, the receptionist asks your intake questions, then collects preferred timing in the caller's own words, any budget, and notes.

**On the booking page**: quote-only services show **We'll quote you**. Customers fill in the intake questions, preferred timing, name, phone number, and optionally email and notes.

## Reviewing quote requests

Open **Conversations** → **Quote requests**. Unread requests show a badge.

Each request shows the requested items, the answers to your intake questions, the customer's notes, and a summary from the receptionist. Filter by status (open, booked, or ordered), read state, and date received, and use **Mark all as read**.

## Converting a request

After pricing the job, convert the request:

| Action                 | Use for                     |
| ---------------------- | --------------------------- |
| **Create appointment** | Quote requests for services |
| **Create order**       | Quote requests for products |

The price you enter is kept on the booking or order, even if catalog prices change later. You can also **Open conversation** to review the original call, or **Delete** the request.
