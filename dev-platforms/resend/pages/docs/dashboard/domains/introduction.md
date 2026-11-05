---
title: "Verified Domains"
source: https://resend.com/docs/dashboard/domains/introduction
path: docs/dashboard/domains/introduction
---

An introduction to verified domains in Resend.

## Verified domains

Resend sends emails using a domain you own (i.e., not a shared or public domain). You must [add and verify at least one domain](/docs/add-a-domain) to send emails with Resend. You can optionally [configure your domain to receive emails](/docs/dashboard/receiving/custom-domains).

You can add and verify multiple [subdomains](#subdomains) from the same root domain (e.g., `newsletter.example.com` and `account.example.com`) to identify different sending purposes and still assure recipients and inbox providers that the emails come from you. This can protect the sending reputation of your transactional emails from any negative recipient response to your marketing emails, and allows you to configure different domain settings such as open and click tracking for each subdomain.

## Domain features

When you add a domain, you can choose to:

* Enable [open and click tracking](/docs/dashboard/domains/tracking) for your emails.
* Configure [Enforced Transport Layer Security (TLS)](/docs/dashboard/domains/tls) to ensure that you only send encrypted emails.
* Set a custom subdomain for the [Return-Path address](/docs/dashboard/domains/custom-return-path).
* Choose which [geographical region](/docs/dashboard/domains/regions) to send emails from to reach your recipients sooner.

After your domain is verified, you can:

* Send and receive emails [using any email address at your domain](/docs/knowledge-base/how-do-I-create-an-email-address-or-sender-in-resend#sender-email-addresses-in-resend) without any extra configuration.
* Implement [DMARC](/docs/dashboard/domains/dmarc) and [BIMI](/docs/dashboard/domains/bimi) to build trust and improve inbox placement.

## Subdomains

We recommend sending your emails from one or more subdomains (e.g., `updates.example.com`) instead of your root domain to isolate your sending reputation and to clearly communicate your intent to your recipients.

> [!NOTE]
>
> If you're [moving email from another provider](#moving-from-another-provider)
> that already sends from an address with an established reputation, keep that
> address instead.

You must [add each subdomain](/docs/add-a-domain) individually, and they will be displayed in the [**Domains** Dashboard page](https://resend.com/domains) as separate entries where you can manage and configure them independently.

There are several benefits to sending from a subdomain:

* **Sender intent:** clearly communicate your intent to your recipients, increasing trust through transparency.
* **Reputation control:** Using separate subdomains can help segment sending reputation.
* **Configuration settings**: [Enabling open and click tracking](/docs/dashboard/domains/tracking) for your marketing emails, while keeping it disabled for your important transactional emails such as password resets.

Subdomains of your main domain also help reinforce your brand identity and build trust with inbox providers.

Domains that look like your main brand but aren’t actually your main brand (e.g., `example-alerts.com` instead of `alerts.example.com`) can appear suspicious to spam filters and confusing to your recipients. Inbox providers may flag them as phishing or spoofing attempts, and your users are more likely to ignore, delete, or even report the emails as spam.

### Moving from another provider

If you already send emails from an address with an established reputation, keep sending from that address when you switch to Resend to preserve your reputation history. Follow the [existing domain warm up plan](/docs/knowledge-base/warming-up#existing-domain) to avoid any spikes in email volume that might be concerning to inbox service providers.

If you have only sent a few emails, or you send irregularly, your domain has little history to lose if you start sending from a new subdomain in Resend, such as `news.example.com`. Follow the [new domain warm up plan](/docs/knowledge-base/warming-up#new-domain) to maximize your deliverability right from the start.

If you keep using an established email address for your marketing emails, add and warm up a new subdomain for your transactional emails, such as `auth.example.com`. This keeps your existing sender reputation for marketing emails, which are more likely to benefit from your history than transactional emails.

## Domain management

You can view and manage your domains from the [Domains Dashboard page](https://resend.com/domains). The Dashboard allows all members of your team to create, verify, retrieve, update, and delete your domains.

You can also manage your sending and receiving domains using the [API](/docs/api-reference/domains/create-domain), the [CLI](/docs/cli#domains), or the [MCP server](/docs/mcp-server).

Learn more about [managing your domains](/docs/dashboard/domains/manage-domains).

## Related Guides

See how to use Resend's verified domain features.

> [card] [Manage domains](/docs/dashboard/domains/manage-domains)

> [card] [Implement DMARC](/docs/dashboard/domains/dmarc)

> [card] [Enable Tracking](/docs/dashboard/domains/tracking)

> [card] [Enforced TLS](/docs/dashboard/domains/tls)

> [card] [Custom return path](/docs/dashboard/domains/custom-return-path)

> [card] [Choose region](/docs/dashboard/domains/regions)

> [card] [Claim a domain](/docs/dashboard/domains/claim)

> [card] [DNS provider guides](/docs/knowledge-base/introduction#dns-guides)
