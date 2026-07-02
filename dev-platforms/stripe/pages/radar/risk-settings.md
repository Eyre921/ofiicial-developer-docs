---
title: "Risk setting and risk controls"
source: https://docs.stripe.com/radar/risk-settings.md
path: radar/risk-settings
---

# Risk setting and risk controls

Automatically adjust which payments you block based on dynamic detection.

Stripe Radar lets you choose a risk setting that automatically adjusts your protection thresholds based on your business needs and tolerance. Based on the risk setting you choose, we recommend the risk controls that help protect against fraud.

## Risk settings (Recommended)

Risk settings let you balance authorization and fraud on your account by using risk controls. These risk controls set different thresholds to block payments that might result in fraudulent disputes or early fraud warnings. Certain risk settings also recommend that you enable or disable additional risk controls, such as adaptive 3DS, to help protect your account from fraud while allowing non-fraudulent payments.

On the [risk controls](https://dashboard.stripe.com/settings/radar/risk-controls) page, you can choose or modify your risk setting from the options below. You might need to upgrade your plan to adjust your risk setting.

- **Maximize protection**: Prioritize protecting your business against fraud by blocking payments that are likely to receive early fraud warnings.
- **Balance risk and revenue**: Balance protecting your business against fraud with tolerating some risk.
- **Maximize revenue**: Prioritize revenue by blocking high-risk payments, which can help minimize losses because of fraud.

When you change your risk setting, the modal displays the impact to payments with the following statistics. The numbers shown are estimated projections based on your last four months of payment data.

| Metric | Description |
| --- | --- |
| **Fraud** | The estimated payments this setting blocks before they become fraudulent disputes or early fraud warnings. |
| **Payments** | The estimated payments and percentage change your business accepts, based on what this setting allows. |

### Adjust your blocking preference using risk settings 

Beginning March 1, 2026, existing Radar for Fraud Teams users can change blocking preferences using risk settings, instead of the default risk thresholds. If you previously set a risk score block threshold, the `Block if :risk_level: = 'highest'` default rule is likely still enabled. If this is the case, you won’t see the option to change your risk score threshold on the risk controls page.

If you want to change your default block threshold, you can do either of the following:

- *(Recommended)* **Modify your risk setting**. Changing your risk setting alters the enabled risk controls and the thresholds set for each control. Each risk control uses individualized machine learning to improve cost and fraud protection on your behalf. When you first enable a risk setting, Stripe disables the corresponding [high risk block rule](https://docs.stripe.com/radar/rules.md#machine-learning-risk-checks) that uses risk score.
- **Customize the threshold for the Fraudulent dispute risk control**. If you use [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams), you can set a custom blocking threshold for the [Fraudulent dispute](https://docs.stripe.com/radar/risk-settings.md#fraudulent-dispute) risk control. On the control’s overview page, click **Edit configuration** to set a specific threshold and backtest the impact on your payments before applying it. When you set a custom threshold that doesn’t match a preset risk setting, your account displays in **Manual mode**.

## Risk controls

Risk controls use AI to protect your account. You enable them on your account to block payments that might result in fraudulent disputes or early fraud warnings. Risk settings determine which risk controls are enabled and recommend additional risk controls, such as adaptive 3DS.

Risk settings automatically manage the blocking thresholds for risk controls. To block more or less traffic from a risk control, you can change your risk setting, which automatically adjusts the blocking threshold. If you use [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams), you can also adjust the threshold for the [Fraudulent dispute](https://docs.stripe.com/radar/risk-settings.md#fraudulent-dispute) risk control directly.

Risk controls and risk settings won’t override the custom rules you created. You can continue to update your controls, settings, and rules at any time.

You can find the following controls on the [risk controls](https://dashboard.stripe.com/settings/radar/risk-controls) page in the Dashboard.

### Fraudulent dispute

This risk control uses the [fraudulent dispute score](https://docs.stripe.com/radar/risk-settings.md#fraudulent-dispute-score) and blocks payments that are likely to result in fraudulent disputes. Radar determines the number of payments to block versus accept based on your risk setting, and maximizes conversion while preventing the risk of entering [monitoring programs](https://docs.stripe.com/disputes/monitoring-programs.md).

To change how much this control blocks, change your risk setting.

If you use [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams), you can also click **Edit configuration** on the control’s overview page to set a custom blocking threshold. You can backtest the impact of the threshold on your payments before applying it.

### Early fraud warning 

This risk control uses the [early fraud warning score](https://docs.stripe.com/radar/risk-settings.md#early-fraud-warning-score) and determines which payments are likely to result in an [early fraud warning](https://docs.stripe.com/disputes/measuring.md#early-fraud-warnings). Radar determines the threshold based on your risk preferences, and maximizes conversion while preventing the risk of entering [monitoring programs](https://docs.stripe.com/disputes/monitoring-programs.md).

This control is only available if you choose the **Maximize protection** risk setting. We recommend turning on this setting if you’re in a card brand monitoring program, which counts early fraud warnings toward the [VAMP monitoring program](https://docs.stripe.com/disputes/monitoring-programs.md#VAMP).

### Adaptive 3DS

Radar’s adaptive [3D Secure (3DS)](https://docs.stripe.com/payments/3d-secure.md) authentication control adds an extra layer of authentication during checkout to help protect against fraud. Stripe runs machine learning in the background to authenticate medium-risk payments.

In most cases, *3DS* (3D Secure (3DS) provides an additional layer of authentication for credit card transactions that protects businesses from liability for fraudulent card payments) authentication happens with no action required by your customer. If the customer’s bank detects anything unusual, they might ask the customer to confirm their identity through a security challenge. If 3DS authenticates a payment, the [liability](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#disputed-payments) for any fraud-related disputes for that payment typically shifts from your business to the issuer. This means that in most cases, the seller isn’t responsible for fraud costs on 3DS-authenticated payments.

Stripe activates 3DS automatically, if required by a regulatory mandate such as [Strong Customer Authentication (SCA)](https://stripe.com/guides/strong-customer-authentication). Disabling adaptive 3DS doesn’t prevent 3DS from activating when required for compliance. Authentication fraud prevention control isn’t available in testing environments.

### Fraudulent non-card payments

Stripe automatically enables the fraudulent non-card payments control by default for all non-card, local payment methods. This risk control evaluates each transaction and automatically blocks payments that have a high risk level. Radar determines the risk level based on attributes that Stripe has identified as high fraud risk on other payments.

You can monitor performance and review information about blocked payments on the [risk controls page](https://dashboard.stripe.com/settings/radar/risk-controls) in the Dashboard. You can also simulate how this risk control would have affected past payments to better understand the impact on conversion and fraud prevention.

## Radar scores

Radar scores are numerical signals that represent the likelihood of fraud or abuse for a payment. You can use scores to write custom [Radar rules](https://docs.stripe.com/radar/rules.md) or to understand why a payment was blocked. Some scores also contribute to an [overall risk level](https://docs.stripe.com/radar/risk-settings.md#overall-risk-level), which summarizes risk as a single signal.

### Overall risk level 

The overall risk level combines the [fraudulent dispute](https://docs.stripe.com/radar/risk-settings.md#fraudulent-dispute-score), [early fraud warning](https://docs.stripe.com/radar/risk-settings.md#early-fraud-warning-score), and [risk](https://docs.stripe.com/radar/risk-settings.md#risk-score) scores that factored into the payment decision. It takes the maximum of these scores and appears as a single signal (**Normal**, **Elevated**, or **Highest**) on the payment details page. The overall risk level is separate from the `:risk_level:` Radar rules attribute, which only corresponds to the [risk score](https://docs.stripe.com/radar/risk-settings.md#risk-score). The highest applicable score also appears on the Radar [Reviews](https://dashboard.stripe.com/radar/reviews) page and in the **Related payments** section of the payment details page in the Dashboard.

### Fraudulent dispute score 

Stripe Radar assigns each payment a numerical fraudulent dispute score between 0 and 99. This score represents the likelihood that a payment results in a fraudulent dispute, where 0 is the lowest likelihood and 99 is the highest.

> Fraudulent dispute scores apply to card, ACH Direct Debit, and SEPA Direct Debit payments.

If you use [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams) and want to block payments based on the fraudulent dispute score, you can write custom rules on `:fraudulent_dispute_score:`.

### Early fraud warning score 

Stripe Radar assigns each payment a numerical early fraud warning score between 0 and 99. This score represents the likelihood that a payment results in an early fraud warning, where 0 is the lowest likelihood and 99 is the highest.

> Early fraud warning scores apply to card payments only.

If you use [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams) and want to block payments based on the early fraud warning score, you can write custom rules on `:early_fraud_warning_score:`.

### Bot score (Private preview)

Stripe Radar assigns payments made on [Stripe Checkout](https://stripe.com/payments/checkout) a numerical bot score between 0 and 99. This score represents the likelihood that a bot made the payment, where 0 is the lowest likelihood and 99 is the highest.

You can write custom rules on `:bot_score:` to block payments that exceed a threshold you define. For early access, see [Bot abuse prevention](https://docs.stripe.com/radar/bot-abuse.md).

### Risk score (Fraudulent payment) 

Stripe Radar gives each payment a numerical [risk score](https://docs.stripe.com/radar/risk-evaluation.md#risk-outcomes) between 0 and 99, where 0 is the lowest risk and 99 is the highest. This risk score is the probability that a payment results in a fraudulent dispute or early fraud warning.

> Adjusting the risk score applies to card, ACH, and SEPA Direct Debit payments. You can select a specific payment method to test different thresholds and view affected payments.

Radar is deprecating the [high risk block rule](https://docs.stripe.com/radar/rules.md#machine-learning-risk-checks) that uses risk score to block payments. To change your block preference, you must use risk settings, which use separate models to block payments. When you select a risk setting, your default high risk block rule is disabled and you can’t re-enable it.

The risk score appears on a payment when:

- No fraudulent dispute or early fraud warning score is available, or
- The payment was blocked by a rule that uses the legacy risk score, such as a Radar rule with a `:risk_score:` predicate or a Stripe block.

The risk score factors into the [overall risk level](https://docs.stripe.com/radar/risk-settings.md#overall-risk-level) when visible.

If you use [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams) and want to block payments based on the risk score (even after selecting a risk setting) you can continue writing custom rules on `:risk_score:`.

## See also

- [Access risk evaluations](https://docs.stripe.com/radar/risk-evaluation.md)
- [Review card payments](https://docs.stripe.com/radar/reviews.md)
- [Optimize risk factors](https://docs.stripe.com/radar/optimize-risk-factors.md)

