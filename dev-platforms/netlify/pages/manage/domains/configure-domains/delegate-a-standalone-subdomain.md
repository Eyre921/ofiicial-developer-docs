---
title: "Delegate Subdomain to Netlify DNS"
source: https://docs.netlify.com/manage/domains/configure-domains/delegate-a-standalone-subdomain.md
path: manage/domains/configure-domains/delegate-a-standalone-subdomain
---

---
title: "Delegate a standalone subdomain"
description: "Delegate a subdomain to Netlify DNS without bringing the related apex domain."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

You can bring just a subdomain to Netlify DNS and keep your apex domain on a separate domain registrar. This makes all the benefits of Netlify DNS available to your subdomain, including automated wildcard SSL certificates and expanded use cases for your site with branch subdomains.

For example, you can delegate `docs.example.com` to Netlify DNS and keep `example.com` on a different [domain registrar](/manage/domains/domains-fundamentals/domains-glossary#domain-registrar).

If you delegate the stand-alone subdomain `docs.example.com` to Netlify DNS, your site gains these advantages:
  - **Automatic site security benefits.** Netlify DNS provisions your subdomain, and all subdomains of your subdomain, with [wildcard SSL certificates](/manage/domains/secure-domains-with-https/https-ssl).
  - **More use cases with branch subdomains.** Your site can serve different content from different branches using [branch subdomains](/manage/domains/domains-fundamentals/domains-glossary#branch-subdomain). For example, the `staging` branch of your site can serve unique content at `staging.docs.example.com`. Likewise, your site's `beta` branch can serve unique content at `beta.docs.example.com`.
  - **Wider reach with IPv6 support.** Your subdomain can reach a wider audience with [IPv6](/manage/domains/configure-domains/enable-ipv6), which you can enable for your subdomain in the Netlify UI.
  - **Performance gains with the Netlify CDN.** Your site will be served from our global CDN, from the server closest to your site visitors. Between this and CDN-level routing, sites will often gain a performance boost from being served on the Netlify CDN.

## Netlify DNS support for subdomains and apex domains

When you add an [apex domain](/manage/domains/domains-fundamentals/domains-glossary#apex-domain) to Netlify DNS, subdomains of this apex domain are managed by Netlify DNS automatically.

If you delegate a stand-alone subdomain to Netlify DNS, additional configuration is required outside of Netlify. You will need to access the domain registrar for the related apex domain to set NS records ([Name Server records](/manage/domains/configure-domains/dns-records#supported-record-types) for your subdomain.

For example, if you've already added the apex domain `petsofnetlify.com` to Netlify DNS and you add the subdomain `rover.petsofnetlify.com` to your site on Netlify, then Netlify DNS will automatically manage this subdomain for you.

Alternatively, if you have an apex domain that is already managed by an external domain registrar, such as `example.com`, and you want to bring just the subdomain `docs.example.com` to Netlify DNS, then you need to follow the steps below.

## Delegate a stand-alone subdomain to Netlify DNS

There are two main starting places in the Netlify UI to delegate just a subdomain to Netlify DNS: 
- **From your team's Domains page:** If you have access to your team's 
### NavigationPath Component:

Domains
 page, then you can delegate a subdomain to Netlify DNS for your team and use this subdomain for one of your team's sites. This flow allows you to wait for DNS propagation to complete before adding this subdomain to your site.
- **From your site configuration:** If you only have access to a single site or want to add a subdomain directly to a site before the domain is live and then delegate it to Netlify DNS, then you can manage this through your site's 
### NavigationPath Component:

Domain management
 configuration.

### Note

Avoid <code>www</code> as a stand-alone subdomain</span>">
We recommend that you do not delegate `www` as a stand-alone subdomain. Netlify treats `www` subdomains and apex domains as alternates for each other. Attempts to delegate `www` as a stand-alone subdomain may lead to inconsistent behavior if one site is using the `www` subdomain while another uses the apex domain.

### Delegate a subdomain to Netlify DNS through site configuration

When you delegate a subdomain to Netlify DNS through your site configuration, we recommend you add your stand-alone subdomain and then delegate this domain to Netlify DNS.

1. Check the [domain registrar](/manage/domains/domains-fundamentals/domains-glossary#domain-registrar) that manages your apex domain to make sure it supports NS records for subdomains. You will need to access this domain registrar to update the NS records for your subdomain later in these steps.

2. Navigate to your site and go to 
### NavigationPath Component:

Domain management
.

3. Select **Add custom domain**. 

4. Enter your stand-alone subdomain, such as `docs.example.com`. This flow assumes that your subdomain stems from an apex domain, such as `example.com`, that is already registered through an external domain registrar.

5. Select **Verify**, then **Add subdomain**. Now this subdomain is connected to your site but is not yet delegated to Netlify DNS.

6. To delegate your subdomain to Netlify DNS, next to your subdomain, use the **Options** menu to select **Set up Netlify DNS**.
    ![](/images/domains-https-menu-to-delegate-to-netlify-dns-from-site-settings.png)

7. Follow the UI prompts to delegate your subdomain to Netlify DNS. During this UI flow, you may be asked to select **Verify** and **Add subdomain** again.

8. To complete your subdomain delegation setup, copy the NS records for your subdomain from the Netlify UI. Log in to the domain registrar that manages the related apex domain, such as `example.com`, and enter NS records for your subdomain. 

   These DNS updates can take up to 48 hours to take effect. Learn more in our [Support Guide on DNS propagation](https://answers.netlify.com/t/support-guide-why-do-dns-ssl-changes-take-up-to-48-hours-to-propagate-ttl/9359).
