---
title: "Notifications and SMS"
source: https://elevenlabs.io/docs/reception-ai/features/notifications.md
path: docs/reception-ai/features/notifications
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Notifications and SMS

Reception.ai sends notifications to you, your staff, and your clients when calls end, bookings change, and orders are placed. Configure them in **Settings** → **Notifications**, which has **General**, **Email**, and **SMS** tabs.

## Notifications for you and your team

| Notification                    | Default      | What it sends                                                                                                                   |
| ------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| **Post-call summary**           | On, by email | A summary after each conversation, listing new, rescheduled, and cancelled bookings, orders, messages, and unanswered questions |
| **Staff booking notifications** | On, by email | Tells the assigned staff member when their booking is created, updated, or cancelled                                            |
| **Your order notifications**    | On, by email | Tells your business what to prepare when an order is placed, with a link to the order                                           |

For post-call summaries, choose **Notify me about** every conversation (the default), or only conversations with bookings, orders, messages, or FAQ questions. Summaries go to the account owner's email by default. You can add up to 10 email addresses, or receive summaries by SMS.

## Notifications for clients

| Notification                      | Default      | What it sends                                                                                                     |
| --------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------- |
| **Appointment reminders**         | On, by email | A reminder before each appointment                                                                                |
| **Clients booking notifications** | On           | A confirmation right after booking, and messages when a booking is rescheduled or cancelled                       |
| **Clients order notifications**   | On           | A confirmation when an order is placed, updated, or cancelled, with a confirmation number and a link to manage it |

### Appointment reminders

* **Timing**: 4, 6, 8, 12, 24 (default), or 48 hours before the appointment.
* **Reminder mode**: **Reminder only**, or **Ask client to confirm**. With confirmation, the client replies YES to confirm or NO to cancel.

## Email templates

In the **Email** tab, upload a logo (JPG, PNG, or WEBP, up to 5 MB) and edit the text of each email: confirmations, cancellations, reschedules, reminders, staff notifications, and order updates. Select text to edit it, and drag placeholders such as the client's name or appointment time into the message. Select **Restore defaults** to reset a template.

A **custom procedure email** template is also available. Reference it in a [procedure](/docs/reception-ai/receptionist/rules-and-procedures#procedures) to have your receptionist send a specific email to a client during a conversation.

## SMS

SMS lets you send confirmations, reminders, and updates by text message.

### Sending numbers

| Your number                                                                                           | Can send SMS                             |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| A number from your own Twilio account ([BYO](/docs/reception-ai/phone-numbers/bring-your-own-number)) | Yes, in any country                      |
| A Reception.ai number in Canada                                                                       | Yes                                      |
| A Reception.ai number in the US or elsewhere                                                          | No. Connect a Twilio number to send SMS. |

Choose the number to send from under **SMS phone number** in the notification settings.

Reception.ai numbers have a daily SMS limit: Trial 100, Basic 300, Plus 750, Premium 1,500. Numbers from your own Twilio account are not limited.

### SMS templates

In the **SMS** tab, choose a style for each message type: **Professional**, **Friendly**, or **Concise**. Message types include reminders, confirmations, booking and order updates, post-call summaries, staff booking notifications, and the automatic reply to HELP.

### Consent and opt-out

Clients receive SMS only when they are opted in. A client who replies STOP, STOPALL, UNSUBSCRIBE, CANCEL, END, or QUIT is opted out. Only the client can opt back in, by texting START or UNSTOP. A reply of HELP or INFO receives an automatic help message.

> **Note**
>
> To receive replies such as STOP on your own Twilio number, turn on **Enable inbound SMS** for that
> number.

### Sending an SMS to a client

Open a client and select **Send SMS** on their timeline. Messages can be up to 459 characters, and your workspace can send up to 30 per hour. Sending requires a number from your own Twilio account. The message is logged on the client's timeline.

### Incoming texts

When a known client texts your number, the message is logged as **SMS Received** on their timeline. Your receptionist does not reply to text messages conversationally.
