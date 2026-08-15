---
title: "Build a custom Capital program"
source: https://docs.stripe.com/capital/api-integration.md
path: capital/api-integration
---

# Build a custom Capital program

Integrate with our API to build a custom Capital program.

> Capital for platforms is available in [public preview](https://docs.stripe.com/release-phases.md).

[Stripe Capital](https://docs.stripe.com/capital/how-capital-for-platforms-works.md) enables your platform to retrieve prequalified financing offers for your connected accounts, expose a compliant financing offer application, and provide ongoing reporting for in-progress financing.

This guide explains how [Connect](https://docs.stripe.com/connect.md) platforms can integrate with the [Capital API](https://docs.stripe.com/api/capital/financing_offers.md) to send offer emails and manage reporting. When you send offer emails, you must BCC [capital-offers@stripe.com](mailto:capital-offers@stripe.com) on all of them.

### Capital lifecycle

To launch the program, your platform must support the three phases of the Capital lifecycle:

- Market financing offers to eligible connected accounts through offer emails, [embedded components](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-application.md), or a combination of both.
- Provide access to the financing reporting page for in-progress financing through a hosted page, [embedded components](https://docs.stripe.com/connect/supported-embedded-components/capital-financing.md), API-based custom reporting, or a combination of all three.
- Continue to provide access to the financing reporting page after connected accounts fully repay their financing.

This guide explains how to leverage the Capital API to:

- Retrieve financing offers for eligible connected accounts.
- Make the financing application available to connected accounts.
- Provide connected accounts access to financing reporting.

### Implementation phases

1. **Before you begin:** Confirm your platform branding settings and create a test offer.
2. **Build the offer-delivery flow:** Retrieve offers, send offer emails, create or refresh Account Links, and mark offers delivered.
3. **Handle financing lifecycle updates:** Process webhooks, application submission review, financing payout, payment, financing reporting, and repayment.
4. **Validate and launch your integration:** Review the test flow, enable automatic offers, then add refills and reporting.

## Confirm your branding settings [Dashboard]

All connected accounts that receive Capital offers see your business name, icon, logo, and branding color in the offer emails, application, and financing reporting page.

Navigate to your **[Connect branding settings](https://dashboard.stripe.com/settings/connect/stripe-dashboard/branding)**, and make sure your platform’s branding settings are correct.
![Capital offer application page](https://b.stripecdn.com/docs-statics-srv/assets/offer-page.66c647c99e2b25b314b7ca8be2cc98a4.png)

## Create a test undelivered financing offer [Dashboard]

We recommend using a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) to build your integration. In a sandbox, visit the [Capital Dashboard](https://dashboard.stripe.com/test/connect/capital).

1. Click **Create** to open the **Create financing offer** modal, which allows you to create test financing offers. The default options create an undelivered financing offer with a 1,000 USD financing amount.
2. Leave the default options, and click **Create financing offer**.
3. From the Dashboard, click the row corresponding to the offer you created.

The loans and financing section of the connected account details page displays details about the connected account’s financing offer.

## Retrieve financing offers [Server-side]

You can retrieve financing offers for all of your platform’s connected accounts with the [List financing offers](https://docs.stripe.com/api/capital/financing_offers/list.md) endpoint.

#### curl

```bash
curl https://api.stripe.com/v1/capital/financing_offers \
  -u <<YOUR_SECRET_KEY>>:
```

If the offer is successfully created, you receive a response similar to the following:

```json
{
  "object": "list",
  "url": "/v1/capital/financing_offers",
  "has_more": false,
  "data": [
    {
      "id": "financingoffer_abc123",
      "object": "capital.financing_offer"
      ...
    },
    {...}
  ]
}
```

You can look up a financing offer using the [Retrieve financing offer](https://docs.stripe.com/api/capital/financing_offers/retrieve.md#retrieve_financing_offer) endpoint. Retrieve the first financing offer from the list above.

#### curl

```bash
curl https://api.stripe.com/v1/capital/financing_offers/financingoffer_abc123 \
  -u <<YOUR_SECRET_KEY>>:
```

## Send offer email [Server-side]

### Handle offer creation with a webhook

To send your own financing offer emails, listen for the `capital.financing_offer.created` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), which Stripe sends after it creates a financing offer. When you receive this webhook, send the offer email to the connected account immediately.

You must configure Capital webhook events from your account, not as Connect webhooks. Although these events carry data about connected accounts, Stripe creates and manages financing offers on your platform account. Set up your Capital webhook endpoint in the [Dashboard](https://dashboard.stripe.com/webhooks) or using the [Webhook Endpoints API](https://docs.stripe.com/api/webhook_endpoints/create.md) without a `connect` parameter to register it as a platform account webhook rather than a Connect webhook that listens for activity on connected accounts.

> Make sure the contents of your offer email comply with banking regulations by reviewing the [marketing guidance](https://docs.stripe.com/capital/marketing.md) page. Submit all changes to user-facing materials for review and approval using the [Change Request Form](https://form.asana.com/?k=8K51UWmWhttehNFD5qBLdg&d=974470123217835).

### Send offer emails

In the email, link connected accounts to a dedicated Capital section in your platform Dashboard, such as a Capital landing page or Capital Dashboard. That page can use the Capital financing application with [Account Links](https://docs.stripe.com/api/account_links.md) to give connected accounts access to the Capital application.

### Create a financing application Account Link

Include a link to the financing application in your platform Dashboard by generating an Account Link. You can generate Account Links with the `capital_financing_offer` type to provide temporary access to a Stripe-hosted application page. Account Links expire shortly after Stripe generates them, so generate them as needed or give connected accounts a way to regenerate the application link by using a redirect.

### Handle Account Link Expiration

Don’t send an Account Link URL directly in an offer email because the Account Link can expire before the recipient even opens the email. Instead, include a stable URL hosted on your platform (for example, `https://yourplatform.com/capital/accept_offer`). Configure the link to:

1. Authenticate the connected account.
2. Generate a new Account Link using the API.
3. Redirect the connected account to the newly generated Account Link URL.

This way, the connected account always receives a fresh, valid Account Link regardless of when they open the email.

#### curl

```bash
curl https://api.stripe.com/v1/account_links \
  -u <<YOUR_SECRET_KEY>>: \
  -d account=acct_123 \
  # The URL the connected account will be redirected to if the account link is expired, has been previously-visited, or is otherwise invalid.
  -d refresh_url="https://example.com/reauth" \
  # The URL the connected account will be redirected to after completing the linked flow.
  -d return_url="https://example.com/thanks" \
  -d type=capital_financing_offer
```

If the creation of an account link is successful, you receive a response similar to the following:

```json
{
  "object": "account_link",
  "created": 1611264596,
  "expires_at": 1611264896,
  "url": "https://connect.stripe.com/capital/offer/SrjgLUfa0O7K"
}
```

After updating your webhook integration, create another offer in the [Dashboard](https://dashboard.stripe.com/test/connect/capital), and verify you receive the `capital.financing_offer.created` webhook.

### Mark the offer as delivered

After you send an offer email, update your webhook integration to [mark the financing offer as delivered](https://docs.stripe.com/api/capital/financing_offers/mark_delivered.md). You can verify that the financing offer’s status is `delivered` in either the [Dashboard](https://dashboard.stripe.com/test/connect/capital) or the [Financing Offers API](https://docs.stripe.com/api/capital/financing_offers/retrieve.md).

#### curl

```bash
curl https://api.stripe.com/v1/capital/financing_offers/financingoffer_abc123/mark_delivered \
  -u <<YOUR_SECRET_KEY>>:
```

You must mark an offer as delivered to verify with Stripe that you’ve marketed the offer to the connected account. When you send your offer emails, you need to BCC [capital-offers@stripe.com](mailto:capital-offers@stripe.com).

## Listen for status changes [Server-side]

In addition to the `capital.financing_offer.created` webhook, Stripe sends additional webhooks as the financing offer transitions through different states. Stripe sends all Capital webhooks to your platform account webhook endpoint, not to a Connect webhook endpoint. You can receive any of the following webhooks related to Capital:

| **Webhook identifier** | **Trigger** |
| --- | --- |
| `capital.financing_offer.created` | Financing offer is created |
| `capital.financing_offer.accepted` | Connected account submits their offer application |
| `capital.financing_offer.paid_out` | Stripe approves the offer application and funds are paid out to the connected account |
| `capital.financing_offer.fully_repaid` | Connected account fully pays the financing balance |
| `capital.financing_offer.canceled` | Connected account cancels the financing offer |
| `capital.financing_offer.rejected` | Connected account’s application isn’t approved |
| `capital.financing_offer.expired` | Financing offer expires and is no longer available |
| `capital.financing_offer.replacement_created` | Financing offer is [replaced](https://docs.stripe.com/capital/replacements.md) with a new financing offer |
| `capital.financing_offer.accepted_other_offer` | Connected account accepts a different financing offer |
| `capital.financing_summary.line_of_credit_update` | Connected account’s line-of-credit terms are updated |
| `capital.financing_transaction.created` | Financing transaction is created |

From the [Dashboard](https://dashboard.stripe.com/test/connect/capital), find the offer you delivered earlier.

1. Click the overflow menu (⋯).
2. Click the **Expire offer** option, which lets you simulate expiring the offer.
3. Verify you receive the `capital.financing_offer.expired` webhook.

With the exception of `capital.financing_offer.canceled`, you can simulate all webhooks while in a testing environment.

## Apply for an offer [Dashboard] [Server-side]

You can simulate the `capital.financing_offer.accepted` webhook by applying for an offer.

1. From the [Dashboard](https://dashboard.stripe.com/test/connect/capital), create a delivered offer with a maximum financing amount of 20,000 USD.
2. Generate an account link of type `capital_financing_offer`, and go to the link. Here, you can preview what the application looks like for your connected accounts.
3. Continue to the end of the application, and click **Submit**.
4. Verify you received the `capital.financing_offer.accepted` webhook.
5. View the offer in the Dashboard, and check it has status accepted.

### View the application tracker

A financing offer with the `accepted` status is pending application review by the Stripe [servicing](https://docs.stripe.com/capital/servicing.md) team. During this review, you can direct the connected account to the financing reporting page by using an [Account Link](https://docs.stripe.com/api/account_links.md) with the `capital_financing_reporting` type. The financing reporting page includes an application tracker with an estimated application review timeline.

#### curl

```bash
curl https://api.stripe.com/v1/account_links \
  -u <<YOUR_SECRET_KEY>>: \
  -d account=acct_123 \
  # When the connected account refreshes the page, where should we redirect them
  -d refresh_url="https://example.com/reauth" \
  # When the connected account completes the application, where should they return
  -d return_url="https://example.com/thanks" \
  -d type=capital_financing_reporting
```

Navigate to the link, and view the application tracker.

## Approve the application [Dashboard]

In the [Dashboard](https://dashboard.stripe.com/test/connect/capital), find the row corresponding to the accepted offer.

1. Click the overflow menu (⋯).
2. Click the **Approve and disburse funds** option, which lets you simulate an application approval and funds disbursal.
3. Verify you receive the `capital.financing_offer.paid_out` webhook, which notifies you that the financing has been paid out.
4. Generate another [Account Link](https://docs.stripe.com/api/account_links.md) of type `capital_financing_reporting`. This reporting page provides access to outstanding balance and payout and payment transaction details for the connected account’s in-progress financing.
5. Click **Make payment**, and create a manual payment.

> It takes up to 15 minutes for the **Make payment** button to be enabled on the reporting page for test financing offers.

After the transaction is processed, view the payment in the transactions table. You can programmatically view the connected account’s paid-down financing amount for in-progress financing using the [financing summary API](https://docs.stripe.com/api/capital/financing_summary.md).

#### curl

```bash
curl https://api.stripe.com/v1/capital/financing_summary \
  -u <<YOUR_SECRET_KEY>>: \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
```

If the retrieval of the financing summary is successful, you receive a response similar to the following:

```json
{
  "object": "capital.financing_summary",
  "details": {
    "currency": "usd",
    "advance_amount": 1000000,
    "fee_amount": 100000,
    "withhold_rate": 0.2,
    "remaining_amount": 999950,
    "paid_amount": 50,
    "current_repayment_interval": {
      "due_at": 123456789,
      "remaining_amount": 50,
      "paid_amount": 50
    },
    "repayments_begin_at": 123456789,
    "advance_paid_out_at": 123456789
  }
}
```

## Fully pay the financing [Dashboard]

In the [Dashboard](https://dashboard.stripe.com/test/connect/capital), find the row corresponding to the paid-out financing.

1. Click the overflow menu (⋯).
2. Click the **Repay offer** option, which lets you simulate fully paying down the financing balance.
3. Verify you receive the `capital.financing_offer.fully_repaid` webhook, which notifies you that the financing has been fully paid.
4. Generate another [Account Link](https://docs.stripe.com/api/account_links.md) of type `capital_financing_reporting`.

After a connected account pays the total amount of its financing, they can access past financing details on the reporting page at any time.

## Review your test integration

By now, your integration:

- Responds to the `capital.financing_offer.created` webhook by sending an offer email and marking the offer as delivered
- Expose the financing application link in your platform Dashboard by using Account Links with the `capital_financing_offer` type
- Expose the financing reporting link in your platform Dashboard by using Account Links with the `capital_financing_reporting` type

The Capital section of your platform dashboard might appear differently depending on which phase the connected account’s financing is in. Review the state diagram below for a list of possible financing offer status values.
Capital financing offer state machine (See full diagram at https://docs.stripe.com/capital/api-integration)
| **Segment** | **What it means for the platform** |
| --- | --- |
| Undelivered | Stripe has created the financing offer, but it hasn’t yet been communicated to the connected account through an approved offer delivery channel. All offers begin in this state. |
| Delivered | The connected account has been sent or shown the offer. This indicates delivery, not that they opened, reviewed, or accepted it. |
| Accepted | The connected account has accepted the offer and progressed into the application or financing process. It isn’t necessarily funded yet, and any required review, approval, or disbursement might still be pending. |
| Paid out | The financing has been disbursed to the connected account. This is the origination or funding event, and Stripe uses this status for platform origination volume and revenue share reporting. |
| Fully repaid | The connected account has repaid the full financing amount, including the applicable financing fee. No remaining balance exists for that financing. |

## Prepare to enable automatic offers

When automatic offers are enabled in live mode, Stripe automatically creates financing offers for your connected accounts on a daily basis. Before enabling automatic offers, make sure that you:

1. Confirm and update email addresses for your connected accounts through the [Comms Center](https://dashboard.stripe.com/connect/comms_center/collect) if you’re planning to leverage Stripe co-branded no-code offer emails. To be eligible for Capital financing, connected accounts must have an email saved with Stripe so that they can receive transactional emails such as payment progress updates.
2. [Contact us](mailto:capital-review@stripe.com) to enable live mode access to the financing offers API.

### Enable additional features

Over time, some of your connected accounts might become eligible for refills. Refills are additional financing offers sent to connected accounts that have made substantial payment progress towards their in-progress loans. Follow the [refills integration guide](https://docs.stripe.com/capital/refills.md) to update your integration to support refill financing offers.

If you want to include Capital transactions on your platform dashboard and update your connected accounts’ custom payout reporting, refer to the [reporting and reconciliation guide](https://docs.stripe.com/capital/reporting-and-reconciliation.md).

## See also

- [Refill offers](https://docs.stripe.com/capital/refills.md)
- [Replace offers](https://docs.stripe.com/capital/replacements.md)
- [Capital testing](https://docs.stripe.com/capital/testing.md)
- [Account Links](https://docs.stripe.com/api/account_links.md)

