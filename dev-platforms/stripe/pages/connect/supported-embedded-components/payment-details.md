---
title: "Payment details"
source: https://docs.stripe.com/connect/supported-embedded-components/payment-details.md
path: connect/supported-embedded-components/payment-details
---

# Payment details

Show details of a given payment and allow users to manage disputes and perform refunds.

This component is a subset of `payments`, which provides the detail overlay of a given payment. The UI rendered by the payment details component is equivalent to the overlay that the `payments` component renders when the user clicks on a payment row.

Use the `payment-details` component to invoke the payment details overlay without the need to inline the entirety of the `payments` list in your website. This allows you to invoke the payment detail overlay from your existing UI (for example, your payments list) and integrate with our detail view to enable your customers to view payment details, issue refunds, and manage disputed payments.

The payment-details component shows different information and supports different features for different charge types:

- For direct charges, your connected accounts can view the complete set of information. They can also manage refunds and disputes, and capture payments if you enable the corresponding features when creating an account session.
- For [destination charges](https://docs.stripe.com/connect/destination-charges.md) and [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md), your connected accounts can only see the transfer object associated with the selected charge, which contains limited information.
- For destination charges with the `on_behalf_of` attribute, you can [enable features](https://docs.stripe.com/connect/supported-embedded-components/payment-details.md#allow-your-connected-accounts-to-manage-destination-charges) that allow your connected accounts more control than regular destination charges.

Note: The following is a preview/demo component that behaves differently than live mode usage with real connected accounts. The actual component has more functionality than what might appear in this demo component. For example, for connected accounts without Stripe dashboard access (custom accounts), no user authentication is required in production.

When [creating an Account Session](https://docs.stripe.com/api/account_sessions/create.md), enable payment details by specifying `payment_details` in the `components` parameter. You can turn on or off an individual feature of the payment details component by specifying the `features` parameter under `payment_details`:

```curl
curl https://api.stripe.com/v1/account_sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "account={{CONNECTEDACCOUNT_ID}}" \
  -d "components[payment_details][enabled]=true" \
  -d "components[payment_details][features][refund_management]=true" \
  -d "components[payment_details][features][dispute_management]=true" \
  -d "components[payment_details][features][capture_payments]=true" \
  -d "components[payment_details][features][destination_on_behalf_of_charge_management]=false"
```

After creating the account session and [initializing ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components.md#account-sessions), you can render the payment details component in the frontend:

#### JavaScript

```js
// Include this element in your HTML
const paymentDetails = stripeConnectInstance.create('payment-details');
paymentDetails.setPayment('{{PAYMENT_INTENT_OR_CHARGE_ID}}');
// use setOnClose to set a callback function to close payment-details
paymentDetails.setOnClose(() => {
  paymentDetails.remove();
});
container.appendChild(paymentDetails);
```

> For [destination charges](https://docs.stripe.com/connect/destination-charges.md) and [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md), the PaymentIntent doesn’t exist on the connected account. Instead, pass the associated charge ID that belongs to the connected account.

### Allow your connected accounts to manage destination charges

You can set the `destination_on_behalf_of_charge_management` feature to `true` to present destination charges that have the [on_behalf_of](https://docs.stripe.com/connect/charges.md#on_behalf_of) attribute in the payment details component. You can then enable [dispute and refund management](https://docs.stripe.com/connect/supported-embedded-components/payment-details.md#disputes-and-refunds-for-destination-charges) to allow your connected accounts to handle disputes and issue refunds from within the payment details component.

Enabling the `destination_on_behalf_of_charge_management` feature has the following limitations:

- You can’t filter by charge status or payment methods.
- You can’t export certain data columns.

## Disputes and refunds for destination charges

When you enable `destination_on_behalf_of_charge_management` feature in the payment details component, you can also enable the `refund_management` and `dispute_management` features to allow your connected accounts to take action on destination charges with the `on_behalf_of` attribute set to the connected account:

- Issue refunds
- Submit and update dispute evidence
- Counter disputes
- Accept disputes

### Refunds

Refunding a destination charge through the payment details component automatically reverses its associated transfer.

Refunding any type of charge in the component doesn’t refund application fees, which is consistent with the default behavior on the [Refunds API](https://docs.stripe.com/api/refunds/create.md#create_refund-refund_application_fee).

### Disputes

Stripe debits dispute amounts and fees from your platform account for all [destination charges](https://docs.stripe.com/connect/destination-charges.md), with or without `on_behalf_of`.

Set up [a webhook](https://docs.stripe.com/webhooks.md) to listen for [dispute created events](https://docs.stripe.com/api/events/types.md#event_types-charge.dispute.created).

You can reverse the transfer to your connected account through the [Dashboard](https://dashboard.stripe.com/test/transfers) or by [creating a transfer reversal](https://docs.stripe.com/api/transfer_reversals/create.md) to recover the dispute chargeback funds. If the connected account has a negative balance, Stripe attempts to debit its external account if [debit_negative_balances](https://docs.stripe.com/connect/account-balances.md#automatically-debit-connected-accounts) is set to `true`.

Time your reversal according to how you choose to handle the dispute:

- If you accept the dispute, you can reverse the transfer immediately.
- If you challenge the dispute, wait for the dispute outcome before reversing the transfer.
  - If you win, don’t reverse the transfer.
  - If you lose, reverse the transfer.

If you reverse the transfer for a disputed payment that you challenge and win, transfering those funds back to a connected account can have unexpected results:

- If your platform has an insufficient balance, the transfer fails. Prevent insufficient balance errors by [adding funds to your Stripe balance](https://docs.stripe.com/get-started/account/add-funds.md).
- [Cross-border transfer restrictions](https://docs.stripe.com/connect/account-capabilities.md#transfers-cross-border) might prevent you from repaying your connected account.

## Supported parameters

This embedded component supports the following parameters:

#### HTML + JS

| Method | Type | Description |  |
| --- | --- | --- | --- |
| `setPayment` | `string` | The ID of the payment, charge, or PaymentIntent that displays in the overlay. This should be an ID of the payment, charge, or PaymentIntent on the connected account. If this attribute isn’t defined, the embedded component renders nothing. To obtain this ID, query the [charges API](https://docs.stripe.com/api/charges.md) or use a payment ID that you’ve created or stored in your integration. | required |
| `setOnClose` | `() => void` | We send this event when the user closes the overlay. |  |

To enable the dismiss behavior of this component, listen to the `close` event by calling `setOnClose`.

#### React

| React prop | Type | Description |  |
| --- | --- | --- | --- |
| `payment` | `string` | The ID of the payment, charge, or PaymentIntent that displays in the overlay. This should be an ID of the payment, charge, or PaymentIntent on the connected account. If this parameter isn’t passed in, the embedded component renders nothing. To obtain this ID, query the [charges API](https://docs.stripe.com/api/charges.md) or use a payment ID that you’ve created or stored in your integration. | required |
| `onClose` | `() => void` | The function that runs when the user closes the overlay. | required |

