---
title: "Orders and shop"
source: https://elevenlabs.io/docs/reception-ai/features/orders.md
path: docs/reception-ai/features/orders
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Orders and shop

Orders let your receptionist and booking page sell products, such as baked goods, retail items, or takeout. Orders are tracked from placement to completion in the **Shop** page.

## Turning orders on

Go to **Settings** → **Features** and turn on **Products** and **Orders**. Orders are off by default. Once they are on, products move from **Business** to **Shop** → **Products**.

## Setting up products

Open a product and go to its ordering settings:

| Setting                    | Description                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------------------- |
| **Available for ordering** | Whether customers can order this product                                                          |
| **Price**                  | Optional. Leave empty for [quote-only](/docs/reception-ai/features/quote-requests) products.      |
| **Track quantity**         | **No limit**, or **Limited** to track stock. Stock is tracked per location, and orders reduce it. |
| **Fulfillment options**    | Pickup (default), Delivery, or Digital. At least one is required.                                 |
| **Locations**              | Where the product is sold                                                                         |
| **Intake questions**       | Details to collect when ordering, such as a cake message                                          |

## Delivery fees

In **Shop** → **Settings**, set a **Delivery fee** and optionally **Free delivery above** an order total. Set the threshold to 0 to always charge the fee.

## How customers order

* **By phone**: the receptionist takes the order, confirms items and fulfillment, and gives the caller a confirmation number. Callers can also check, change, or cancel an existing order.
* **Online**: on your booking page, customers choose **Order**, add items, and submit the order. They receive a link to update or cancel the order.

Each order can have up to 50 lines, with a quantity of 1–99 per line.

## Managing orders

Open **Shop** → **Orders** to see orders from your receptionist, your website, and manual entries. Select **Add order** to create one yourself. Orders also appear on the [calendar](/docs/reception-ai/scheduling/overview#calendar).

Each order shows the customer, items, delivery details, total, timing, answers to intake questions, customer notes, and internal notes. Move an order through its statuses with **Mark as**:

| Status        | Meaning                          |
| ------------- | -------------------------------- |
| **Pending**   | Placed, not yet confirmed        |
| **Confirmed** | Accepted by your business        |
| **Preparing** | Being prepared                   |
| **Ready**     | Ready for pickup or delivery     |
| **Completed** | Picked up or delivered           |
| **Cancelled** | Cancelled by you or the customer |

## Notifications

When orders are placed, changed, or cancelled, Reception.ai notifies your business and the customer by email and/or SMS. Orders also appear in post-call summaries. See [Notifications and SMS](/docs/reception-ai/features/notifications).
