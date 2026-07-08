---
title: "Real-time insights"
source: https://elevenlabs.io/docs/eleven-agents/dashboard/spotlight/real-time-insights.md
path: docs/eleven-agents/dashboard/spotlight/real-time-insights
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Real-time insights

Real-time insights show what is happening with an agent now and what may need attention next.

Use this view to monitor activity, review trend changes, and act on suggested improvements without digging through every conversation manually.

## Overview

Real-time insights combine recent conversation metrics, agent configuration, and conversation analysis results into a single operational view.

The view is useful for answering questions such as:

* Is this agent receiving the expected number of conversations?
* Did a recent change affect volume, duration, cost, or success rate?
* Are conversations hitting limits or failing in a repeated way?
* Is there a suggested configuration change that could improve performance?

Some data updates in near real time. Analysis-based fields can appear after a conversation ends and the transcript has been processed.

## What you can review

Real-time insights can include:

* **Conversation volume**: Recent conversation count and changes over the selected time window.
* **Success rate**: The share of evaluated conversations that passed your configured success criteria.
* **Usage trends**: Changes in duration, cost, or other activity metrics.
* **Operational issues**: Patterns such as conversations hitting duration limits or using deprecated configuration.
* **Suggested actions**: Recommendations to inspect, update, or configure based on the issue.

The exact metrics and suggestions depend on the agent configuration and the conversations available in the workspace.

## Suggestions and recommendations

Spotlight can surface cards when it detects something that may need attention.

For example, a suggestion may recommend that you:

* Update a deprecated speech or language model.
* Inspect conversations that are reaching the maximum call duration.
* Configure a newer model when it may improve quality or reliability.

Suggestions are designed to point you to the next useful action. They do not replace conversation review, testing, or evaluation criteria.

## How to use real-time insights

Use Real-time insights as the first step in an investigation:

### Review the headline cards

Start with suggested actions and the top-level trend charts. Look for large changes, repeated issues, or recommendations marked as important.

### Inspect the affected conversations

If a card points to a pattern, open the relevant conversations and review examples before changing the agent.

### Compare with analysis results

Use [Topic discovery](/docs/eleven-agents/dashboard/spotlight/topic-discovery), [Sentiment analysis](/docs/eleven-agents/customization/agent-analysis/sentiment-analysis), and [Analytics](/docs/eleven-agents/dashboard) to confirm whether the issue is isolated or part of a broader trend.

### Apply and monitor changes

After updating the agent, continue monitoring the same metrics to confirm whether the change improved the outcome.

## Relationship to deeper analysis

Real-time insights are for monitoring and triage. They help you decide where to look first.

Deeper analysis, such as sentiment and topic discovery, depends on completed conversations and post-conversation analysis. If a conversation is still active or has just ended, some analysis fields may not appear immediately.

Use real-time insights to find unusual activity, then review the supporting conversations before
changing prompts, tools, models, or evaluation criteria.
