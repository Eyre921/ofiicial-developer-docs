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

* **Length.** Every message adds to the conversation's context, so long conversations cost more per message than short ones.
* **Investigation depth.** Requests that read many conversations, run tests, or edit several resources take more steps than a product question.
* **Model tier.** Premium conversations cost more than Lite conversations. See [Architect Premium and Lite](/docs/eleven-agents/operate/architect/premium-and-lite).

See [Reduce Architect costs](#reduce-architect-costs) for ways to keep each conversation's cost down.

Your agents' own conversations, tests, and simulations are billed as usual, even when Architect starts them.

## Reduce Architect costs

Most of a conversation's cost comes from how much context Architect carries and how many steps it takes. These habits keep both down:

* **Start a new conversation when the topic changes.** Every message is sent with the conversation so far, so a long conversation costs more per message. A fresh conversation for an unrelated task starts with no history to carry.
* **Use Lite for simpler questions.** Product questions, single edits, and summaries of a conversation you already have rarely need Premium. Choose **Lite** in the composer before the first message. On self-serve plans, this also keeps your daily Premium conversation for a task that needs it.
* **Move to Premium instead of retrying.** If Lite struggles with a task, start a new conversation on Premium rather than rephrasing the request several times on Lite.
* **Scope the request.** Name the agent, the time range, and how many conversations to read, for example "the 20 most recent failed calls for the booking agent" instead of "all conversations". Architect reads less to reach the same answer.
* **Give it what you already know.** Paste the conversation ID, the failing test, or the error message. Architect can go straight to the cause instead of searching for it.
* **Save standing context once.** Put conventions Architect would otherwise rediscover, such as naming rules, testing standards, and which branch to work on, in your [agent context and preferences](/docs/eleven-agents/operate/architect/customization).
* **Run only the tests you need.** Ask Architect to run the tests related to the change rather than the full suite. Tests and simulations are billed as your agent's usage, and reading their results adds to the Architect conversation.
* **Check what you spend.** Review **Usage** > **Cost** regularly, and use the **Team** view to see who uses Architect most. Admins can [limit who can use Architect](#control-who-can-use-architect).

## Premium and Lite

Architect runs in one of two tiers. **Premium** runs on our most capable model and suits investigations across many conversations, multi-step changes, and test writing. **Lite** runs on a faster, lighter model, suits product questions and quick edits, and costs less.

On self-serve plans, each user gets one Premium conversation per day, and every other conversation runs on Lite. On Enterprise plans, conversations run on Premium by default with no daily limit, and you can choose Lite for any new conversation. The tier is chosen before the first message and is locked for the rest of the conversation.

See [Architect Premium and Lite](/docs/eleven-agents/operate/architect/premium-and-lite) for how the tier is set, how to choose one in the web app and Slack, and which tasks suit each.

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

Yes. Resuming it the same day keeps it on Premium. On a later day, a resumed conversation runs
on Premium only if that day's Premium conversation is still available, and using it counts as
that day's Premium conversation. Otherwise it runs on Lite.

#### Can a self-serve workspace get more Premium conversations?

No. Self-serve plans include one Premium conversation per user per day. Enterprise plans run on
Premium by default with no daily limit. [Contact sales](https://elevenlabs.io/contact-sales) to
move to an Enterprise plan.

#### Are Architect conversations in Slack billed differently?

No. Slack conversations use the same tiers and pricing as the web app. Architect in Slack is in
private alpha. A Slack thread is one conversation.
