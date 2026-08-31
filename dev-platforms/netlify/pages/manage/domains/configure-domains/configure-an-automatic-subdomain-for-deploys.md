---
title: "Netlify Automatic Deploy Subdomains"
source: https://docs.netlify.com/manage/domains/configure-domains/configure-an-automatic-subdomain-for-deploys.md
path: manage/domains/configure-domains/configure-an-automatic-subdomain-for-deploys
---

---
title: "Configure an automatic subdomain for deploys"
description: "Apply a custom domain to your site's Deploy Previews or branch deploys, so you can share branded deploy URLs and unlock new services and auth flows."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

With automatic deploy subdomains, you can set up automatically branded URLs for Deploy Previews or branch deploys - unifying your site's preview environments, auth flows, third-party services, and other site versions with a shared custom domain.

Automatic deploy subdomains are a type of custom domain that you can set for all Deploy Previews or all branch deploys.

![Diagram showing that `early-access.company.com` is the automatic deploy subdomain for the Deploy Preview URL of `https://deploy-preview-42.early-access.company.com`.](/images/domains-https-ads-defined.png)

### Use cases 

When you set up an automatic deploy subdomain for all of your Deploy Previews or branch deploys, you can:
- Share branded deploy URLs that don't include the Netlify subdomain. For example, build greater trust with your stakeholders by sharing `deploy-preview-42.company.com` instead of `deploy-preview-42--mysitename.netlify.app`.
- Use third-party services the way you do for your production site, such as auth flow services that rely on a custom domain.
- Ensure deploys are "trusted" and in the "allowed domain list" for any third-party scripts or services that require this.
- Meet internal security requirements while leveraging Netlify's Deploy Previews and branch deploys to preview and collaborate on changes before they go live.

Once you configure an automatic deploy subdomain, Netlify uses this custom domain for your Deploy Previews and/or branch deploys by default within the Netlify UI, the API, CLI, and deploy notifications.

### Domain requirements 

The custom domain you set as your automatic deploy subdomain must be managed by [Netlify DNS](/manage/domains/why-netlify-dns) and available to your team.

By default, domains managed by Netlify DNS can be applied to your Deploy Previews or branch deploys.

For example, if you already delegated `company.com` to Netlify DNS, then subdomains of `company.com`, such as `early-access.company.com`, are also delegated to Netlify DNS by default. That means you can use `early-access.company.com` as your automatic deploy subdomain.

![Diagram defining parts of the Deploy Preview URL `https://deploy-preview-42.early-access.company.com`, where the Deploy Preview prefix is `deploy-preview-42`, the optional newly added subdomain is `early-access` and `company.com` is the domain managed by Netlify DNS.](/images/domains-https-ads-parts-defined-for-deploy-previews.png)

If you want to use a custom domain that Netlify DNS does not already manage, add the custom domain to your Netlify team and configure it to be managed by Netlify DNS. Learn more in these [domain setup steps](/manage/domains/manage-domains/automatic-deploy-subdomains#use-a-new-custom-domain-for-your-automatic-deploy-subdomain).

### Tip - Want to use a subdomain without bringing the apex domain to Netlify DNS?

You can bring a subdomain to Netlify DNS without the apex domain. For example, you can delegate  `docs.company.com` to Netlify DNS without also delegating `company.com`. Learn more about [stand-alone subdomain support](/manage/domains/configure-domains/delegate-a-standalone-subdomain).

### Example deploy URLs

| Site deploys | Netlify subdomain | Automatic deploy subdomain |
|----|----|----|
| [Deploy Preview](/deploy/deploy-overview#definitions) | `deploy-preview-42--mysitename.netlify.app` | `deploy-preview-42.company-internal-testing.com` |
| [Branch deploy](/deploy/deploy-overview#definitions), e.g. `staging` branch |`staging--mysitename.netlify.app` | `staging.company-internal-testing.com` |
| [Atomic deploy permalink](/manage/domains/domains-fundamentals/domains-glossary#atomic-deploy-permalink) | Uses the Netlify subdomain and a deploy ID, such as `1234abcd12acde000111cdef--mysitename.netlify.app`. | N/A |

When you set an automatic deploy subdomain for all Deploy Previews or all branch deploys, your deploys are still accessible at the Netlify subdomain, such as `deploy-preview-42--mysitename.netlify.app` or `staging--mysitename.netlify.app`.

### Note - Using High-Performance Edge?

If your site is on the [High-Performance Edge](https://www.netlify.com/platform/core/high-performance-edge/), then automatic deploy subdomains are served from the High-Performance Edge. However, Netlify subdomains (`*.netlify.app`) are always served from the standard network.

Your [deploy permalinks](/deploy/deploy-overview#definitions), which offer unique URLs for successful deploys of your site, will continue to use the Netlify subdomain. Unlike other deploy URLs, deploy permalinks do not update with new Git commits. Instead, Netlify generates new deploy permalinks for each successful deploy of your site.

### Tip - Not sure if you want to use Deploy Previews or branch deploys?

Deploy Previews are scoped to a pull/merge request while branch deploys are scoped to a branch. Branch deploys can offer a longer-standing URL than Deploy Previews since they are based on the branch name and not the pull/merge request. Learn more about the difference between these deploys in these [docs](/deploy/deploy-overview#branch-deploys-versus-deploy-previews).

## Automatic deploy subdomains for Deploy Previews

Deploy Previews are automatically enabled for all sites using continuous integration with Netlify. If your site doesn't have Netlify continuous integration set up, check out [these docs](/deploy/create-deploys#deploy-with-git).

### Set an automatic deploy subdomain for Deploy Previews

To set up an automatic deploy subdomain for your site's Deploy Previews:
1. Go to 
### NavigationPath Component:

Domain management > Automatic deploy subdomains
.
2. Select **Edit custom domains**.
3. Next to **Deploy Previews**, select **Add custom domain**.
4. Under **Domain**, you'll find domains managed by Netlify DNS. Select your chosen custom domain. Optionally, enter an additional subdomain, such as `early-access` or `qa`.

    ![](/images/domains-https-ads-for-deploy-previews.png)

### Tip - Want to use a different domain?

If you can't find the domain you want to add in the drop-down menu, check out these docs for [adding a new custom domain](/manage/domains/manage-domains/automatic-deploy-subdomains#use-a-new-custom-domain-for-your-automatic-deploy-subdomain).

5. Review the preview of the deploy URL for your Deploy Previews. To confirm,  select **Save**.

Once saved, Netlify updates the domain for all open Deploy Previews. If you applied a custom domain that is not already live as your primary site domain (or does not already have a security certificate), then your new deploy URL may take up to 24 hours to resolve and work with HTTPS.

## Automatic deploy subdomains for branch deploys

Branch deploys are often used for maintaining a separate version of your site for QA, internal testing, or even to manage different versions of site content for different audiences or product versions.

If you are already using [branch subdomains](/manage/domains/domains-fundamentals/domains-glossary#branch-subdomain), check out [our branch subdomain comparison docs](/manage/domains/manage-domains/manage-domains-for-branch-deploys#compare-subdomain-options-for-branch-deploys) to understand the key differences between these subdomains and how they can work together.

If you set up an automatic deploy subdomain for branch deploys on your site, then each branch deploy will generate the same automatic deploy subdomain and include your branch deploy's unique branch name.

![Diagram defining parts of the branch deploy URL `https://staging.early-access.company.com`, where the branch deploy prefix is the `staging` branch name, the optional newly added subdomain is `early-access` and `company.com` is the domain managed by Netlify DNS.](/images/domains-https-ads-parts-defined-for-branch-deploys.png)

### Prerequisites 

To set up an automatic deploy subdomain for your site's branch deploys, you must first enable branch deploys for your site.

1. To enable branch deploys for your site, go to 
### NavigationPath Component:

Project configuration > Build & deploy > Branches and deploy contexts
.
2. Select **Configure**.
3. Next to **Branch deploys**, set up branch deploys for a specific branch or for all non-production branches. To confirm, select **Save**.
4. Once branch deploys are enabled, create a new branch and push a commit to this branch in your connected site repo. Netlify will automatically generate a branch deploy, which you can preview in your site's deploy list.

### Tip - Created a deploy with the CLI?

If you created a deploy using the [Netlify CLI's `--alias` flag](/api-and-cli-guides/cli-guides/get-started-with-cli#draft-deploys), then be aware that these deploys are not branch deploys and do not support branch subdomains or automatic deploy subdomains. We recommend you avoid using `--alias` with any of your branch names.

### Set an automatic deploy subdomain for branch deploys

To set up an automatic deploy subdomain for your site's branch deploys:
1. Go to 
### NavigationPath Component:

Domain management > Automatic deploy subdomains
.
2. Select **Edit custom domains**.
3. Next to **Branch deploys**, select **Add custom domain**.
4. Under **Domain**, you'll find domains managed by Netlify DNS. Select your chosen custom domain. Optionally, enter an additional subdomain, such as `early-access` or `qa`.

   ![](/images/domains-https-ads-for-branch-deploys.png)

### Tip - Want to use a different domain?

If you can't find the domain you want to add in the drop-down menu, check out these docs for [adding a new custom domain](/manage/domains/manage-domains/automatic-deploy-subdomains#use-a-new-custom-domain-for-your-automatic-deploy-subdomain).

5. Review the preview of the deploy URL for your branch deploys. To confirm,  select **Save**.

Once saved, Netlify updates the domain for all active branch deploys. If you applied a custom domain that is not already live as your primary site domain (or does not already have a security certificate), then your new deploy URL may take up to 24 hours to resolve and work with HTTPS.

### Choose a unique URL for your branch deploys

It is possible to configure automatic subdomains for branch deploys so that a branch subdomain conflicts with another site's production domain. Since Deploy Previews are appended with the pull/merge request number, their automatic subdomains are unlikely to conflict with other domains.

For example: 
- Site A has a primary site domain of `staging.company.com` for the production site.
- Site B has an automated domain of `staging.company.com` for its `staging` branch. 

When there is a conflict, domains listed in your **Production domains** settings will take precedence over other internal domains. So in this example, `staging.company.com` will resolve to the content of site A.

To prevent accidental domain duplication, you might choose to add another subdomain level to your branch subdomains that is not used in production, such as `internal` in `staging.internal.company.com`.

If you get a domain conflict, you can rename the branch. For example, you can rename the branch from `staging` to `qa`. Then, the next time you deploy this branch, it would use the `qa.company.com` domain.

### Limitations for sites with existing branch subdomains

Once you add an automatic deploy subdomain for branch deploys, you cannot edit or change existing manual [branch subdomains](/manage/domains/domains-fundamentals/domains-glossary#branch-subdomain). You also cannot manually add new branch subdomains, but existing branch subdomains will still work.

If you configured branch subdomains before enabling automatic deploy subdomains, both the branch subdomains and automatic deploy subdomains will resolve and be available. If both are set up, the Netlify UI, CLI, API, and deploy notifications will link to the automatic deploy subdomain by default. 

To make changes to your branch subdomain, you must [remove the automatic deploy subdomain](/manage/domains/manage-domains/automatic-deploy-subdomains#remove-an-automatic-deploy-subdomain) first.

If you want to compare using branch subdomains with automatic deploy subdomains, check out our [comparison docs for applying a custom domain to a branch deploy](/manage/domains/manage-domains/manage-domains-for-branch-deploys).

## Use a new custom domain for your automatic deploy subdomain

By default, you can choose primary site domains that are also managed by [Netlify DNS](/manage/domains/why-netlify-dns) as your automatic deploy subdomain. You can also add additional subdomains to these domains, such as `early-access` or `qa`.

![](/images/domains-https-domain-drop-down-menu.png)

If you want to use a custom domain that is not listed in the Netlify UI, you must first delegate this domain to Netlify DNS.

### Tip - Want to use a subdomain without bringing the apex domain to Netlify DNS?

You can bring a subdomain to Netlify DNS without the apex domain. For example, you can delegate  `docs.company.com` to Netlify DNS without also delegating `company.com`. Learn more about [stand-alone subdomain support](/manage/domains/configure-domains/delegate-a-standalone-subdomain).

To delegate an existing domain you own to Netlify DNS:

1. Go to your project dashboard, on the left, choose **Domain management**. 
2. Under **Automatic deploy subdomains**, check **Add custom domain**.
3. Optionally, you can add a subdomain to your custom domain, such as `early-access`, `internal`, or `docs`.
4. Under **Domain**, choose a custom domain or add a new custom domain with the option **Configure Netlify DNS for a custom domain**.
5. Enter new domain and confirm with **Set up with Netlify DNS**.
6. Point your domain's name servers to Netlify. To use Netlify DNS, go to your domain registrar and change your domain's name servers to the following custom hostnames assigned to your DNS zone.
7. Confirm with **I've done this, proceed**.
8. Select **Save**.

Your changes may need more time to take effect depending on your DNS updates. Some DNS updates can take up to 24 hours to take effect and some changes take even longer.

Once your changes take effect, your Deploy Preview or branch deploy URLs will automatically update to use the new domain and/or subdomain.

## Use the Netlify API to set automatic deploy subdomains

You can set automatic deploy subdomains when you create a site using the Netlify API. In your [`createSite`](https://open-api.netlify.com/#tag/site) request, use the following query parameters to pass the values to use for the subdomains:
  - `deploy_preview_custom_domain` 
  - `branch_deploy_custom_domain`

Note that when you create or update a site with an automatic deploy subdomain, the build environment variable `DEPLOY_PRIME_URL` will update for all relevant deploys. Learn more about [`DEPLOY_PRIME_URL`](/build/configure-builds/environment-variables#deploy-urls-and-metadata).

## Custom certificate requirements

If you use a [custom certificate](/manage/domains/secure-domains-with-https/https-ssl#custom-certificates) for your site's domains, that certificate must explicitly include any new subdomains used for automatic deploy subdomains. The standard wildcard syntax, such as `*.company.com`, does not cover this new subdomain.

For example, your custom certificate will not work as expected in this scenario:
- you have `early-access.company.com` as your automatic deploy subdomain, where `early-access` is the optional new subdomain you [added in the Netlify UI](/manage/domains/manage-domains/automatic-deploy-subdomains#set-an-automatic-deploy-subdomain-for-deploy-previews)
 ![Diagram defining parts of the Deploy Preview URL `https://deploy-preview-42.early-access.company.com`, where the optional newly added subdomain is `early-access` and `company.com` is the custom domain managed by Netlify DNS.](/images/domains-https-ads-parts-defined-without-prefix.png)
- you have a custom certificate with `*.company.com` as your wildcard domain but not `*.early-access.company.com` 

In this scenario, you must update your certificate to include the domains `*.company.com, *.early-access.company.com` so that `early-access.company.com` will work as expected.

## Remove an automatic deploy subdomain

To remove an automatic deploy subdomain from your Deploy Previews or branch deploys: 
  1. Go to 
### NavigationPath Component:

Domain management > Automatic deploy subdomains
.
  2. Select **Edit custom domains**.
  3. Next to **Branch deploys** or **Deploy Previews**, clear the **Add custom domain** checkbox.
  4. To confirm,  select **Save**.
