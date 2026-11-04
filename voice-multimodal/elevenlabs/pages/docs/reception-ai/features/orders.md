---
title: "Orders and shop"
source: https://elevenlabs.io/docs/reception-ai/features/orders.md
path: docs/reception-ai/features/orders
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Orders and shop

Orders let your receptionist and booking page sell products, such as baked goods, retail items, or takeout. Orders are tracked from placement to completion in the **Shop** page.

## Turning orders on

Go to **Settings** → **Features** and turn on **Products** and **Orders**. **Orders** is marked **Alpha**. Orders are off by default. Once they are on, products move from **Business** to **Shop** → **Products**. Until then, products stay on your business page, and the page describes them as items your receptionist can sell or mention during calls.

## Product details

Open a product and use the **Details** tab:

| Field                                  | What it sets                                                                                                                                                                   |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Product name**                       | Required.                                                                                                                                                                      |
| **Price set later (requires a quote)** | Marked **Alpha**. Files a [quote request](/docs/reception-ai/features/quote-requests) instead of taking an order. Hidden when quotes are off.                                  |
| **Price**                              | Optional, in your [currency](/docs/reception-ai/scheduling/overview#business-profile). Leave it empty when the price varies or does not apply. Hidden for quote-only products. |
| **Groups**                             | Optional. Up to 20.                                                                                                                                                            |
| **Description**                        | Optional.                                                                                                                                                                      |
| **Active (visible to clients)**        | On by default. Turn it off to hide the product. Inactive products show **Inactive**.                                                                                           |

## Setting up products

The **Ordering** tab controls whether a product can be ordered:

| Setting                    | Description                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------------------- |
| **Available for ordering** | Whether customers can order this product                                                          |
| **Track quantity**         | **No limit**, or **Limited** to track stock. Stock is tracked per location, and orders reduce it. |
| **Fulfillment options**    | Pickup (default), Delivery, or Digital. At least one is required.                                 |
| **Locations**              | Where the product is sold                                                                         |
| **Intake questions**       | Details to collect when ordering, such as a cake message                                          |

When orders are on, a product that can be ordered shows **Orderable**. One that cannot shows **Catalog only** and **Info & quotes only**. A product whose tracked stock is gone shows **Sold out**. Unlimited stock shows **No limit**.

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
