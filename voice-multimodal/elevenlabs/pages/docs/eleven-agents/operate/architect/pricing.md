---
title: "Pricing and usage"
source: https://elevenlabs.io/docs/eleven-agents/operate/architect/pricing.md
path: docs/eleven-agents/operate/architect/pricing
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Pricing and usage

## Overview

ElevenAgents Architect is billed on usage. Each conversation is charged to your workspace's credits based on the model tokens it uses. Architect usage appears as its own **Architect** line item, separate from your agents' minutes and LLM cost.

The same pricing applies wherever you use Architect: the sidebar chat, the Architect tab, and Slack. Architect in Slack is in private alpha.

> **Note**
>
> Billing for Architect started after the alpha ended in October 2026 and is being turned on
> gradually. To see how your workspace is billed, check the note under the Architect composer.

## What is billed

Architect charges for the model tokens used to answer you. That includes your messages and Architect's replies, plus the work Architect does in the background for a conversation, such as analyzing conversations and summarizing long chats to keep them within the model's context.

Some things affect what a conversation costs:

* **Length.** Every message adds to the conversation's context, so long conversations cost more per message than short ones. Start a new conversation when you switch to an unrelated task.
* **Investigation depth.** Requests that read many conversations, run tests, or edit several resources take more steps than a product question.
* **Model tier.** Premium conversations cost more than Lite conversations. See [Premium and Lite](#premium-and-lite).

Your agents' own conversations, tests, and simulations are billed as usual, even when Architect starts them.

## Premium and Lite

Architect runs in one of two tiers:

| Tier    | Model                   | Use it for                                                                      |
| ------- | ----------------------- | ------------------------------------------------------------------------------- |
| Premium | Our most capable model  | Investigations across many conversations, multi-step changes, and test writing. |
| Lite    | A faster, lighter model | Product questions, quick edits, and lower-cost conversations.                   |

The tier is set when a conversation starts and stays the same for that conversation. The chat header shows the tier of the current conversation.

### Self-serve plans

On self-serve plans, each user gets one Premium conversation per day. Your first new conversation of the day runs on Premium. Every other conversation that day runs on Lite. The Premium conversation resets at midnight UTC.

Resuming a Premium conversation, for example after an idle session ends, keeps it on Premium and does not use another day's conversation. A Slack thread counts as one conversation.

### Enterprise plans

On Enterprise plans, conversations run on Premium by default and have no daily limit. To start a conversation on Lite and lower its cost, choose the tier before you send the first message:

#### Web

Select **Premium** or **Lite** in the composer controls before you send the first message. The
choice is locked once the conversation starts. Choosing a different tier starts a new
conversation.

#### Slack

Architect in Slack is in private alpha.

Start your message with `premium` or `lite` after mentioning Architect, for example `@Architect
    lite summarize yesterday's failed calls`. Replies in the same thread keep the thread's tier.

## Plans and credits

| Plan        | How Architect is billed                                                                              |
| ----------- | ---------------------------------------------------------------------------------------------------- |
| Free        | Not available. Upgrade to a paid plan to use Architect.                                              |
| Self-serve  | Uses your workspace's credits. One Premium conversation per user per day, then Lite.                 |
| Enterprise  | Uses your workspace's credits. Premium by default, with Lite available per conversation.             |
| ElevenEmbed | Uses the Architect allowance included in your ElevenEmbed plan first, then your workspace's credits. |

The note under the Architect composer shows which of these applies to your workspace, and tells ElevenEmbed workspaces when their allowance is used up.

### Running out of credits

When your workspace is out of credits and cannot go over its limit, Architect does not start new conversations. If credits run out during a conversation, Architect finishes its current reply and then ends the session. In both cases you see a message asking you to add credits or upgrade your plan. In Slack, the message is sent privately to you.

Enterprise and trial workspaces are not blocked from starting Architect conversations for being at their credit limit. Their usage is still billed.

## Track usage

Workspace members can see Architect usage on the **Usage** tab of the Architect page. Open **Agents** > **Architect** and select **Usage**.

The tab has these views:

* **Cost** shows what Architect has cost over the selected time range.
* **Conversations** shows how many Architect conversations were held.
* **Access** controls who can use Architect. Only workspace admins see this view.

Switch between **My usage** and **Team** to see your own usage or a breakdown by workspace member.

## Control who can use Architect

Workspace admins can limit Architect to specific members from the **Access** view of the **Usage** tab. Access applies in both the web app and Slack.

1. Open **Agents** > **Architect** and select **Usage** > **Access**.
2. Turn off **Everyone in this workspace**.
3. Turn Architect on for each member who should keep access, or use **Turn all on** and **Turn all off** for the members shown by your search.
4. Review the summary of who gains and loses access, then select **Save changes**.

Admins always have access to Architect. Members who get access through a [workspace group](/docs/overview/administration/workspaces/user-groups) keep it until they are removed from the group. When **Everyone in this workspace** is off, new members do not get Architect automatically.

## FAQ

#### Does Architect usage count against my agents' minutes or LLM cost?

No. Architect usage is billed as its own Architect line item from your workspace's credits.

#### Is there a separate subscription for Architect?

No. Architect is included in paid plans and billed from the same credits as the rest of your
workspace.

#### Does a Premium conversation that I resume tomorrow use tomorrow's Premium conversation?

Resuming a Premium conversation keeps it on Premium without using another Premium conversation.

#### Can a self-serve workspace get more Premium conversations?

No. Self-serve plans include one Premium conversation per user per day. Enterprise plans run on
Premium by default with no daily limit. [Contact sales](https://elevenlabs.io/contact-sales) to
move to an Enterprise plan.

#### Are Architect conversations in Slack billed differently?

No. Slack conversations use the same tiers and pricing as the web app. Architect in Slack is in
private alpha. A Slack thread is one conversation.
