---
title: "Manage fraud"
source: https://docs.stripe.com/treasury/connect/fraud-guide.md
path: treasury/connect/fraud-guide
---

# Manage fraud

Prevent fraud against your platform's Treasury and Issuing programs.

If you manage fraud risk for your connected accounts and are responsible for losses on their Treasury and Issuing programs, Stripe fraud controls available for Treasury and Issuing can supplement your fraud prevention strategy. You’re responsible for defining and operating your fraud prevention program, including how you balance user experience and fraud controls based on connected accounts, money movement patterns, card spend behavior, and risk tolerance.

## Fraud control layers

Use Treasury and Issuing fraud controls at each point in the risk lifecycle:

- **Stripe defense layer**: Rely on the Stripe automatic controls to block selected Treasury and Issuing activity that we identify as [high risk](https://docs.stripe.com/radar/transaction-risk-prevention.md#high-risk). These controls run by default and don’t require rules.

- **Platform-owned Treasury controls**: Build and operate controls for account onboarding, bank account linking, inbound transfers, outbound money movement, received credits, returns, negative balances, and financial account feature changes.

- **Platform-owned Issuing controls**: Build and operate controls for card creation, authorization decisions, cardholder monitoring, card testing, compromised cards, and unusual business or spend patterns.

- **Paid risk tooling**: Use optional Stripe products, such as Radar Plus, when you need Stripe risk signals, rules, dashboards, review workflows, and automated actions to identify, review, and respond to risky activity.

## Stripe defense layer

Stripe runs automatic risk controls that help reduce your fraud exposure within Treasury and Issuing without requiring action to enable. The defense layer controls supplement your platform’s own risk management program, but don’t change your loss liability or replace your own onboarding, monitoring, review, and intervention workflows.

### Treasury defense layer controls

Stripe monitors Treasury money movement activity and can block transactions that its risk models evaluate as the highest risk. For example, Stripe can block activity that appears consistent with small deposit verification abuse, such as repeated attempts to verify or use bank accounts in a way that indicates suspicious account-linking behavior.

If Stripe detects inbound transfer risk, we can block the inbound transfer and restrict the financial account’s `inbound_transfers` capability. In rare cases involving serious suspected fraud (typically for a new account), Stripe can also restrict additional financial account capabilities, such as `outbound_transfers`, `outbound_payments`, `spend_card`, and `charge_card`.

### Issuing defense layer controls

If your platform uses Issuing, connected accounts can spend funds from their financial account balances using issued cards. Card spend introduces different fraud risks than bank transfers, including card testing, stolen card details, unusual merchant activity, or high-risk authorization attempts.

The Stripe defense layer monitors Issuing authorization activity and can block authorizations that its risk models evaluate as the highest risk or suspect as card testing. These controls usually affect less than 0.5% of authorizations. They can reduce exposure to the highest-risk card activity without requiring you to configure rules.

## Common fraud patterns

The following fraud patterns are common for Treasury platforms. Consider the control recommendations to design your own onboarding, monitoring, review, and intervention workflows.

### Inbound transfer fraud

An inbound transfer moves money into a financial account by a bank transfer such as an ACH debit in the US or a SEPA or Bacs Direct Debit in Europe or the UK.

Inbound transfer fraud happens when a fraudulent actor moves funds from a bank account into a financial account, then moves the funds out of the financial account before the bank reverses the debit because the bank account is stolen, unauthorized, closed, or has insufficient funds. Your platform can become liable for the loss if the account holder spends or withdraws the funds before Stripe receives a return from the bank, resulting in a negative balance on the financial account.

Return timing depends on the payment system (rail) and the reason for the return. For example, with ACH debits in the US, insufficient-funds returns often arrive within a few business days, while unauthorized consumer debit returns can arrive much later, such as within 60 days. This period between funds becoming available and the final return deadline is the return window.

### Prevent inbound transfer fraud

Design controls around both the inbound transfer and the account’s ability to move funds out during the return window. Common protections include:

- **Verify the connected account before you enable funding**: Use your onboarding, identity, business verification, and account monitoring workflows to decide when an account can initiate inbound transfers.
- **Treat new accounts as higher risk**: Apply lower limits, longer review periods, or stricter outbound money movement controls for accounts with limited history.
- **Review risky bank account linking behavior**: Watch for:
  - Repeated failed verification attempts
  - Many bank accounts linked to the same connected account
  - The same bank account linked across many connected accounts
  - Other unusual account-linking patterns.
- **Limit or delay outbound money movement after risky funding**: Consider holding, limiting, or reviewing outbound transfers, outbound payments, Issuing spend, or other outflows until the inbound transfer risk is acceptable.
- **Monitor returns and negative balances**: Track unauthorized returns, insufficient-funds returns, return rates, negative balance events, and repeat losses by connected account.
- **Escalate high-risk activity to review**: Route suspicious inbound transfers or connected accounts to manual review before allowing outbound movement.

If you use [Radar for platforms](https://docs.stripe.com/radar/account-fraud-prevention.md), use [recommended rules](https://docs.stripe.com/treasury/connect/fraud-guide.md#treasury-for-platforms) to review high-risk inbound transfers and pause outbound money movement when account risk is elevated.

## Authorized push payment fraud

Authorized push payment (APP) fraud happens when a fraudulent actor deceives an account holder into sending money to them or to an account they control. Unlike unauthorized fraud, the legitimate account holder initiates and approves the payment.

If you allow your connected accounts to move money out of their financial accounts, consider APP fraud risk in your prevention program. Because the account holder authorizes the payment, the transfer looks legitimate at the time it’s initiated and the fraud only surfaces after the funds have left the account. APP fraud can include:

- Impersonation
- Fake invoices
- Investment scams
- Romance scams
- Business email compromise
- Pressure to move funds urgently

The common pattern is that the fraudulent actor manipulates the account holder into believing the payment is expected, safe, or necessary.

### APP fraud regional considerations

APP fraud obligations vary by market. In the UK, platforms that support outbound Faster Payments or other local push-payment flows can have additional APP scam responsibilities, including reimbursement obligations for eligible APP scam claims under UK rules and program terms. This means APP fraud can create loss exposure even when the connected account holder authorized the payment and the transfer otherwise passed standard controls.

If you operate in the UK, design APP fraud controls and operations around local requirements. Consider clear scam warnings, confirmation or cooling-off steps for higher-risk payments or new payees, claim intake and investigation workflows, recipient and account restrictions during review, and reporting processes. Work with your Stripe and legal teams to confirm how UK APP scam rules apply to your Treasury program.

### Prevent APP fraud

Focus your APP fraud controls on suspicious outbound payment behavior, recipient risk, account takeover signals, and account holder intervention before funds leave the account. Common protections include:

- **Review new or changed recipients**: Add extra review or step-up checks when an account holder sends funds to a new recipient, recently changed recipient, or a recipient with limited payment history.
- **Monitor unusual payment behavior**: Look for payments that are unusually large, high velocity, inconsistent with the account’s history, or sent shortly after a profile, password, device, email, phone, or recipient change.
- **Create customer-facing friction when risk is elevated**: Consider confirmation prompts, warnings, step-up authentication, cooling-off periods, or manual review for high-risk outbound payments.
- **Detect account takeover indicators**: Monitor login, device, credential, contact detail, and session changes that could indicate the account holder is no longer in control of the account.
- **Provide reporting and recovery workflows**: Give account holders a clear way to report suspected scams, and define an operational process for investigation, recalls, recipient restrictions, and account-level controls.
- **Restrict outbound money movement during investigation**: When the account or recipient appears suspicious, consider temporarily restricting additional outbound transfers, outbound payments, or Issuing spend while your team reviews the activity.

APP fraud often requires combining transaction monitoring with user experience controls. A payment can technically be authorized and still be fraudulent because the account holder was deceived.

### Suspicious recipient or mule account activity

Your platform can be liable for APP fraud using a connected account to receive and move fraud proceeds. In this scenario, the connected account might be controlled by a fraudulent actor, a mule account, or a compromised account that receives incoming credits and quickly attempts to move funds out.

Treat unusually large or high-velocity inbound received credits as suspicious, especially when they’re followed by attempts to quickly move funds out to a new or recently changed recipient. These patterns can indicate using an account to receive and move fraudulently obtained funds.

Review the account, assess recent activity, and consider whether to restrict outbound money movement while you investigate the activity.

## Paid risk tooling options (Private preview)

### Treasury for platforms

[Radar for platforms](https://docs.stripe.com/radar/account-fraud-prevention.md) is an optional paid risk tool that helps you manage fraud and credit risk across connected accounts. It provides a no-code rules engine, risk insights, review workflows, and automated actions that let your risk team respond to suspicious activity in a consistent way.

If your platform uses Radar for platforms, you can create rules to identify risky inbound transfers, route suspicious activity to review, and pause outbound money movement in response to elevated risk. You can:

- Use the bank debit risk score from Stripe to create rules for inbound bank transfers.
- Create rules to pause outbound money movement on high-risk connected accounts.
- Trigger a review for activity that needs manual investigation.

Take action earlier in the fraud lifecycle by sending suspicious activity to review when the signal is uncertain, or pausing outbound money movement when you have stronger evidence that a connected account can create losses.

Use the following recommended default rules to manage inbound transfer fraud and suspicious received credits. Use the rule builder to select the corresponding attributes and confirm exact rule syntax for your integration.

#### Rule actions

Configure rules to take one of the following actions:

- `review` adds the financial account action to the **Radar Review** list in the Dashboard, where you can manually assess how to proceed based on the connected account, its recent activity, and any relevant identity or transaction signals. Use it when you see signs that an account might be fraudulent, but the signal isn’t strong enough to automatically restrict the account. Review rules don’t block the inbound transfer, remove account capabilities, or automatically restrict money movement.
- `pause outbound money movement action` prevents the connected account from moving funds out of any of its balances, including transfers or withdrawals. Use it when you have a strong signal that a connected account is fraudulent or likely to create losses. After the rule triggers, review the connected account and decide whether to keep the restriction in place, request additional information, or take other action based on your platform’s risk procedures.

#### Review rules

##### Review accounts where inbound transfer transaction risk level is elevated

```
Raise for review if :treasury_transaction_risk_level: = 'elevated'
```

##### Review accounts where inbound transfer transaction risk level is elevated and account risk level is elevated

```
Raise for review if :treasury_transaction_risk_level: = 'elevated' and :account_risk_level: = 'elevated'
```

##### Review accounts where the number of unauthorized returns in a day is greater than 5

```
Raise for review if :unauthorized_return_count_for_account_daily: > 5
```

##### Review new accounts with high-value inbound transfers

```
Raise for review if amount_in_usd > 10000 and :days_since_account_was_created: < 2
```

#### Pause outbound money movement rules

##### Pause outbound money movement for high account risk

```
Pause outbound money movement if :account_risk_level: = 'highest'
```

##### Pause outbound money movement where inbound transfer transaction risk level is high and account risk level is high

```
Pause outbound money movement if :treasury_transaction_risk_level: = 'highest' and :account_risk_level: = 'highest'
```

### Issuing

If your platform uses Issuing, [Radar](https://docs.stripe.com/issuing/controls/radar.md#get-started-with-radar) can help identify and prevent fraud on issued cards. This is a separate product from Radar for platforms. You can:

- Receive fraud risk signals for each authorization.
- Create rules that block or challenge authorizations based on your criteria.
- Require SMS-based fraud challenges for elevated-risk authorizations.
- Get alerts when Stripe detects that an issued card might be compromised.

These tools help your platform reduce third-party card fraud while limiting disruption to legitimate cardholder spend. Configure authorization rules and challenge workflows based on your cardholders, transaction patterns, product experience, and risk appetite.

