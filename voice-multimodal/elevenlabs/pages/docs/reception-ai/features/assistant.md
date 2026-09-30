---
title: "Business assistant"
source: https://elevenlabs.io/docs/reception-ai/features/assistant.md
path: docs/reception-ai/features/assistant
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Business assistant

The business assistant is a built-in AI chat for managing your business. Ask it to look things up or make changes, and it proposes the changes for your approval.

## What the assistant can do

| Category         | Example requests                                                                                |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| **Scheduling**   | "Show me tomorrow's appointments", "Book John for a haircut at 3pm Friday"                      |
| **Clients**      | "Find the client who called yesterday about pricing", "Create a new client for Sarah, 555-0123" |
| **Services**     | "Add a new service called Deep Tissue Massage, 60 min, \$90"                                    |
| **Staff**        | "Who's working this Saturday?", "Add a day off for Mark next Wednesday"                         |
| **Locations**    | "Close the downtown location on December 26"                                                    |
| **Receptionist** | "Add a rule to always mention free parking", "Add a transfer rule for billing questions"        |
| **Booking page** | "Change the booking page slug to downtown-salon", "Make the header dark blue"                   |
| **Analytics**    | "What's my revenue this week vs last week?", "How many bookings came from the website?"         |
| **Products**     | "Add a product: Organic Shampoo, \$24.99"                                                       |

The assistant can also manage procedures, group sessions, and holidays, and look up an appointment by confirmation number.

It cannot manage messages, orders, quote requests, SMS, or FAQ answers. To answer unanswered questions, go to **Business** → **FAQ**.

## How to access it

* **Docked panel**: select **Assistant** in the header on any page.
* **Full page**: open **Assistant** from the **More** menu in the sidebar. Pin it to keep it in the sidebar.

## Confirming changes

When you ask the assistant to create, update, or delete anything, it shows exactly what it plans to do and waits for you to select **Proceed** or **Cancel**. For batch changes, such as cancelling several appointments, you can accept or reject each change individually.

The assistant never changes data without your approval.

## Attachments and suggestions

* **Attach a text file** to give the assistant more context, such as a price list. One file per message: `.txt`, `.md`, `.json`, `.yml`, or `.yaml`, up to 5 MB.
* After most replies, the assistant suggests 3–5 follow-up actions you can select instead of typing.

## Rich responses

Responses include clickable mentions of staff, services, assets, clients, and products. Select one to open its details.

## Conversation history

Select **Open history** to browse, continue, or delete past chats. Select **New chat** to start over.

## Daily message limit

Each plan has a daily message limit that resets at midnight UTC:

| Plan    | Messages per day |
| ------- | ---------------- |
| Trial   | 150              |
| Basic   | 150              |
| Plus    | 300              |
| Premium | 500              |

When you reach the limit, a banner appears with an option to upgrade.

## Setup

The assistant is created automatically when you first open it. If it hasn't been set up yet, select **Create Assistant** to provision it for your workspace.
