---
title: "Sentiment analysis"
source: https://elevenlabs.io/docs/eleven-agents/customization/agent-analysis/sentiment-analysis.md
path: docs/eleven-agents/customization/agent-analysis/sentiment-analysis
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Sentiment analysis

Sentiment analysis helps you understand whether users are having positive, neutral, or negative conversations with an agent.

Use it to identify topics, flows, or user intents that may need attention.

## Overview

Sentiment is calculated from completed conversations after the platform analyzes the transcript.

Sentiment can appear at different levels:

* Across the agent's conversations in the selected time window.
* Within topic discovery, where sentiment is aggregated for each topic.
* Within supporting conversations, where you can review examples behind a trend.

## Enable sentiment analysis

To enable sentiment analysis, open your agent's **Analysis** settings and turn on **Sentiment analysis**.

The same settings page also includes the **Topic discovery** toggle, which controls whether the agent's completed conversations are clustered into topics in Spotlight.

![Analysis settings showing sentiment analysis and topic discovery
toggles](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/75dff75af2e2aebca0ab6547562afef6f6b59fe988de2eea7814f27440dd2e53/assets/images/spotlight-analysis-settings.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260930%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260930T233221Z&X-Amz-Expires=604800&X-Amz-Signature=d59a0e0455d19ac2e3b25d5e157b6440bf0030e4a1bbdc347e09cf922aa525c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## How to interpret sentiment

Sentiment is most useful when combined with volume and conversation review.

* High-volume topics with negative sentiment usually deserve attention first.
* Low-volume negative sentiment can still matter if it involves compliance, safety, or customer escalation.
* Neutral sentiment can indicate routine conversations or conversations where the user did not express a clear emotion.

## Sentiment trajectory

For individual conversations, sentiment analysis can show how user sentiment changes over time.

Each scored user turn is plotted on a scale from negative to positive sentiment. Use the trajectory to identify where a conversation improved, declined, or stayed neutral.

![Sentiment over time chart showing scored user turns and the best moment in the
conversation](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/b095a26cc1fb6eb6a13adc01841628da32d357afe5783cce27fb6a64c2d58f0b/assets/images/sentiment-analysis-trajectory.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260930%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260930T233221Z&X-Amz-Expires=604800&X-Amz-Signature=d1e8635aa35c8d42309dedc5faf1c40e11d3a45fb5a2c6728b48605533378432&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Relationship to topic discovery

[Topic discovery](/docs/eleven-agents/dashboard/spotlight/topic-discovery) groups similar conversations into topics. Sentiment is then aggregated across the conversations assigned to each topic.

This helps you answer questions such as:

* Which topics are users most frustrated by?
* Which topics are improving over time?
* Which high-volume topics have mostly neutral or positive sentiment?

## Historical data

Historical conversations show sentiment only if sentiment analysis was generated for those conversations.

If older conversations appear in Spotlight but sentiment is unavailable, the underlying historical analysis may not exist for that period.
