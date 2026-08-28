---
title: "The PaymentMethod object"
source: https://docs.stripe.com/api/payment_methods/object.md
path: api/payment_methods/object
---

# The PaymentMethod object

### The PaymentMethod object

```json
{
  "id": "pm_1Q0PsIJvEtkwdCNYMSaVuRz6",
  "object": "payment_method",
  "allow_redisplay": "unspecified",
  "billing_details": {
    "address": {
      "city": null,
      "country": null,
      "line1": null,
      "line2": null,
      "postal_code": null,
      "state": null
    },
    "email": null,
    "name": "John Doe",
    "phone": null
  },
  "created": 1726673582,
  "customer": null,
  "livemode": false,
  "metadata": {},
  "type": "us_bank_account",
  "us_bank_account": {
    "account_holder_type": "individual",
    "account_type": "checking",
    "bank_name": "STRIPE TEST BANK",
    "financial_connections_account": null,
    "fingerprint": "LstWJFsCK7P349Bg",
    "last4": "6789",
    "networks": {
      "preferred": "ach",
      "supported": [
        "ach"
      ]
    },
    "routing_number": "110000000",
    "status_details": {}
  }
}
```

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string, value is "payment_method")
  String representing the object’s type. Objects of the same type share the same value.

- [`acss_debit`](https://docs.stripe.com/api/payment_methods/object.md?query=acss_debit) (object, nullable)
  If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.

- `affirm` (object, nullable)
  If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.

- `afterpay_clearpay` (object, nullable)
  If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.

- `alipay` (object, nullable)
  If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.

- `allow_redisplay` (enum, nullable)
  This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to “unspecified”.
Possible enum values:
  - `always`
    Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

  - `limited`
    Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

  - `unspecified`
    This is the default value for payment methods where `allow_redisplay` wasn’t set.

- `alma` (object, nullable)
  If this is a Alma PaymentMethod, this hash contains details about the Alma payment method.

- `amazon_pay` (object, nullable)
  If this is a AmazonPay PaymentMethod, this hash contains details about the AmazonPay payment method.

- [`au_becs_debit`](https://docs.stripe.com/api/payment_methods/object.md?query=au_becs_debit) (object, nullable)
  If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.

- [`bacs_debit`](https://docs.stripe.com/api/payment_methods/object.md?query=bacs_debit) (object, nullable)
  If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.

- `bancontact` (object, nullable)
  If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.

- `billie` (object, nullable)
  If this is a `billie` PaymentMethod, this hash contains details about the Billie payment method.

- [`billing_details`](https://docs.stripe.com/api/payment_methods/object.md?query=billing_details) (object)
  Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.

- [`bizum`](https://docs.stripe.com/api/payment_methods/object.md?query=bizum) (object, nullable)
  If this is a `bizum` PaymentMethod, this hash contains details about the Bizum payment method.

- [`blik`](https://docs.stripe.com/api/payment_methods/object.md?query=blik) (object, nullable)
  If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.

- [`boleto`](https://docs.stripe.com/api/payment_methods/object.md?query=boleto) (object, nullable)
  If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.

- [`card`](https://docs.stripe.com/api/payment_methods/object.md?query=card) (object, nullable)
  If this is a `card` PaymentMethod, this hash contains the user’s card details.

- [`card_present`](https://docs.stripe.com/api/payment_methods/object.md?query=card_present) (object, nullable)
  If this is a `card_present` PaymentMethod, this hash contains details about the Card Present payment method.

- [`cashapp`](https://docs.stripe.com/api/payment_methods/object.md?query=cashapp) (object, nullable)
  If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `crypto` (object, nullable)
  If this is a Crypto PaymentMethod, this hash contains details about the Crypto payment method.

- [`custom`](https://docs.stripe.com/api/payment_methods/object.md?query=custom) (object, nullable)
  If this is a `custom` PaymentMethod, this hash contains details about the Custom payment method.

- `customer` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer.

- `customer_balance` (object, nullable)
  If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.

- [`eps`](https://docs.stripe.com/api/payment_methods/object.md?query=eps) (object, nullable)
  If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.

- [`fpx`](https://docs.stripe.com/api/payment_methods/object.md?query=fpx) (object, nullable)
  If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.

- `giropay` (object, nullable)
  If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.

- `grabpay` (object, nullable)
  If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.

- [`ideal`](https://docs.stripe.com/api/payment_methods/object.md?query=ideal) (object, nullable)
  If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.

- [`interac_present`](https://docs.stripe.com/api/payment_methods/object.md?query=interac_present) (object, nullable)
  If this is an `interac_present` PaymentMethod, this hash contains details about the Interac Present payment method.

- `kakao_pay` (object, nullable)
  If this is a `kakao_pay` PaymentMethod, this hash contains details about the Kakao Pay payment method.

- [`klarna`](https://docs.stripe.com/api/payment_methods/object.md?query=klarna) (object, nullable)
  If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.

- `konbini` (object, nullable)
  If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.

- [`kr_card`](https://docs.stripe.com/api/payment_methods/object.md?query=kr_card) (object, nullable)
  If this is a `kr_card` PaymentMethod, this hash contains details about the Korean Card payment method.

- [`link`](https://docs.stripe.com/api/payment_methods/object.md?query=link) (object, nullable)
  If this is an `Link` PaymentMethod, this hash contains details about the Link payment method (Link is also known as Onelink in the UK).

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `mb_way` (object, nullable)
  If this is a MB WAY PaymentMethod, this hash contains details about the MB WAY payment method.

- `metadata` (map, nullable)
  Set of [key-value pairs](https://docs.stripe.com/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `mobilepay` (object, nullable)
  If this is a `mobilepay` PaymentMethod, this hash contains details about the MobilePay payment method.

- `multibanco` (object, nullable)
  If this is a `multibanco` PaymentMethod, this hash contains details about the Multibanco payment method.

- [`naver_pay`](https://docs.stripe.com/api/payment_methods/object.md?query=naver_pay) (object, nullable)
  If this is a `naver_pay` PaymentMethod, this hash contains details about the Naver Pay payment method.

- [`nz_bank_account`](https://docs.stripe.com/api/payment_methods/object.md?query=nz_bank_account) (object, nullable)
  If this is an nz_bank_account PaymentMethod, this hash contains details about the nz_bank_account payment method.

- `oxxo` (object, nullable)
  If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.

- [`p24`](https://docs.stripe.com/api/payment_methods/object.md?query=p24) (object, nullable)
  If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.

- `pay_by_bank` (object, nullable)
  If this is a `pay_by_bank` PaymentMethod, this hash contains details about the PayByBank payment method.

- `payco` (object, nullable)
  If this is a `payco` PaymentMethod, this hash contains details about the PAYCO payment method.

- `paynow` (object, nullable)
  If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.

- [`paypal`](https://docs.stripe.com/api/payment_methods/object.md?query=paypal) (object, nullable)
  If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.

- `paypay` (object, nullable)
  If this is a `paypay` PaymentMethod, this hash contains details about the PayPay payment method.

- [`payto`](https://docs.stripe.com/api/payment_methods/object.md?query=payto) (object, nullable)
  If this is a `payto` PaymentMethod, this hash contains details about the PayTo payment method.

- [`pix`](https://docs.stripe.com/api/payment_methods/object.md?query=pix) (object, nullable)
  If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.

- `promptpay` (object, nullable)
  If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.

- [`radar_options`](https://docs.stripe.com/api/payment_methods/object.md?query=radar_options) (object, nullable)
  Options to configure Radar. See [Radar Session](https://docs.stripe.com/radar/radar-session.md) for more information.

- `revolut_pay` (object, nullable)
  If this is a `revolut_pay` PaymentMethod, this hash contains details about the Revolut Pay payment method.

- `samsung_pay` (object, nullable)
  If this is a `samsung_pay` PaymentMethod, this hash contains details about the SamsungPay payment method.

- `satispay` (object, nullable)
  If this is a `satispay` PaymentMethod, this hash contains details about the Satispay payment method.

- `scalapay` (object, nullable)
  If this is a Scalapay PaymentMethod, this hash contains details about the Scalapay payment method.

- [`sepa_debit`](https://docs.stripe.com/api/payment_methods/object.md?query=sepa_debit) (object, nullable)
  If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.

- [`sofort`](https://docs.stripe.com/api/payment_methods/object.md?query=sofort) (object, nullable)
  If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.

- `sunbit` (object, nullable)
  If this is a `sunbit` PaymentMethod, this hash contains details about the Sunbit payment method.

- `swish` (object, nullable)
  If this is a `swish` PaymentMethod, this hash contains details about the Swish payment method.

- `twint` (object, nullable)
  If this is a TWINT PaymentMethod, this hash contains details about the TWINT payment method.

- `type` (enum)
  The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
Possible enum values:
  - `acss_debit`
    [Pre-authorized debit payments](https://docs.stripe.com/payments/acss-debit.md) are used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).

  - `affirm`
    [Affirm](https://docs.stripe.com/payments/affirm.md) is a buy now, pay later payment method in the US.

  - `afterpay_clearpay`
    [Afterpay / Clearpay](https://docs.stripe.com/payments/afterpay-clearpay.md) is a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.

  - `alipay`
    [Alipay](https://docs.stripe.com/payments/alipay.md) is a digital wallet payment method used in China.

  - `alma`
    [Alma](https://docs.stripe.com/payments/alma.md) is a Buy Now, Pay Later payment method that lets customers pay in 2, 3, or 4 installments.

  - `amazon_pay`
    [Amazon Pay](https://docs.stripe.com/payments/amazon-pay.md) is a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.

  - `au_becs_debit`
    [BECS Direct Debit](https://docs.stripe.com/payments/au-becs-debit.md) is used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).

  - `bacs_debit`
    [Bacs Direct Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit.md) is used to debit UK bank accounts.

  - `bancontact`
    [Bancontact](https://docs.stripe.com/payments/bancontact.md) is a bank redirect payment method used in Belgium.

  - `billie`
    [Billie](https://docs.stripe.com/payments/billie.md) is a payment method.

  - `bizum`
    [Bizum](https://docs.stripe.com/payments/bizum.md) is a payment method.

  - `blik`
    [BLIK](https://docs.stripe.com/payments/blik.md) is a single-use payment method common in Poland.

  - `boleto`
    [Boleto](https://docs.stripe.com/payments/boleto.md) is a voucher-based payment method used in Brazil.

  - `card`
    [Card payments](https://docs.stripe.com/payments/payment-methods/overview.md#cards) are supported through many networks, card brands, and select Link funding sources (Link is also known as Onelink in the UK).

  - `card_present`
    [Stripe Terminal](https://docs.stripe.com/terminal/payments/collect-card-payment.md) is used to collect in-person card payments.

  - `cashapp`
    [Cash App Pay](https://docs.stripe.com/payments/cash-app-pay.md) enables customers to frictionlessly authenticate payments in the Cash App using their stored balance or linked card.

  - `crypto`
    [Stablecoin payments](https://docs.stripe.com/payments/stablecoin-payments.md) enable customers to pay in stablecoins like USDC from 100s of wallets including Phantom and Metamask.

  - `custom`
    Custom payment methods are user-defined payment methods that Stripe doesn’t process. You can’t use them in PaymentIntents or SetupIntents.

  - `customer_balance`
    Uses a customer’s [cash balance](https://docs.stripe.com/payments/customer-balance.md) for the payment.

  - `eps`
    [EPS](https://docs.stripe.com/payments/eps.md) is an Austria-based bank redirect payment method.

  - `fpx`
    [FPX](https://docs.stripe.com/payments/fpx.md) is a Malaysia-based bank redirect payment method.

  - `giropay`
    [giropay](https://docs.stripe.com/payments/giropay.md) is a German bank redirect payment method.

  - `grabpay`
    [GrabPay](https://docs.stripe.com/payments/grabpay.md) is a digital wallet payment method used in Southeast Asia.

  - `ideal`
    [iDEAL](https://docs.stripe.com/payments/ideal.md) is a Netherlands-based bank redirect payment method.

  - `interac_present`
    [Stripe Terminal](https://docs.stripe.com/terminal/payments/collect-card-payment.md) accepts [Interac](https://docs.stripe.com/terminal/payments/regional.md?integration-country=CA#interac-payments) debit cards for in-person payments in Canada.

  - `kakao_pay`
    [Kakao Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `klarna`
    [Klarna](https://docs.stripe.com/payments/klarna.md) is a global buy now, pay later payment method.

  - `konbini`
    [Konbini](https://docs.stripe.com/payments/konbini.md) is a cash-based voucher payment method used in Japan.

  - `kr_card`
    [Korean cards](https://docs.stripe.com/payments/kr-card/accept-a-payment.md) enables customers to accept local credit and debit cards in South Korea.

  - `link`
    [Link (also known as Onelink in the UK)](https://docs.stripe.com/payments/link.md) allows customers to pay with their saved payment details.

  - `mb_way`
    MB WAY is a payment method.

  - `mobilepay`
    [MobilePay](https://docs.stripe.com/payments/mobilepay.md) is a Nordic card-passthrough wallet payment method where customers authorize the payment in the MobilePay application.

  - `multibanco`
    [Multibanco](https://docs.stripe.com/payments/multibanco.md) is a voucher payment method

  - `naver_pay`
    [Naver Pay](https://docs.stripe.com/payments/naver-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `nz_bank_account`
    [New Zealand BECS Direct Debit](https://docs.stripe.com/payments/nz-bank-account.md) is used to debit New Zealand bank accounts through the Bulk Electronic Clearing System (BECS).

  - `oxxo`
    [OXXO](https://docs.stripe.com/payments/oxxo.md) is a cash-based voucher payment method used in Mexico.

  - `p24`
    [Przelewy24](https://docs.stripe.com/payments/p24.md) is a bank redirect payment method used in Poland.

  - `pay_by_bank`
    [Pay By Bank](https://docs.stripe.com/payments/pay-by-bank.md) is an open banking payment method in the UK.

  - `payco`
    [PAYCO](https://docs.stripe.com/payments/payco/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `paynow`
    [PayNow](https://docs.stripe.com/payments/paynow.md) is a QR code payment method used in Singapore.

  - `paypal`
    [PayPal](https://docs.stripe.com/payments/paypal.md) is an online wallet and redirect payment method commonly used in Europe.

  - `paypay`
    [PayPay](https://docs.stripe.com/payments/paypay.md) is a payment method.

  - `payto`
    [PayTo](https://docs.stripe.com/payments/payto.md) is a real time payment method

  - `pix`
    [Pix](https://docs.stripe.com/payments/pix.md) is an instant bank transfer payment method in Brazil.

  - `promptpay`
    [PromptPay](https://docs.stripe.com/payments/promptpay.md) is an instant funds transfer service popular in Thailand.

  - `revolut_pay`
    [Revolut Pay](https://docs.stripe.com/payments/revolut-pay.md) is a digital wallet payment method used in the United Kingdom.

  - `samsung_pay`
    [Samsung Pay](https://docs.stripe.com/payments/samsung-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `satispay`
    [Satispay](https://docs.stripe.com/payments/satispay.md) is a payment method.

  - `scalapay`
    Scalapay is a payment method.

  - `sepa_debit`
    [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit.md) is used to debit bank accounts within the Single Euro Payments Area (SEPA) region.

  - `sofort`
    [Sofort](https://docs.stripe.com/payments/sofort.md) is a bank redirect payment method used in Europe.

  - `sunbit`
    [Sunbit](https://docs.stripe.com/payments/sunbit.md) is a payment method.

  - `swish`
    [Swish](https://docs.stripe.com/payments/swish.md) is a Swedish wallet payment method where customers authorize the payment in the Swish application.

  - `twint`
    [TWINT](https://docs.stripe.com/payments/twint.md) is a single-use payment method used in Switzerland.

  - `upi`
    [UPI](https://docs.stripe.com/payments/upi.md) is an instant real-time payment system in India.

  - `us_bank_account`
    [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit.md) is used to debit US bank accounts through the Automated Clearing House (ACH) payments system.

  - `wechat_pay`
    [WeChat Pay](https://docs.stripe.com/payments/wechat-pay.md) is a digital wallet payment method based in China.

  - `zip`
    [Zip](https://docs.stripe.com/payments/zip.md) is a Buy now, pay later Payment Method

- [`upi`](https://docs.stripe.com/api/payment_methods/object.md?query=upi) (object, nullable)
  If this is a `upi` PaymentMethod, this hash contains details about the UPI payment method.

- [`us_bank_account`](https://docs.stripe.com/api/payment_methods/object.md?query=us_bank_account) (object, nullable)
  If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.

- `wechat_pay` (object, nullable)
  If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.

- `zip` (object, nullable)
  If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method.

