---
title: "Account quotas"
source: https://docs.fireworks.ai/guides/quotas_usage/account-quotas
path: guides/quotas_usage/account-quotas
---

Account-wide request limits, spending tiers, budget controls, and on-demand GPU quotas

<a />

Fireworks uses different controls for serverless and on-demand deployments. This page is the canonical reference for spending tiers, budget controls, on-demand GPU quotas, and account-wide request limits.

For serverless TPM and adaptive limits, see [Serverless rate limits](/serverless/rate-limits).

## Check your current limits

View your account's current quotas and limits:

```bash theme={null}
firectl quota list
```

This shows your rate limits, GPU quotas, spend limits, and usage across serverless and on-demand deployments.

## Spending tiers

Your account tier determines the maximum budget you can set:

| Tier      | Criteria                                                                 | Max Monthly Budget |
| --------- | ------------------------------------------------------------------------ | ------------------ |
| Tier 1    | [Valid payment method and billing profile](https://fireworks.ai/billing) | \$50               |
| Tier 2    | Spend or add \$50 in credits                                             | \$500              |
| Tier 3    | Spend or add \$500 in credits                                            | \$5,000            |
| Tier 4    | Spend or add \$5,000 in credits                                          | \$50,000           |
| Unlimited | [Contact us](https://fireworks.ai/company/contact-us)                    | Unlimited          |

<Tip>
  Add prepaid credits to unlock a higher tier. For example, adding \$100 moves you from Tier 1 to Tier 2. Your new tier activates within minutes.
</Tip>

<Note>
  These spending tiers control both your maximum monthly budget and the maximum [serverless TPM upper bounds](/serverless/rate-limits) your account can reach.

  Fireworks operates on a pre-paid credits billing system. Contracted customers may have the option to move to post-paid billing — [contact our sales team](https://fireworks.ai/company/contact-us) to discuss your options.
</Note>

### Training GPU quota

Fine-tuning jobs use training GPU quota (separate from on-demand deployment quota), granted automatically by spending tier:

| Tier              | How to reach it                                       | B200 / B300 (Blackwell) |  H200  | H100 / A100 |
| ----------------- | ----------------------------------------------------- | :---------------------: | :----: | :---------: |
| No payment method | —                                                     |            0            |    0   |      0      |
| Tier 1            | Valid payment method and billing profile              |            0            |   16   |      8      |
| Tier 2            | Spend or add \$50 in credits                          |            16           |   16   |      16     |
| Tier 3            | Spend or add \$500 in credits                         |            24           |   24   |      24     |
| Tier 4            | Spend or add \$5,000 in credits                       |            32           |   32   |      32     |
| Enterprise        | [Contact us](https://fireworks.ai/company/contact-us) |          Custom         | Custom |    Custom   |

Counts are GPUs of that type available to training jobs. Blackwell (B200/B300) is `0` until Tier 2, and current managed fine-tuning shapes run on Blackwell, so most fine-tuning needs Tier 2. If a job is rejected with HTTP 429 `quota_exceeded`, raise your tier and resubmit.

<Note>
  Need more training quota than your tier allows? [Reach out for enterprise support](https://fireworks.ai/contact-training) and we'll help size the right allocation for your workload.
</Note>

### Enterprise accounts

Enterprise accounts do not have the same spend limits. If you have an Enterprise account, the spending tiers and budget controls described on this page do not apply to you. For information about Enterprise quotas and resource allocation, see [Enterprise quotas](/faq/enterprise/service/quotas) or contact your enterprise account representative.

## Manage your quotas

<h3>
  Account-wide request limits
</h3>

All API usage on your account shares a single request-throughput envelope:

| Account state                     |  Request-rate limit |
| --------------------------------- | ------------------: |
| No payment method or no credits   |              10 RPM |
| Payment method and active credits | 6,000 RPM (maximum) |

The **6,000 RPM** cap applies account-wide—it is **not** a separate serverless-only limit—and it is a **fixed** ceiling, not adaptive. Per-minute request volume above this cap is rejected (for example HTTP 429), regardless of your spending tier.

### Budget control

Control your monthly spending with flexible budget limits. Set a limit that fits your needs and adjust it anytime.

### View and adjust your spend limit

Check your current spend limit:

```bash theme={null}
firectl quota list
```

Set a custom monthly budget:

```bash theme={null}
firectl quota update monthly-spend-usd --value <AMOUNT>
```

For example, to set a \$200 monthly budget:

```bash theme={null}
firectl quota update monthly-spend-usd --value 200
```

### When you reach your budget

When you reach your spending limit, all API requests pause automatically across serverless inference, deployments, and fine-tuning. To resume, [add credits](https://fireworks.ai/billing) and/or raise your budget cap.

<Note>
  This does not apply to Enterprise accounts. Enterprise accounts do not have the same spend limits and will not be paused due to spending.
</Note>

### On-demand deployment quotas

On-demand deployments have GPU quotas instead of rate limits:

| GPU Type          | Default Quota |
| ----------------- | ------------- |
| Nvidia A100       | 8 GPUs        |
| Nvidia H100       | 8 GPUs        |
| Nvidia H200       | 8 GPUs        |
| Nvidia B200       | 8 GPUs        |
| LoRAs (on-demand) | 100           |

<Tip>
  Need more GPUs? [Contact us](https://fireworks.ai/company/contact-us) to request a quota increase.
</Tip>

<Callout type="info">
  On-demand and dedicated deployments are **not limited by adaptive serverless TPM upper bounds**. If you receive HTTP **429** on those endpoints, it typically means **deployment saturation** (GPUs busy) rather than hitting a TPM tier cap. Requests still count toward [account-wide request limits](#account-wide-request-limits). See [understanding 429 errors](/guides/inference-error-codes#understanding-429-errors) for details and resolution steps.
</Callout>

### Account recovery

If your account is suspended due to payment issues:

1. Go to [Billing](https://fireworks.ai/billing)
2. Resolve failed payment methods and add credits (or pay outstanding invoices for postpaid accounts)
3. Your account reactivates automatically within an hour

<Tip>
  Still suspended after resolving payment issues? Contact support via [Discord](https://discord.gg/fireworks-ai) or email [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai).
</Tip>
