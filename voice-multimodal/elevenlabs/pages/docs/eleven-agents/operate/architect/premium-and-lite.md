---
title: "Architect Premium and Lite"
source: https://elevenlabs.io/docs/eleven-agents/operate/architect/premium-and-lite.md
path: docs/eleven-agents/operate/architect/premium-and-lite
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Architect Premium and Lite

## Overview

Every ElevenAgents Architect conversation runs on one of two tiers. **Architect Premium** runs on our most capable model. **Architect Lite** runs on a faster, lighter model and costs less per conversation. Both tiers have the same tools, permissions, and approval modes, and both can read and change the same resources.

| Tier    | Model                   | Best for                                                                                                          |
| ------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Premium | Our most capable model  | Investigating failures across many conversations, multi-step changes to prompts and workflows, and writing tests. |
| Lite    | A faster, lighter model | Product questions, dashboard walkthroughs, single edits, and summaries of a conversation you already have.        |

Premium conversations cost more than Lite conversations. See [Pricing and usage](/docs/eleven-agents/operate/architect/pricing) for how Architect is billed.

## Which tier you get

| Plan       | Premium                                                  | Lite                                |
| ---------- | -------------------------------------------------------- | ----------------------------------- |
| Self-serve | One Premium conversation per user per day.               | Every other conversation.           |
| Enterprise | The default for every conversation, with no daily limit. | Choose it for any new conversation. |

Architect is available on paid plans.

### Self-serve plans

On self-serve plans, your first new conversation of the day runs on Premium unless you choose Lite. Every other new conversation that day runs on Lite. The limit is per user, not per workspace, and it resets at midnight UTC.

Resuming your Premium conversation on the same day keeps it on Premium, for example after the session ends from being idle or when you open it again from chat history. Resuming a conversation on a later day counts toward that day: it runs on Premium if that day's Premium conversation is still available, and on Lite if it is not. A Slack thread counts as one conversation.

Self-serve plans cannot buy additional Premium conversations. Enterprise plans run on Premium with no daily limit. [Contact sales](https://elevenlabs.io/contact-sales) to move to an Enterprise plan.

### Enterprise plans

On Enterprise plans, every conversation runs on Premium unless you choose Lite before the first message. There is no daily limit, and choosing Lite is a way to lower the cost of simpler conversations.

## Choose a tier

Choose the tier before you send the first message of a conversation. Once the conversation starts, the tier is locked for that conversation. To use a different tier, start a new conversation.

#### Web

Open the tier menu in the composer controls and select **Premium** or **Lite**. On self-serve
plans, **Premium** is unavailable once you have used today's Premium conversation, and the menu
shows when it is back.

#### Slack

Architect in Slack is in private alpha.

Start your message with `premium` or `lite` after mentioning Architect, for example `@Architect
    lite summarize yesterday's failed calls`. Replies in the same thread keep the thread's tier.
Without a keyword, the thread uses your plan's default.

## See which tier you are on

The chat header shows a **Premium** or **Lite** badge for the current conversation. Hover over it to see which model it runs on.

On self-serve plans, the composer also shows whether today's Premium conversation is still available:

* **1 Premium chat a day · Available** means your next new conversation runs on Premium.
* **1 Premium chat a day · Used · Resets at** a time means new conversations run on Lite until that time.

When a new conversation starts on Lite because today's Premium conversation is used, Architect shows a notice in the chat: "Today's Premium chat is used, so this chat runs on Architect Lite."

## When to use each tier

Use Premium when the answer depends on reasoning across a lot of data or several steps:

* Finding why calls fail by reading many conversations and comparing them.
* Changing a prompt, procedure, or workflow and then writing and running tests for the change.
* Building a new agent from a description.

Use Lite when the task is narrow and the answer is close at hand:

* Asking how a feature works or where a setting is.
* Making one known edit, such as changing the first message or adding a knowledge base document.
* Summarizing a single conversation or test run you already have open.

Lite is not recommended for analytical or complex work. If a Lite conversation struggles with a task, start a new conversation on Premium instead of retrying on Lite. Retries add messages, and every message adds cost.

On self-serve plans, save your Premium conversation for the day's hardest task. Choose **Lite** for quick questions while your Premium conversation is still available, so a short question doesn't use it up.

## FAQ

#### Can I switch a conversation from Lite to Premium?

No. The tier is locked once a conversation starts. Start a new conversation to use a different
tier. On self-serve plans, the new conversation runs on Premium only if today's Premium
conversation is still available.

#### Do Premium and Lite have different capabilities?

No. Both tiers have the same tools and permissions. Premium is better at long, multi-step work
and at reasoning across many conversations.

#### Is the daily Premium conversation shared across my workspace?

No. Each user on a self-serve plan gets their own Premium conversation per day.

#### Does choosing Lite use my Premium conversation?

No. A conversation you start on Lite leaves today's Premium conversation available.

#### Which tier do Slack conversations use?

The same rules as the web app. Architect in Slack is in private alpha.
