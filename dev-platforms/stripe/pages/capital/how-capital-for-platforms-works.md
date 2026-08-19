---
title: "Stripe Capital for platforms"
source: https://docs.stripe.com/capital/how-capital-for-platforms-works.md
path: capital/how-capital-for-platforms-works
---

# Stripe Capital for platforms

Offer financing to your connected accounts.

> Capital for platforms is available in [public preview](https://docs.stripe.com/release-phases.md).

Stripe Capital for platforms lets you offer financing to your connected accounts through your existing *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) integration. Stripe and its financial partners manage eligibility, underwriting, pricing, funding, servicing, and collections.

To see see what connected accounts see, try the interactive demo.

[Capital for platforms demo](https://dashboard.stripe.com/capital/demo)

## Availability

Capital for platforms is available in the following countries:

- AU
- DE
- FR
- GB
- US

## How Capital for platforms works

| **Step** | **What happens** |
| --- | --- |
| **1. Stripe reviews your accounts** | Stripe prequalifies connected accounts daily using their payment activity on Stripe with your platform. No action required from your platform. Not all connected accounts are eligible. |
| **2. Eligible businesses get an offer** | Qualified accounts receive a financing offer consisting of a principal amount plus a flat fee, with no variable interest. |
| **3. Funds are deposited** | After the connected account accepts, Stripe deposits funds into their bank account within 1–2 business days. |
| **4. Repayment is automatic** | Stripe withholds a fixed percentage of each transaction until the complete balance is repaid. Payments adjust with sales volume, with no fixed monthly bill. |
| **5. Stripe handles support** | Stripe and its financial partners manage all financing questions, servicing, and collections. |

## Financing offers 

Each Capital financing offer includes the following components:

| **Component** | **What it means** |
| --- | --- |
| **Principal amount** | The amount the connected account receives upfront |
| **Payment rate** | The percentage of each future transaction withheld toward repayment |
| **Premium amount** | A flat, one-time fee on top of the principal, with no compounding interest |
| **Minimum payment** | A repayment floor over a set period (where applicable) |

For example, consider the following offer:

- Principal: 20,000 in local currency
- Payment rate: 15%
- Premium: 2,000 (total repayment: 22,000)

Stripe withholds 15% of each transaction until the full balance is paid. In areas where a minimum payment applies, if withholdings fall short, Stripe automatically debits the shortfall for that period. There’s no prepayment penalty. Connected accounts can pay their balance in full at any time from the **Capital** tab in their Dashboard.

### Country-specific offer types 

Offer types, limits, and minimum payments vary by country.

#### US

Four types of financing offers are available to US connected accounts:

| **Type** | **Provider** | **How it works** |
| --- | --- | --- |
| **Flex loan** | Celtic Bank or Lead Bank | A term loan with 60-day minimum payments. If withholdings fall short of the minimum, Stripe debits the difference from the connected account’s external bank account. |
| **Merchant cash advance (MCA)** | YouLend | A purchase of future receivables, not a loan. Payments vary with processing volume with no fixed schedule or regular debits. Soft credit check only. There’s no impact on the connected account’s personal credit score. |
| **Fixed-term loan** | Celtic Bank or Lead Bank | Available to connected accounts that process payments outside Stripe and whose payment data has been imported to Stripe. Repaid through weekly minimums with a capped withholding structure. |
| **Line of credit** | Celtic Bank or Lead Bank | Draw up to a prequalified credit limit, accessing only the amount needed. Each draw is repaid as principal plus a fixed fee over nine monthly payments. Available credit replenishes as repayments are made, and the credit limit is reevaluated every 90 days. |

> The line of credit is in private preview. Contact your Stripe account team for access.

#### AU

### Additional eligibility considerations

- The person applying and guaranteeing the offer must be a representative, controller, or director with at least 25% ownership, be at least 18 years old, and be able to provide an address in Australia.
- Applicants who are directors and beneficial owners of the business must provide a personal guarantee as part of the financing application.
- Capital isn’t available to connected accounts based in New Zealand.

### Types of financing offers

Fundbox provides Australian connected accounts a single financing type: a `loan`.

| **Offer terms** | **Loan** |
| --- | --- |
| **Min offer** | 500 AUD |
| **Max offer** | 150,000 AUD (up to 250,000 AUD for refills) |
| **Expected duration** | 8–9 months |
| **Minimum payment** | Every 30 days |
| **Bank debit if minimum not met** | Yes |
| **Credit check** | No |
| **Transaction withholding** | Fixed % for the life of the loan |

### Refill behavior

When an Australian connected account accepts a refill, the payout automatically pays down the remaining balance on their current financing before the new financing begins. Connected accounts pay one offer at a time.

*Financing is provided by Fundbox, an external finance provider, with payments facilitated by Stripe. Funding amounts, rates, and terms are based on review and approval of a completed application, and are subject to change. Financing offers might require additional documentation.*

#### DE

### Regulatory requirement for platforms

In Germany, credit brokerage is a regulated activity under the German Trade Ordinance (§34c GewO). Platforms offering Capital to German connected accounts might need to obtain a credit broker license from their local Chamber of Industry and Commerce (*Industrie- und Handelskammer*) before going live. Licensing typically takes 1–3 months and generally requires a physical presence in the relevant German district. This information is for general guidance only and doesn’t constitute legal advice—seek independent legal counsel to assess the requirements that apply to your business. See [Regulatory compliance](https://docs.stripe.com/capital/regulatory-compliance.md) for more details.

### Additional eligibility considerations

- The person applying and guaranteeing the offer must be a representative, controller, or director with at least 25% ownership, be at least 18 years old, and be able to provide an address in Germany.
- Applicants who are directors and beneficial owners of the business must provide a personal guarantee as part of the financing application.

### Types of financing offers

German connected accounts can access a single financing type: a `loan advance`, provided by YouLend GmbH.

| **Offer terms** | **Loan advance** |
| --- | --- |
| **Min offer** | — |
| **Max offer** | 150,000 EUR |
| **Expected duration** | 6–7 months |
| **Minimum payment** | Weekly (contractual) |
| **Bank debit if minimum not met** | No |
| **Credit check** | Soft check on application (no score impact); hard check upon funding |
| **Transaction withholding** | Fixed % per YouLend agreement |

### Refill behavior

When a German connected account accepts a refill, the original financing remains active and the refill payout doesn’t automatically pay it. YouLend applies the new withholding rate to the original financing. After the original financing clears, withholding shifts to the new financing.

*All financing requests are subject to final review before approval. Financing is provided in cooperation with YouLend GmbH and its affiliates. Technical support and customer management provided by YouLend GmbH.* *Stripe Technology Europe Limited acts as an intermediary and technology provider. Stripe Technology Europe Limited holds a license for loan brokerage pursuant to Sect. 34c para. 1 sentence 1 no. 2 of the German Trade Ordinance. Competent Supervisory Authority: Industrie- und Handelskammer für München und Oberbayern, 80333 München. https://www.ihk-muenchen.de/de/*

#### FR

### Regulatory requirement for platforms

In France, introducing users to financing products is a regulated activity. Platforms offering Capital to French connected accounts might need to register as an IOBSP (*Intermédiaire en Opérations de Banque et Services de Paiement*) with [ORIAS](https://www.orias.fr/) before going live. Registration typically takes 2–3 months and requires a French legal entity. Stripe can assist with certain documentation as part of this process. This information is for general guidance only and doesn’t constitute legal advice—seek independent legal counsel to assess the requirements that apply to your business. See [Regulatory compliance](https://docs.stripe.com/capital/regulatory-compliance.md) for more details.

### Additional eligibility considerations

- The person applying and guaranteeing the offer must be a representative, controller, or director with at least 25% ownership, be at least 18 years old, and be able to provide an address in France.
- Applicants who are directors and beneficial owners of the business must provide a personal guarantee as part of the financing application.

### Types of financing offers

French connected accounts can access a single financing type: a `loan advance`, provided by YouLend SAS.

| **Offer terms** | **Loan advance** |
| --- | --- |
| **Min offer** | 500 EUR |
| **Max offer** | 150,000 EUR |
| **Expected duration** | 6–7 months |
| **Minimum payment** | Weekly (contractual) |
| **Bank debit if minimum not met** | No |
| **Credit check** | No |
| **Transaction withholding** | Fixed % per YouLend agreement |

### Refill behavior

When a French connected account accepts a refill, the original financing remains active and the refill payout doesn’t automatically pay it. YouLend applies the new withholding rate to the original financing. After the original financing clears, withholding shifts to the new financing.

*All financing requests are subject to final review prior to approval. Financing is provided in co-operation with YouLend SAS and its affiliates. Technical support and customer management provided by YouLend SAS.*

*YouLend SAS is registered in the Single Register of Insurance, Banking, and Finance Intermediaries (ORIAS) under the registration number N 21001409 as an Intermediary in Banking Operations and Payment Services (MOBSPL). YouLend SAS’s registered office is located at the SNCF station, 14 rue de Dunkerque, 75010, Paris.*

#### GB

### Additional eligibility considerations

- The person applying and guaranteeing the offer must be a representative, controller, or director with at least 25% ownership, be at least 18 years old, and be able to provide a UK address.
- Applicants who are directors and beneficial owners of the business must provide a personal guarantee as part of the financing application.

### Types of financing offers

There are two types of financing offers available to UK connected accounts. The connected account’s legal entity structure determines the offer type.

- **Cash advance**: A purchase of the connected account’s future receivables, not a loan or credit transaction. YouLend purchases a percentage of the business’s payment processing volume as specified in the YouLend Advance Agreement. It has no fixed payment schedule or regular debits; payments vary based on the connected account’s processing volume. It’s available to sole proprietors, individuals, and unincorporated entities.

- **Loan advance**: A loan disbursement with conditions including rates and a fixed repayment structure. It’s available to incorporated entities (companies, LLCs, Ltd).

The connected account’s current incorporation status determines the offer type and doesn’t change unless the connected account updates their incorporation status. If a connected account applies with incorrect information, ask the connected account to update their Stripe account information before reapplying.

The following table compares these financing options:

| **Offer terms** | **Cash advance** | **Loan advance** |
| --- | --- | --- |
| **Max offer** | 350,000 GBP (up to 500,000 GBP for refills) | 350,000 GBP (up to 500,000 GBP for refills) |
| **Expected duration** | 6–7 months | 6–7 months |
| **Minimum payment** | None | Weekly (contractual) |
| **Bank debit if minimum not met** | No | No |
| **Credit check** | Soft check on application (no score impact); hard check upon funding | None |
| **Transaction withholding** | Fixed % per YouLend agreement | Fixed % per YouLend agreement |

### Refill behavior

When a British connected account accepts a refill, the original financing remains active and the refill payout doesn’t automatically pay it. YouLend applies the new withholding rate to the original financing. After the original financing clears, withholding shifts to the new financing.

*All financing applications are subject to review prior to approval. In the UK, Stripe Capital loans and cash advances are provided by YouLend.*

## Who qualifies 

Stripe and its financial partners review each connected account’s eligibility automatically based on their Stripe payment activity. This runs daily and requires no action from your platform.

| **Requirement** | **Details** |
| --- | --- |
| **Business type** | For-profit business located or incorporated in a [supported country](https://docs.stripe.com/capital/how-capital-for-platforms-works.md#country-specific-details), with an address in that country |
| **Processing history** | At least 3 months of payments on Stripe with your platform, with an annual volume of at least 5,000 in local currency and a monthly average of at least 1,000 in local currency |
| **Standing** | In good standing with Stripe Capital |
| **Applicant** | A representative, controller, or director, at least 18 years old, with at least 25% ownership |

Meeting these requirements doesn’t guarantee an offer. Stripe and its partners also weigh processing consistency, growth trajectory, customer breadth, and dispute rate.

> You can import non-Stripe payment data for accounts that process sales elsewhere. This can make more of your connected accounts eligible. See [Improve underwriting with non-Stripe data](https://docs.stripe.com/capital/import-non-stripe-data.md).

## How to integrate 

After you confirm eligibility, choose an integration option. See [Compare integrations](https://docs.stripe.com/capital/getting-started.md#compare-integrations) for the options available in each country.

| **Option** | **Best for** | **What you build** |
| --- | --- | --- |
| [No-code integration](https://docs.stripe.com/capital/no-code-integration.md) | Fastest to launch | Enable from the Dashboard. Stripe sends co-branded offer emails on your behalf. |
| [Embedded components](https://docs.stripe.com/capital/embedded-component-integration.md) | Most platforms | Prebuilt Capital UI added to your product, styleable to match your brand |
| [API integration](https://docs.stripe.com/capital/api-integration.md) | Custom experiences | Your own notifications and flows; Stripe hosts offer acceptance |

Regardless of integration type, connected accounts must accept their offer on a Stripe-hosted Capital page or an embedded component.
![Stripe-hosted Capital offer acceptance page](https://b.stripecdn.com/docs-statics-srv/assets/offer-anatomy.25435a5c27bd4804965991bf4ba77e00.png)

Connected accounts use this Stripe-hosted Capital page, or an embedded component, to accept a financing offer.

## Connected account experience 

After a connected account accepts an offer and receives their payout, you can show them their financing balance, transaction history, and payment progress:

| **Option** | **Details** |
| --- | --- |
| **Email** | Co-branded notifications on offer acceptance, payout disbursement, and payment progress, with links to the Stripe-hosted Capital page. Enabled by default in all markets. |
| [Embedded component](https://docs.stripe.com/connect/supported-embedded-components/capital-financing.md) | Embed the Capital financing component in your platform UI. This component doesn’t include standard payment processing data such as charges, refunds, or disputes. |
| [API](https://docs.stripe.com/capital/reporting-and-reconciliation.md) | Use the Financing Transactions API to monitor Capital transactions alongside detailed payments data and build custom reporting interfaces. |

### Email notifications

Stripe can send the following emails to connected accounts throughout the financing process:

| **Type** | **When it’s sent** |
| --- | --- |
| **Marketing** | New offers, refreshed offers (when a prior offer expires after 30 days), and refill offers (when an account is approximately 80% through repayment). Available in select markets. See [Capital refills](https://docs.stripe.com/capital/refills.md). |
| **Application status** | Submission confirmation, approval, rejection, and KYC/KYB resolution requests. |
| **Transactional** | Weekly progress updates, milestones at 25%, 50%, and 75% completion, minimum payment reminders, and upcoming bank debit notifications. |

## Repayment 

Repayment is fully automated. Stripe deducts a fixed percentage of each connected account’s transactions until the complete balance is repaid. There is no prepayment penalty.

### Minimum payments

Some financing types require a minimum payment each period. If withholdings fall short, Stripe automatically debits the difference from the connected account’s linked bank account. Connected accounts can also pay manually in the Dashboard. If a connected account can’t meet its minimum, tell them to [contact support](mailto:capital+support@stripe.com).

## Additional financing 

Refills are additional offers available after a connected account is roughly 80% through repaying an existing balance. Stripe then sends a refill marketing email. Refill behavior varies by country. See Country-specific offer types (#country-specific-details).

Stripe automatically re-evaluates connected accounts for new offers as they pay down their financing. Paying off early doesn’t guarantee a new offer. When an account becomes eligible, the offer appears automatically in their Dashboard.

## Capital servicing 

Stripe and its financial partners handle all Capital-related support and servicing. Direct connected accounts to [email our dedicated support team](mailto:capital+support@stripe.com) as their first point of contact. For connected accounts experiencing financial difficulty, Stripe’s financial partners might be able to arrange extended payment plans.

## See also

- [Set up Capital](https://docs.stripe.com/capital/getting-started.md)

