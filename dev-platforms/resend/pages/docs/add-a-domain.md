---
title: "Add and verify a domain"
source: https://resend.com/docs/add-a-domain
path: docs/add-a-domain
---

Get started sending emails by adding a domain to your account.

Resend sends emails using a domain you own. Before you can send or receive emails with Resend, you must have a verified domain associated with your account.

> [!NOTE]
>
> If you don't own a domain, please purchase one from a domain registrar such as
> [Cloudflare](https://www.cloudflare.com/) or
> [Namecheap](https://www.namecheap.com/) before continuing.

## Choose a sending domain

For deliverability best practices, send emails from a subdomain (e.g., `notifications.example.com`) instead of your root domain (`example.com`).

If you are [transferring from another provider](/docs/dashboard/domains/introduction#moving-from-another-provider) and already have an established sender reputation for your marketing emails, add the domain or subdomain that matches your existing `from` address, then verify it to continue sending from that address.

You can have multiple subdomains associated with your root domain (e.g., `updates.example.com`, `notifications.example.com`). Each one must be added and verified individually, and they will be displayed as separate entries in the [**Domains** Dashboard page](https://resend.com/domains) where you can manage and configure them independently.

> [!NOTE]
>
> If you only verify a subdomain, you must send from an address at that subdomain, not your
> root domain.
>
> For example, if you verify `newsletters.example.com`, you can
> send from `updates@newsletters.example.com` but not from `updates@example.com`.
>
> If you encounter a 403 domain mismatch error, check the [**Logs** Dashboard page](https://resend.com/logs) and make sure the `from` field in your API requests matches one of your verified domains.

## Add a domain

You can add and verify a domain you own in four ways:

* in the [**Domains** Dashboard page](/docs/dashboard/domains/introduction)
* using the [Resend API](/docs/api-reference/domains/create-domain)
* with a [Resend CLI command](/docs/cli#domains)
* with the [Resend MCP server](/docs/mcp-server)

To add a new domain from the Resend Dashboard:

**1. In your Resend Dashboard, navigate to the **Domains** page.**

**2. Click the **Add Domain** button.**

**3. Enter your domain (including a subdomain, if you wish) to use for your Resend emails.**

Enter the existing domain you send emails from, or choose a subdomain that reflects the purpose of your emails, such as `customers.example.com` or `updates.example.com`.

If you add a domain already used by another team, the Dashboard will notify you and you can [claim the domain](/docs/dashboard/domains/claim) to transfer it to your team.

**4. Choose a region from the list provided.**

Select a region to send your emails from. Choose one that is closest to the majority of your recipients.

**5. (optional) Enter a custom subdomain for the Return-Path address if desired.**

Return-Path defaults to `send.example.com`, although you can [provide a custom path](/docs/dashboard/domains/custom-return-path).

**6. Update your DNS records with values provided by Resend.**

View the **Records** tab for your domain to find the records to provide to your DNS host provider. Adding these records will verify that you own the domain and have the correct permissions to send and receive emails.

Provide the DomainKeys Identified Mail (DKIM) and Sender Policy Framework (SPF) configurations (`TXT` and `MX` or `CNAME` records) to your DNS provider. These records must match exactly what Resend generated. Copy and paste the records to avoid configuration errors.

> [!TIP]
>
> Consult one of our [DNS provider guides](/docs/knowledge-base/introduction) for specific examples of updating your DNS records with your host. Also, when shown a CNAME, make sure *not* to use proxying features (e.g., Cloudflare's orange cloud) for that record, as it will prevent verification from completing.

**7. Wait for DNS verification to complete**

When this process is completed correctly, your domain will often verify within 15 minutes of adding the DNS records. However, DNS changes can occasionally take up to 72 hours to propagate globally.

You can use Resend's [dns.email tool](https://dns.email/) to check that your records are visible publicly. If verification hasn't completed after 72 hours, use the **Restart verification** button in the Resend Dashboard to trigger a fresh verification check.

**8. Add a DMARC record.**

After your domain is verified, implement Domain-based Message Authentication, Reporting, and Conformance ([DMARC](/docs/dashboard/domains/dmarc)) to build additional trust in your domain and protect against email spoofing.

This is an email authentication protocol to verify email senders and to allow receivers to reject unauthenticated messages, and is important for email deliverability.

**9. (optional) Update your domain's Resend configuration options.**

After your domain is verified, you may wish to [enable open and click tracking](/docs/dashboard/domains/tracking) or [enforce Transport Layer Security (TLS)](/docs/dashboard/domains/tls).

## Learn more

> [card] [Domains introduction](/docs/dashboard/domains/introduction)
>
> Learn more about configuring, and managing your verified domains.

> [card] [Multi-tenant domain setup](/docs/knowledge-base/setting-up-resend-for-multi-tenants)
>
> Learn how to configure Resend for SaaS platforms where tenants send emails
> from their own domains.

## Next steps

> [card] [Add a DMARC record](/docs/dashboard/domains/dmarc)
>
> Implement Domain-based Message Authentication, Reporting, and Conformance
> (DMARC) to build trust in your domain and protect against email spoofing.

> [card] [Quickstart tutorials](/docs/introduction)
>
> Send your first transactional email with a quick tutorial for your language
> or framework.
