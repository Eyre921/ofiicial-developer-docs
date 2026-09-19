---
title: "Use Stripe to register for US sales tax"
source: https://docs.stripe.com/tax/use-stripe-to-register.md
path: tax/use-stripe-to-register
---

# Use Stripe to register for sales tax

Learn how Stripe can register you for sales tax in the US.

Sales tax registration is the process of formally enrolling with a tax authority so you’re authorized to collect sales tax from customers in that location. In the United States, you must register in a state before collecting sales tax there. This legal requirement applies after your sales to customers in that state exceed its economic nexus threshold. If you’re an eligible remote seller, select **Register for me** in the Dashboard, and Stripe registers with the US tax authority on your behalf.

## Eligibility

To qualify for tax registration services through Stripe, your business must meet the following criteria:

- Be a remote, out-of-state seller with no physical presence in the state you want to register in.
- Have a US bank account. This is required in [states that charge fees](https://docs.stripe.com/tax/use-stripe-to-register.md#pricing-and-state-fees) or require banking details.
- Not have received a notice or set up an online account with the jurisdiction.
- Have no prior acquisitions of an existing business.
- For businesses based outside of the US or with direct entity ownership based outside of the US:
  - Employer Identification Number (EIN) for their business
  - Social Security Number (SSN) or Individual Taxpayer Identification Number (ITIN) for the required parties:
    - **Single-owner entities** (individual, sole proprietor, single-member LLC): One SSN or ITIN for the business owner, who is also likely the business representative.
    - **Multi-owner entities** (any entity type with multiple owners): At least two SSNs or ITINs, which can include the business representative as one of them.
      - Employer Identification Number (EIN) for any entity with ownership in the business.

## How to sign up

Under [Needs attention](https://dashboard.stripe.com/tax/locations?primary_tab=needs_attention) tab on the Tax page:

- Hover over the jurisdiction where you want to sign up and click **Add registration**.
- Select **Register for me** to have Stripe complete your application.

Under [Locations](https://dashboard.stripe.com/tax/locations) on the Tax page:

- Click **Add registration**.
- Select the US state you want to register in.
- Select **Register for me**.

## What to expect

### Gather information needed to register

Gather key business information such as address, EIN, contact and ID information (for business owners and your business representative), and any state-specific information such as previous year sales and the date you want your registration to become effective.

> Some state tax registrations require complete business ownership details, including investor information, cap table data, and ownership percentages. This detailed ownership information only needs to be provided once, and will be used for all applicable state registrations.

### After you submit your application

One of Stripe’s tax experts typically completes your registration with the state in 30 days or less. December, January, and February are high-volume months for registration and tax filings. Within these months, registration takes 60 days or less. If we require any additional information from you, those timeframes might get extended.

After we complete it, you receive a detailed confirmation email from our team of tax experts containing a secure document link with relevant information about your new tax registration. You can also view this in the [Documents](https://dashboard.stripe.com/settings/documents) section of your Stripe Dashboard.

Your new tax registration is automatically added to your Stripe Dashboard after Stripe registers for you. If you’re [set up to collect using Stripe Tax](https://docs.stripe.com/tax/set-up.md), Stripe begins automatically calculating tax in this jurisdiction according to your collection start date.

## Pricing and state fees

### Pricing

Registrations are only available as part of a Tax Complete subscription. Check your plan in the Dashboard under [Stripe plans](https://dashboard.stripe.com/settings/plans). Learn more about [Tax Complete pricing](https://support.stripe.com/questions/understanding-stripe-tax-pricing).

### State fees

The following states charge a fee to all remote sellers who register to collect tax. Because most states require ACH debit to process fees, your provided bank account is debited for any state fees charged upon the initial registration submission. The exact fee can vary slightly depending on your unique business characteristics.

- **Arizona**: 12 USD state fee charged with registration plus 1-50 USD per local jurisdiction, charged after you file and remit in a new local jurisdiction
- **Colorado**: 16 USD per location site plus a 50 USD deposit, refunded automatically after you collect 50 USD in state sales tax
- **Connecticut**: 100 USD
- **Hawaii**: 20 USD
- **Indiana**: 25 USD
- **Nevada**: 15 USD plus a security deposit, which depends on your estimated sales volume and is held by the state for a minimum of 3 years
- **South Carolina**: 50 USD
- **Washington**: 50 USD plus 5 USD per DBA (“doing business as," or trade name)
- **West Virginia**: 30 USD
- **Wisconsin**: 20 USD
- **Wyoming**: 60 USD

## When to register for tax collection

When you need to register to collect tax in the US as a remote seller, it’s typically based on the following two primary factors:

### When you exceed an economic nexus threshold, based on sales or transaction count

In the US, you need to register as a remote seller after you meet the state’s economic nexus threshold requirements. Check out the [US state tax pages](https://docs.stripe.com/tax/supported-countries/united-states.md) or [Needs attention](https://dashboard.stripe.com/tax/locations?primary_tab=needs_attention) tab in your Stripe Dashboard to see how your payment volume compares to each jurisdiction’s thresholds. Stripe also notifies you with email and Dashboard alerts after you appear to have crossed a threshold based on your Stripe payment volume.

### Whether the jurisdiction provides a grace period to allow taxpayers more time to register after exceeding a threshold

The chart below shows the current state grace periods by state, if offered.

| State | Grace Period, if available |
| --- | --- |
| **Alabama** | January 1 of the calendar year after the threshold is exceeded |
| **Alaska** | 1st day of the month not more than 30 days after the threshold is exceeded |
| **Arizona** | 1st day of the following month, 2 months after the threshold is exceeded |
| **Arkansas** | When the threshold is exceeded |
| **California** | When the threshold is exceeded |
| **Colorado** | 1st day of the following month, 90 days after the threshold is exceeded |
| **Connecticut** | January 1 of the calendar year after the threshold is exceeded over the 12 months ending September 30 |
| **District of Columbia** | When the threshold is exceeded |
| **Florida** | January 1 of the next calendar year after the threshold is exceeded |
| **Georgia** | When the threshold is exceeded |
| **Hawaii** | 1st day of the month not more than 30 days after the threshold is exceeded |
| **Idaho** | When the threshold is exceeded |
| **Illinois** | 1st day of the quarter after the threshold is exceeded |
| **Indiana** | When the threshold is exceeded |
| **Iowa** | 1st day of the month no more than 30 days after the threshold is exceeded |
| **Kansas** | 1st day of the month no more than 30 days after the threshold is exceeded |
| **Kentucky** | 1st day of the month no more than 30 days after the threshold is exceeded |
| **Louisiana** | 30 days after the threshold is exceeded |
| **Maine** | 1st day of the following month, 2 months after the threshold is exceeded |
| **Maryland** | 1st day of the month and not more than 30 days after the threshold is exceeded |
| **Massachusetts** | 1st day of the following month, 2 months after the threshold is exceeded |
| **Michigan** | January 1 of the next calendar year after the threshold is exceeded |
| **Minnesota** | 1st day of the following month, 2 months after the threshold is exceeded |
| **Mississippi** | When the threshold is exceeded |
| **Missouri** | 1st day of the following month, 90 days after the threshold is exceeded |
| **Nebraska** | 1st day of the following month, 2 months after the threshold is exceeded |
| **Nevada** | 1st day of the month and not more than 30 days after the threshold is exceeded |
| **New Jersey** | 1st day of the month and not more than 30 days after the threshold is exceeded |
| **New Mexico** | January 1 of the next calendar year after the threshold is exceeded |
| **New York** | 30 days after the threshold is exceeded |
| **North Carolina** | 60 days after the threshold is exceeded |
| **North Dakota** | 60 days after the threshold is exceeded or the following calendar year, whichever is earlier |
| **Ohio** | When the threshold is exceeded |
| **Oklahoma** | 1st day of the month and not more than 30 days after the threshold is exceeded |
| **Pennsylvania** | 1st day of the following month, 90 days after the threshold is exceeded |
| **Puerto Rico** | When the threshold is exceeded |
| **Rhode Island** | January 1 of the next calendar year after the threshold is exceeded |
| **South Carolina** | 1st day of the following month, 2 months after the threshold is exceeded |
| **South Dakota** | When the threshold is exceeded |
| **Tennessee** | 1st day of the following month, 3 months after the threshold is exceeded |
| **Texas** | 1st day of the following month, 4 months after the threshold is exceeded based on a rolling 12 months |
| **Utah** | When the threshold is exceeded |
| **Vermont** | 1st day of the month and not more than 30 days after the threshold is exceeded |
| **Virginia** | 1st day of the month and not more than 30 days after the threshold is exceeded |
| **Washington** | 1st day of the following month, 2 months after the threshold is exceeded |
| **West Virginia** | When the threshold is exceeded |
| **Wisconsin** | When the threshold is exceeded |
| **Wyoming** | When the threshold is exceeded |

## Late registration

If you’re late in registering to collect tax, you have two main options:

The first option is to register as soon as possible with a registration effective date of when nexus was established in the jurisdiction, even if this date is in the past. This date reflects when you should have initially registered. Keep in mind that the state often requires you to file overdue returns for missing tax periods and back-pay any taxes along with penalties and interest. If you’re subject to penalties, most states offer penalty waivers that you can file to ask for a reduction or elimination of any penalties you owe.

The second option is to work with your tax advisor to file a Voluntary Disclosure Agreement (VDA) in any jurisdictions where you’re late to register. VDAs allow taxpayers to become compliant with the state and ask for leniency on any overdue returns, taxes, and penalties. States might limit how far back you have to pay previously owed taxes (for example, 3 years versus 5 years) or waive any associated penalties. You can often do this anonymously through a third party. This can be costly, so it’s important to consult your tax advisor and weigh the pros and cons of both options.

## Registration considerations

### Your collection start date might be different from your registration date

- The registration effective date is the date you provided in your application indicating when you need to register.
- The collection start date is the date Stripe began automatically calculating and collecting tax for this jurisdiction.
- On the day our tax experts complete your registration, if your registration effective date is:
  - In the future, your collection will be scheduled for that same future date. This means both of these dates are the same.
  - The same day, collection starts immediately.
  - In the past, collection starts immediately. This means that your earlier registration effective date and later collection start date in Stripe differ.

### Contact information for both states and Stripe

In your application, you provided contact information including an email address. We recommended that this is an email that someone frequently checks and that isn’t tied to any single individual. Stripe uses this contact information if we need to contact you about your registration, and the states use it on a long-term basis. In some states, this email address also becomes your username.

### The Dashboard shows an issue status for a registration in progress

If you see an “issue” status next to your registration in process, check the email address you provided as your contact information. One of our tax experts will have reached out to you explaining what additional information is needed to process your request.

### No support for in-state registrations

We can only support remote (out-of-state) sellers with no physical presence in the state. Physical presence laws vary by state, but generally include factors such as an office, storefront, employees, salespeople, contractors, warehouses, inventory, or trade show attendance. Consult your tax advisor if you’re unsure about whether you have physical presence in the state.

### Register with the taxing authorities before you can add this registration to your Stripe Dashboard

Adding a registration to the Stripe Dashboard doesn’t automatically register you in that jurisdiction.

If Stripe registers on your behalf, one of our tax experts automatically adds this new tax registration to your Stripe Dashboard with the correct effective date, so you don’t need to take any further action to begin automatically calculating tax.

### Viewing the signup option or reviewing an in-progress application

### US-based businesses with US-based direct entity ownership

- US-based business information, including a *Federal Employer Identification Number (FEIN)*
- A US address
- A US (+1) phone number
- A Social Security Number (SSN) for your business representative and direct individual business owners with 10% or more ownership

### Businesses based outside of the US or with direct entity ownership based outside of the US

- Employer Identification Number (EIN) for the business.
- A valid business address.
- A phone number.
- Social Security Number (SSN) or Individual Taxpayer Identification Number (ITIN) for the required parties:
  - **Single-owner entities** (individual, sole proprietor, single-member LLC): *One SSN or ITIN* for the business owner.
  - **Multi-owner entities** (any entity type with multiple owners): *Two SSNs or ITINs*, which can include the business representative as one of them.

### Filing assistance post-registration

Stripe doesn’t provide an in-house filing solution. See [tax filing](https://docs.stripe.com/tax/filing.md) to learn more about our trusted filing partners.

### Determining NAICS and SIC codes

The North American Industry Classification System (NAICS) and Standard Industrial Classification (SIC) are two federal standardized code systems used in the US to classify your primary business activity and industry. Certain state jurisdictions use NAICS while others use SIC. If you don’t yet know the NAICS or SIC code for your business, here’s how you can determine it:

- You can start by searching for an [NAICS code here](https://www.naics.com/search/). We recommend doing this first, as NAICS codes typically offer a bit more details. After you identify the proper NAICS code, you can enter it in the [NAICS column](https://www.naics.com/naics-to-sic-crosswalk-2/) to see the possible corresponding SIC codes.
- Alternatively, you can search for a [SIC code](https://www.naics.com/everything-sic/) here and then enter it in the [SIC column](https://www.naics.com/naics-to-sic-crosswalk-2/) to see the possible corresponding NAICS codes.

### Editing or canceling your registration application

If your registration application is incomplete (you haven’t submitted it yet), you can edit or cancel it in the Dashboard by clicking the overflow menu (⋯) next to your incomplete registration on the [Needs attention](https://dashboard.stripe.com/tax/locations?primary_tab=needs_attention) tab or on the relevant jurisdiction page in the Dashboard.

If you already submitted your registration, you can request to edit or cancel your application by contacting support.

