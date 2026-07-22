---
title: "Pay As You Go"
source: https://elevenlabs.io/docs/overview/administration/pay-as-you-go.md
path: docs/overview/administration/pay-as-you-go
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Pay As You Go

## Overview

Pay As You Go (PAYG) allows you to prepay for usage without committing to a monthly subscription. It's designed for developers and builders who want to start using ElevenLabs APIs quickly, scale up on their own terms, and only pay for what they use.

PAYG is a feature available on self-serve subscription plans, including free. Enterprise contracts remain on overage-based billing and are not affected by this change.

Existing subscribers who already have usage based billing enabled are not affected.

## How it works

When you activate PAYG, you add a payment method and add funds to your account balance. That balance is drawn down as you use ElevenLabs APIs and products. If your balance runs low, you can top it up manually or enable Auto Top Up to recharge automatically.

This feature is labeled **Top Up** and can be found in your [**Developers** settings](https://elevenlabs.io/app/developers).

### Credit priority order

If you have both a subscription plan and a PAYG balance, your subscription plan's included credits are consumed first. Once your subscription credits are exhausted, usage is then drawn from your PAYG balance. This means your PAYG balance effectively extends your plan beyond your monthly quota.

## Eligibility and plan limits

PAYG Top Ups are available to all self-serve tiers, including free, Starter, Creator, Pro, Scale, and Business.

If you upgrade from a free subscription plan while holding a PAYG balance, your remaining balance carries over and will be used after your subscription credits are depleted.

Voice slot limits and other plan-level restrictions (e.g., custom voice limits, API access tiers) come from your subscription plan, not your PAYG balance. For example, a free plan user on PAYG is still limited to the free tier's voice slots. Upgrading to a paid subscription is required to unlock higher limits.

## Pricing

PAYG pricing varies depending on whether you're generating content using the API or the UI. API usage has lower rates than UI usage.

For detailed pricing information, visit our [pricing page](https://elevenlabs.io/pricing).

## Adding funds

Funds are added directly from your account in your local currency.

Key limits:

* **Minimum Top Up**: \$5 USD / ₹500 INR
* **Supported currencies**: USD, INR

Your balance is displayed in USD or INR in [Developer settings](https://elevenlabs.io/app/developers) → Top Up, but is converted to credits and displayed as credits elsewhere in the platform.

To top up manually:

### Navigate to Top Up settings

Go to [Developer settings](https://elevenlabs.io/app/developers) → Top Up

### Enter amount

Enter the amount you'd like to add (minimum \$5 USD / ₹500 INR)

### Confirm payment

Confirm payment with your saved payment method

If you do not yet have a payment method on file, you will be prompted to add one before completing your first Top Up.

If your balance hits \$0 and Auto Top Up is off (or fails), your service will pause immediately.
This is by design. PAYG is a prepaid model with no overage charges.

## Auto Top Up

Auto Top Up automatically charges your saved payment method when your credit balance falls below a defined threshold, ensuring your usage is never interrupted unexpectedly.

### Enabling Auto Top Up

### Navigate to Top Up settings

Go to [Developer settings](https://elevenlabs.io/app/developers) → Top Up

### Toggle on Auto Top Up

Enable the Auto Top Up feature

### Set Top Up amount

Set your Top Up amount (the amount to be charged each time). Default is \$20 USD / ₹2,000 INR

### Set low balance threshold

Set your low balance threshold (the balance level that triggers a Top Up). Default is \$10 USD / ₹1,000 INR

With Auto Top Up on, a minimum balance of \$5 USD / ₹500 INR is required to ensure service continues in the event of a payment failure. If an Auto Top Up attempt fails, your service will pause until you top up manually.

With Auto Top Up off, your balance can run down to \$0. Once depleted, your usage will be paused until you manually top up.

Auto Top Up can occasionally be delayed or fail due to payment processing issues. If you rely on
uninterrupted API usage, consider maintaining a healthy balance buffer or contacting Sales about
an Enterprise plan.

## Credit rollover

If you upgrade to a subscription plan, your remaining PAYG balance carries over and will be used after your subscription credits are depleted.

There is no monthly rollover cap on PAYG funds.

PAYG credits expire 12 months after purchase. Any unused credits will be removed from your balance
after this period.

## Plan changes and credit conversion

Your PAYG balance is stored as a dollar value, not a fixed number of credits. Each plan has its own credit-to-dollar rate, so when you change subscription plans, your remaining dollar balance is converted using the new plan's rate.

If you downgrade to a plan with a different rate that gives you fewer credits per dollar, your credit balance will go down, even though you haven't used credits. The dollar value of your unused credits stays the same; only the number of credits it converts to changes.

If you upgrade your subscription, your remaining dollar amount is converted at the new plan's higher rate, so you may see your credit balance increase. The dollar value remains the same across all plans.

Before you confirm a downgrade, we show you how your existing PAYG credit balance will be affected.

## Concurrency and rate limits

For paid subscriptions, your subscription plan limits apply. For free plans with PAYG enabled, the following limits apply:

* **Concurrency**: Starter-tier level (3 concurrent requests)
* **Priority**: Starter-tier level (priority 4)

If you need higher concurrency, consider upgrading to a paid subscription plan.

## Relationship to usage based billing

PAYG replaces the previous usage based billing (overage) model for new self-serve customers.

* Existing subscribers who already have usage based billing enabled are not affected.
* Enterprise contracts remain on the overage model and are not affected.
* Usage based billing will not be available for new self-serve customers. PAYG Top Ups are the replacement mechanism for extending beyond your included plan credits.

### Switching from a legacy plan

If you're currently on a legacy usage based billing subscription, you can switch to the new Pay As You Go version.

### Navigate to Subscriptions

Go to [Subscriptions](https://elevenlabs.io/app/subscription) → **Manage Subscription**

### Select **Switch to new pricing**

Choose **Switch to new pricing** to move onto the new version of your current subscription

### Confirm the change

Once confirmed, the change will take effect at the end of your current billing cycle

If you move onto the new plan, it won't be possible to return to the legacy plan in the future.

## FAQ

#### Who can use PAYG?

All self-serve users, including those on the free plan. Enterprise contracts are not eligible.
They remain on the overage billing model.

#### Is PAYG a separate plan?

Not exactly. Activating PAYG (by adding funds or enabling Auto Top Up) transitions your account
display to show "Pay As You Go" rather than "Free," but your underlying plan tier (and its
limits) remains the same unless you separately upgrade to a paid subscription.

#### What happens when my balance hits \$0?

Your usage pauses immediately. There is no postpaid billing or debt incurred. Top up manually to
resume, or enable Auto Top Up to avoid this.

#### Do funds expire?

Yes. PAYG credits expire 12 months after purchase. Any unused credits will be removed from your
balance after this period.

#### Are Top Ups refundable?

No. All Top Up purchases are non-refundable.

#### Can I use PAYG alongside a subscription?

Yes. If you have both a subscription and a PAYG balance, your subscription credits are consumed
first. Once depleted, your PAYG balance is used. This effectively extends your plan beyond your
monthly quota.

#### Will PAYG give me access to Music, Video, and other APIs?

Yes. PAYG is intended to unlock access to APIs that are otherwise disabled for users on the free
plan, including Music, Sound Effects, and more.

#### Is there a monthly spend cap?

You can optionally set a monthly spend cap in the Top Up settings. This is off by default.

#### What is the maximum I can purchase in one transaction?

There is no fixed maximum. Your available Top Up limit depends on your account status and
currency. Visit [Developer settings](https://elevenlabs.io/app/developers) → Top Up to see the
amounts available to you.

#### What was usage based billing, and how is PAYG different?

Usage based billing was a postpaid mechanism that allowed users to spend beyond their plan
limits and be charged later. PAYG replaces this with a prepaid model, where you load funds in
advance.

#### What happens to my PAYG credits if I change subscription plans?

Your PAYG balance is stored as a dollar value and converted to credits at your current plan's
rate. When you change plans, the dollar value stays the same, but the number of credits it
converts to may change. If you downgrade to a plan with fewer credits per dollar, your credit
balance will go down. If you upgrade, it may increase. The system shows you the impact before
you confirm a downgrade.
