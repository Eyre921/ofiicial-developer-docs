---
title: "Netlify DNS and HTTPS Troubleshooting"
source: https://docs.netlify.com/manage/domains/troubleshooting-tips.md
path: manage/domains/troubleshooting-tips
---

---
title: "DNS & HTTPS troubleshooting tips"
description: "Reference tips to help get things working if you can't access a site's custom domain or branch subdomain. Review common problems with DNS or HTTPS setup."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

If you're having trouble accessing your site at your custom domain or branch subdomain, there is likely a problem with your DNS or HTTPS setup. This page includes tips and information to help get things working properly.

## DNS configuration

The `dig` command line tool is a great tool for quickly diagnosing and understanding DNS responses. It is built into Linux and Mac, but can also be installed on Windows. Alternatively, you can use an online tool to [run `dig` in the browser](https://toolbox.googleapps.com/apps/dig/).

NS1, the DNS provider backing Netlify DNS, has a great series of articles on [using DIG](https://ns1.com/articles/decoding-dig-output) to test and troubleshoot your DNS configuration.

### Inactive Netlify DNS zone

A common DNS configuration issue is an inactive Netlify DNS zone. This prevents our service from creating or updating the automatic Let's Encrypt SSL certificates for your custom domain. This can cause problems for branch subdomains. For more information, visit our Forums for a verified Support Guide on [how to detect and fix inactive Netlify DNS zones](https://answers.netlify.com/t/support-guide-how-to-detect-and-fix-inactive-netlify-dns-zones/21742).

## Custom certificate not working for automatic deploy subdomain

If a custom certificate is not working for your automatic deploy subdomain, ensure your certificate includes any new subdomains used for automatic deploy subdomains.

For example, for the automatic deploy subdomain  `early-access.company.com` , your custom certificate should include the domains `*.company.com, *.early-access.company.com` and not just `*.company.com`. 

Learn more about [custom certificates and automatic deploys subdomains](/manage/domains/manage-domains/automatic-deploy-subdomains#custom-certificate-requirements).

## Certificates and HTTPS

There are many reasons why adding a Netlify certificate or uploading a custom certificate might not work. The common causes are listed below, but if they don't seem to apply to you or you have additional questions, our [Support team](https://www.netlify.com/support) will be happy to help out!

1. Most importantly, you'll need to [**configure the DNS for the custom domain**](/manage/domains/get-started-with-domains) before Netlify can issue a certificate for you. Netlify must validate the domain in order to provision the certificate, and this step cannot be completed until the DNS records for your custom domain are pointing to our servers.

2. **All previous DNS settings must have their cache timeouts expired.** The [TTL setting](https://www.dnsknowledge.com/whatis/time-to-live-ttl/) on a DNS record determines how long the record may be cached. This cache must expire before your new DNS settings can be validated for certificate provisioning.

3. If your site is configured to go through another service (for example, using [Cloudflare "accelerate and protect"](https://answers.netlify.com/t/common-issue-why-isn-t-my-ssl-certificate-provisioning-automatically-with-cloudflare-netlify-are-there-other-problems-with-using-cloudflare-in-front-of-netlify/138), or similar), **you need to disable that routing before we can provision the certificate**. Netlify must handle TLS termination to be able to provision a certificate.

4. It is possible that the name servers we use have some old cached values for your domain name. You can attempt to **accelerate cache expiration** for your domains using the [Flush Cache tool](https://developers.google.com/speed/public-dns/cache) provided by Google Public DNS.

5. It is possible that we will get a certificate for one name (for example, `petsofnetlify.com`) and not for another (for example, `www.petsofnetlify.com` or some domain alias). In this case selecting **Renew certificate** should resolve the issue. If it doesn't, please post in the [Netlify Support Forums](https://answers.netlify.com/categories) so our support engineers can repair the certificate.

### HTTPS error messages

You can check the status of your certificate in 
### NavigationPath Component:

Domain management > HTTPS
. If there is a problem with the certificate, you may find one of the error messages below. (We're using `petsofnetlify.com` as an example.)

#### "petsofnetlify.com doesn't appear to be served by Netlify"

In order to make sure that the site is served by Netlify, check the HTTP response headers.

1. Examine the HTTP response headers in your browser's [dev tools](https://developer.chrome.com/docs/devtools/network/reference/#headers), using an [online checker](https://httpstatus.io/), or with the following terminal command:

   ```
   curl -s -v http://your-newly-configured-hostname.com 2>&1 | grep -i server
   ```

2. Check for a line that says `server: Netlify`. 

3. Repeat this for **each** domain connected to your site. If your custom domain is the apex domain or `www` subdomain (for example, `petsofnetlify.com` or `www.petsofnetlify.com`), we automatically serve your site and provision a certificate for both domains, so be sure they both have records pointing to Netlify.

The next steps depend on what you find in the HTTP response headers.

- If you do find `server: Netlify` in all response headers, but still receive this error, it may be caused by incorrect A records. For information on setting a proper A record with Netlify, refer to our documentation on [external DNS configuration](/manage/domains/configure-domains/configure-external-dns).

- If you don't find `server: Netlify` in all response headers, and you've eliminated the [common problem sources listed above](#certificates-and-https), please [contact support](https://www.netlify.com/support).

#### "petsofnetlify.com is not resolvable with a resolver that validates DNSSEC"

Netlify DNS doesn't support DNSSEC. To use Netlify DNS, disable DNSSEC with your domain registrar or previous DNS host. You can use tools like [DNSViz](http://dnsviz.net/) to figure out where DNSSEC is currently enabled. To keep DNSSEC enabled, you can stop using Netlify DNS and use [external DNS](/manage/domains/configure-domains/configure-external-dns) instead.
