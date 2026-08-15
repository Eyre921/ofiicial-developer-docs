---
title: "Set up Capital"
source: https://docs.stripe.com/capital/getting-started.md
path: capital/getting-started
---

# Set up Capital

Determine which integration option to use when you set up Stripe Capital.

> Capital for platforms is available in [public preview](https://docs.stripe.com/release-phases.md).

Use Stripe Capital to offer financing to eligible connected accounts. First, choose the integration that fits your platform. Then use the quickstart to launch with Stripe co-branded emails, or follow the relevant integration guide to customize your messaging.

## Choose your integration

Use this table to determine which integration best fits your platform’s markets, technical capabilities, and desired level of control.

| Criteria | [No-code](https://docs.stripe.com/capital/no-code-integration.md) | [Embedded components](https://docs.stripe.com/capital/embedded-component-integration.md) | [API](https://docs.stripe.com/capital/api-integration.md) |
| --- | --- | --- | --- |
| **Supported markets** | US, AU | US, AU, GB, FR, DE | US, AU, GB, FR, DE |
| **Access requirements** | Available to platforms with Capital access in the US and AU | Available to all platforms with Capital access | Available to all platforms with Capital access |
| **Implementation effort** | Minutes to hours | Hours to days | Days to weeks |
| **Customization level** | Low: Use Stripe’s co-branded emails and hosted pages | Medium: Embed Capital components in your platform’s UI and optionally send custom emails | High: Control email content and notification timing. The application flow stays Stripe-hosted for compliance |
| **Recommended for** | Platforms that want to launch with minimal development effort and are comfortable with Stripe co-branding | Platforms that want to embed Capital in their own UI so connected accounts don’t leave the platform to apply or manage financing | Platforms that need control over messaging and want to build Capital into their own product |

For a detailed capability comparison, see [Compare integrations](https://docs.stripe.com/capital/getting-started.md#compare-integrations).

## Quickstart

Use the Dashboard to launch a Capital program to offer financing to your connected accounts. Launching your program means you enable sending automatic financing offers to all eligible connected accounts. The quickstart helps you choose options for you to launch your program as fast as possible, usually within minutes to a few days.

1. In the [Capital](https://dashboard.stripe.com/connect/capital/discovery) page in the Stripe Dashboard, click **Get Started**.

2. Select either:

   - **No-code** (Recommended): If you choose this option, Stripe sends all emails on your behalf to your eligible connected accounts, including co-branded emails with financing offers, weekly paydown progress update emails, and any servicing or collections emails if needed. Co-branded emails contain a button that redirects connected accounts to a Stripe-hosted Capital page, where they can apply for an offer or track their weekly paydown progress. Only available for platforms in the US and AU.
   - **Custom**: If you choose this option, you’re responsible for sending financial offers and payment progress emails to your connected accounts by monitoring webhook events and updating offers as delivered using the Stripe APIs. Sending your own email copy requires additional compliance reviews from Stripe, which might take up to 5-7 days for approval.

3. You can market your Capital program to your connected accounts in several ways. Select either:

   - **Stripe co-branded marketing only** (Recommended): Opt into Stripe sending co-branded emails with financing offers to your connected accounts. You can always add custom marketing assets, such as announcement landing pages, ads, and social media posts, that comply with our [guidelines](https://docs.stripe.com/capital/marketing.md#promoting-capital) after you launch. This option is only available to platforms in the US and AU.

   - **Stripe co-branded and custom marketing**: Stripe automatically sends co-branded [emails](https://docs.stripe.com/capital/how-capital-for-platforms-works.md#emails) to your connected accounts, excluding marketing emails outside of the US and AU, and you provide additional custom marketing for your Capital program, such as additional emails, landing pages, social media posts, and advertisements. Any custom marketing you upload must pass compliance review, which can take up to 5–7 business days.

     > To build a Capital program with as little Stripe co-branding as possible, see [Set up an API integration](https://docs.stripe.com/capital/api-integration.md). This requires you to use APIs, and therefore isn’t a quickstart option. For compliance reasons, eligible connected accounts must still apply for your Capital program in a Stripe-hosted Capital page if you choose this option.

4. Confirm that onboarding to Capital can affect the data shown in any existing financial reports you might already provide to connected accounts in your platform’s UI. Review your options for providing paydown information in [Reconcile and provide reports](https://docs.stripe.com/capital/getting-started.md#after-quickstart-launch).

5. Sign the partnership contract and send automatic financing offers to eligible connected accounts.

## After quickstart launch

As you wait for connected accounts to accept their Capital financing offers, or at any point after you enable automatic offers, you can customize your Capital program.

1. Reconcile and provide financial reports for connected accounts.

   If you already provide existing financial reports to your connected accounts in your platform’s UI, onboarding to Capital might affect the amount reflected in those transactions. Confirm with your team developer the types of reports and the level of detail you provide to your connected accounts.

   Depending on the complexity (usually if your reports have filtering or grouping functionality), you might need to synchronize the data for these reports with Capital’s transactions. Alternatively, you can provide separate Capital reports (using embedded components or Stripe APIs) in the designated Capital page in your platform’s UI to your connected accounts. To learn more, see [Reconcile and provide reports](https://docs.stripe.com/capital/reporting-and-reconciliation.md).

2. (Optional) Promote your program.

   After launch, you can use embedded components to help with program outreach and discoverability. This means connected accounts can learn about and accept an offer for Capital financing directly in your platform’s UI. You can also use embedded components to help your connected accounts manage payments on your platform’s UI, instead of requiring them to access a separate Stripe-hosted Capital page. To learn more, see:

   - [Embed the Capital promo tile component](https://docs.stripe.com/capital/promotional-tile.md)
   - [Embed the Capital financing component](https://docs.stripe.com/connect/supported-embedded-components/capital-financing.md)

3. (Optional) Customize marketing assets.

   In addition to co-branded offer emails, you might want to send your own marketing emails, publish a blog post, or create a landing page so your connected accounts can learn more about your Capital program.

   Stripe reviews all custom marketing assets to confirm they comply with the [Capital marketing guidelines](https://docs.stripe.com/capital/marketing.md). This includes any copy used alongside embedded components, such as headers, footers, landing page titles, and URLs. Review and approval might take up to 5-7 business days. To learn more, see:

   - [Marketing for Capital](https://docs.stripe.com/capital/marketing.md)
   - [Servicing Stripe Capital](https://docs.stripe.com/capital/servicing.md)

4. (Optional) Increase eligibility.

   Stripe might be able to improve the eligibility of your connected accounts if you share additional payment data from connected accounts that also process payments outside of Stripe. Providing non-Stripe payment data allows us to review the full scope of each connected account’s business for financing eligibility. To learn more, see [Import non-Stripe data into Capital underwriting](https://docs.stripe.com/capital/import-non-stripe-data.md).

## Compare integrations

Use this comparison to learn how each integration handles communications, information for connected accounts, and reporting.

| Capability | No-code | Embedded components | API |
| --- | --- | --- | --- |
| **Marketing** | Use Stripe to send co-branded emails | Use existing marketing templates or publish your own marketing assets | Use existing marketing templates or publish your own marketing assets |
| **Capital offer emails** | Stripe sends co-branded offer emails | (Optional) Stripe sends co-branded offer emails (US/AU only) or (Recommended) the platform sends offer emails (GB, FR, DE) | (Recommended) Platform sends offer emails |
| **In-product notifications** | (Optional) Use embedded components to notify connected accounts in your website, such as a [promo tile](https://docs.stripe.com/capital/promotional-tile.md) | Use the [promo tile](https://docs.stripe.com/capital/promotional-tile.md) or [financing promotion](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion.md) embedded component to promote new financing offers | (Optional) Platform can build custom notifications or banners |
| **Capital application** | Stripe-hosted co-branded application flow | Use the Capital [financing promotion](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion.md) or [financing application](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-application.md) component to embed the application flow into your website | Stripe-hosted UI application flow or embedded components |
| **Metrics and insights** | View metrics in the Stripe Dashboard | View metrics in the Stripe Dashboard | View some metrics in the Stripe Dashboard |

If your platform sends Capital offer emails, [call the API](https://docs.stripe.com/capital/api-integration.md#mark-the-offer-as-delivered) to mark each offer as delivered and update offer email metrics.

### Shared program responsibilities

These responsibilities apply to every integration:

- Stripe conducts a compliance review of custom marketing assets and periodic program audits.
- Stripe manages the underwriting process and sets pricing.
- Stripe manages servicing of customer financing.

## See also

- [Set up a no-code integration](https://docs.stripe.com/capital/no-code-integration.md)
- [Set up an embedded components integration](https://docs.stripe.com/capital/embedded-component-integration.md)
- [Set up an API integration](https://docs.stripe.com/capital/api-integration.md)

