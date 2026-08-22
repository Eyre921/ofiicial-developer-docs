---
title: "Manage deploys"
source: https://docs.netlify.com/deploy/manage-deploys/manage-deploys-overview.md
path: deploy/manage-deploys/manage-deploys-overview
---

---
title: "Manage deploys"
description: "Roll back, lock, cancel, skip, cleanup, or delete a deploy for your site, or use environment variables to control the deploy environment."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Netlify versions all deploys. From the **Deploys** tab for your site in the Netlify UI, you can browse any deploy you've ever made and preview it from a unique URL.

## Find a deploy

As a Developer or Team Owner, you can find deploys using the search or filter options available on the  
### NavigationPath Component:

Deploys
 tab.

Use the search field above the deploy list to search by deploy ID or branch name. 

### Tip - Where to find your deploy ID

You can find the deploy ID in the first part of a [deploy permalink](/deploy/deploy-overview#definitions). For example: `1234abcd12acde000111cdef` is the deploy ID of `1234abcd12acde000111cdef--mysitename.netlify.app`.

You can also filter deploys for your site based on these options: 
  - Time frame
    - Filter deploys triggered in the **Last hour**, **Last day**, **Last 7 days**, or filter by a **Custom** date and time range.
  - [Deploy context](/deploy/deploy-overview#deploy-contexts)
  - Deploy status
    - `Successful`
    - `Unsuccessful` (includes `Failed`, `Canceled`, or `Skipped` deploys)
    - `Enqueued` for deploys that are in the queue awaiting deployment
    - `Pending review`, `Accepted`, or `Rejected` for deploys triggered by an unrecognized author. Learn more about [deploy requests and permissions](/deploy/deploy-overview#deploy-permissions).

## Rollbacks 

If you need to roll back, you can publish one of the previous deploys listed in the UI as the live version of your site in production. Use the **Publish Deploy** button on the detail page of any successful deploy. This doesn't trigger a new deploy but instead publishes a previous atomic deploy that is still available to you. Rollbacks are instantaneous.

> **Video**: [Watch video](https://www.youtube.com/embed/aPk6qs9H3Gs)

### Note - Note

If your Netlify site is connected to a Git repository and has auto publishing turned on, any new Git-triggered production deploys will overwrite the previously rolled back version.

## Locked deploys

Locked deploys give you the ability of pinning a site to the latest published deploy for the time being. New deploys won't be published to the main site, although Netlify will still build them and they will be ready for whenever you want to publish them.

### Lock a published deploy

You can lock a deploy by disabling auto publishing. To disable auto publishing, navigate to your site's 
### NavigationPath Component:

Deploys
 list and select **Lock to stop auto publishing**.

![](/images/site-deploys-manage-deploys-lock-deploy-lock.png)

### Unlock a locked deploy

After a deploy has been locked, you can use **Unlock to start auto publishing** to unlock it from the same 
### NavigationPath Component:

Deploys
 list.

![](/images/site-deploys-manage-deploys-lock-deploy-unlock.png)

### Event notifications

> **Pricing Information:** This feature is available on all [Pro](https://www.netlify.com/pricing/?category=developer) and [Enterprise](https://www.netlify.com/pricing/?category=enterprise) plans.

You can get notifications about locked deploys by email, outgoing webhook, or Slack. Netlify can notify you when a deploy is either locked or unlocked.

![](/images/site-deploys-manage-deploys-locked-deploys-events.png)

You can configure these notifications from the notifications section in 
### NavigationPath Component:

Project configuration > Notifications > Deploy notifications
. Visit the [deploy notifications documentation](/deploy/deploy-notifications) to learn more.

## Cancel a deploy

Sometimes, you may want to cancel a deploy after it has started. To do this, go to the detail page of the deploy in progress and select **Cancel deploy**. You'll then be prompted to confirm the canceling action. Select **Yes, cancel deploy** to confirm.

If you later want to restart the deploy, you can [deploy from the latest branch commit](#retry-deploy-from-latest-branch-commit).

## Skip a deploy

Sometimes, you may want to push commits to a branch without triggering a deploy on Netlify.

- To avoid generating a Deploy Preview for a pull/merge request, add `[skip ci]` or `[skip netlify]` to the title of the pull/merge request.

- To avoid generating a branch or production deploy for a commit pushed directly to a branch, add `[skip ci]` or `[skip netlify]` anywhere in the Git commit message.

- To avoid generating a branch or production deploy for multiple commits pushed together, add `[skip ci]` or `[skip netlify]` to the most recent commit, and it will apply to all other commits in the push.

The next commit pushed without one of those messages will trigger a new branch deploy or production deploy, including all changes from the skipped commits as well. To generate a Deploy Preview from a pull/merge request, remove `[skip ci]` or `[skip netlify]` from the title and push a new commit.

To trigger a deploy at will on your production branch, go to your site's **Deploys** page and select **Trigger deploy** at the top of the deploy list.

To avoid triggering automated deploys of _any_ kind, you can [stop builds](/build/configure-builds/stop-or-activate-builds) for the entire site.

If you would like to continue building your deploys but don't want them published to your main URL, you can [stop auto publishing](/deploy/manage-deploys/manage-deploys-overview#locked-deploys).

## Retry deploy from latest branch commit

If your build fails or you run into other issues, you can retry your deploy with the latest branch commit. You can also retry your deploy with a cleared cache.

![](/images/configure-builds-retry-deploy-dropdown.png)

When you retry a deploy, the build triggers from the HEAD of your branch. If the HEAD of the branch differs from the original deploy SHA, Netlify still builds from the HEAD of the branch.

## Automated cleanup for failed and canceled deploys

By default, Netlify automatically deletes failed and canceled deploys older than 30 days (or 90 days on paid plans) as a part of deploy cleanup and maintenance.

Once deleted, you can expect deploys and their associated builds to disappear from the Netlify UI and API queries.

## Automatic deploy deletion

By default, Netlify will delete deploys after 30 days (or 90 days on paid plans). This includes deploys triggered by either source control changes, the Netlify UI or CLI, manual uploads, or third-party integrations.

Netlify will not automatically delete:
1. The deploy currently published to your site (also called the [published deploy](/deploy/deploy-overview#definitions).
1. The most recent successful production deploy.
1. The most recent successful branch deploy for a given branch. 

Owners and Developers on an Enterprise plan can adjust the default retention period for up to 365 days.

Once a deploy is automatically deleted, you can expect the deploy and its associated builds to disappear from the Netlify UI and API queries. If you visit the deploy permalink for an automatically deleted deploy, a generic 404 page is returned. 

The [team audit log](/manage/accounts-and-billing/team-management/team-audit-log) updates with `Deploy retention has changed` when a Developer or Team Owner changes the deploy retention limit for a site.

### Change the deploy retention limit

> **Pricing Information:** This feature is available on [Enterprise](https://www.netlify.com/pricing/?category=enterprise) plans.

To adjust a site's default deploy retention limit, you must be a Team Owner or Developer.

After you change the deploy retention limit for a site and save, all changes take effect instantly. For example, if you set your site's deploy retention to 30 days and confirm this update, all eligible deploys older than 30 days will delete with no additional warning. Netlify runs deploy deletions daily.

1. As a Developer or Team Owner, go to 
### NavigationPath Component:

Project configuration > Build & Deploy > Automatic Deletion
.

2. Select **Configure**, and use the drop-down to select a new deploy retention limit.

3. Confirm with **Save setting**.

## Manual deploy deletion through the Netlify UI

You may want to [delete a deploy](/deploy/manage-deploys/manage-deploys-overview#delete-a-deploy-through-the-ui) to remove sensitive data, as a part of your team's security best practices, or to clean up your Netlify deploys list. Deploy deletions are logged in the team audit log as `Deploy deleted` actions.

### Deploy deletion requirements

To delete a deploy manually in the Netlify UI, you must be a [Developer or Team Owner](/manage/accounts-and-billing/team-management/roles-and-permissions).

You cannot delete the deploy that was most recently published to a site's main URL.

You also cannot delete a deploy that is still in progress. You must either cancel the deploy or wait until the deploy is finished before you can delete it.

### Deploy deletion considerations

Be aware that deleting a deploy is permanent and does not reduce costs for your Netlify team or help you preserve build minutes. More details on this are below.

Once a deploy is deleted, you cannot access any artifacts associated with the deploy, including URLs, deploy logs, or functions unique to the deploy. The deploy permalink for the deleted deploy will no longer work and will show a generic 404 error message instead.

After you delete a deploy, you may encounter the following:
- **The deploy context URL may no longer work.** If you delete a deploy and there are no other deploys in the context, the [deploy context](/deploy/deploy-overview#deploy-contexts) URL will return a generic 404 message.
- **Your deploy context URL may show changes from a different deploy.** If you delete the most recent deploy to a [deploy context](/deploy/deploy-overview#deploy-contexts), then that URL will point to the next most recent deploy in the same context.
- **Split testing results may be disrupted.** If the deleted deploy is from a branch with split testing configured, your split testing results may be disrupted. 

After a deploy is deleted, the deploy's associated build is removed from the team's [builds list](/manage/monitoring/monitor-builds#current-status) on the main **Builds** page. However, the build data from deleted deploys is still included in the aggregated [build minute counts and insights analytics](/manage/monitoring/monitor-builds#historical-insights) to help you make an accurate assessment of your team's build minutes usage.

### Delete a deploy through the UI

As a Developer or Team Owner, you can delete a single deploy manually through the UI.

1. To find the deploy you want to delete, go to the 
### NavigationPath Component:

Deploys
 page for your site and select the deploy from the deploy list or use the deploy search.

3. From the deploy details page:
   - For successful deploys, select **Options > Delete deploy**.
![](/images/site-deploys-delete-deploy-for-successful-deploys.png)
   - For failed or canceled deploys, select **Delete deploy**.

   If the **Delete deploy** option is not available, make sure the deploy meets the [requirements for deploy deletion](#deploy-deletion-requirements).

4. To confirm, review the deploy deletion warning, then select **Delete**.

## Download a deploy

From the detail page of any successful deploy, including [Netlify Drop](/deploy/create-deploys#drag-and-drop) deploys, you can download individual files or an entire copy of your site.

### Download an individual file

1. On the detail page for a successful deploy, scroll down to **Deploy file browser**.
2. Search for or browse to the file you want to inspect, then select **Download**.

   ![](/images/site-deploys-manage-deploys-deploy-file-browser.png)

### Download all deployed files

To generate a ZIP file containing all of your deployed files:

1. In the deploy detail page header for a successful deploy, select **Download**.
2. When the ZIP finishes generating, select **Download ready** to download the deploy.

   ![](/images/site-deploys-manage-deploys-download-deploy.png)

If you're looking to update a site you deployed manually through the UI, you can download and edit the deployed files locally, and then use the [deploy dropzone](/deploy/create-deploys#drag-and-drop) to deploy the update.

## Configure your deploy environment

You can use environment variables to control the environment your site gets deployed to. 

Environment variables created using the [Netlify UI, CLI, or API](/build/environment-variables/get-started/#create-variables-with-the-netlify-ui-cli-or-api) are available to **Builds**, **Functions**, **Runtime** and **Post processing** [scopes](/build/environment-variables/overview#scopes). This means that you can use them in your [serverless functions](/build/functions/overview) and [edge functions](/build/edge-functions/overview) at execution time, [snippet injection](/build/post-processing/snippet-injection/) during post processing, and more. 

Note that environment variables created in a `netlify.toml` are not available to the deploy environment.

To learn more about how to set and use environment variables review our [environment variables](/build/environment-variables/overview) docs. For more information on using environment variables with functions during runtime specifically, review environment variables with [serverless functions](/build/functions/environment-variables) and [edge functions](/build/edge-functions/environment-variables).

## Failed deploy troubleshooting tips

To help you fix failed deploys, Netlify offers AI capabilities that diagnose and suggest solutions for deploy failures and build errors so you can get back to shipping code.

Learn more about Netlify's AI capabilities to [give solutions for failed deploys](/resources/troubleshooting/fix-a-failed-deploy/).

  ![A failed deploy with a "Why did it fail?" button and a diagnosis and suggested solution above the deploy log details](/images/site-deploys-ai-helps-fix-failed-deploys.png)
For more help troubleshooting failed builds, check out our [Build troubleshooting tips](/build/configure-builds/troubleshooting-tips#app). If your deploy returns an error, you can also clear your cache and retry the deploy in the Netlify UI or trigger a new deploy.

