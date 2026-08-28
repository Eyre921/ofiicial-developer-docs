---
title: "Set up Capital"
source: https://docs.stripe.com/capital/getting-started.md
path: capital/getting-started
---

# Set up Capital

Determine which integration option to use when you set up Stripe Capital.

Use Stripe Capital to offer financing to eligible connected accounts. Choose the integration that fits your platform, then use the quickstart to launch.

## Compare integrations 

Use this table to determine which integration best fits your platform’s markets, technical capabilities, and desired level of control.

| Capability | No-code (Recommended) | Embedded components | API |
| --- | --- | --- | --- |
| **Supported markets** | US, AU | US, AU, GB, FR, DE | US, AU, GB, FR, DE |
| **Implementation effort** | Minutes to hours | Hours to days | Days to weeks |
| **Who sends offer emails** | Stripe | Stripe (US/AU) or platform (GB, FR, DE) | Platform |
| **Who handles the application flow** | Stripe | Embedded in your UI | Stripe-hosted |
| **Who handles marketing** | Stripe sends co-branded emails | Platform with optional Stripe co-branding | Platform |
| **Customization** | Low | Medium | High |
| **In-product notifications** | Optional: [promo tile](https://docs.stripe.com/capital/promotional-tile.md) | [Promo tile](https://docs.stripe.com/capital/promotional-tile.md) or [financing promotion](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion.md) component | Custom |
| **Metrics and insights** | Stripe Dashboard | Stripe Dashboard | Stripe Dashboard (some metrics) |
| **Best for** | Platforms that want to launch more quickly with minimal development effort | Platforms embedding Capital directly in their UI | Platforms that need full control over messaging and notifications |

### Shared responsibilities

Regardless of integration type, Stripe:

- Conducts compliance reviews of custom marketing assets and periodic program audits
- Manages the underwriting process and sets pricing
- Manages servicing of connected account financing

## Quickstart 

Use the Dashboard to launch a Capital program for your connected accounts.

1. In the [Capital](https://dashboard.stripe.com/connect/capital/discovery) page in the Stripe Dashboard, click **Get started**.

2. Select your integration type: **No-code** (recommended) or **Custom**. Custom email copy requires a Stripe compliance review of up to 5–7 business days.

3. Select your marketing preference: **Stripe co-branded only** (recommended) or **co-branded and custom**. Custom marketing assets require a compliance review of up to 5–7 business days.

4. Confirm that Capital transactions can affect data in any existing financial reports you provide to connected accounts.

5. Sign the partnership contract to enable automatic financing offers for eligible connected accounts.

After completing the quickstart, follow the implementation guide for your integration, then use the [launch checklist](https://docs.stripe.com/capital/launch-checklist.md) to go live.

## See also

- [Set up without code](https://docs.stripe.com/capital/no-code-integration.md)
- [Set up with embedded components](https://docs.stripe.com/capital/embedded-component-integration.md)
- [Build with the API](https://docs.stripe.com/capital/api-integration.md)
- [Launch checklist](https://docs.stripe.com/capital/launch-checklist.md)

