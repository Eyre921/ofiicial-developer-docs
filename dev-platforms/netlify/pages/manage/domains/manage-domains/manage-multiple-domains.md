---
title: "Netlify Multiple Domains"
source: https://docs.netlify.com/manage/domains/manage-domains/manage-multiple-domains.md
path: manage/domains/manage-domains/manage-multiple-domains
---

---
title: "Manage multiple domains"
description: "Your production site or app can support more than one domain through domain aliases, redirects, subdomains, and more."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Your production site or app can support more than one domain through domain aliases, redirects, subdomains, and more.

Find the domains associated with your site or app in the **Domain management** section of your site configuration.

## Manage domains for your production site

You can find the domains for your production site at 
### NavigationPath Component:

Domain management > Production domains
. 

## Manage domains for your team's sites 

From your Team Overview's domains list, you can: 
- review your domain's DNS records (if applicable)
- review [Netlify name servers](/manage/domains/configure-domains/netlify-name-servers) for your domain
- transfer a domain between two team accounts you own
- delete DNS zones

To find your Team Overview's domains list:

> **Snippet** component (self-closing)

2. Select 
### NavigationPath Component:

DNS
 from the left sidebar.
    ![DNS option highlighted from team dashboard](/images/dns-option-from-team-dashboard.png)

3. Next, select a domain from the domains list for your team.

You can find your domain's DNS records (if applicable) and [Netlify name servers](/manage/domains/configure-domains/netlify-name-servers).

For more help reviewing DNS records, check out our docs on [Managing DNS records](/manage/domains/manage-domains/manage-dns-records/).

## Apex domains and `www` subdomains

When you assign an apex domain (eg. `petsofnetlify.com`) _or_ a `www` subdomain (eg. `www.petsofnetlify.com`) as the primary domain for your site, two entries are added to the **Production domains** panel:

- one entry for the apex domain, and
- one entry for the `www` subdomain.

The primary domain is the custom domain you entered. The other entry is for the alternative domain that gets redirected automatically to the primary domain.

- If you set the `www` subdomain as your primary domain, Netlify will automatically redirect the apex domain to the `www` subdomain.
- If you set the apex domain as your primary domain, Netlify will automatically redirect the `www` subdomain to the apex domain.

If you're using external DNS, **we strongly recommend setting the `www` subdomain (or another subdomain) as your primary domain**. If you want to set an apex domain as your primary domain, we recommend using Netlify DNS. Our blog post [How to Set Up Netlify DNS](https://www.netlify.com/blog/2020/03/26/how-to-set-up-netlify-dns-custom-domains-cname-a-records/) has more details on these recommendations.

### Tip

Redirects for non-<code>www</code> subdomains</span>">
Though Netlify automatically redirects between the apex domain and `www` subdomain, we don't do this for any other subdomains. You can configure this behavior yourself with [domain-level redirects](/manage/routing/redirects/redirect-options#domain-level-redirects).

## Branch subdomains

_This feature requires [Netlify DNS](/manage/domains/why-netlify-dns)._

Netlify can generate a branch subdomain for specified branch deploys using your site's primary custom domain. The resulting branch subdomains use the syntax `branchname.yourcustomdomain.com`. For example, if your custom domain is `example.com` and your branch is `staging`, you can access the latest deploy of that branch at `staging.example.com`.

To use this feature, you must first [enable branch deploys](/deploy/deploy-overview#branch-deploy-controls) in your site's deploy settings and have at least one deployed branch. You can then configure branch subdomains in 
### NavigationPath Component:

Domain management > Branch subdomains
.

Learn more about [branch subdomains and branch deploys](/manage/domains/manage-domains/manage-domains-for-branch-deploys/#custom-branch-subdomains-for-branch-deploys).

### Set up Netlify DNS for branch subdomains

If you want to use a custom domain in your branch subdomain that is not already delegated to Netlify DNS, you must delegate your custom domain to Netlify's name servers.

To set up Netlify DNS for branch subdomains:

1. Go to 
### NavigationPath Component:

Domain management > Branch subdomains
 and select **New subdomain**.

2. If your domain doesn't already use Netlify DNS, you'll see a panel displaying the Netlify name servers for your domain. These are in a format similar to `dns1.p01.nsone.net`.

3. Log in to your domain registrar (where you bought and registered your domain) and find their settings for updating name servers.

4. Replace your current name servers with the Netlify name servers displayed in the Netlify UI.

5. Save your settings at your domain registrar.

### Note - DNS propagation time

It may take up to 24 hours for the name server changes to propagate and for your SSL certificate to be issued. During this time, your branch deploys may not be available over HTTPS.

