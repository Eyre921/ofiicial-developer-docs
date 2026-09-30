---
title: "Rules and procedures"
source: https://elevenlabs.io/docs/reception-ai/receptionist/rules-and-procedures.md
path: docs/reception-ai/receptionist/rules-and-procedures
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Rules and procedures

Rules and procedures are the main way to shape your receptionist's behavior. Both are managed in the **Teach your receptionist** card on the Receptionists page.

| Type          | When it applies                                           | Example                                                  |
| ------------- | --------------------------------------------------------- | -------------------------------------------------------- |
| **Rule**      | On every call                                             | "Never give medical advice."                             |
| **Procedure** | Only when the caller asks for the thing it is written for | "When the caller wants to book, follow these steps: ..." |

Use a rule for a constraint that is always true. Use a procedure for a multi-step flow tied to one type of request.

## Adding rules and procedures

Open **Teach your receptionist**. The dialog has a **Rules** panel and a **Procedures** panel. Each panel offers:

* **Browse ready-made**: a catalog of common rules and procedures for your business type. Select **Add this rule** or **Add this procedure**, then edit it as needed.
* **Write your own**: start from a blank rule or procedure.

Everything you have added appears in the **In use** list. Select an item to edit or delete it.

## Rules

Each rule has a title, a description, and a priority. You can have up to **50 rules** per receptionist.

| Field           | Limit                | Notes                                    |
| --------------- | -------------------- | ---------------------------------------- |
| **Title**       | 1–200 characters     | Only visible to you                      |
| **Description** | 1–2,000 characters   | The instruction the receptionist follows |
| **Priority**    | Strict or Suggestion | Defaults to Strict                       |

| Priority       | Behavior                                                                                         |
| -------------- | ------------------------------------------------------------------------------------------------ |
| **Strict**     | The receptionist must follow this rule                                                           |
| **Suggestion** | The receptionist follows this rule when it fits, and may deviate if the conversation requires it |

Use strict for hard business rules such as pricing, legal requirements, and safety. Use suggestion for stylistic preferences.

### Example rules

| Priority   | Title                    | Description                                                                                          |
| ---------- | ------------------------ | ---------------------------------------------------------------------------------------------------- |
| Strict     | No medical advice        | Never provide medical advice. Always recommend the caller schedule an appointment with a specialist. |
| Strict     | Confirm phone number     | Always confirm the caller's phone number before booking any appointment.                             |
| Suggestion | Mention discount         | When booking a first appointment, mention our 20% new client discount.                               |
| Strict     | No competitor discussion | Never discuss competitor products, pricing, or services.                                             |

## Procedures

A procedure is a step-by-step flow that runs when a caller's request matches its trigger. You can have up to **20 procedures** per receptionist.

| Field       | Limit                   | Notes                                                                         |
| ----------- | ----------------------- | ----------------------------------------------------------------------------- |
| **Name**    | Up to 200 characters    | Optional. Defaults to "Untitled procedure".                                   |
| **Trigger** | Up to 2,000 characters  | Required. Describes when to run, for example "When the caller wants to book". |
| **Steps**   | Up to 40,000 characters | Markdown. The instructions the receptionist follows.                          |

### References

In the steps, type **@** or select **Reference** to insert a reference to another procedure, a service, a staff member, a location, a tool, a variable, or a knowledge base file.

### Default procedures

New workspaces start with procedures for the flows the business supports, such as:

* Book an appointment (worded for your industry)
* Book a group session
* Reschedule or cancel a booking
* Place an order
* Check, change, or cancel an order
* Take a message for callback

Edit these to match how your business works, for example to collect extra details before booking.

### Example procedure

**Trigger:** When the caller reports a water leak.

**Steps:**

```markdown
1. Ask whether water is actively leaking right now.
2. If it is, tell them to shut off the main water valve, then take an urgent message for a callback within 30 minutes.
3. If it is not, collect the address and offer the next available inspection slot.
```

## Best practices

* Use **strict** sparingly, only for non-negotiable rules.
* Keep each rule to one instruction. Several focused rules work better than one long one.
* Put multi-step flows in procedures, not rules.
* Write procedure triggers from the caller's point of view.
* [Test](/docs/reception-ai/receptionist/testing) after every change.
