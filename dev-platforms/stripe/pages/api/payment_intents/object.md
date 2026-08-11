---
title: "The PaymentIntent object"
source: https://docs.stripe.com/api/payment_intents/object.md
path: api/payment_intents/object
---

# The PaymentIntent object

### The PaymentIntent object

```json
{
  "id": "pi_3MtwBwLkdIwHu7ix28a3tqPa",
  "object": "payment_intent",
  "amount": 2000,
  "amount_capturable": 0,
  "amount_details": {
    "tip": {}
  },
  "amount_received": 0,
  "application": null,
  "application_fee_amount": null,
  "automatic_payment_methods": {
    "enabled": true
  },
  "canceled_at": null,
  "cancellation_reason": null,
  "capture_method": "automatic",
  "client_secret": "pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH",
  "confirmation_method": "automatic",
  "created": 1680800504,
  "currency": "usd",
  "customer": null,
  "description": null,
  "last_payment_error": null,
  "latest_charge": null,
  "livemode": false,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": null,
  "payment_method_options": {
    "card": {
      "installments": null,
      "mandate_options": null,
      "network": null,
      "request_three_d_secure": "automatic"
    },
    "link": {
      "persistent_token": null
    }
  },
  "payment_method_types": [
    "card",
    "link"
  ],
  "processing": null,
  "receipt_email": null,
  "review": null,
  "setup_future_usage": null,
  "shipping": null,
  "source": null,
  "statement_descriptor": null,
  "statement_descriptor_suffix": null,
  "status": "requires_payment_method",
  "transfer_data": null,
  "transfer_group": null
}
```

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `allowed_payment_method_types` (array of enums, nullable)
  The list of payment method types allowed for use with this payment. Stripe automatically returns compatible payment methods from this list in the `payment_method_types` field of the response, based on the other PaymentIntent parameters, such as `currency`, `amount`, and `customer`.
Possible enum values:
  - `acss_debit`
    [Pre-authorized debit payments](https://docs.stripe.com/docs/payments/acss-debit.md) are used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).

  - `affirm`
    [Affirm](https://docs.stripe.com/docs/payments/affirm.md) is a buy now, pay later payment method in the US.

  - `afterpay_clearpay`
    [Afterpay / Clearpay](https://docs.stripe.com/docs/payments/afterpay-clearpay.md) is a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.

  - `alipay`
    [Alipay](https://docs.stripe.com/docs/payments/alipay.md) is a digital wallet payment method used in China.

  - `alma`
    [Alma](https://docs.stripe.com/docs/payments/alma.md) is a Buy Now, Pay Later payment method that lets customers pay in 2, 3, or 4 installments.

  - `amazon_pay`
    [Amazon Pay](https://docs.stripe.com/docs/payments/amazon-pay.md) is a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.

  - `au_becs_debit`
    [BECS Direct Debit](https://docs.stripe.com/docs/payments/au-becs-debit.md) is used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).

  - `bacs_debit`
    [Bacs Direct Debit](https://docs.stripe.com/docs/payments/payment-methods/bacs-debit.md) is used to debit UK bank accounts.

  - `bancontact`
    [Bancontact](https://docs.stripe.com/docs/payments/bancontact.md) is a bank redirect payment method used in Belgium.

  - `billie`
    [Billie](https://docs.stripe.com/docs/payments/billie.md) is a payment method.

  - `bizum`
    [Bizum](https://docs.stripe.com/docs/payments/bizum.md) is a payment method.

  - `blik`
    [BLIK](https://docs.stripe.com/docs/payments/blik.md) is a single-use payment method common in Poland.

  - `boku_promptpay`
    PromptPay is a payment method.

  - `boleto`
    [Boleto](https://docs.stripe.com/docs/payments/boleto.md) is a voucher-based payment method used in Brazil.

  - `capchase_pay`
    CapchasePay is a payment method.

  - `card`
    [Card payments](https://docs.stripe.com/docs/payments/payment-methods/overview.md#cards) are supported through many networks, card brands, and select Link funding sources (Link is also known as Onelink in the UK).

  - `card_present`
    [Stripe Terminal](https://docs.stripe.com/docs/terminal/payments/collect-card-payment.md) is used to collect in-person card payments.

  - `cashapp`
    [Cash App Pay](https://docs.stripe.com/docs/payments/cash-app-pay.md) enables customers to frictionlessly authenticate payments in the Cash App using their stored balance or linked card.

  - `check_scan`
    CheckScan is a payment method.

  - `click_to_pay`
    ClickToPay is a payment method.

  - `crypto`
    [Stablecoin payments](https://docs.stripe.com/docs/payments/stablecoin-payments.md) enable customers to pay in stablecoins like USDC from 100s of wallets including Phantom and Metamask.

  - `customer_balance`
    Uses a customer’s [cash balance](https://docs.stripe.com/docs/payments/customer-balance.md) for the payment.

  - `demo_pay`
    DemoPay is a payment method.

  - `duitnow`
    Duitnow is a payment method.

  - `dummy_auth_push`
    Dummy auth push payment method for internal testing.

  - `dummy_passthrough_card`
    Dummy auth push payment method for internal testing.

  - `edenred`
    [Edenred](https://docs.stripe.com/docs/payments/edenred.md) is a payment method.

  - `eps`
    [EPS](https://docs.stripe.com/docs/payments/eps.md) is an Austria-based bank redirect payment method.

  - `fpx`
    [FPX](https://docs.stripe.com/docs/payments/fpx.md) is a Malaysia-based bank redirect payment method.

  - `gcash`
    GCash is a payment method.

  - `getbalance`
    [Getbalance](https://docs.stripe.com/docs/payments/getbalance.md) is a payment method.

  - `gift_card`
    Gift card is a payment method for redeeming third-party gift cards.

  - `giropay`
    [giropay](https://docs.stripe.com/docs/payments/giropay.md) is a German bank redirect payment method.

  - `gopay`
    Gopay is a payment method.

  - `grabpay`
    [GrabPay](https://docs.stripe.com/docs/payments/grabpay.md) is a digital wallet payment method used in Southeast Asia.

  - `id_bank_transfer`
    [Indonesia bank transfer](https://docs.stripe.com/docs/payments/id-bank-transfer.md) payments are used to accept bank transfers from customers in Indonesia.

  - `ideal`
    [iDEAL](https://docs.stripe.com/docs/payments/ideal.md) is a Netherlands-based bank redirect payment method.

  - `interac_present`
    [Stripe Terminal](https://docs.stripe.com/docs/terminal/payments/collect-card-payment.md) accepts [Interac](https://docs.stripe.com/docs/terminal/payments/regional.md?integration-country=CA#interac-payments) debit cards for in-person payments in Canada.

  - `kakao_pay`
    [Kakao Pay](https://docs.stripe.com/docs/payments/kakao-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `klarna`
    [Klarna](https://docs.stripe.com/docs/payments/klarna.md) is a global buy now, pay later payment method.

  - `knet`
    KNET is a bank redirect payment method used in Kuwait.

  - `konbini`
    [Konbini](https://docs.stripe.com/docs/payments/konbini.md) is a cash-based voucher payment method used in Japan.

  - `kr_card`
    [Korean cards](https://docs.stripe.com/docs/payments/kr-card/accept-a-payment.md) enables customers to accept local credit and debit cards in South Korea.

  - `kr_market`
    KrMarket is a payment method.

  - `kriya`
    Kriya is a payment method.

  - `link`
    [Link (also known as Onelink in the UK)](https://docs.stripe.com/docs/payments/link.md) allows customers to pay with their saved payment details.

  - `mb_way`
    MB WAY is a payment method.

  - `mobilepay`
    [MobilePay](https://docs.stripe.com/docs/payments/mobilepay.md) is a Nordic card-passthrough wallet payment method where customers authorize the payment in the MobilePay application.

  - `momo`
    Momo is a payment method.

  - `mondu`
    [Mondu](https://docs.stripe.com/docs/payments/mondu.md) is a payment method.

  - `multibanco`
    [Multibanco](https://docs.stripe.com/docs/payments/multibanco.md) is a voucher payment method

  - `naver_pay`
    [Naver Pay](https://docs.stripe.com/docs/payments/naver-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `netbanking`
    [NetBanking](https://docs.stripe.com/docs/payments/netbanking.md) is a bank redirect payment method used in India.

  - `ng_bank`
    Naira wallet is a payment method.

  - `ng_bank_transfer`
    Naira bank transfer is a payment method.

  - `ng_card`
    Naira card is a payment method.

  - `ng_market`
    NgMarket is a payment method.

  - `ng_ussd`
    Naira USSD is a payment method used in Nigeria to power USSD payments.

  - `ng_wallet`
    NgWallet is a payment method.

  - `nz_bank_account`
    [New Zealand BECS Direct Debit](https://docs.stripe.com/docs/payments/nz-bank-account.md) is used to debit New Zealand bank accounts through the Bulk Electronic Clearing System (BECS).

  - `octopus`
    [Octopus](https://docs.stripe.com/docs/payments/octopus.md) is a payment method.

  - `oxxo`
    [OXXO](https://docs.stripe.com/docs/payments/oxxo.md) is a cash-based voucher payment method used in Mexico.

  - `p24`
    [Przelewy24](https://docs.stripe.com/docs/payments/p24.md) is a bank redirect payment method used in Poland.

  - `paper_check`
    PaperCheck is a payment method.

  - `pay_by_bank`
    [Pay By Bank](https://docs.stripe.com/docs/payments/pay-by-bank.md) is an open banking payment method in the UK.

  - `payco`
    [PAYCO](https://docs.stripe.com/docs/payments/payco/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `paynow`
    [PayNow](https://docs.stripe.com/docs/payments/paynow.md) is a QR code payment method used in Singapore.

  - `paypal`
    [PayPal](https://docs.stripe.com/docs/payments/paypal.md) is an online wallet and redirect payment method commonly used in Europe.

  - `paypay`
    [PayPay](https://docs.stripe.com/docs/payments/paypay.md) is a payment method.

  - `payto`
    [PayTo](https://docs.stripe.com/docs/payments/payto.md) is a real time payment method

  - `pix`
    [Pix](https://docs.stripe.com/docs/payments/pix.md) is an instant bank transfer payment method in Brazil.

  - `promptpay`
    [PromptPay](https://docs.stripe.com/docs/payments/promptpay.md) is an instant funds transfer service popular in Thailand.

  - `qris`
    [QRIS](https://docs.stripe.com/docs/payments/qris.md) is a QR Code payment method in Indonesia.

  - `rechnung`
    [Rechnung](https://docs.stripe.com/docs/payments/rechnung.md) is a buy now, pay later payment option in Germany using white-label invoicing.

  - `revolut_pay`
    [Revolut Pay](https://docs.stripe.com/docs/payments/revolut-pay.md) is a digital wallet payment method used in the United Kingdom.

  - `samsung_pay`
    [Samsung Pay](https://docs.stripe.com/docs/payments/samsung-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `satispay`
    [Satispay](https://docs.stripe.com/docs/payments/satispay.md) is a payment method.

  - `scalapay`
    Scalapay is a payment method.

  - `sepa_debit`
    [SEPA Direct Debit](https://docs.stripe.com/docs/payments/sepa-debit.md) is used to debit bank accounts within the Single Euro Payments Area (SEPA) region.

  - `sequra`
    Sequra is a payment method.

  - `shop_pay`
    [Shop Pay](https://docs.stripe.com/docs/payments/shop-pay.md) is a Wallet payment method that lets hundreds of millions of Shopify customers pay their way, every day.

  - `shopeepay`
    Shopeepay is a payment method.

  - `sofort`
    [Sofort](https://docs.stripe.com/docs/payments/sofort.md) is a bank redirect payment method used in Europe.

  - `south_korea_market`
    SouthKoreaMarket is a payment method.

  - `stripe_balance`
    [Pay with Stripe balance](https://docs.stripe.com/docs/payments/balance-pay.md) is a payment method linked directly to a Stripe account’s available balance.

  - `sunbit`
    [Sunbit](https://docs.stripe.com/docs/payments/sunbit.md) is a payment method.

  - `swish`
    [Swish](https://docs.stripe.com/docs/payments/swish.md) is a Swedish wallet payment method where customers authorize the payment in the Swish application.

  - `tamara`
    [Tamara](https://docs.stripe.com/docs/payments/tamara.md) is a payment method.

  - `test_pay`
    TestPay is a payment method.

  - `truemoney`
    TrueMoney is a payment method.

  - `twint`
    [TWINT](https://docs.stripe.com/docs/payments/twint.md) is a single-use payment method used in Switzerland.

  - `upi`
    [UPI](https://docs.stripe.com/docs/payments/upi.md) is an instant real-time payment system in India.

  - `us_bank_account`
    [ACH Direct Debit](https://docs.stripe.com/docs/payments/ach-direct-debit.md) is used to debit US bank accounts through the Automated Clearing House (ACH) payments system.

  - `us_cash_voucher`
    UsCashVoucher enables Treasury customers to add cash to their account using a voucher at select major US retailers.

  - `vipps`
    [Vipps](https://docs.stripe.com/docs/payments/vipps.md) is a Nordic card-passthrough wallet payment method where customers authorize the payment in the Vipps application.

  - `wechat_pay`
    [WeChat Pay](https://docs.stripe.com/docs/payments/wechat-pay.md) is a digital wallet payment method based in China.

  - `wero`
    Wero is a payment method.

  - `zip`
    [Zip](https://docs.stripe.com/docs/payments/zip.md) is a Buy now, pay later Payment Method

- `amount` (integer)
  Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://docs.stripe.com/docs/currencies.md#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

- `amount_capturable` (integer)
  Amount that can be captured from this PaymentIntent.

- [`amount_details`](https://docs.stripe.com/api/payment_intents/object.md?query=amount_details) (object, nullable)
  Provides industry-specific information about the amount.

- `amount_received` (integer)
  Amount that this PaymentIntent collects.

- `application` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the Connect application that created the PaymentIntent.

- `application_fee_amount` (integer, nullable)
  The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner’s Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://docs.stripe.com/docs/payments/connected-accounts.md).

- [`automatic_payment_methods`](https://docs.stripe.com/api/payment_intents/object.md?query=automatic_payment_methods) (object, nullable)
  Settings to configure compatible payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

- `canceled_at` (timestamp, nullable)
  Populated when `status` is `canceled`, this is the time at which the PaymentIntent was canceled. Measured in seconds since the Unix epoch.

- `cancellation_reason` (enum, nullable)
  Reason for cancellation of this PaymentIntent, either user-provided (`duplicate`, `fraudulent`, `requested_by_customer`, or `abandoned`) or generated by Stripe internally (`failed_invoice`, `void_invoice`, `automatic`, or `expired`).
Possible enum values:
  - `abandoned`
  - `automatic`
  - `duplicate`
  - `expired`
  - `failed_invoice`
  - `fraudulent`
  - `requested_by_customer`
  - `void_invoice`

- `capture_method` (enum)
  Controls when the funds will be captured from the customer’s account.
Possible enum values:
  - `automatic`
    Stripe automatically captures funds when the customer authorizes the payment.

  - `automatic_async`
    (Default) Stripe asynchronously captures funds when the customer authorizes the payment. Recommended over `capture_method=automatic` due to improved latency. Read the [integration guide](https://docs.stripe.com/docs/payments/payment-intents/asynchronous-capture.md) for more information.

  - `manual`
    Place a hold on the funds when the customer authorizes the payment, but [don’t capture the funds until later](https://docs.stripe.com/docs/payments/capture-later.md). (Not all payment methods support this.)

- `client_secret` (string, nullable)
  The client secret of this PaymentIntent. Used for client-side retrieval using a publishable key.

  The client secret can be used to complete a payment from your frontend. It should not be stored, logged, or exposed to anyone other than the customer. Make sure that you have TLS enabled on any page that includes the client secret.

  Refer to our docs to [accept a payment](https://docs.stripe.com/docs/payments/accept-a-payment.md?ui=elements) and learn about how `client_secret` should be handled.

- `confirmation_method` (enum)
  Describes whether we can confirm this PaymentIntent automatically, or if it requires customer action to confirm the payment.
Possible enum values:
  - `automatic`
    (Default) PaymentIntent can be confirmed using a publishable key. After `next_action`s are handled, no additional confirmation is required to complete the payment.

  - `manual`
    All payment attempts must be made using a secret key. The PaymentIntent returns to the `requires_confirmation` state after handling `next_action`s, and requires your server to initiate each payment attempt with an explicit confirmation.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies.md).

- `customer` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the Customer this PaymentIntent belongs to, if one exists.

  Payment methods attached to other Customers cannot be used with this PaymentIntent.

  If [setup_future_usage](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-setup_future_usage) is set and this PaymentIntent’s payment method is not `card_present`, then the payment method attaches to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is `card_present` and isn’t a digital wallet, then a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card is created and attached to the Customer instead.

- `customer_account` (string, nullable)
  ID of the Account representing the customer that this PaymentIntent belongs to, if one exists.

  Payment methods attached to other Accounts cannot be used with this PaymentIntent.

  If [setup_future_usage](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-setup_future_usage) is set and this PaymentIntent’s payment method is not `card_present`, then the payment method attaches to the Account after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is `card_present` and isn’t a digital wallet, then a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card is created and attached to the Account instead.

- `description` (string, nullable)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `excluded_payment_method_types` (array of enums, nullable)
  The list of payment method types to exclude from use with this payment.
Possible enum values:
  - `acss_debit`
    [Pre-authorized debit payments](https://docs.stripe.com/docs/payments/acss-debit.md) are used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).

  - `affirm`
    [Affirm](https://docs.stripe.com/docs/payments/affirm.md) is a buy now, pay later payment method in the US.

  - `afterpay_clearpay`
    [Afterpay / Clearpay](https://docs.stripe.com/docs/payments/afterpay-clearpay.md) is a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.

  - `alipay`
    [Alipay](https://docs.stripe.com/docs/payments/alipay.md) is a digital wallet payment method used in China.

  - `alma`
    [Alma](https://docs.stripe.com/docs/payments/alma.md) is a Buy Now, Pay Later payment method that lets customers pay in 2, 3, or 4 installments.

  - `amazon_pay`
    [Amazon Pay](https://docs.stripe.com/docs/payments/amazon-pay.md) is a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.

  - `au_becs_debit`
    [BECS Direct Debit](https://docs.stripe.com/docs/payments/au-becs-debit.md) is used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).

  - `bacs_debit`
    [Bacs Direct Debit](https://docs.stripe.com/docs/payments/payment-methods/bacs-debit.md) is used to debit UK bank accounts.

  - `bancontact`
    [Bancontact](https://docs.stripe.com/docs/payments/bancontact.md) is a bank redirect payment method used in Belgium.

  - `billie`
    [Billie](https://docs.stripe.com/docs/payments/billie.md) is a payment method.

  - `bizum`
    [Bizum](https://docs.stripe.com/docs/payments/bizum.md) is a payment method.

  - `blik`
    [BLIK](https://docs.stripe.com/docs/payments/blik.md) is a single-use payment method common in Poland.

  - `boleto`
    [Boleto](https://docs.stripe.com/docs/payments/boleto.md) is a voucher-based payment method used in Brazil.

  - `card`
    [Card payments](https://docs.stripe.com/docs/payments/payment-methods/overview.md#cards) are supported through many networks, card brands, and select Link funding sources (Link is also known as Onelink in the UK).

  - `card_present`
    [Stripe Terminal](https://docs.stripe.com/docs/terminal/payments/collect-card-payment.md) is used to collect in-person card payments.

  - `cashapp`
    [Cash App Pay](https://docs.stripe.com/docs/payments/cash-app-pay.md) enables customers to frictionlessly authenticate payments in the Cash App using their stored balance or linked card.

  - `crypto`
    [Stablecoin payments](https://docs.stripe.com/docs/payments/stablecoin-payments.md) enable customers to pay in stablecoins like USDC from 100s of wallets including Phantom and Metamask.

  - `customer_balance`
    Uses a customer’s [cash balance](https://docs.stripe.com/docs/payments/customer-balance.md) for the payment.

  - `eps`
    [EPS](https://docs.stripe.com/docs/payments/eps.md) is an Austria-based bank redirect payment method.

  - `fpx`
    [FPX](https://docs.stripe.com/docs/payments/fpx.md) is a Malaysia-based bank redirect payment method.

  - `giropay`
    [giropay](https://docs.stripe.com/docs/payments/giropay.md) is a German bank redirect payment method.

  - `grabpay`
    [GrabPay](https://docs.stripe.com/docs/payments/grabpay.md) is a digital wallet payment method used in Southeast Asia.

  - `ideal`
    [iDEAL](https://docs.stripe.com/docs/payments/ideal.md) is a Netherlands-based bank redirect payment method.

  - `interac_present`
    [Stripe Terminal](https://docs.stripe.com/docs/terminal/payments/collect-card-payment.md) accepts [Interac](https://docs.stripe.com/docs/terminal/payments/regional.md?integration-country=CA#interac-payments) debit cards for in-person payments in Canada.

  - `kakao_pay`
    [Kakao Pay](https://docs.stripe.com/docs/payments/kakao-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `klarna`
    [Klarna](https://docs.stripe.com/docs/payments/klarna.md) is a global buy now, pay later payment method.

  - `konbini`
    [Konbini](https://docs.stripe.com/docs/payments/konbini.md) is a cash-based voucher payment method used in Japan.

  - `kr_card`
    [Korean cards](https://docs.stripe.com/docs/payments/kr-card/accept-a-payment.md) enables customers to accept local credit and debit cards in South Korea.

  - `mb_way`
    MB WAY is a payment method.

  - `mobilepay`
    [MobilePay](https://docs.stripe.com/docs/payments/mobilepay.md) is a Nordic card-passthrough wallet payment method where customers authorize the payment in the MobilePay application.

  - `multibanco`
    [Multibanco](https://docs.stripe.com/docs/payments/multibanco.md) is a voucher payment method

  - `naver_pay`
    [Naver Pay](https://docs.stripe.com/docs/payments/naver-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `nz_bank_account`
    [New Zealand BECS Direct Debit](https://docs.stripe.com/docs/payments/nz-bank-account.md) is used to debit New Zealand bank accounts through the Bulk Electronic Clearing System (BECS).

  - `oxxo`
    [OXXO](https://docs.stripe.com/docs/payments/oxxo.md) is a cash-based voucher payment method used in Mexico.

  - `p24`
    [Przelewy24](https://docs.stripe.com/docs/payments/p24.md) is a bank redirect payment method used in Poland.

  - `pay_by_bank`
    [Pay By Bank](https://docs.stripe.com/docs/payments/pay-by-bank.md) is an open banking payment method in the UK.

  - `payco`
    [PAYCO](https://docs.stripe.com/docs/payments/payco/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `paynow`
    [PayNow](https://docs.stripe.com/docs/payments/paynow.md) is a QR code payment method used in Singapore.

  - `paypal`
    [PayPal](https://docs.stripe.com/docs/payments/paypal.md) is an online wallet and redirect payment method commonly used in Europe.

  - `paypay`
    [PayPay](https://docs.stripe.com/docs/payments/paypay.md) is a payment method.

  - `payto`
    [PayTo](https://docs.stripe.com/docs/payments/payto.md) is a real time payment method

  - `pix`
    [Pix](https://docs.stripe.com/docs/payments/pix.md) is an instant bank transfer payment method in Brazil.

  - `promptpay`
    [PromptPay](https://docs.stripe.com/docs/payments/promptpay.md) is an instant funds transfer service popular in Thailand.

  - `revolut_pay`
    [Revolut Pay](https://docs.stripe.com/docs/payments/revolut-pay.md) is a digital wallet payment method used in the United Kingdom.

  - `samsung_pay`
    [Samsung Pay](https://docs.stripe.com/docs/payments/samsung-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `satispay`
    [Satispay](https://docs.stripe.com/docs/payments/satispay.md) is a payment method.

  - `scalapay`
    Scalapay is a payment method.

  - `sepa_debit`
    [SEPA Direct Debit](https://docs.stripe.com/docs/payments/sepa-debit.md) is used to debit bank accounts within the Single Euro Payments Area (SEPA) region.

  - `sofort`
    [Sofort](https://docs.stripe.com/docs/payments/sofort.md) is a bank redirect payment method used in Europe.

  - `sunbit`
    [Sunbit](https://docs.stripe.com/docs/payments/sunbit.md) is a payment method.

  - `swish`
    [Swish](https://docs.stripe.com/docs/payments/swish.md) is a Swedish wallet payment method where customers authorize the payment in the Swish application.

  - `twint`
    [TWINT](https://docs.stripe.com/docs/payments/twint.md) is a single-use payment method used in Switzerland.

  - `upi`
    [UPI](https://docs.stripe.com/docs/payments/upi.md) is an instant real-time payment system in India.

  - `us_bank_account`
    [ACH Direct Debit](https://docs.stripe.com/docs/payments/ach-direct-debit.md) is used to debit US bank accounts through the Automated Clearing House (ACH) payments system.

  - `wechat_pay`
    [WeChat Pay](https://docs.stripe.com/docs/payments/wechat-pay.md) is a digital wallet payment method based in China.

  - `zip`
    [Zip](https://docs.stripe.com/docs/payments/zip.md) is a Buy now, pay later Payment Method

- [`hooks`](https://docs.stripe.com/api/payment_intents/object.md?query=hooks) (object, nullable)
  Automations to be run during the PaymentIntent lifecycle

- [`last_payment_error`](https://docs.stripe.com/api/payment_intents/object.md?query=last_payment_error) (object, nullable)
  The payment error encountered in the previous PaymentIntent confirmation. It will be cleared if the PaymentIntent is later updated for any reason.

- `latest_charge` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the latest [Charge object](https://docs.stripe.com/docs/api/charges.md) created by this PaymentIntent. This property is `null` until PaymentIntent confirmation is attempted.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- [`managed_payments`](https://docs.stripe.com/api/payment_intents/object.md?query=managed_payments) (object, nullable)
  Settings for Managed Payments.

- `metadata` (map)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Learn more about [storing information in metadata](https://docs.stripe.com/docs/payments/payment-intents/creating-payment-intents.md#storing-information-in-metadata).

- [`next_action`](https://docs.stripe.com/api/payment_intents/object.md?query=next_action) (object, nullable)
  If present, this property tells you what actions you need to take in order for your customer to fulfill a payment using the provided source.

- `on_behalf_of` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  You can specify the settlement merchant as the connected account using the `on_behalf_of` attribute on the charge. See the PaymentIntents [use case for connected accounts](https://docs.stripe.com/payments/connected-accounts.md) for details.

- [`payment_details`](https://docs.stripe.com/api/payment_intents/object.md?query=payment_details) (object, nullable)
  Payment details for this PaymentIntent.

- `payment_method` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the payment method used in this PaymentIntent.

- [`payment_method_configuration_details`](https://docs.stripe.com/api/payment_intents/object.md?query=payment_method_configuration_details) (object, nullable)
  Information about the [payment method configuration](https://docs.stripe.com/docs/api/payment_method_configurations.md) used for this PaymentIntent.

- [`payment_method_options`](https://docs.stripe.com/api/payment_intents/object.md?query=payment_method_options) (object, nullable)
  Payment-method-specific configuration for this PaymentIntent.

- `payment_method_types` (array of strings)
  The list of payment method types (e.g. card) that this PaymentIntent is allowed to use. A comprehensive list of valid payment method types can be found [here](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-type).

- [`presentment_details`](https://docs.stripe.com/api/payment_intents/object.md?query=presentment_details) (object, nullable)
  A hash containing information about the currency presentation to the customer, including the displayed currency and amount used for conversion from the integration currency.

- [`processing`](https://docs.stripe.com/api/payment_intents/object.md?query=processing) (object, nullable)
  If present, this property tells you about the processing state of the payment.

- `receipt_email` (string, nullable)
  Email address that the receipt for the resulting payment will be sent to. If `receipt_email` is specified for a payment in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails).

- `review` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the review associated with this PaymentIntent, if any.

- `setup_future_usage` (enum, nullable)
  Indicates that you intend to make future payments with this PaymentIntent’s payment method.

  If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

  If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

  When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).
Possible enum values:
  - `off_session`
    Use `off_session` if your customer may or may not be present in your checkout flow.

  - `on_session`
    Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

- [`shipping`](https://docs.stripe.com/api/payment_intents/object.md?query=shipping) (object, nullable)
  Shipping information for this PaymentIntent.

- `statement_descriptor` (string, nullable)
  Text that appears on the customer’s statement as the statement descriptor for a non-card charge. This value overrides the account’s default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors.md).

  Setting this value for a card charge returns an error. For card charges, set the [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors.md#dynamic) instead.

- `statement_descriptor_suffix` (string, nullable)
  Provides information about a card charge. Concatenated to the account’s [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors.md#static) to form the complete statement descriptor that appears on the customer’s statement.

- `status` (enum)
  Status of this PaymentIntent, one of `requires_payment_method`, `requires_confirmation`, `requires_action`, `processing`, `requires_capture`, `canceled`, or `succeeded`. Read more about each PaymentIntent [status](https://docs.stripe.com/docs/payments/intents.md#intent-statuses).
Possible enum values:
  - `canceled`
    The PaymentIntent has been canceled.

  - `processing`
    The PaymentIntent is currently being processed.

  - `requires_action`
    The PaymentIntent requires additional action from the customer.

  - `requires_capture`
    The PaymentIntent has been confirmed and requires capture.

  - `requires_confirmation`
    The PaymentIntent requires confirmation.

  - `requires_payment_method`
    The PaymentIntent requires a payment method to be attached.

  - `succeeded`
    The PaymentIntent has succeeded.

- [`transfer_data`](https://docs.stripe.com/api/payment_intents/object.md?query=transfer_data) (object, nullable)
  The data that automatically creates a Transfer after the payment finalizes. Learn more about the [use case for connected accounts](https://docs.stripe.com/docs/payments/connected-accounts.md).

- `transfer_group` (string, nullable)
  A string that identifies the resulting payment as part of a group. Learn more about the [use case for connected accounts](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md).

