---
title: "Netlify Build Control"
source: https://docs.netlify.com/build/configure-builds/stop-or-activate-builds.md
path: build/configure-builds/stop-or-activate-builds
---

---
title: "Stop or activate builds"
description: "Stop builds for your site at will for more control of your workflow. When you're ready for Netlify to build your site again, you can activate builds."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

If your site is linked to a Git repository, Netlify will by default build your site according to your continuous deployment settings when you push to your Git provider. You can [stop builds](/build/configure-builds/stop-or-activate-builds#stop-builds) for your site at will for more control of your workflow. When you're ready for Netlify to build your site again, you can [activate builds](/build/configure-builds/stop-or-activate-builds#activate-builds).

For example, you might:

- stop builds while you use a continuous integration tool to run validations and then activate builds after all validations are successful.
- stop builds while you're sequentially pushing many small commits in response to review feedback on a pull/merge request and then activate builds before you push the last commit.
- stop builds as part of implementing a content freeze and then activate builds when the freeze is over.

### Note - Stop builds vs. stop auto publishing

When you stop builds for a site, you prevent Netlify from building production deploys, Deploy Previews, and branch deploys. If you only want to stop new production deploys from being published, you can [stop auto publishing](/deploy/manage-deploys/manage-deploys-overview#locked-deploys).

## Stop builds

To stop builds for a site, go to 
### NavigationPath Component:

Project configuration > Build & deploy > Continuous deployment > Build settings
, select **Configure**, and then toggle **Build status** to **Stopped builds**.

![](/images/configure-builds-stop-builds-stop.png)

When builds are stopped, Netlify will never build your site.

- If you push to your linked repository, Netlify will not build production deploys, Deploy Previews, or branch deploys.
- If requests are sent to build hook URLs, Netlify will not build your site.
- You will not be able to trigger a build of your site with the Netlify API. Any POST requests to `/api/v1/sites/{site_id}/builds` will return an error message.
- You will not be able to build your site using the Netlify UI. On the **Deploys** page, the **Trigger deploy** button will be unavailable. On the detail page for a past deploy, the **Retry with latest branch commit** button will be unavailable.

### Tip - Tip

You can still update your site by [running a build locally](/api-and-cli-guides/cli-guides/get-started-with-cli#run-builds-locally) with the CLI and then creating a deploy manually with the [CLI](/api-and-cli-guides/cli-guides/get-started-with-cli#manual-deploys) or the [API](/api-and-cli-guides/api-guides/get-started-with-api#deploy-with-the-api).

Netlify will send a notification email to let any other site members know that builds are stopped for the site. There will also be warnings in these locations in the Netlify UI:

- your team's **Sites** page.
- the **Site overview** page.
- the site's **Deploys** page.
- **project configuration** under 
### NavigationPath Component:

Project configuration > Build & deploy > Continuous deployment > Build settings
.

### Note - Relinking the Git repository will activate builds

If you [unlink]( /build/git-workflows/repo-permissions-linking#unlink-a-git-repository) and then [relink]( /build/git-workflows/repo-permissions-linking#link-a-git-repository) your site's repository or [link to a different repository]( /build/git-workflows/repo-permissions-linking#change-linked-git-repository), builds will be activated as part of the new configuration.

## Activate builds

By default, builds are active. If builds have been stopped for a site, there are multiple ways you can activate them. You can:

- go to 
### NavigationPath Component:

Project configuration > Build & deploy > Continuous deployment > Build settings
, select **Configure**, and then toggle **Build status** to **Active builds**.

   ![](/images/configure-builds-stop-builds-activate-on-settings.png)

- go to the 
### NavigationPath Component:

Site overview
 page and use the **Activate builds** button.

   ![](/images/configure-builds-stop-builds-activate-on-overview.png)

- go to the site's 
### NavigationPath Component:

Deploys
 page and use the **Activate builds** button.

   ![](/images/configure-builds-stop-builds-activate-on-deploys.png)

### Note - Activating builds does not trigger a build

Netlify does not immediately build your site when you activate builds. After you activate builds, Netlify will build your site when you push to your Git repository, trigger a build hook, POST to `/api/v1/sites/{site_id}/builds`, or trigger/retry a deploy using the Netlify UI.

Netlify will send a notification email to let any other site members know that builds have been activated for the site. 

