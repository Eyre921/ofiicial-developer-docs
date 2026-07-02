---
title: "Netlify DNS: Manage Domains"
source: https://docs.netlify.com/manage/domains/set-up-netlify-dns.md
path: manage/domains/set-up-netlify-dns
---

---
title: "Set up Netlify DNS"
description: "Set up Netlify DNS for your new or existing domain."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Set up Netlify DNS for your new or existing domain.

Netlify DNS offers you advanced subdomain automation and deployment features, such as: 
- standalone subdomains, such as `docs.company.com` without delegating `company.com`
- branch deploys, such as deploying the `staging` branch of your site/app
- a wildcard SSL certification for all your deploys

Netlify DNS also ensures that your site uses our CDN for the apex domain as well as subdomains like www. Learn more in [Why Netlify DNS](/manage/domains/why-netlify-dns).

## Enable Netlify DNS

There are several pathways to enabling Netlify DNS. 

### For a domain already added to your site

If you already assigned a production domain to your site, to set up Netlify DNS:

1. Go to your site's dashboard, then select **domain management** from the left sidebar. 

2. Next to your domain, select **Options**, then **Set up Netlify DNS**.

3. Follow the prompts to finish setting up Netlify DNS.

### For a domain you already registered

If your domain is registered with another provider, you can still take advantage of Netlify's managed DNS service by delegating your domain to Netlify. 

#### Delegate to Netlify

### Caution - Transfer your DNS records first!

If you have any existing records on your current DNS provider, such as MX records for email service, make sure to copy them to Netlify DNS first. This will ensure continuous service as you change providers.

Visit the [DNS records](/manage/domains/configure-domains/dns-records) page or the verified Support Guide in our Forums on [migrating a domain to Netlify-managed DNS](https://answers.netlify.com/t/support-guide-how-do-i-migrate-a-domain-to-netlify-managed-dns-with-zero-downtime/3397) for details.

Assuming you have copied existing DNS records from your current provider, the final step to making your DNS records live is to update your domain registrar with the name servers that will be authoritative for your domain.

The process for changing your domain's name servers varies from registrar to registrar. Check your domain registrar's documentation for updating name servers. For your convenience, we've gathered links to instructions for popular registrars [GoDaddy](https://www.godaddy.com/help/change-nameservers-for-my-domains-664), [Google Domains](https://support.google.com/domains/answer/3290309), [AWS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register-other-dns-service.html), [Name.com](https://www.name.com/support/articles/205934547-changing-nameservers-for-dns-management), and [Hover](https://help.hover.com/hc/en-us/articles/217282477-How-to-Change-your-domain-name-servers-DNS-servers).

To delegate your domain to Netlify:

> **Snippet** component (self-closing)

2. Select 
### NavigationPath Component:

DNS
 from the left sidebar.
    ![DNS option highlighted from team dashboard](/images/dns-option-from-team-dashboard.png)
2. Select your domain.
3. Make note of the four name servers listed in the **Name servers** panel.
4. Log in to the account you have with your domain registrar and find their instructions for updating name servers.
5. Replace the name servers with the name servers for your Netlify DNS zone. If your registrar requires name server IP addresses, visit our Forums for a verified Support Guide on [finding the IP addresses for Netlify's name servers](/manage/domains/configure-domains/netlify-name-servers/).

It may take up to a day for the changes to propagate to the public internet.

### Tip - Next steps

Once your name server settings have propagated across the domain name system, you're ready to start using your domain and its subdomains.

- To use the domain or a subdomain to access a Netlify site, visit the instructions for [assigning a domain to a site](/manage/domains/manage-domains/assign-a-domain-to-your-site-app).
- If you want to point your domain or a subdomain to another service, like an email provider, visit the [DNS records](/manage/domains/configure-domains/dns-records) doc for details.
- If it's been more than 24 hours, and your domain doesn't seem to have propagated yet, visit the [troubleshooting](/manage/domains/troubleshooting-tips) page for tips and resources.

### For a new domain you need to buy and register

Check out our instructions to [register and buy a domain](/manage/domains/configure-domains/register-and-buy-a-domain) from Netlify.

