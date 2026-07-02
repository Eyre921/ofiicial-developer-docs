---
title: "Marketing workflows"
source: https://trigger.dev/docs/guides/use-cases/marketing
path: docs/guides/use-cases/marketing
---

Learn how to use Trigger.dev for marketing workflows, including drip campaigns, behavioral triggers, personalization engines, and AI-powered content workflows

## Overview

Build marketing workflows from email drip sequences to orchestrating full multi-channel campaigns. Handle multi-day sequences, behavioral triggers, dynamic content generation, and build live analytics dashboards.

## Featured examples

<CardGroup>
  <Card title="Email sequences with Resend" icon="book" href="/guides/examples/resend-email-sequence">
    Send multi-day email sequences with wait delays between messages.
  </Card>

  <Card title="Product image generator" icon="book" href="/guides/example-projects/product-image-generator">
    Transform product photos into professional marketing images using Replicate.
  </Card>

  <Card title="Human-in-the-loop workflow" icon="book" href="/guides/example-projects/human-in-the-loop-workflow">
    Approve marketing content using a human-in-the-loop workflow.
  </Card>
</CardGroup>

## Benefits of using Trigger.dev for marketing workflows

**Delays without idle costs:** Wait hours or weeks between steps. Waits over 5 seconds are automatically checkpointed and don't count towards compute usage. Perfect for drip campaigns and scheduled follow-ups.

**Guaranteed delivery:** Messages send exactly once, even after retries. Personalized content isn't regenerated on failure.

**Scale without limits:** Process thousands in parallel while respecting rate limits. Send to entire segments without overwhelming APIs.

## Production use cases

<Card title="Icon customer story" href="https://trigger.dev/customers/icon-customer-story">
  Read how Icon uses Trigger.dev to process and generate thousands of videos per month for their AI-driven video creation platform.
</Card>

## Example workflow patterns

<Tabs>
  <Tab title="Drip email campaign">
    Simple drip campaign. User signs up, waits specified delay, sends personalized email, tracks engagement.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[userCreateAccount] --> B[sendWelcomeEmail]
          B --> C[wait.for 24h]
          C --> D[sendProductTipsEmail]
          D --> E[wait.for 7d]
          E --> F[sendFeedbackEmail]

      ```
    </div>
  </Tab>

  <Tab title="Multi-channel campaigns">
    **Router pattern with delay orchestration**. User action triggers campaign, router selects channel based on preferences (email/SMS/push), coordinates multi-day sequence with delays between messages, tracks engagement across channels.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[startCampaign] --> B[fetchUserProfile]
          B --> C[selectChannel]
          C --> D{Preferred<br/>Channel?}

          D -->|Email| E[sendEmail1]
          D -->|SMS| F[sendSMS1]
          D -->|Push| G[sendPush1]

          E --> H[wait.for 2d]
          F --> H
          G --> H

          H --> I[sendFollowUp]
          I --> J[trackConversion]
      ```
    </div>
  </Tab>

  <Tab title="AI content with approval">
    **Supervisor pattern with approval gate**. Generates AI marketing content (images, copy, assets), pauses with wait.forToken for human review, applies revisions if needed, publishes to channels after approval.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[createCampaignAssets] --> B[generateAIContent]
          B --> C[wait.forToken approval]
          C --> D{Approved?}

          D -->|Yes| E[publishToChannels]
          D -->|Needs revision| F[applyFeedback]
          F --> B
      ```
    </div>
  </Tab>

  <Tab title="Survey response enrichment">
    **Coordinator pattern with enrichment**. User completes survey, batch triggers parallel enrichment from CRM/analytics, analyzes and scores responses, updates customer profiles, triggers personalized follow-up campaigns.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[processSurveyResponse] --> B[coordinateEnrichment]
          B --> C[batchTriggerAndWait]

          C --> D[fetchCRMData]
          C --> E[fetchAnalytics]
          C --> F[fetchBehaviorData]

          D --> G[analyzeAndScore]
          E --> G
          F --> G

          G --> H[updateCRMProfile]
          H --> I[triggerFollowUp]
      ```
    </div>
  </Tab>
</Tabs>

## Featured use cases

<CardGroup>
  <Card title="Data processing & ETL workflows" icon="database" href="/guides/use-cases/data-processing-etl">
    Build complex data pipelines that process large datasets without timeouts.
  </Card>

  <Card title="Media processing workflows" icon="film" href="/guides/use-cases/media-processing">
    Batch process videos, images, audio, and documents with no execution time limits.
  </Card>

  <Card title="AI media generation workflows" icon="wand-magic-sparkles" href="/guides/use-cases/media-generation">
    Generate images, videos, audio, documents and other media using AI models.
  </Card>

  <Card title="Marketing workflows" icon="bullhorn" href="/guides/use-cases/marketing">
    Build drip campaigns, create marketing content, and orchestrate multi-channel campaigns.
  </Card>
</CardGroup>
