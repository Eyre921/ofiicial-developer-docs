---
title: "Netlify HTTPS Setup Guide"
source: https://docs.netlify.com/manage/domains/secure-domains-with-https/https-ssl.md
path: manage/domains/secure-domains-with-https/https-ssl
---

---
title: "HTTPS (SSL)"
description: "Take advantage of automatically provisioned and renewed TLS certificates to manage HTTPS for your site or use your own custom certificate."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Netlify offers free HTTPS on all sites, including automatic certificate creation and renewal. Our certificates use the modern TLS protocol, which has replaced the now deprecated SSL standard.

HTTPS brings a lot of advantages:

- **Content integrity.** Without HTTPS, free Wi-Fi services can inject ads into your pages.
- **Security.** If your site has a login or accepts form submissions, HTTPS is essential for your users' security and privacy.
- **SEO.** Google search results prioritize sites with HTTPS enabled.
- **Referral analytics.** HTTPS-enabled sites will not send referral data to sites without HTTPS enabled.
- **HTTP/2.** Boost your sites' performance - [HTTP/2](#http-2) requires HTTPS.

## Certificate service types

Netlify offers two different ways of providing a certificate for HTTPS.

**Netlify-managed certificates** are offered to all Netlify sites for free. Find details for this in the section on [Netlify-managed certificates](#netlify-managed-certificates).

**Custom certificates** are a way for you to provide a certificate that matches your specifications - things like a wildcard certificate or an Extended Validation (EV) certificate. If you'd like to provide your own custom certificate, refer to [Custom certificates](#custom-certificates) below for more details.

For all certificate service types, Netlify enables HTTPS for only Netlify-hosted content. If you use Netlify to host content on an apex domain and other hosts for content on subdomains, Netlify cannot enable HTTPS for the subdomains with externally-hosted content. 

### Netlify-managed certificates

When you create a new site on Netlify, it's instantly secured at the Netlify-generated URL (for example, `https://brave-curie-12345.netlify.app`). If you add a [custom domain](/manage/domains/get-started-with-domains), we will automatically provision a certificate with [Let's Encrypt](https://letsencrypt.org/), enabling HTTPS on your domain. Certificates are generated and renewed automatically as needed.

To ensure that only Netlify can create Let's Encrypt certificates for your custom domain, you can add a [Certificate Authority Authorization (CAA) record](https://letsencrypt.org/docs/caa/) to your DNS provider that specifies Netlify's `accounturi`, which is `https://acme-v02.api.letsencrypt.org/acme/acct/54403714`.

For example, this is a CAA record for our domain `petsofnetlify.com`:

```
petsofnetlify.com         300	IN	CAA	0 issue "letsencrypt.org;accounturi=https://acme-v02.api.letsencrypt.org/acme/acct/54403714"
```

### Tip - Use Netlify DNS for automatic wildcards

If your domain uses [Netlify DNS](/manage/domains/why-netlify-dns), we'll automatically provision a wildcard certificate, which ensures instant HTTPS for all of the Netlify sites using subdomains of that domain.

In rare circumstances, there can be problems when provisioning a certificate for some domains. You can check the status of your site's certificates in 
### NavigationPath Component:

Domain management > HTTPS
.

If you're having trouble with the automatic provisioning, visit [Troubleshoot SSL and HTTPS](/manage/domains/troubleshooting/troubleshoot-ssl-and-https) or the [troubleshooting page](/manage/domains/troubleshooting-tips) for an error message guide and other tips. You can also visit our Forums for a verified Support Guide on [SSL / TLS certificate provisioning](https://answers.netlify.com/t/support-guide-ssl-tls-certificate-provisioning/1300). 

#### Domain aliases

Your certificate will include all your [domain aliases](/manage/domains/configure-domains/add-a-domain-alias) when it's issued, but note that DNS also needs to be configured _in advance_ for all aliases for us to include them on your certificate. Visit the [troubleshooting page](/manage/domains/troubleshooting-tips) for more information on confirming the new configuration.

### Caution - Avoid rate limiting for subdomains

If you have more than 5 aliases that are subdomains of the same domain, you might run into rate limits with our certificate provider. In that case we recommend you provide your own wildcard certificate using Netlify DNS or [contact support](https://www.netlify.com/support) for our assistance for getting them set up with our certificate provider. Please do this _before adding any aliases_!

### Custom certificates

If you already have a certificate for your domain and prefer that to Netlify's domain-validated certificate, you can install your own.

To install a certificate, you'll need:

- the certificate itself, in X.509 PEM format (usually a .crt file)
- the unencrypted private key you used to request the certificate
- a chain of intermediary certificates from your Certificate Authority (CA)

In 
### NavigationPath Component:

Domain management > HTTPS
, select **Set Custom Certificate**, then enter the information above. For tips on specific formatting and the contents of the certificate, visit our Forums for a verified support guide on [custom SSL certificates](https://answers.netlify.com/t/support-guide-tips-for-bringing-your-own-custom-ssl-certificates-to-netlify/53633).

### Caution - Renewal is not automatic

When the time comes to renew your custom certificate, Netlify cannot do this automatically. You will need to renew it at your Certificate Authority, then follow the steps above to install it on your Netlify site. For automatic renewal, you can switch to a [Netlify-managed certificate](#netlify-managed-certificates).

Netlify validates that the certificate matches the custom domain for your site and that the DNS record for the domain is pointed at Netlify, then installs your certificate. If your certificate covers several of your sites (in other words, if it's a wildcard certificate or uses Subject Alternative Names), you can install it on one site, and it will apply to all other sites covered by the certificate.

### Note - Using automatic deploy subdomains?

If you use a custom certificate for your site's domains, that certificate must explicitly include any new subdomains used for automatic deploy subdomains. The standard wildcard syntax, such as `*.company.com`, does not cover this new subdomain. Learn more about [custom certificates and automatic deploy subdomains](/manage/domains/manage-domains/automatic-deploy-subdomains#custom-certificate-requirements).

## HSTS preload

Most major browsers use a list of predefined domains to automatically connect to websites using HTTPS. This list is called the HTTP Strict Transport Security (HSTS) preload list. Your site can be included in this list if you follow the requirements in [hstspreload.org](https://hstspreload.org):

- Your custom domain must be accessible in the www subdomain. For example: `www.petsofnetlify.com`.
- You must include this header in your [`_headers` file](/manage/routing/headers) or [Netlify configuration file](/build/configure-builds/file-based-configuration):

### Tabs Component:

<TabItem label="_headers">
  ```
  /* 
    Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
  ```
  </TabItem>

  <TabItem label="netlify.toml">
  ```toml
  [[headers]]
    for = "/*"
    [headers.values]
      Strict-Transport-Security = '''
      max-age=63072000;
      includeSubDomains;
      preload'''
  ```
  </TabItem>

When this is set, the browser assumes that your site, along with all subdomains, can be accessed using HTTPS, and it will force those connections.

### Danger - This action is not easily reversible

Please make sure to only use the directive `preload` once you're confident that the domain _and all subdomains_ are ready to be served using _only_ HTTPS, since this setting is hard to remove once it's in place, [as described at hstspreload.org](https://hstspreload.org/#removal).

## HTTP/2

When HTTPS is enabled for your site, Netlify supports HTTP/2, a newer internet protocol engineered for faster web performance. This brings support for core HTTP/2 features like request multiplexing and compressed headers, but does not include server push capability.
