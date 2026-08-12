---
title: "Deploy notifications"
source: https://docs.netlify.com/deploy/deploy-notifications.md
path: deploy/deploy-notifications
---

---
title: "Deploy notifications"
description: "Enable notifications for deploy events triggered by your site's deploy activity. Use Slack, webhooks, email, your Git provider, or other integrations."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Deploy notifications can inform you or external services about a specific site's deploy activity.

Netlify supports the following deploy events: 

- **Deploy started:** event emitted when Netlify starts building your site for a new deploy.
- **Deploy succeeded:** event emitted when Netlify finishes uploading a new deploy to our CDN.
- **Deploy failed:** event emitted when a deploy does not complete.
- **Deploy deleted:** event emitted when a deploy is manually [deleted](/deploy/manage-deploys/manage-deploys-overview#delete-a-deploy).
- **Deploy locked:** event emitted when the site is [locked to a published deploy](/deploy/manage-deploys/manage-deploys-overview#locked-deploys), stopping auto publishing.
- **Deploy unlocked:** event emitted when deploys are unlocked, resuming auto publishing.
- **Deploy request pending:** event emitted when an [untrusted deploy requires approval](/deploy/deploy-overview#deploy-permissions) to begin building.
- **Deploy request accepted:** event emitted when an untrusted deploy request is accepted and can begin building.
- **Deploy request rejected:** event emitted when an untrusted deploy request is rejected.
- **Deploy restored:** event emitted when a deploy is manually published (usually for [rollback or rollforward](/deploy/manage-deploys/manage-deploys-overview#rollbacks).
- **Previously successful deploy failed:** event emitted when a deploy was previously successful but then failed.
- **Previously failed deploy succeeded:** event emitted when a deploy succeeded after it had failed.

You can enable notifications for deploy events in 
### NavigationPath Component:

Project configuration > Notifications > Deploy notifications
. Select the type of notification you want to create and add the required configuration.

![](/images/site-deploys-outgoing-notifications.png)

You can also set up Slack notifications with our Netlify App for Slack.

## Slack notifications

Send deploy event information to a Slack channel. Learn more in our [Netlify App for Slack docs](/extend/install-and-use/setup-guides/netlify-app-for-slack).

## Email notifications

> **Pricing Information:** This feature is available on all [Pro](https://www.netlify.com/pricing/?category=developer) and [Enterprise](https://www.netlify.com/pricing/?category=enterprise) plans.

This type of notification allows you to send event information to an email address of your choice.

![](/images/site-deploys-email-notification.png)

## HTTP Post Request

This type of notification works as an outgoing webhook and allows you to send event information to an arbitrary URL using a POST request.

The body of the outgoing webhook request will have a JSON representation of the object relevant to the event.

![](/images/site-deploys-outgoing-webhook.png)

### Payload signature

If you provide a JWS secret token for an outgoing webhook, Netlify will generate a JSON Web Signature(JWS) and send it along with the notification in the request header `X-Webhook-Signature`.

We include the following fields in the signature's data section:

- `iss`: always sent with value `netlify`, identifying the source of the request
- `sha256`: the hexadecimal representation of the generated payload's SHA256

You can use any JWT client library to verify this signature in the service receiving the notification. This is an example of an API built with the Sinatra framework that verifies the signature header:

```ruby
require "digest"
require "jwt"
require "sinatra"

def signed(request, body)
  signature = request["X-Webhook-Signature"]
  return unless signature

  options = {iss: "netlify", verify_iss: true, algorithm: "HS256"}
  decoded = JWT.decode(signature, "your signature secret", true, options)

  ## decoded :
  ## [
  ##   { sha256: "..." }, # this is the data in the token
  ##   { alg: "..." } # this is the header in the token
  ## ]
  decoded.first[:sha256] == Digest::SHA256.hexdigest(body)
rescue JWT::DecodeError
  false
end

post "/netlify-hook" do
  body = request.body.read
  halt 403 unless signed(request, body)

  json = JSON.parse(body)
  # do something with the notification payload here
end
```

If your project uses Node.js with Express for backend, you need to compare the incoming request data before it's transformed to JSON:

```js
import crypto from "crypto";
import jwt from "jsonwebtoken";
import express from "express";

const app = express();

// parse body and keep the raw contents
app.use(
  bodyParser.json({
    verify: (req, res, buffer, encoding) => {
      req.rawBody = buffer;
    }
  })
);

app.post("/", (req, res) => {
  const signature = req.headers['x-webhook-signature'];
  const isValid = validateSignature(signature, req.rawBody);
  res.send(isValid);
});

app.listen(3000);

const secret = "your signature secret";

function validateSignature(token, buffer) {
  const options = { issuer: "netlify", algorithms: ["HS256"] };
  const decoded = jwt.verify(token, secret, options);
  const hashedBody = crypto.createHash("sha256").update(buffer).digest("hex");
  return decoded.sha256 === hashedBody;
}
```

## GitHub commit statuses

This type of notification sets commit status directly in your GitHub pull requests and commit lists. For successful deploys, this will include a link to the Deploy Preview. For failed deploys, this will include a link to the detail page for the deploy where you can examine the deploy log and deploy the latest branch commit.

![](/images/site-deploys-github-commit-status-example.png)

These notifications are added to all new GitHub-connected Netlify sites by default. You can add, remove, or edit them in 
### NavigationPath Component:

Project configuration > Notifications > Deploy notifications
.

The settings include a field for a custom message, which will replace the "Deploy preview ready!" message that displays by default.

![](/images/site-deploys-github-commit-status.png)

## GitHub pull request comments

This type of notification adds a comment to your GitHub pull requests indicating the status of the associated deploy and providing a link to the Deploy Preview when ready. If you append more commits to a pull request, this notification will update the comment to indicate status changes.

![](/images/site-deploys-github-pr-comment-example.png)

GitHub pull request comment notifications are added to all new GitHub-connected Netlify sites by default. You can add, remove, or edit them in 
### NavigationPath Component:

Project configuration > Notifications > Deploy notifications
.

The settings include a field for a custom message, which will replace the "Deploy preview ready!" message that displays by default.

![](/images/site-deploys-github-pr-comment.png)

## GitHub commit checks

This type of notification adds rich deploy information from your [deploy summary](/deploy/deploy-overview#deploy-summary) to your GitHub pull requests and commit lists.
This includes more detailed information in the **Checks** tab of your pull requests on GitHub.

![](/images/site-deploys-checks-only.png)

These notifications are added to all new GitHub-connected Netlify sites by default. You can add, remove, or edit them in 
### NavigationPath Component:

Project configuration > Notifications > Deploy notifications
.

![](/images/site-deploys-checks-setting.png)

If you don't find the option for GitHub commit checks in the **Add notification** menu, you will need to configure your site to use the [Netlify GitHub App]( /build/git-workflows/repo-permissions-linking#authentication-with-the-netlify-github-app).

## GitLab commit statuses

### Tip - Personal access token (PAT) required

If your deploy notifications stop working, you may need to add a GitLab PAT to Netlify. Learn more at our [Troubleshoot GitLab notifications docs](/deploy/deploy-notifications#troubleshoot-gitlab-deploy-notifications).

This type of notification creates commit statuses in your GitLab repositories.

![](/images/site-deploys-gitlab-commit-status-example.png)

You can configure this notification through the Netlify UI using your GitLab personal access token (PAT). Your PAT must have the `api` scope. Learn more in [GitLab's PAT docs](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html). You can add, remove, or edit access in 
### NavigationPath Component:

Project configuration > Notifications > Deploy notifications
.

![](/images/site-deploys-gitlab-commit-status.png)

## GitLab merge request comments

### Tip - Personal access token (PAT) required

If your deploy notifications stop working, you may need to add a GitLab PAT to Netlify. Learn more at our [Troubleshoot GitLab notifications docs](/deploy/deploy-notifications#troubleshoot-gitlab-deploy-notifications).

This type of notification adds a comment to your GitLab merge requests indicating the status of the associated deploy and providing a link to the Deploy Preview when ready. If you append more commits to a merge request, this notification will update the comment to indicate status changes.

![](/images/site-deploys-gitlab-merge-request-example.png)

You can configure this notification through the Netlify UI using your GitLab personal access token (PAT). Your PAT must have the `api` scope. Learn more in [GitLab's PAT docs](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html). You can add, remove, or edit access in 
### NavigationPath Component:

Project configuration > Notifications > Deploy notifications
.

![](/images/site-deploys-gitlab-merge-request.png)

## Troubleshoot GitLab deploy notifications

If you set up your GitLab deploy notifications with a GitLab API access token, you'll need to edit your notifications settings in the Netlify UI and add a GitLab personal access token (PAT).

GitLab 15.0 no longer supports OAuth tokens without an expiration date and introduced a 2-hour expiration window. Learn more about expiring tokens in [GitLab's OAuth docs](https://docs.gitlab.com/ee/integration/oauth_provider.html#access-token-expiration).

### Tip - Use Git Gateway or collaborative Deploy Previews?

Your connection to GitLab for these features may also be impacted by the GitLab 15.0 update. Learn more about how to resolve these issues for [Git Gateway](/manage/security/secure-access-to-sites/git-gateway#troubleshoot-git-gateway-connection-issues-with-gitlab) or [collaborative Deploy Previews](/deploy/deploy-types/deploy-previews#troubleshooting-collaborative-deploy-previews).

### GitLab deploy notifications stop working

If your GitLab deploy notifications stop working, ensure that you are using a GitLab personal access token (PAT) with the right scopes.

1. On GitLab, generate a new GitLab PAT with the `api` scope. Learn more in [GitLab's PAT docs](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html).
2. On Netlify, add your GitLab PAT for each desired deploy notification at 
### NavigationPath Component:

Project configuration > Notifications > Deploy notifications
.

![](/images/site-deploys-gitlab-merge-request.png)

## Bitbucket notifications

Deploy notifications for Bitbucket allow your team to check out the latest deploy status and Deploy Preview from Bitbucket.

### Bitbucket commit statuses

This type of notification sets commit statuses directly in your Bitbucket branches, pull requests, and commit lists. For successful deploys, this will include a link to the Deploy Preview. For failed deploys, this will include a link to the detail page for the deploy where you can examine the deploy log and deploy the latest branch commit.

![](/images/site-deploys-bitbucket-commit-status.png)

### Bitbucket pull request comments

This type of notification adds a comment to your Bitbucket pull requests with a Deploy Preview link and deploy status. This comment automatically updates with any new commits to your pull request.

![](/images/site-deploys-bitbucket-pull-request-comment.png)

## Azure DevOps notifications

Deploy notifications for Azure DevOps allow your team to check out the latest deploy status and Deploy Preview from Azure DevOps.

### Azure DevOps commit statuses

This type of notification adds a Netlify Deploy Preview link to the [Commit details page](https://docs.microsoft.com/en-us/azure/devops/repos/git/commit-details?view=azure-devops) for successfully deployed commits.

To set up this notification, you must create an [Azure DevOps personal access token (PAT)](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows) with **Code: Read & write** permissions.

Once you have a PAT, configure the notification on Netlify. Go to 
### NavigationPath Component:

Project configuration > Notifications > Deploy notifications
, select **Azure DevOps commit status**, and add your PAT.

![](/images/site-deploys-azure-devops-commit-status-configuration.png)

Once configured, you can open a Deploy Preview for a commit with a successful build. To open a Deploy Preview from Azure DevOps, go to the [Commit details page](https://docs.microsoft.com/en-us/azure/devops/repos/git/commit-details?view=azure-devops), and select the **succeeded** build status for the desired commit.

![](/images/site-deploys-azure-devops-commit-succeeded.png)

![](/images/site-deploys-azure-devops-deploy-preview-link.png)

### Azure DevOps pull request comments

This type of notification adds a comment to your Azure DevOps pull requests with a Deploy Preview link and deploy status. This comment automatically updates with any new commits to your pull request.

![](/images/site-deploys-azure-devops-pull-request-comment.png)

To set up this notification, you must create an [Azure DevOps personal access token (PAT)](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows) with **Code: Read & write** permissions.

Once you have a PAT, configure this notification on Netlify. Go to 
### NavigationPath Component:

Project configuration > Notifications > Deploy notifications
, select **Azure DevOps pull request comment**, and add your PAT.

![](/images/site-deploys-azure-devops-pull-request-configuration.png)

## Notifications for monorepos or repositories building multiple apps

For monorepos or setups where one repository builds multiple applications, you can manage the amount of commit status and commit check notifications for sites linked from GitHub or GitLab. This team-level setting works in tandem with deploy notifications configured individually for each site. Check out our [monorepo docs](/build/configure-builds/monorepos#commit-status-notifications) to learn more.

## Zapier integrations

Netlify is available on Zapier, where you can connect Netlify with over 1,000 other applications. You can use Zapier "Zaps" to trigger an action in another service on every successful deploy or when a deploy does not complete. You can [find out more on our blog](https://www.netlify.com/blog/2018/11/07/automate-your-netlify-sites-with-zapier/), or use one of the templates below to get started:

### Integration: zapier-deploys

- **ID**: zapier-deploys
- **Description**: Show new Netlify deployments in Status Hero
- **Subtext**: Netlify + Status Hero
- **Link**: https://zapier.com/webintent/create-zap?template
- **CTA Text**: Use this Zap

### Integration: zapier-deploys

- **ID**: zapier-deploys
- **Description**: Make ServiceNow records from new Netlify deploy failures
- **Subtext**: Netlify + ServiceNow
- **Link**: https://zapier.com/webintent/create-zap?template
- **CTA Text**: Use this Zap

### Integration: zapier-deploys

- **ID**: zapier-deploys
- **Description**: Plant trees with Ecologi when new deploys in Netlify succeed
- **Subtext**: Ecologi + Netlify
- **Link**: https://zapier.com/webintent/create-zap?template
- **CTA Text**: Use this Zap

## n8n integrations

Netlify is available on <a href="https://n8n.io/" target="_blank">n8n</a>, an open source tool that allows you to connect Netlify with other applications. By using one of n8n's Netlify nodes, you can create your own automated workflow. To get started, you can use the [Netlify node](https://n8n.io/integrations/netlify/), [Netlify Trigger node](https://n8n.io/integrations/netlify-trigger/), or you can use the existing workflow below:

### Integration: n8n-deploys

- **ID**: n8n-deploys
- **Description**: Send notification when deployment fails
- **Subtext**: Netlify Trigger Node
- **Link**: https://n8n.io/workflows/1255-send-notification-when-deployment-fails/
- **CTA Text**: Use workflow


