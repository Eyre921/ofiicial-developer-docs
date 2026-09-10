---
title: "testing environment comparison"
source: https://docs.stripe.com/testing-use-cases.md
path: testing-use-cases
---

# Testing use cases

Learn how to test your integration.

*Sandboxes* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) are the Stripe testing environment. They allow you to test your integration without making actual charges or payments. Sandboxes simulate creating real objects without affecting actual transactions or moving real money. You can access your sandboxes using the account picker or on the [Sandboxes page](https://dashboard.stripe.com/sandboxes) in the Dashboard. We recommend using our [quality assurance (QA) testing use cases](https://docs.stripe.com/testing-use-cases.md#testing-use-cases) and importing our [Postman collection](https://docs.stripe.com/testing-use-cases.md#postman-collection) to help you in the testing process.

## Testing environments 

In a sandbox, you can charge test credit cards and create test products and prices. Sandboxes let you simulate transactions to make sure that your integration works correctly. This helps identify bugs or errors in your Stripe implementation before you go live with actual payments.

After you create a Stripe account, Stripe places you in a sandbox. You can find a set of [test API keys](https://docs.stripe.com/keys.md#obtain-api-keys) on the Stripe Dashboard home page or the API keys page. You can use these API keys to create and retrieve simulated data by making requests to the Stripe API.

To start accepting real payments, you need to [set up your Stripe account](https://docs.stripe.com/get-started/account/set-up.md), exit your sandbox with the account picker, and use the live API keys in your integration. Store live API keys in a secrets vault or environment variables. Don’t store keys in source code or configuration files checked into version control. For more information, see [Best practices for managing secret API keys](https://docs.stripe.com/keys-best-practices.md).

> #### Impact on live mode when using the test mode sandbox
> 
> If you change settings in the Dashboard while in the *test mode sandboxes* (Every Stripe account includes the test mode sandbox. It shares some settings with live mode, has characteristics that differ from other sandboxes you create, but you can't delete it), you might also change them in live mode. Many Dashboard pages have a notification box and disable live mode settings while in the test mode sandbox. In this case, any settings still enabled are safe to use. If you don’t see the notification, assume any changes made in the test mode sandbox affect live mode settings (unless you see a test data banner).

### Compare sandboxes 

Your Stripe account includes a test mode sandbox and the ability to create additional sandboxes. Although test mode is a sandbox, it differs from the general sandboxes that you create. Understanding these differences can help you build your testing strategy.

For new integrations, use a general sandbox instead of the test mode sandbox. General sandboxes isolate settings and data from live mode and let you create separate environments for local development, CI, and staging. Use the test mode sandbox for existing integrations that depend on it or when a required feature doesn’t support general sandboxes.

|  | Test mode sandbox | General sandboxes |
| --- | --- | --- |
| Number of sandboxes | Use one sandbox. | Use up to five sandboxes. The test mode sandbox doesn’t count toward the limit of five. |
| Access control | Grant all users the same roles and access as live mode. | Control access more strictly. When the sandbox access level is **Private**, only administrators automatically have access. You can invite users to sandboxes only, without granting them access to live mode. When the sandbox access level is **Developer**, administrators, developers, and sandbox administrators automatically inherit the **Administrator** role in the sandbox. When the sandbox access level is **All team members**, all users with roles receive the same roles and access. |
| Settings | Share settings between live mode and the test mode sandbox. You can’t test many settings independently. | Isolate settings completely for each sandbox. Copy settings from live mode at creation time, and test independently from your live integration. |
| API support | Supports V1 and [partially supports V2](https://docs.stripe.com/api-v2-overview.md#limitations). | Supports V1 and V2. |
| Deletion | Can’t be deleted. | Can be deleted. |
| Apps | Installs require the app to support a test mode sandbox. | Installs require the app to support sandboxes. |
| Product limitations | You can’t test *IC+* (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs) pricing in test mode sandbox. | You can’t test *IC+* (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs) pricing in a sandbox. |
| Rate limits | Maintain consistent [rate limits](https://docs.stripe.com/rate-limits.md). | Maintain consistent [rate limits](https://docs.stripe.com/rate-limits.md). |
| Test card numbers | Use the same [test card numbers](https://docs.stripe.com/testing-use-cases.md#test-card-numbers). | Use the same [test card numbers](https://docs.stripe.com/testing-use-cases.md#test-card-numbers). |

## Sandboxes versus live mode 

All Stripe API requests occur in either a sandbox or *live mode* (Use this mode when you’re ready to launch your app. Card networks or payment providers process payments). API objects in one mode aren’t accessible to the other. For example, a test [Product](https://docs.stripe.com/api/products/object.md) object can’t be part of a live mode payment.

| Type | When to use | Objects | How to use | Considerations |
| --- | --- | --- | --- | --- |
| Sandboxes | Use a sandbox, and its associated test API keys, as you build your integration. In a sandbox, card networks and payment providers don’t process payments. | API calls return simulated objects. For example, you can retrieve and use test [Customer](https://docs.stripe.com/api/customers/object.md), [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md), [Refund](https://docs.stripe.com/api/refunds/object.md), and [Subscription](https://docs.stripe.com/api/subscriptions/object.md) objects. | Use [test credit cards and accounts](https://docs.stripe.com/testing.md#cards). You can’t accept real payment methods or work with real accounts. | [Identity](https://docs.stripe.com/identity.md) doesn’t perform any verification checks. Also, Connect [account objects](https://docs.stripe.com/api/accounts/object.md) don’t return sensitive fields. |
| Live mode | Use live mode, and its associated live API keys, when you’re ready to launch your integration and accept real money. In live mode, card networks and payment providers do process payments. | API calls return real objects. For example, you can retrieve and use real [Customer](https://docs.stripe.com/api/customers/object.md), [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md), [Refund](https://docs.stripe.com/api/refunds/object.md), and [Subscription](https://docs.stripe.com/api/subscriptions/object.md) objects. | Accept real credit cards and work with customer accounts. You can accept actual payment authorizations, charges, and captures for credit cards and accounts. | Disputes have a more nuanced flow and a simpler [testing process](https://docs.stripe.com/testing.md#disputes). Also, some [payment methods](https://docs.stripe.com/payments/payment-methods.md) have a more nuanced flow and require more steps. |

Being in a sandbox in the Dashboard doesn’t affect your integration code. Your test and live mode API keys affect the behavior of your code.

## Create an additional sandbox

To create and set up an additional sandbox in the Dashboard:

#### Create the sandbox

1. Go to the [Sandboxes page](https://dashboard.stripe.com/sandboxes) in the Dashboard.
2. Click **Create** in the top right.

#### Manage access

New sandboxes use the **Private** access level by default and don’t automatically give other team members access. You can change the access level to grant broader access:

1. Go to the [Sandboxes page](https://dashboard.stripe.com/sandboxes) in the Dashboard.
2. Click the overflow menu (⋯) for the sandbox.
3. Select **Change access**.

You can manage individual-level access in any of these ways:

- Grant access to a [specific sandbox](https://docs.stripe.com/sandboxes/dashboard/manage-access.md#grant-users-access-to-a-specific-sandbox).
- Grant [testing-only access](https://docs.stripe.com/sandboxes/dashboard/manage-access.md#grant-users-access-for-testing-only).
- Grant access to [all sandboxes](https://docs.stripe.com/sandboxes/dashboard/manage-access.md#grant-users-access-to-all-sandboxes-in-an-account).

#### Get your sandbox credentials

Use these credentials to connect your integration to the sandbox. Save them where your team can access them for testing.

1. Copy the test API keys for the sandbox.
2. Copy the sandbox account ID.

#### Update test environment

You can update any references that depend on test data you created earlier.

1. Set up any resources you need for testing, such as products, customers, subscriptions, and payment methods.
2. Update any part of your testing processes that depends on specific test object IDs. This changes when you create new objects in a sandbox.

#### (Optional) Set up simulations

Set up simulations to test your Billing integration. Simulations let you move time forward in the sandbox so resources such as subscriptions change state and trigger webhook events.

## Test card numbers 

Stripe provides a set of [test card numbers](https://docs.stripe.com/testing.md#cards) that you can use to simulate various payment scenarios. You can use these test card numbers to create simulated payments in sandboxes without processing actual payments or charges.

When you use test card numbers, you can enter any expiration date in the future and any three-digit CVC code to simulate a successful payment. If you want to simulate a failed payment, you can use specific test card numbers and CVC codes provided by Stripe.

Test card numbers are only valid in sandboxes. Don’t use them for real payments.

## Delete test data 

To delete all of your test data from your Stripe account, complete the following steps:

1. [Log in to the Dashboard](https://dashboard.stripe.com) using your existing Stripe account.
2. While in your sandbox, click **Developers** > **Overview**.
3. Under **Test data**, click **Review test data**. The dialog gives you a list of all of your existing test data objects.
4. Click **Delete test data** to initiate the deletion process. You can’t undo the deletion of your test data.

Sandboxes are temporarily unusable while the deletion process occurs.

> You must manually delete [Meters](https://docs.stripe.com/api/billing/meter.md) because the object isn’t supported by the automated test data deletion process.

## Test email 

By default, Stripe doesn’t email customers in sandboxes. For example, paying an invoice in a sandbox doesn’t send a receipt email to the customer. Invoices finalized through the API in sandboxes also don’t send a receipt email to the customer.

If you want Stripe to email customers in a sandbox, you can do the following in the Dashboard:

1. Create and manually send an invoice to a specific customer.
2. Manually send a receipt for a paid invoice.

To verify emails for invoices and receipts, set the email address for your [Team](https://dashboard.stripe.com/settings/team) on the `Customer` object or `receipt_email` attribute on the PaymentIntent.

## Testing use cases 

The following table contains quality assurance (QA) testing use cases:

> #### Don't use search to verify recent changes
> 
> Search data is eventually consistent, so objects you create or update might not appear immediately in search results. If an object is missing, don’t retry the request that created it because retrying can create duplicate objects, such as `Customer` or `Subscription` objects. Learn more about [search data freshness](https://docs.stripe.com/search.md#data-freshness).
> 
> To verify a recently created or updated object, retrieve it using a deterministic ID from the creating request, callback, or return URL, such as a Checkout Session ID. If you don’t have one, use the appropriate list endpoint for immediate availability.

| **Use case** | **Action** |
| --- | --- |
| Charge success (capturing immediately) | - No error.
- The charge appears as **Succeeded** in the Dashboard under [Payments](https://dashboard.stripe.com/payments).
- Stripe captures the charge. |
| PaymentIntent authorization success ([capturing funds for later](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md)) | ```json
{
  ...
  "capture_method": "manual",
  ...
  "status": "requires_capture",
  ...
}
``` |
| PaymentIntent capture success (capturing immediately or [capturing funds for later](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md)) | ```json
  {
    ...
    "status": "succeeded",
    ...
  }
``` |
| Charge fail | The charge appears as **Failed** in the Dashboard under [Payments](https://dashboard.stripe.com/payments).
```json
{
  "error": {
    "charge": "ch_orWziM4j7CiRL8J4",
    "code": "card_declined",
    "decline_code": "<<REASON HERE>>",
    "doc_url": "https://docs.stripe.com/error-codes#card-declined",
    "message": "Your card was declined.",
    "type": "card_error"
  }
}
``` |
| Radar block | No matter which version of Radar you use, it might block a charge because of [high risk](https://docs.stripe.com/radar/transaction-risk-prevention.md#high-risk) or a [rule](https://docs.stripe.com/radar/rules.md). The response is the same as what you get when a charge fails. |
| Charge disputed | - The charge appears as **Disputed** in the Dashboard under [Payments](https://dashboard.stripe.com/payments).
- Stripe debits the charge amount plus the dispute fee from the balance, creates a `Dispute` object along with its associated `charge.dispute.created` event.

```json
{
  "object": {
    "id": "du_orWziM4j7CiRL8J4",
    "object": "dispute",
    "charge_id": "ch_orWziM4j7CiRL8J4",
    ...
    "status": "needs_response"
  }
}
``` |
| Charge inquiry opened | Inquiries are similar to disputes, with three key distinctions: no funds are withdrawn unless we elevate an inquiry to a dispute, they remain refundable until disputed, and have a different set of statuses. In this case, Stripe fires a `charge.dispute.created` event.

```json
{
  "object": {
    "id": "du_orWziM4j7CiRL8J4",
    "object": "dispute",
    "charge_id": "ch_orWziM4j7CiRL8J4",
    ...
    "is_charge_refundable": true,
    ...
    "status": "warning_needs_response"
  }
}
``` |
| Dispute won | - When a customer wins a dispute, the funds of the original charge are restored to the account, less the dispute fee.
- Stripe updates the existing `Dispute` object, and fires a `charge.dispute.closed` event.

```json
{
  "object": {
    "id": "du_orWziM4j7CiRL8J4",
    "object": "dispute",
    "charge_id": "ch_orWziM4j7CiRL8J4",
    ...
    "status": "won"
  }
}
``` |
| Dispute lost | When a customer loses a dispute, Stripe updates the existing `Dispute` object, and fires a `charge.dispute.closed` event.

```json
{
  "object": {
    "id": "du_orWziM4j7CiRL8J4",
    "object": "dispute",
    "charge_id": "ch_orWziM4j7CiRL8J4",
    ...
    "status": "lost"
  }
}
``` |
| Inquiry won | When you win an inquiry, your balance remains the same, as no funds were removed when you initially opened the inquiry. Stripe updates the existing `Dispute` object, and sends a `charge.dispute.closed` event.

```json
{
  "object": {
    "id": "du_orWziM4j7CiRL8J4",
    "object": "dispute",
    "charge_id": "ch_orWziM4j7CiRL8J4",
    ...
    "status": "warning_closed"
  }
}
``` |
| Inquiry lost | - When you lose an inquiry, it escalates to a dispute.
- When it escalates to a dispute, its status changes with a `charge.dispute.updated` event, and funds are withdrawn in a `charge.dispute.funds_withdrawn` event:

```json
{
  "object": {
    "id": "du_orWziM4j7CiRL8J4",
    "object": "dispute",
    "charge_id": "ch_orWziM4j7CiRL8J4",
    ...
    "status": "needs_response"
  }
}
``` |
| Charge refunded | You can see the charge as `Refunded` in the Dashboard under [Payments](https://dashboard.stripe.com/payments).

```json
{
  "id": "re_orWziM4j7CiRL8J4",
  "object": "refund",
  "amount": "<<FULL AMOUNT>>",
  "charge": "ch_orWziM4j7CiRL8J4",
  ...
  "payment_intent": "pi_orWziM4j7CiRL8J4", // if you're using PaymentIntents
  ...
  "status": "succeeded"
}
``` |
| Charge partially refunded | - You can see the charge as `Refunded` in the Dashboard under [Payments](https://dashboard.stripe.com/payments).
- The refund amount is different from the charge amount, and you can still dispute partially-refunded charges.

```json
{
  "id": "re_orWziM4j7CiRL8J4",
  "object": "refund",
  "amount": "<<PARTIAL AMOUNT>>",
  "charge": "ch_orWziM4j7CiRL8J4",
  ...
  "payment_intent": "pi_orWziM4j7CiRL8J4", // if you're using PaymentIntents
  ...
  "status": "succeeded"
}
``` |
| Account balance goes negative | Make sure to test for a negative balance on Stripe and verify that your bank accounts can accept debits from us. |
| Successful payout | If you enable webhooks for a [successful payout](https://docs.stripe.com/api/events/types.md#event_types-payout.paid) (recommended), test your handling of the event. |
| Failed payout | If you enable webhooks for a [failed payout](https://docs.stripe.com/api/events/types.md#event_types-payout.failed) (recommended), test your handling of the event. |

## The Stripe Postman collection 

Postman is a common API development tool. To help integrate Stripe, we provide a [Payments-specific Postman collection](https://www.getpostman.com/collections/080102f58f29afa081d7) with the tools you need to test the server-side component of your integration.

### Import the collection 

To begin, you need to access the Postman app. You can use either the browser or desktop version. After launching the app, import the collection.

To start this process on the web, click **Import** in the top-left corner, then click **Link**. Insert the [Payments collection](https://www.getpostman.com/collections/080102f58f29afa081d7) link. If you’re using the Postman desktop app, click **File** > **Import**. After successfully importing, the collection appears under **Collections**.

### Use the collection 

To use the collection, go to the collection you just imported and click **Variables**. Copy your Stripe sandbox secret key from the Stripe Dashboard, and paste it into the `Initial Value` field of the `secret_key` row. After you complete this step, you can begin making requests.

During collection runtime, scripts populate other variables. For example, when creating a [customer](https://docs.stripe.com/api/customers/create.md), [price](https://docs.stripe.com/api/prices/create.md), [charge](https://docs.stripe.com/api/charges/object.md) or [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md), the system saves that ID through a script in the collection, making it accessible for later requests, such as issuing a refund.

## See also

- [Test your integration](https://docs.stripe.com/testing.md)
- [Sandboxes](https://docs.stripe.com/sandboxes.md)
- [API keys](https://docs.stripe.com/keys.md)

