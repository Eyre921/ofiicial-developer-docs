---
title: "Campaigns"
source: https://elevenlabs.io/docs/eleven-agents/phone-numbers/campaigns.md
path: docs/eleven-agents/phone-numbers/campaigns
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Campaigns

> **Info**
>
> Outbound calling is regulated differently by country, state, and industry, so the right calling
> hours and attempt limits depend on who you call and why. You are responsible for outbound calling
> compliance, including consents, what the agent says, and managing next steps, and for setting
> limits that match the rules where your contacts live. See the [ElevenAgents Terms](https://elevenlabs.io/agents-terms) and the [TCPA guidance](/docs/eleven-agents/legal/tcpa)
> for details.

## Overview

Campaigns run outbound communications for your agents. You submit a list of recipients, and your campaign contacts them across retries, callbacks, redirects, and calling windows until each recipient reaches a final outcome, controlled by you. Campaigns replace batch calling.

### What are campaigns for

Use campaigns for outreach that takes more than one call to complete:

* **Conversation-driven follow-ups.** A recipient asks to be called back at 4pm, or asks you to try a colleague's number. Your campaign reads the call analysis and schedules the right next call.
* **Calling windows.** Calls are only placed inside the windows you define, evaluated in your specified timezone. The one exception is a callback at a time the recipient requested, which is dialed at that time.
* **Bounded persistence.** Failed and unanswered calls are retried on a schedule, up to ceilings you control.
* **Operator visibility.** You can see every recipient, every call, and why each decision was made, and you can pause or cancel at any time.

## Campaign policy

A campaign's policy defines how persistent it is and when it may call. You set a default policy for your workspace, and each campaign takes a snapshot of it when it is created. Changing the workspace policy later only affects campaigns created afterwards.

```json
{
  "policy": {
    "timezone": "America/New_York",
    "retry": {
      "retry_delay_seconds": 600,
      "max_short_retries": 1,
      "max_total_calls": 6,
      "max_callbacks": 2,
      "max_redirects": 2,
      "interval_placement": "start"
    },
    "calling_periods": [
      {
        "weekdays": [0, 1, 2, 3, 4],
        "intervals": [
          { "start": "10:00", "end": "12:00" },
          { "start": "16:00", "end": "18:00" }
        ]
      }
    ],
    "data_collection": {
      "callback_time": "__system_data_collection_callback_time",
      "redirect_phone_number": "__system_data_collection_redirect_phone_number",
      "stop": "__system_data_collection_do_not_call"
    }
  }
}
```

### Retry limits

| Field                                 | Description                                                                                                                                                      |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `retry_delay_seconds`                 | Delay before a short retry after a failed, unanswered, or voicemail call.                                                                                        |
| `max_total_calls`                     | Hard ceiling on attempts per recipient, including the first call. A recipient is never called more than this many times. Default 6, maximum 30.                  |
| `max_short_retries`                   | Short retries allowed in each calling window before the retry moves to the next window.                                                                          |
| `max_callbacks`, `max_redirects`      | Ceilings on callbacks and redirects a recipient can request. Retry and callback budgets reset per number when a call is redirected.                              |
| `max_consecutive_failures_per_number` | Optional. Failures in a row on one number before the recipient moves to the next number on record (up to five per recipient), or finishes if there is none.      |
| `interval_placement`                  | Where a call lands when it is pushed into a future window: the start of the window, a random time within it, or rotated to avoid times that have already failed. |

### Calling windows

`calling_periods` define the weekly windows in which calls may be placed. Weekdays are numbered 0 to 6, where Monday is 0. Times are local `HH:MM` in the policy `timezone`, and intervals on the same weekday cannot overlap.

Exact-time callbacks are the one exception. When a recipient asks to be called at a specific time, that call is dialed at that time, even if it falls outside your windows. Set max_callbacks with this in mind.

A policy has a single `timezone`. If your contacts are in several time zones, create a separate campaign for each zone, with its own `timezone` and calling windows, so every call lands inside permitted hours where the recipient lives.

### Dynamic variable mapping

Campaigns attach the default data collection items to your agent with one click, which enables callbacks, redirects, and stop calling.

You can also map additional analysis results into [dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables) for follow-up calls, so a retry or callback can start with what was learned on the previous call.

### Follow-up context

Reference these variables in your agent's prompt to make callbacks feel continuous.

| Variable                             | Contains                                                           |
| ------------------------------------ | ------------------------------------------------------------------ |
| `campaign__call_type`                | Whether the call is a first contact, retry, callback, or redirect. |
| `campaign__previous_conversation_id` | The ID of the previous conversation with the recipient.            |
| `campaign__previous_summary`         | The summary of the previous conversation.                          |
| `campaign__previous_transcript`      | The transcript of the previous conversation.                       |

## Channels

| Channel  | Mode  | Notes                                                                                                                                                 |
| -------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Phone    | Voice | Full retry, callback, and redirect behavior.                                                                                                          |
| WhatsApp | Voice | A single permission request is sent per recipient, followed by retries and callbacks. See [WhatsApp outbound](/docs/eleven-agents/whatsapp/outbound). |
| WhatsApp | Text  | Sends an approved WhatsApp message template to each recipient. Retries do not apply. See [WhatsApp outbound](/docs/eleven-agents/whatsapp/outbound).  |

Email and SMS channels are coming soon.

## Create a campaign

#### Open Campaigns

In the ElevenAgents navigation, select **Campaigns**.

#### Save your workspace policy

Open **Settings**, define your timezone, retry limits, and calling windows, then save. See
[Campaign policy](#campaign-policy).

#### Create the campaign

Select **New campaign**, choose an agent, a channel, and a phone number, then upload your
recipients. Upload a CSV, or submit recipients through the API with the same request shape as a
batch call. Each recipient can have up to five phone numbers (`phone_number` through
`phone_number_5` in the CSV).

#### Enable advanced features

Toggle the **Advanced controls** to enable retries, callbacks, and follow-ups within specified
calling windows. These will automatically propagate from your workspace settings, or you can
tweak them here for each campaign.

#### Monitor progress

Follow progress on the **Analytics** tab.

Calls are queued when you create a campaign and dialed once they fall inside a calling window.

> **Warning**
>
> Campaigns are not available for workspaces or agents using [Zero Retention Mode](/docs/eleven-agents/customization/privacy/zrm). Follow-up decisions depend on durable call
> state and conversation analysis, so requests from zero-retention workspaces and submissions for
> zero-retention agents are rejected.

## Concurrency

Campaign calls count toward your workspace and agent concurrency limits. By default, a campaign uses the lower of 50% of your workspace concurrency or 70% of the agent's concurrency. You can set a lower cap for an individual campaign.

## API

Campaign creation, management, and analytics are available through the ElevenLabs API, which lets you integrate campaigns into your existing workflows and applications. See the [API reference](/docs/api-reference/introduction) for the available endpoints.

## Best practices

* **Start narrow.** Test with a short list and a conservative `max_total_calls` before launching to the full audience.
* **Set windows deliberately.** Calling windows are your main control for respecting local calling hours. Set `timezone` to where your recipients are, and keep windows well inside permitted hours.
* **Collect the follow-up signals.** Campaigns only handle callbacks, redirects, and do-not-call requests if the agent captures them. Tell the agent in its prompt when to record each one.
* **Use follow-up context.** Reference `campaign__previous_summary` in your prompt so a retry or callback picks up where the last call left off instead of repeating the opening.
* **Keep ceilings low.** Persistence is a cost to your recipients as well as to you. Prefer a few well-timed attempts to many.

## FAQ

#### Can I change a running campaign's policy?

No. A campaign's policy is fixed when it is created. Changes to your workspace policy apply to
campaigns you create afterwards. To change a running campaign, stop it and create a new one.

#### Can a recipient be in more than one campaign?

Each campaign tracks its own leads, and do-not-call state belongs to the campaign. Deduplicate
recipients across campaigns before creating them if you need to avoid contacting someone twice.

## Next steps

* [Data collection](/docs/eleven-agents/customization/agent-analysis/data-collection): Capture the signals your agent acts on.
* [Dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables): Personalize each recipient's call.
* [Guardrails](/docs/eleven-agents/best-practices/guardrails): Keep your outbound agent on-topic and on-brand.
