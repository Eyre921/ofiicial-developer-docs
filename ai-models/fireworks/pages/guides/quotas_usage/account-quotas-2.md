---
title: "Account quotas"
source: https://docs.fireworks.ai/guides/quotas_usage/account-quotas
path: guides/quotas_usage/account-quotas
---

Account-wide request limits, spending tiers, spend limits, and on-demand GPU quotas

Fireworks uses different controls for serverless and on-demand deployments. This page is the canonical reference for spending tiers, monthly spend limits, on-demand GPU quotas, and account-wide request limits.

For serverless TPM and adaptive limits, see [Serverless rate limits](/serverless/rate-limits).

## Check your current limits

View your account's current quotas and limits:

```bash theme={null}
firectl quota list
```

This shows your rate limits, GPU quotas, spend limits, and usage across serverless and on-demand deployments.

## Spending tiers

Your spend tier controls available quotas and capacity. For legacy self-serve postpaid accounts, it also determines the maximum monthly spend limit. Prepaid accounts can set a monthly spend limit independently of tier.

| Tier      | Criteria                                                                 | Legacy Postpaid Max Monthly Spend Limit |
| --------- | ------------------------------------------------------------------------ | --------------------------------------- |
| Tier 1    | [Valid payment method and billing profile](https://fireworks.ai/billing) | \$50                                    |
| Tier 2    | Spend or add \$50 in credits                                             | \$500                                   |
| Tier 3    | Spend or add \$500 in credits                                            | \$5,000                                 |
| Tier 4    | Spend or add \$5,000 in credits                                          | \$50,000                                |
| Unlimited | [Contact us](https://fireworks.ai/company/contact-us)                    | Unlimited                               |

<Tip>
  Add prepaid credits to unlock a higher tier. For example, adding \$100 moves you from Tier 1 to Tier 2. Your new tier activates within minutes.
</Tip>

<Note>
  These spending tiers control the maximum [serverless TPM upper bounds](/serverless/rate-limits) your account can reach. The spend-limit maximum shown above applies only to legacy self-serve postpaid accounts.

  Fireworks operates on a pre-paid credits billing system. Contracted customers may have the option to move to post-paid billing — [contact our sales team](https://fireworks.ai/company/contact-us) to discuss your options.
</Note>

### Training GPU quota

Training jobs use training GPU quota (separate from on-demand deployment quota), granted automatically by spending tier:

| Tier              | How to reach it                                       | B200 / B300 (Blackwell) |  H200  | H100 / A100 |
| ----------------- | ----------------------------------------------------- | :---------------------: | :----: | :---------: |
| No payment method | —                                                     |            0            |    0   |      0      |
| Tier 1            | Valid payment method and billing profile              |            0            |   16   |      8      |
| Tier 2            | Spend or add \$50 in credits                          |            16           |   16   |      16     |
| Tier 3            | Spend or add \$500 in credits                         |            24           |   24   |      24     |
| Tier 4            | Spend or add \$5,000 in credits                       |            32           |   32   |      32     |
| Enterprise        | [Contact us](https://fireworks.ai/company/contact-us) |          Custom         | Custom |    Custom   |

Counts are GPUs of that type available to training jobs. Blackwell (B200/B300) is `0` until Tier 2, and current managed training shapes run on Blackwell, so most training needs Tier 2. If a job is rejected with HTTP 429 `quota_exceeded`, raise your tier and resubmit.

<Note>
  Need more training quota than your tier allows? [Reach out for enterprise support](https://fireworks.ai/contact-training) and we'll help size the right allocation for your workload.
</Note>

### Enterprise accounts

Enterprise accounts can configure monthly spend alerts, but those alerts do not pause service. They track the cost of Fireworks usage, including usage paid for with credits. Adding credits itself does not count as spend.

For Enterprise quota details, see [Enterprise quotas](/faq/enterprise/service/quotas) or contact your account representative.

## Manage your quotas

### Account-wide request limits

All API usage on your account shares a single request-throughput envelope:

| Account state                     |  Request-rate limit |
| --------------------------------- | ------------------: |
| No payment method or no credits   |              10 RPM |
| Payment method and active credits | 6,000 RPM (maximum) |

The **6,000 RPM** cap applies account-wide—it is **not** a separate serverless-only limit—and it is a **fixed** ceiling, not adaptive. Per-minute request volume above this cap is rejected (for example HTTP 429), regardless of your spending tier.

### Monthly spend limit

Set a monthly spend limit that fits your needs and adjust it anytime.

For prepaid accounts, the limit tracks the dollar value of your usage regardless of whether credits pay for that usage. Adding credits increases your available balance, but does not raise or reset your monthly spend limit.

Auto Reload is separate from the spend limit. Auto Reload purchases credits when your balance is low; it does not change how much usage your account can accrue during the month.

### View and adjust your spend limit

Check your current spend limit:

```bash theme={null}
firectl quota list
```

Set a custom monthly spend limit:

```bash theme={null}
firectl quota update monthly-spend-usd --value <AMOUNT>
```

For example, to set a \$200 monthly spend limit:

```bash theme={null}
firectl quota update monthly-spend-usd --value 200
```

### Warnings and suspension

By default, Fireworks sends a warning email when usage reaches 80% of your monthly spend limit. You can add other notification amounts from the Billing page.

When usage reaches 100% of the limit, all API requests pause automatically across serverless inference, deployments, and training. Raise the monthly spend limit to resume usage. If your credit balance is also depleted, you must add credits as well.

<Note>
  The suspension behavior described here does not apply to Enterprise accounts. Their monthly spend alerts are informational.
</Note>

### On-demand deployment quotas

On-demand deployments have GPU quotas instead of rate limits:

| GPU Type            | Default Quota |
| ------------------- | ------------- |
| Nvidia A100         | 8 GPUs        |
| Nvidia H100         | 8 GPUs        |
| Nvidia H200         | 8 GPUs        |
| Nvidia B200         | 8 GPUs        |
| Nvidia B300         | 8 GPUs        |
| AMD MI325X / MI350X | 8 GPUs        |
| LoRAs (on-demand)   | 100           |

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
