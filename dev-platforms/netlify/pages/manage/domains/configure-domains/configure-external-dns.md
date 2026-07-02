---
title: "External DNS Configuration"
source: https://docs.netlify.com/manage/domains/configure-domains/configure-external-dns.md
path: manage/domains/configure-domains/configure-external-dns
---

---
title: "Configure external DNS for a custom domain"
description: "Configure an external DNS provider to point your domain to our platform. You can use external DNS for a subdomain or apex domain you registered externally."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

If you've assigned an externally registered domain to your site, and you don't want to use [Netlify DNS](/manage/domains/why-netlify-dns), you need to configure your external DNS provider to point your domain to Netlify.

To access customized details about the DNS records you need to configure, go to 
### NavigationPath Component:

Domain management > Production domains
 and select **Pending DNS verification** next to the custom domain.

![The link is between the domain name and the options menu.](/images/domains-https-check-dns-configuration.png)

The next steps vary depending on the type of domain or subdomain.

- For a [subdomain](/manage/domains/domains-fundamentals/domains-glossary#subdomain) of a domain you own, such as `blog.petsofnetlify.com` or `www.petsofnetlify.com`, follow the directions below for [subdomain configuration](#configure-a-subdomain).
- For an [apex domain](/manage/domains/domains-fundamentals/domains-glossary#apex-domain) with no subdomain, such as `petsofnetlify.com`, make sure to read our [advice about using apex domains](/manage/domains/manage-domains/manage-multiple-domains#apex-domains-and-www-subdomains), then follow the directions below for [apex domain configuration](#configure-an-apex-domain).

### Note

Special handling for apex and <code>www</code></span>">
If you assign an apex domain or a `www` subdomain to your site, Netlify will automatically add _both_ the apex domain and the `www` subdomain. This means you should follow directions for both [configuring a subdomain](#configure-a-subdomain) and [configuring an apex domain](#configure-an-apex-domain). For more information, visit the section on [apex domains and `www` subdomains](/manage/domains/manage-domains/manage-multiple-domains#apex-domains-and-www-subdomains).

### Tip - Need to delegate just a subdomain?

You can delegate a subdomain to Netlify DNS without the apex domain. Learn more in this [doc](/manage/domains/configure-domains/delegate-a-standalone-subdomain).

## Configure a subdomain

To point a subdomain such as `blog.petsofnetlify.com` or `www.petsofnetlify.com` to your site on Netlify, you must first [add the domain to your site](/manage/domains/manage-domains/assign-a-domain-to-your-site-app) on Netlify and then create a CNAME record with your DNS provider.

For example, if your site's domain is `blog.petsofnetlify.com` and your [Netlify subdomain](/manage/domains/domains-fundamentals/domains-glossary#subdomain) is `brave-curie-12345.netlify.app`:

1. Follow the instructions to [add the domain](/manage/domains/manage-domains/assign-a-domain-to-your-site-app) `blog.petsofnetlify.com` to the `brave-curie-12345.netlify.app` site on Netlify. At the end of the process, Netlify provides a CNAME record to add to your DNS provider.
2. Find your DNS provider's DNS record settings for your apex domain, `petsofnetlify.com`.
3. On your DNS provider's site, add the CNAME record with your subdomain, `blog`, as the host.
4. Point the record to your Netlify subdomain, `brave-curie-12345.netlify.app`.

### Caution - High-Performance Edge uses a different subdomain

If your site is on the High-Performance Edge, point the record to the dedicated subdomain in your High-Performance Edge onboarding PDF.

5. Save your settings. It may take a full day for the settings to propagate across the global Domain Name System.

If your site uses the `www` subdomain, as in `www.petsofnetlify.com`, you will use the same procedure described above. Once you configure the `www` subdomain, an apex domain will also be added automatically to your site. You'll need to follow the steps in the section below to configure the apex domain too. Learn more about our [special handling for `www` subdomains](/manage/domains/manage-domains/manage-multiple-domains#apex-domains-and-www-subdomains).

## Configure an apex domain

Unlike subdomains, apex domains don't support CNAME records. You must configure your apex domain with an ALIAS, ANAME, flattened CNAME, or A record. Different DNS providers support different record types. Depending on what your DNS provider supports, use either the recommended configuration or the fallback option below.

If your [DNS provider supports ALIAS, ANAME, or flattened CNAME records](https://answers.netlify.com/t/support-guide-which-are-some-good-dns-providers-for-alias-aname-support/211), use this recommended configuration, which is more resilient than the fallback option.

1. Find your DNS provider's DNS record settings for your apex domain, such as `petsofnetlify.com`.
2. Add an **ALIAS**, **ANAME**, or **flattened CNAME record**. Depending on your provider, leave the host field empty or enter `@`.
3. Point the record to Netlify's load balancer at: `apex-loadbalancer.netlify.com`.

### Caution - High-Performance Edge uses a different load balancer

If your site is on the High-Performance Edge, point the record to the High-Performance Edge load balancer noted in the [**Pending DNS verification** modal's customized details](#check-dns-configuration).

4. Save your settings. It may take a full day for the settings to propagate across the global Domain Name System.

If your DNS provider does not support ALIAS, ANAME, or flattened CNAME records, use this fallback option.

1. Find your DNS provider's DNS record settings for your apex domain, such as `petsofnetlify.com`.
2. Add an **A record**. Depending on your provider, leave the host field empty or enter `@`.
3. Point the record to Netlify's load balancer IP address: `75.2.60.5`.

### Caution - High-Performance Edge uses a different load balancer

If your site is on the High-Performance Edge, point the record to the High-Performance Edge load balancer IP address noted in the [**Pending DNS verification** modal's customized details](#check-dns-configuration).

4. Save your settings. It may take a full day for the settings to propagate across the global Domain Name System.

In both cases, the apex domain eventually resolves to our load balancer IP address. This means the apex domain can't take advantage of direct DNS routing on a [global CDN like Netlify's](https://www.netlify.com/products/edge/). Because of this, we recommend using a subdomain for your [primary domain](/manage/domains/configure-domains/add-a-domain-alias) when using external DNS. 

### Note - Special handling for apex domains

If you assign an apex domain to your site, Netlify will automatically add a `www` subdomain for the domain as well, which requires the [subdomain configuration](#configure-a-subdomain) as described above. To find out how this affects your site configuration, visit the section on [apex domains and `www` subdomains](/manage/domains/manage-domains/manage-multiple-domains#apex-domains-and-www-subdomains).

## DNS record propagation

Depending on your DNS provider, **changes to DNS records can take several hours to propagate and take effect for the entire internet.**

If more than 24 hours have passed since you configured your DNS records, and your site is still not accessible at your custom domain, try our [DNS troubleshooting tips](/manage/domains/troubleshooting-tips).

