---
title: "the migration process"
source: https://docs.stripe.com/get-started/data-migrations/pan-import.md
path: get-started/data-migrations/pan-import
---

# Request a payments data import

Securely import sensitive payments data.

Stripe enables you to retain your existing customer and payment data when you migrate to Stripe. We work with your team and current payment provider, as needed, to securely migrate your information.

This process allows you to accept and charge new customers on Stripe and continue charging your existing customers with your current processor until the migration is complete. Your customers incur no downtime. After the migration process completes, you can process all payments on Stripe.

This guide describes how to migrate to Stripe from another payment processor or a custom payment solution. You’ll also build a Stripe integration that you can test in a sandbox before you accept real payments. If you have any questions about the migration process or integrating with Stripe, see [support](https://support.stripe.com/topics/migration). If you haven’t already, [review Stripe pricing](https://stripe.com/pricing).

If you have to transfer sensitive payment information, you must complete a [Data migration request](https://support.stripe.com/questions/request-a-data-migration) before you migrate. We can help you do so in a secure and *PCI-compliant* (Any party involved in processing, transmitting, or storing credit card data must comply with the rules specified in the Payment Card Industry (PCI) Data Security Standards. PCI compliance is a shared responsibility and applies to both Stripe and your business) way.

## Review Stripe integration features

Stripe simplifies your security requirements so that your customers don’t have to leave your site to complete a payment. We do this through a combination of client-side and server-side steps:

1. From your website running in the customer’s browser, Stripe securely collects their payment details.
2. Stripe responds with a representative token.
3. The browser submits the token to your server, along with any other form data.
4. Your server-side code uses that token in an API request (for example, when [creating a PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md)).

This approach simplifies your website’s checkout flow, while sensitive payment information never touches your server. This allows you to operate in accordance with [PCI-compliance](https://docs.stripe.com/security/guide.md#validating-pci-compliance) regulations, which can save you time and provide financial benefits.
![Stripe payment process flow](https://b.stripecdn.com/docs-statics-srv/assets/charge-workflow.6d5c025c1b1e62a53803f1908104e0a8.png)

The Stripe payment process flow

Compared to other payment processors, a Stripe integration can differ in the following ways:

- Your customer never leaves your website.
- Token creation isn’t tied to a specific product or amount.
- It doesn’t require you to create of a client-side key on-demand. You use a set, publishable [API key](https://docs.stripe.com/keys.md) instead.

## Create a Stripe account

Before integrating with Stripe, you must create a Stripe account.

1. [Create an account](https://dashboard.stripe.com/register) by entering your email address, full name, country, and creating a password.
2. Fill out your business profile.
3. In the Dashboard, click **Verify your email**. Stripe sends a verification email to your email address.
4. Verify your email address.

Coding agents should install the Stripe CLI (`npm i -g @stripe/cli`) and run the command `stripe sandbox create --help` to provision an anonymous Stripe sandbox with working API keys. No account registration required.

## Build a Stripe integration

For all new customer tokens (not imported), implement the following:

1. Create [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) objects and attach them to [Customer](https://docs.stripe.com/api/customers/object.md) objects to save payment information.

2. Collect and tokenize customer card information with one of our recommended [payments integrations](https://docs.stripe.com/payments/online-payments.md#compare-features-and-availability). Build your Stripe integration before you ask your payment processor to transfer data to Stripe. For most startups, we recommend building an [Embedded Checkout](https://docs.stripe.com/payments/checkout/how-checkout-works.md) integration, a payment form you embed in your website.

   To set up this integration, see the [Embedded Checkout Quickstart](https://docs.stripe.com/checkout/embedded/quickstart.md) and accept payments for one-time and subscription payments (if applicable).

3. [Create PaymentIntents](https://docs.stripe.com/api/payment_intents/create.md) to charge these new customers.

Using this approach, you can accept payments from your new customers on Stripe without impacting your current customers in your existing processor during the migration process.

### Integration considerations

Designing your integration before you ask your payment processor to transfer data to Stripe is the most efficient way to handle imported data. Some actions you can take before requesting an import include:

- [Remap customer records](https://docs.stripe.com/get-started/data-migrations/pan-import.md#remap-customer-ids)
- [Protect updates to saved payment methods during the migration](https://docs.stripe.com/get-started/data-migrations/pan-import.md#handle-card-updates).
- Enable all [optimizations](https://docs.stripe.com/payments/analytics/optimization.md), such as Adaptive Acceptance, card account updater (CAU), and network tokens.

## Optional: Map customers to Stripe IDs

If you prefer, you can configure your integration to [import the payment method data from prior records into existing Stripe Customer objects](https://docs.stripe.com/get-started/data-migrations/map-payment-data.md). Doing so prevents the migration from creating a new (possibly duplicate) customer in your Stripe account for each unique customer ID in the files we receive from your prior processor.

After migrating, you might still have to update some records to correspond with the new Stripe [Customer](https://docs.stripe.com/api/customers.md) identifier, if:

- You created the Stripe `Customer` before migration, then we imported the payment information to update this customer record.
- We imported the payment information as a new customer record.

For example, customer jenny.rosen@example.com might have ID `42` in your database, corresponding to ID `1893` in your previous processor’s system, but is ID `cus_12345` in your Stripe account. In this case, you must now map your ID `42` to the Stripe ID `cus_12345` in your database. Stripe provides a post-import [mapping file](https://docs.stripe.com/get-started/data-migrations/pan-import.md#update-integration) to help you identify required remapping.

## Optional: Protect updates to saved payment methods

If customers update their payment information with your previous processor in the window between transferring the data and completing the import, those changes are lost.

Update your site’s process for handling updates to saved payments to prevent errors or billing issues for your customers. This includes preparations to perform a self-migration for any customer without a stored Stripe `Customer` ID:

1. Create a new [Customer object](https://docs.stripe.com/api/customers/object.md) in Stripe for your customer.
2. Attach the payment method to the `Customer` object.
3. If necessary, [migrate subscriptions](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit.md).

After migration completes, Stripe [automatically handles card-triggered updates](https://stripe.com/blog/smarter-saved-cards), such as expiration date changes.

## Test your Stripe integration

To test your embedded payment form integration:

1. Create an embedded Checkout Session and mount the payment form on your page.
2. Fill out the payment details with a method from the table below.
   - Enter any future date for card expiry.
   - Enter any 3-digit number for CVC.
   - Enter any billing postal code.
3. Click **Pay**. You’re redirected to your `return_url`.
4. Go to the Dashboard and look for the payment on the [Transactions page](https://dashboard.stripe.com/test/payments?status%5B0%5D=successful). If your payment succeeded, you’ll see it in that list.
5. Click your payment to see more details, like a Checkout summary with billing information and the list of purchased items. You can use this information to fulfill the order.

Learn more about [testing your integration](https://docs.stripe.com/testing.md).

#### Cards

| Card number | Scenario | How to test |
| --- | --- | --- |
| 4242424242424242 | The card payment succeeds and doesn’t require authentication. | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000002500003155 | The card payment requires *authentication* (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase). | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000000000009995 | The card is declined with a decline code like `insufficient_funds`. | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 6205500000000000004 | The UnionPay card has a variable length of 13-19 digits. | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |

#### Wallets

| Payment method | Scenario | How to test |
| --- | --- | --- |
| Alipay | Your customer successfully pays with a redirect-based and [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. | Choose any redirect-based payment method, fill out the required details, and confirm the payment. Then click **Complete test payment** on the redirect page. |

#### Bank redirects

| Payment method | Scenario | How to test |
| --- | --- | --- |
| Bancontact, EPS, iDEAL, and Przelewy24 | Your customer fails to authenticate on the redirect page for a redirect-based and immediate notification payment method. | Choose any redirect-based payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page. |
| Pay by Bank | Your customer successfully pays with a redirect-based and [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. | Choose the payment method, fill out the required details, and confirm the payment. Then click **Complete test payment** on the redirect page. |
| Pay by Bank | Your customer fails to authenticate on the redirect page for a redirect-based and delayed notification payment method. | Choose the payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page. |
| BLIK | BLIK payments fail in a variety of ways—immediate failures (for example, the code is expired or invalid), delayed errors (the bank declines) or timeouts (the customer didn’t respond in time). | Use email patterns to [simulate the different failures.](https://docs.stripe.com/payments/blik/accept-a-payment.md#simulate-failures) |

#### Bank debits

| Payment method | Scenario | How to test |
| --- | --- | --- |
| BECS Direct Debit | Your customer successfully pays with BECS Direct Debit. | Fill out the form using the account number `900123456` and BSB `000000`. The confirmed PaymentIntent initially transitions to `processing`, then transitions to the `succeeded` status 3 minutes later. |
| BECS Direct Debit | Your customer’s payment fails with an `account_closed` error code. | Fill out the form using the account number `111111113` and BSB `000000`. |
| SEPA Direct Debit | Your customer successfully pays with SEPA Direct Debit. | Fill out the form using the account number `AT321904300235473204`. The confirmed PaymentIntent initially transitions to processing, then transitions to the succeeded status three minutes later. |
| SEPA Direct Debit | Your customer’s payment intent status transitions from `processing` to `requires_payment_method`. | Fill out the form using the account number `AT861904300235473202`. |

#### Vouchers

| Payment method | Scenario | How to test |
| --- | --- | --- |
| Boleto, OXXO | Your customer pays with a Boleto or OXXO voucher. | Select Boleto or OXXO as the payment method and submit the payment. Close the dialog after it appears. |

See [Testing](https://docs.stripe.com/testing.md) for additional information to test your integration.

## Request and confirm the migration details

1. After you complete your integration and are ready to process payments on Stripe, [request your payment data from your previous processor](https://support.stripe.com/questions/request-data-from-a-current-processor-for-a-data-import-to-stripe). Many processors require the account owner to request a data transfer.
2. Log in to your Stripe account to submit the [migration request form](https://support.stripe.com/questions/request-a-data-migration) to request your import migration.
3. Engage with Stripe through the authenticated email thread we create upon receipt of your migration request.

> Never send sensitive credit card details or customer information directly to Stripe. If you have this data, let us know in your migration request form so we can help you securely transfer your data.

Stripe can import your customer billing address information and payment details. You can also:

- [Migrate specific payment types](https://docs.stripe.com/get-started/data-migrations/payment-method-imports.md)
- [Migrate subscriptions](https://docs.stripe.com/billing/subscriptions/migrate-subscriptions.md) or import them using the [Billing Migration Toolkit](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit.md).

Your previous processor might take a few days or several weeks to transfer the final data to Stripe. Allow for this transition time in your migration plan. After your previous processor transfers your data, Stripe reviews the data and identifies any problems with the import. We work with you and your previous processor to correct any issues. We then share a summary of the import for your final review and approval.

After your approval, Stripe imports the data into your account. We create a [Customer](https://docs.stripe.com/api.md#customer_object) for each unique customer in the transferred data file, and create and attach the customer’s cards as [Card](https://docs.stripe.com/api.md#card_object) or [Payment Method](https://docs.stripe.com/api/payment_methods/object.md) objects. If the transferred data specifies the customer’s default card, we set that as the customer’s [default payment method](https://docs.stripe.com/api.md#customer_object-default_source) for charges and [subscription](https://docs.stripe.com/api/subscriptions/create.md) payments.

If your Stripe account has accumulated significant customer records by the time you migrate, consider [mapping import data into existing Stripe Customer objects](https://docs.stripe.com/get-started/data-migrations/map-payment-data.md) instead of creating new `Customer` objects.

Stripe typically imports data within 10 business days of receiving the correct data from your previous processor, along with any supplementary data files you want to share with our team.

## Update your integration

After completing the import, Stripe sends you a choice of a CSV or JSON file that shows the mapped relationship between your current processor’s IDs and the imported Stripe object IDs. Parse this mapping file and update your database accordingly. Make sure your integration [handled any card updates](https://docs.stripe.com/get-started/data-migrations/pan-import.md#handle-card-updates) that took place during the transition.

### Post import mapping file

After you update your integration with this mapping file, you can begin charging all of your customers on Stripe.

```
{
  "1893": {
    "cards": {
      "2600": {
        "id": "card_2222222222",
        "fingerprint": "x9yW1WE4nLvl6zjg",
        "last4": "4242",
        "exp_month": 1,
        "exp_year": 2020,
        "brand": "Visa"
      },
      "3520": {
        "id": "card_3333333333",
        "fingerprint": "nZnMWbJBurX3VHIN",
        "last4": "0341",
        "exp_month": 6,
        "exp_year": 2021,
        "brand": "Mastercard"
      }
    },
    "id": "cus_abc123def456"
  }
}
```

The example JSON mapping above shows:

- Imported customer ID 1893 as a new Stripe `Customer` with ID `cus_abc123def456`.
- Imported customer card ID 2600 as a new Stripe `Card` with ID `card_2222222222`.
- Imported customer card ID 3520 as a new Stripe `Card` with ID `card_3333333333`.

Stripe can import card data as [PaymentMethods](https://docs.stripe.com/api.md#payment_method_object) instead of `Card` objects if you specify it in your migration request. The following examples show the mapping files for different types of payment information imports.

#### Card as card_ CSV

```csv
old_customer_id,customer_id,old_card_id,card_id,card_fingerprint,card_last4,card_exp_month,card_exp_year,card_brand
old_cus_100,cus_abc123def456,old_src_100,card_2222222222,x9yW1WE4nLvl6zjg,4242,09,2024,Visa
```

#### Card as PaymentMethod (pm_) CSV

```
old_id,source_old_id,created_customer,source_new_id,card_fingerprint,card_last4,card_exp_month,card_exp_year,card_brand
old_cus_100,old_src_100,cus_abc123def456,pm_2222222222,x9yW1WE4nLvl6zjg,4242,09,2024,Visa
```

#### ACH as bank account (ba_) CSV

```
old_customer_id,customer_id,old_bank_account_id,bank_account_id,bank_account_fingerprint,bank_account_last4
old_cus_100,cus_abc123def456,old_src_100,ba_2222222222,x9yW1WE4nLvl6zjg,4242
```

#### ACH as PaymentMethod (pm_) CSV

```
old_customer_id,customer_id,old_bank_account_id,bank_account_id,bank_account_fingerprint,bank_account_last4
old_cus_100,cus_abc123def456,old_src_100,pm_2222222222,x9yW1WE4nLvl6zjg,4242
```

#### BACs as PaymentMethod (pm_) CSV

```
old_id,source_old_id,created_customer,source_new_id,mandate_id
old_cus_100,old_src_100,cus_abc123def456,pm_2222222222,mandate_1MvojA2eZvKYlo2CvqTABjZs
```

#### SEPA as PaymentMethod (pm_) CSV

```
old_customer_id,customer_id,old_source_id,source_id,type,bank_code,branch_code,country,fingerprint,last4,mandate_reference,mandate_url,mandate_id
old_cus_100,cus_abc123def456,old_src_100,pm_2222222222,sepa_debit,1111,000,DE,x9yW1WE4nLvl6zjg,4242,ref_000,example.com,mandate_1MvojA2eZvKYlo2CvqTABjZs
```

## Monitor your imported payments

After migrating, monitor your payments performance to make sure the acceptance rate for imported payment data matches your expectations.

Payment acceptance (or issuer authorization rate) is the percentage of transactions that issuers successfully authorize out of all transactions submitted for payment. This metric excludes blocked transactions (for example due to Radar rules) because those are never submitted for authorization.

In both your general approach and post migration, align your [payment authorization optimization](https://stripe.com/guides/optimizing-authorization-rates) goals with your business objectives. For example, a digital goods business with low unit cost might set their risk level to block fewer payments. Consider the potential effects:

- Increased conversion rates due to less friction.
- Increased exposure to fraud due to riskier payments getting through.
- Lower raw issuer authorization rates due to fraud model blocks by the issuer.

Make sure you provide accurate data (such as cardholder name, billing address, and email). Reflecting the cardholder’s intent maximizes successful authorization potential.

### Identify cards on file

Payment data migrations involve *cards on file* (cards saved for a future [merchant-initiated or off session](https://support.stripe.com/questions/what-is-the-difference-between-on-session-and-off-session-and-why-is-it-important) payment for the same customer). Make sure you store imported payment data and label payments using those cards on file with the correct `off_session` parameter. If you improperly identify cards on file:

- Issuers who can’t confirm a cardholder’s consent to future or recurring payments might [decline](https://docs.stripe.com/declines.md#issuer-declines) them.
- The payment data might be ineligible for certain Stripe optimization products such as Card account updater (CAU) and Network tokens (NT).

### Monitor decline reasons for optimization opportunities

Following your migration, your [issuer decline reasons](https://docs.stripe.com/declines/codes.md) can help you identify whether migrated payment data is transacting as expected. Spikes in certain types of declines might benefit from the following optimization products:

- Card account updater: Stripe partnerships with card networks allow us to automatically obtain updates for expired or replaced cards in both real time and the background.
- **Automatic retries** (Dunning): Use caution because retrying numerous cards (such as after a migration) can appear suspicious to issuers. If you use Stripe [Smart retries](https://stripe.com/guides/optimizing-authorization-rates#smart-retries) for your billing payments, our AI model analyzes decline code, payment method updates, and bank risk threshold activity to retry recurring revenue payments more strategically.
- [Network tokens](https://stripe.com/guides/optimizing-authorization-rates#network-tokens): Replace a specific payment account number (PAN) with a secure token from the card network to make sure PAN updates (like renewal or replacement) automatically reflect in the token.
- [Adaptive acceptance](https://stripe.com/guides/optimizing-authorization-rates#adaptive-acceptance): Stripe uses AI to assess the effect of minor adjustments (such as formatting) to an authorization request in real time, then refines the payment retry before returning the original decline to the customer.
- **Customer outreach**: Asking your customer to log in and re-enter or re-verify their payment details often re-establishes your business’s trustworthiness with the customer and the payment providers. Consider notifying customers through channels other than email, such as text messages or in-app notifications.

The following table shows which optimization products offer improvement for a variety of decline reasons.

| Decline codes might include | Migration effect | Do | Don’t |
| --- | --- | --- | --- |
| `incorrect_number`

`invalid_number`

`expired_card` | Updates to card data during the natural migration lag can cause saved card data to be out of date. | - Card account updater
- Network tokens
- Adaptive acceptance
- Contact customer | Retry |
| `generic_decline`

`do_not_honor` | Changes to your statement descriptor or other identification markers might trigger issuer risk models or confuse your customer. | - Retry
- Network tokens
- Adaptive acceptance
- Contact customer | Card account updater |
| `transaction_not_allowed`

`try_again_later`

`authentication_required`

`incorrect_cvc` | Some migrated payment data might be missing initial card validation details, such as the network token or original transaction ID. | - Card account updater
- Retry
- Adaptive acceptance
- Contact customer | Network tokens |
| `lost_card`

`stolen_card`

`invalid_account`

`pickup_card`

`card_not_supported` | Customers might report lost or stolen cards during a migration lag. Look out for a special CONTAC event in conjunction with these declines. | - Network tokens
- Contact customer | - CAU
- Retry1
- Adaptive acceptance |

1 Retrying lost or stolen payment data can appear suspicious to card issuers.

## Optional: Migrate subscriptions

Migrations that involve subscriptions typically involve these stages:

1. Set up your [billing integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md).

2. [Migrate your customer and payment processor information](https://docs.stripe.com/get-started/data-migrations/pan-import.md#request-migration).

3. [Import your subscriptions to Stripe Billing](https://docs.stripe.com/billing/subscriptions/migrate-subscriptions.md).

   You can import existing subscriptions by using either the [Subscriptions API](https://docs.stripe.com/billing/subscriptions/import-subscriptions.md) or the Dashboard’s [Billing migration toolkit](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit.md).

4. After leaving your payment processor, confirm they canceled all automatic billing of your customers.

## Migration PGP key

If you’re unfamiliar with PGP, see [GPG](http://gnupg.org/) and start by [importing a public key](http://www.gnupg.org/gph/en/manual.html#AEN84). After you familiarize yourself with the basics of PGP, use the following PGP key to encrypt sensitive data (such as credit card information) for PCI-compliant migration.

### PGP migration key

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
BJk0jHCnxygA+4LXkoqa/VkgZaYsaXE=
=5EIE
-----END PGP PUBLIC KEY BLOCK-----
```

This creates **FILENAME.gpg** with the following information:

- Key ID: `9C78B7620C1E99AD`
- Key type: `RSA`
- Key size: `4096 bits`
- Fingerprint: `AEBF 7C48 38C4 4D2F DC99 A3F9 9C78 B762 0C1E 99AD`
- User ID: `Stripe Import Key (PCI) <support-migrations@stripe.com>`

After you import our key, you can encrypt files to send by running this command in your command line prompt:

`gpg --encrypt --recipient 9C78B7620C1E99AD FILENAME`

For more details on providing encrypted data to Stripe, see [Upload supplementary data](https://docs.stripe.com/get-started/data-migrations/supplementary-data.md).

## See also

- [Payments optimizations](https://docs.stripe.com/payments/analytics/optimization.md)
- [Multiple accounts](https://docs.stripe.com/get-started/account/multiple-accounts.md)
- [Account checklist](https://docs.stripe.com/get-started/account/checklist.md)

