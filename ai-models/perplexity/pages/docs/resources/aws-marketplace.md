---
title: "AWS Marketplace"
source: https://docs.perplexity.ai/docs/resources/aws-marketplace
path: docs/resources/aws-marketplace
---

Subscribe to the Perplexity API Platform through AWS Marketplace for consolidated billing and enterprise procurement.

The Perplexity API Platform is available as a SaaS listing on AWS Marketplace. You purchase API credits through your AWS account — credits are applied to your Perplexity API balance and work across all APIs (Sonar, Agent, Search, and Embeddings).

<Frame>
  <img alt="Perplexity API Platform on AWS Marketplace" />
</Frame>

<Note>
  This listing is for the **API Platform** (Sonar, Agent API, Search API, and Embeddings). It's a separate product from **Enterprise Pro**, which doesn't include API access.
</Note>

## Why Subscribe Through AWS Marketplace?

Purchasing through AWS Marketplace offers several advantages over direct billing:

* **Consolidated AWS billing** — charges appear on your existing AWS invoice alongside other AWS services, simplifying finance and accounting workflows
* **Enterprise procurement** — satisfies procurement requirements for organizations that mandate AWS Marketplace purchases; no separate vendor relationship needed
* **EDP eligible** — purchases count toward your AWS Enterprise Discount Program (EDP) commitments
* **Simplified vendor management** — no separate contract or payment method to maintain; AWS handles invoicing

<Card title="View the listing on AWS Marketplace" icon="aws" href="https://aws.amazon.com/marketplace/pp/prodview-fslss6gnscauq">
  Subscribe and get started with the Perplexity API Platform.
</Card>

## Pricing

The Perplexity API Platform on AWS Marketplace is available as a **1-month contract** with API platform credits:

| Plan                     |       Credits       | Contract |
| ------------------------ | :-----------------: | :------: |
| **API Platform Credits** | Starting at \$1,000 |  1-month |

Credits are denominated 1:1 with USD — 1 credit = \$1. Credits are applied to your account balance and drawn down as you make API requests.

<Note>
  All Perplexity API products — Sonar, Agent API, Search API, and Embeddings — draw from the same shared credit pool. You don't need separate budgets per product.

  For per-request and per-token pricing details, see the <u>[Pricing page](/docs/getting-started/pricing)</u>.
</Note>

## How to Subscribe

<Tip>
  Credits don't expire — the **1-month contract** refers to the billing cycle, not a usage deadline, so unused credits remain on your balance.
</Tip>

1. Visit the <u>[Perplexity API Platform listing](https://aws.amazon.com/marketplace/pp/prodview-fslss6gnscauq)</u> on AWS Marketplace
2. Click **View purchase options**
3. Choose your credit amount, then click **Create contract**
4. Confirm the purchase — AWS will process the subscription and notify you by email

<Frame>
  <img alt="AWS Marketplace pricing — API platform credits at $1,000/month" />
</Frame>

Once your subscription is confirmed, you'll receive instructions to link your AWS Marketplace account to the Perplexity API Platform.

## Getting Started After Subscribing

After your AWS Marketplace subscription is confirmed:

1. **Sign in or create an account** — go to <u>[console.perplexity.ai](https://console.perplexity.ai)</u> and sign in with your Perplexity account (or create one if you don't have one yet)
2. **Link your subscription** — follow the prompts in the console to connect your AWS Marketplace purchase to your Perplexity account; this associates your purchased credits with your API Group
3. **Set up your API Group** — your credits are tied to an API Group (your organization's workspace in the API Portal). The person who completes the setup becomes the Admin, with full access to billing, API keys, and member invitations. Additional members can join as Admins (full access) or Members (view-only). See <u>[API Groups & Billing](/docs/getting-started/api-groups)</u>.
4. **Generate an API key** — go to API Keys in the console to create a key for your API Group. See <u>[API Key Management](/docs/admin/api-key-management)</u>.
5. **Start making requests** — credits are applied to your API Group's balance and shared across all products (Sonar, Agent API, Search API, Embeddings). Monitor remaining balance and usage in the console at any time.

<Frame>
  <img alt="Generating API keys in the Perplexity console" />
</Frame>

## Refund Policy

If you need to cancel your subscription, refunds are available **within 14 days of purchase** provided that **no credits have been used**. To request a refund, contact <u>[aws-api@perplexity.ai](mailto:aws-api@perplexity.ai)</u> with your AWS Marketplace order ID.

<Warning>
  Refunds are not available once any credits have been consumed, or after the 14-day window has passed.
</Warning>

## Support

For questions about your AWS Marketplace subscription, billing, or API usage, contact the Perplexity API team:

**Email:** <u>[aws-api@perplexity.ai](mailto:aws-api@perplexity.ai)</u>

For issues related to AWS Marketplace registration or account linking, contact the Clazar support team:

**Email:** <u>[support@clazar.io](mailto:support@clazar.io)</u>

Include your AWS Marketplace order ID or account email when reaching out so we can locate your subscription quickly.

## Additional Resources

<CardGroup>
  <Card title="Quickstart" icon="bolt" href="/docs/getting-started/quickstart">
    Make your first API request in minutes.
  </Card>

  <Card title="Pricing" icon="calculator" href="/docs/getting-started/pricing">
    Per-request and per-token pricing for all APIs.
  </Card>

  <Card title="AWS Marketplace listing" icon="aws" href="https://aws.amazon.com/marketplace/pp/prodview-fslss6gnscauq">
    View the Perplexity API Platform listing on AWS Marketplace.
  </Card>
</CardGroup>
