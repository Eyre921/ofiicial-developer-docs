---
title: "File taxes outside the US"
source: https://docs.stripe.com/tax/file-with-stripe-outside-us.md
path: tax/file-with-stripe-outside-us
---

# File taxes outside the US

Use Stripe Tax to prepare and file supported tax returns outside the US.

## Availability

Automated filing outside the US is available for the following registrations:

- **Canada Simplified GST/HST**: Simplified goods and services tax and harmonized sales tax (GST/HST) for eligible non-resident businesses.
- **EU Non-Union OSS**: Non-Union One Stop Shop (OSS) VAT through Ireland for eligible businesses that aren’t established in the European Union.

This guide doesn’t cover other Canadian registrations, including normal GST/HST and provincial sales taxes. It also doesn’t cover other EU filing schemes, including Union OSS and Import One Stop Shop (IOSS). Learn about other [tax filing options](https://docs.stripe.com/tax/filing.md).

## Before you begin

To set up filing, you must:

- **Set up Stripe Tax**: To enable calculations and collection with Stripe Tax, see [Set up Stripe Tax](https://docs.stripe.com/tax/set-up.md). Make sure you’ve added your tax registrations. If you haven’t registered with the taxing authorities and you sell remotely to Canada or the EU, [Stripe can register with local tax authorities on your behalf](https://docs.stripe.com/tax/use-stripe-to-register/outside-united-states.md).
- **Sign up for Tax Complete**: Check your plan under [Stripe plans](https://dashboard.stripe.com/settings/plans) in the Dashboard.
- **Gather relevant company information**: To sign up for automated filing, you’ll need to provide information about your business.

### Canada simplified GST/HST filing

Gather your simplified GST/HST business number, the registration effective date provided by the Canada Revenue Agency (CRA), your four-digit GST/HST NETFILE access code, and the filing currency for the reporting period.

You normally file simplified GST/HST returns in CAD. The CRA can authorize an eligible non-resident business to file and pay in USD or EUR. Don’t select a foreign filing currency unless the CRA has approved it for the relevant reporting periods. Learn how to [file a simplified GST/HST return](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/file-return.html).

### EU Non-Union OSS filing through Ireland

Gather your Irish Non-Union OSS identification number, registration effective date, and registered business details. Stripe might request additional information or authorization.

An OSS identification number isn’t a general Irish VAT number. Filing through Ireland covers eligible Non-Union OSS supplies to non-taxable persons across EU member states. It doesn’t replace local VAT registrations or returns for activities outside the scheme. Learn about the [Irish Non-Union OSS scheme](https://www.revenue.ie/en/vat/vat-ecommerce/non-union-scheme/index.aspx).

## Set up filing

In the Dashboard, open [Tax locations](https://dashboard.stripe.com/tax/locations), select a supported registration, and start the filing setup. Review your business and registration information, provide the required filing details, and submit your application.

Stripe reviews your application and emails you if it requires more information. Filing begins only after Stripe accepts your application and confirms the first supported reporting period.

## Review each filing

Both supported returns use calendar quarters. For each filing period:

1. Stripe emails you when your filing information is ready to review.
2. Use the secure link in the email to download the filing information.
3. Confirm that the filing information is complete and accurate.
4. Send any corrections by the review deadline in the email.
5. Follow any additional instructions in the filing email.

## Meet filing and payment deadlines

After Stripe submits the return, it sends you payment instructions. Pay the tax authority using the return reference and instructions that Stripe provides. Stripe doesn’t automatically debit your bank account or Stripe balance for these filings.

## Understand Canadian simplified GST and HST filing

Canada’s simplified GST/HST regime can apply to specified cross-border digital products and services and certain platform-based short-term accommodation supplies. It’s generally available to qualifying non-resident businesses that don’t carry on business in Canada and aren’t registered under the normal GST/HST regime.

Stripe’s filing service supports only the supply types confirmed during your filing application. It doesn’t cover:

- Normal GST/HST registrations.
- Provincial sales taxes administered separately by British Columbia, Manitoba, Québec, or Saskatchewan.
- Physical goods or other supplies that require normal GST/HST treatment.
- Input tax credits, which simplified registrants generally can’t claim on a simplified return.
- Periods before the effective date of the simplified registration.

If you’re registered under Canada’s simplified GST/HST regime, don’t charge GST/HST on services sold to business customers that provide a GST/HST registration number. Add the customer’s tax ID to their [Stripe Customer record](https://docs.stripe.com/billing/customer/tax-ids.md). Learn more about [collecting tax in Canada](https://docs.stripe.com/tax/supported-countries/canada/collect-tax.md).

Simplified GST/HST returns and payment are due the last day of the month following each calendar quarter:

| Reporting period | Standard deadline |
| --- | --- |
| January 1–March 31 | April 30 |
| April 1–June 30 | July 31 |
| July 1–September 30 | October 31 |
| October 1–December 31 | January 31 of the following year |

Stripe’s review deadline occurs before the legal deadline. Follow the earlier deadline in your filing email so Stripe has time to prepare and submit the return.

The CRA generally considers a return or payment due on a Saturday, Sunday, or CRA-recognized public holiday timely if it receives the return or payment on the next business day. Follow the date in your Stripe filing email and the applicable tax authority guidance.

Keep the records needed to support your GST/HST liabilities and returns for six years after the end of the year to which they relate. Keep them longer if the CRA requires it or an objection or appeal remains unresolved. Supporting records can include transaction records, customer location and registration evidence, tax calculations, filed returns, and payment confirmations.

## Understand Irish non-Union OSS filing

Irish non-Union OSS filing is for a business that isn’t established and doesn’t have a fixed establishment in the EU and supplies services to non-taxable persons in EU member states. After you register for the scheme, you must report all supplies that are within its scope through non-Union OSS.

The filing service doesn’t cover:

- Services supplied to taxable persons under B2B rules.
- Supplies of physical goods.
- Union OSS or IOSS returns.
- Local VAT returns or activities outside the non-Union scheme.
- Input VAT deductions or refunds through the OSS return.
- Periods before the non-Union OSS registration effective date.

File Irish non-Union OSS returns in EUR. For supplies in another currency, Irish Revenue requires you to use the European Central Bank exchange rate for the last day of the calendar quarter. If the bank doesn’t publish a rate that day, use the rate from the next publication date.

The non-Union OSS return and payment deadlines are the last day of the month following each calendar quarter:

| Reporting period | Standard deadline |
| --- | --- |
| January 1–March 31 | April 30 |
| April 1–June 30 | July 31 |
| July 1–September 30 | October 31 |
| October 1–December 31 | January 31 of the following year |

Stripe’s review deadline occurs before the legal deadline. Follow the earlier deadline in your filing email so Stripe has time to prepare and submit the return.

You generally report corrections to a filed OSS return in a later OSS return instead of changing the original return. Tell Stripe promptly if you discover an error. You can generally submit corrections for three years after the original return deadline. After that period, or after deregistration in some cases, you might need to work directly with the member state of consumption.

Keep sufficiently detailed records for 10 years from December 31 of the year in which each transaction occurred. Your records must contain enough information to verify the return, and you must make them available electronically to the relevant tax authority. Learn more in the [European Commission OSS guide](https://taxation-customs.ec.europa.eu/document/download/dce47fbc-144a-4c5c-b5f9-30a06162514a_en).

## Correct filing information

Contact [Stripe support](https://support.stripe.com/contact) as soon as you find missing or incorrect information.

- **Before Stripe submits the return:** Send corrections by the review deadline in your filing email.
- **After a Canadian return is filed:** Don’t file a replacement return. The CRA requires an adjustment to the filed return. Contact Stripe to determine whether you must submit the adjustment directly.
- **After an OSS return is filed:** Report the correction in a later OSS return when permitted. Contact Stripe to determine whether Stripe can include the correction in a later supported filing.

You remain responsible to the applicable tax authority for the completeness and accuracy of your returns and for paying tax, interest, and any penalties legally assessed against you. Providing information late, incompletely, or inaccurately might result in additional tax, interest, or penalties under applicable law. Using Stripe’s filing service doesn’t transfer your statutory tax obligations to Stripe.

## Pricing

You must subscribe to Tax Complete. Contact Stripe for availability and pricing for these filings.

## Next steps

- [Set up Stripe Tax](https://docs.stripe.com/tax/set-up.md)
- [Add a tax registration](https://docs.stripe.com/tax/registering.md)
- [Learn about tax filing options](https://docs.stripe.com/tax/filing.md)
- [Contact Stripe support](https://support.stripe.com/)

