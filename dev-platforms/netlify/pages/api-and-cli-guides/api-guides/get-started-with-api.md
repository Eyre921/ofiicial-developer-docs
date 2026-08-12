---
title: "Netlify API Quickstart"
source: https://docs.netlify.com/api-and-cli-guides/api-guides/get-started-with-api.md
path: api-and-cli-guides/api-guides/get-started-with-api
---

---
title: "Get started with the Netlify API"
description: "Use our REST API to interact with our platform. Learn the basics for using the API, instructions for deploying sites, and notes on commonly used endpoints."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Use the Netlify REST API to manage atomic deploys of your sites and apps, manage form submissions, inject JavaScript snippets, manage DNS, and so much more.

> **Video**: [Watch video](https://www.youtube.com/embed/ypb7x5b83Q0?si)

This document covers the basics for interacting with the Netlify API, plus instructions for [deploying sites](/api-and-cli-guides/api-guides/get-started-with-api#deploy-with-the-api) and notes on some [commonly used endpoints](/api-and-cli-guides/api-guides/get-started-with-api#commonly-used-endpoints).

You can browse the [OpenAPI reference for the Netlify API](https://open-api.netlify.com) to explore available endpoints. Visit our Forums for more tips and conversation about [understanding and using Netlify's API](https://answers.netlify.com/t/common-issue-understanding-and-using-netlifys-api/160).

> **Note - Project ID, site_id, and NETLIFY_SITE_ID are the same value:** The Netlify UI labels this identifier **Project ID**, but the API, CLI, and environment variables still use `site`. Every project has exactly one identifier, and all of the following names refer to the same value:

- **Netlify UI** - **Project ID** (labeled **Site ID** before the rename)
- **Netlify API** - `site_id`, including in paths such as `/api/v1/sites/{site_id}`
- **Netlify CLI, client libraries, and `.netlify/state.json`** - `siteId, `siteID`, `--site`, and `NETLIFY_SITE_ID`

To copy the value, go to 
### NavigationPath Component:

Project configuration > General > Project details > Project information
 and copy **Project ID**.

Project names work the same way: the UI's **Project name** (formerly **Site name**) is the API's `site_slug`. Wherever the API accepts a `{site_id}`, you can also pass the project's domain, such as `mysite.netlify.app`.

Additionally, we have two API clients for your convenience:

- [Go Client](https://github.com/netlify/open-api#go-client)
- [JS Client](https://github.com/netlify/build/tree/main/packages/js-client)

If you'd like to interact with the Netlify API using a no-code tool, you can use n8n.io's [Netlify node](https://n8n.io/integrations/netlify/). The node currently supports the following operations:

- Create a new deployment
- Get a deployment
- Get all deployments
- Cancel a deployment
- Get a site
- Get all sites
- Delete a site

## Make a request

All URLs start with `https://api.netlify.com/api/v1/`. **SSL only**. The path is prefixed with the API version. If we change the API in backward-incompatible ways, we'll bump the version marker and maintain stable support for the old URLs.

To make a request for all sites you have access to, for example, append the `sites` index path to the base URL to form something like `https://api.netlify.com/api/v1/sites`. Here's an example in curl:

```bash
curl -H "User-Agent: MyApp (YOUR_NAME@EXAMPLE.COM)" \
     -H "Authorization: Bearer YOUR_OAUTH2_ACCESS_TOKEN" \
     https://api.netlify.com/api/v1/sites
```

## Authentication

Netlify uses OAuth2 for authentication. All requests must use HTTPS.

To generate a personal access token (PAT): 
1. Go to 
### NavigationPath Component:

Applications > Personal access tokens
.
2. Select **New access token**.
3. Enter a descriptive name to help you remember what the token will be used for.
4. Select **Allow access to my SAML-based Netlify team** to authorize access to your SAML-based team data through the API.
5. Select an **Expiration** date for your token to help keep your information secure. 
6. Select **Generate token**.
7. Copy the token to your clipboard and store it in a safe location. Once you navigate away from this page, you won't be able to access the value again.
8. Select **Done**.

Use your PAT for manual authentication in shell scripts or commands that use the Netlify API. 

To authenticate API requests, include the token in the authorization header: 

  `Authorization: Bearer <YOUR_PERSONAL_ACCESS_TOKEN>` 

To authenticate in shell scripts, refer to the [code sample above](#make-a-request) for an example of how to use this token in a curl request.

### Warning - Password resets invalidate tokens

If you reset your Netlify password, all personal access tokens and OAuth tokens created before the reset will be permanently invalidated. After a password reset, you must [generate new tokens](#authentication) and update any services or scripts that rely on them.

### Tip - SAML SSO

If your team requires you to log in with [single sign-on (SSO)](/manage/security/secure-netlify-access/configure-team-saml-sso), your personal access tokens will be denied access to the team by default. You can choose to grant access to the team when you generate a new token. You must be logged in to the team with SSO to grant access to it.

If you're making a public integration with Netlify for others to enjoy, you must use OAuth2. This allows users to authorize your application to use Netlify on their behalf without having to copy/paste API tokens or touch sensitive login info. You'll need an application client key and a client secret to integrate with the Netlify API. You can register a new application in your Netlify user settings for [OAuth applications](https://app.netlify.com/applications). Visit our blog post on [integrating with Netlify](https://www.netlify.com/blog/2016/10/10/integrating-with-netlify-oauth2/) for more information including common grant types and an example project.

The OAuth2 end-user authorization endpoint is `https://app.netlify.com/authorize`.

## Rate limiting

To protect Netlify from getting flooded by automated deploys or misbehaving applications, the Netlify API is rate limited.

You can make up to 500 requests per minute for most requests.
Certain operations have their own stricter limits. For example, you can deploy through the Netlify API up to 3 times per minute and up to 100 times per day.

You can check the returned HTTP headers of any API request to verify your current rate limit status:

```http
X-RateLimit-Limit: 500
X-RateLimit-Remaining: 56
X-RateLimit-Reset: 1372700873
```

If you need higher limits, please [contact us](https://www.netlify.com/support/).

## Pagination

All API requests that return over 100 items are paginated by default, with a limit of 100 items per page. You can specify further pages with the `?page` parameter. You can also set a custom page size that's less than 100 with the `?per_page` parameter.

Note that page numbering starts with 1 and that omitting the `?page` parameter will return the first page.

### Link header

The pagination info is included in the `Link` header.

```http
Link: <https://api.netlify.com/api/v1/sites?page=3&per_page=20>; rel="next",
    <https://api.netlify.com/api/v1/sites?page=5&per_page=20>; rel="last"
```

Linebreak is included for readability.

The possible `rel` values are:

- `next`
  Shows the URL of the immediate next page of results.
- `last`
  Shows the URL of the last page of results.
- `prev`
  Shows the URL of the immediate previous page of results.

## Deploy with the API

The most common API action is doing deploys, either of a new site or an existing site. If [builds are stopped](/build/configure-builds/stop-or-activate-builds) for an existing site, you can still deploy with the API to update the site.

Netlify supports two ways of doing deploys:

1. [Sending a digest](/api-and-cli-guides/api-guides/get-started-with-api#file-digest-method) of all files in your deploy, and then uploading any files Netlify doesn't already have on its storage servers.
2. [Sending a ZIP file](/api-and-cli-guides/api-guides/get-started-with-api#zip-file-method) of the entire site and letting Netlify unzip and deploy.

If you're looking to deploy sites at scale, such as building an AI code agent and looking for a deploy target, check out the [APIs for code agents docs](/extend/building-code-agents/apis-for-code-agents/#app).

Whether you deploy a brand new site or create a deploy within an existing site, the process is similar.

First [create a new site](/api-and-cli-guides/api-guides/get-started-with-api#create-site), if needed:

```
POST /api/v1/sites
```

Now you have a site ID and you can create a new deploy, either with a [file digest](/api-and-cli-guides/api-guides/get-started-with-api#file-digest-method) or a [ZIP file](/api-and-cli-guides/api-guides/get-started-with-api#zip-file-method).

### File digest method

We recommend using a digest including a file path and SHA1 for each item. This method also allows you to upload serverless functions, however serverless functions should use SHA256 instead.

```
POST /api/v1/sites/{site_id}/deploys
```

```json
{
  "files": {
    "/index.html": "907d14fb3af2b0d4f18c2d46abe8aedce17367bd",
    "/main.css": "f18c2d7367bd9046abe8aedce17d14fb3af2b0d4"
  },
  "functions": {
    "hello-world": "708b029d8aa9c8fa513d1a25b97ffb6efb12b423"
  }
}
```

When using a file digest, the API will return an object which includes the following properties:

```json
{
  "id": "1234",
  "required": ["907d14fb3af2b0d4f18c2d46abe8aedce17367bd"],
  "required_functions": ["708b029d8aa9c8fa513d1a25b97ffb6efb12b423"]
}
```

The `required` property will give you a list of files by SHA1 that you need to upload. Similarly, `required_functions` will get you an array of required functions by SHA256 to upload, if you included a functions digest when creating the deploy.

### Tip - Tip

If you have two files with the same SHA1, you don't have to upload both of them.

Now upload the files, using the deploy ID returned as `id` in the file digest response:

```
PUT /api/v1/deploys/{deploy_id}/files/index.html
```

### Caution - Warning

Be sure to escape the `file_path` parameter, and ensure file paths don't include `#` or `?` characters.

Use `Content-Type: application/octet-stream` and use the file contents as the HTTP request body.

If the required file is a function, upload it to the functions endpoint, again using the deploy ID returned as `id` in the file digest response:

```
PUT /api/v1/deploys/{deploy_id}/functions/hello-world?runtime=js
```

Possible `runtime` parameters are:

- `js`: zipped Node.js programs or bundled JavaScript files
- `go`: Go binaries

When uploading functions, use the name of the function, not the file path or any file extensions. Clients must zip the function prior to uploading to the API.

Once all files have been uploaded, Netlify will post process the deploy and invalidate the CDN.

#### Async requests for large deploys

API requests that last longer than 30 seconds will be terminated automatically. When creating large deploys, pass the `async` property in your file digest:

```json
{
  "async": true,
  "files": {
    "/index.html": "907d14fb3af2b0d4f18c2d46abe8aedce17367bd"
  },
  "functions": {
    "hello-world": "708b029d8aa9c8fa513d1a25b97ffb6efb12b423"
  }
}
```

The request will then return the deploy ID (as `id`) which can be polled to determine when the deploy is ready for file uploads.

```
GET /api/v1/sites/{site_id}/deploys/{deploy_id}
```

You can check the `state` parameter in the response. It will be set to `preparing` as the upload manifest is generated, and either `prepared`, `uploading`, `uploaded`, or `ready` depending on the contents of the deploy. At this point, the deploy is either `ready`, or the API will give you a list of `required` files and `required_functions`.

Additionally, when uploading large files, sometimes the request will time out. It is safe to retry these uploads a few times to verify whether additional attempts are successful.

### ZIP file method

You can deploy using a ZIP file but note there's a limit of 25,000 files per zip extraction for a site. For the same site, you always need to upload a single zip with all the files.

To deploy using a ZIP file, create a new deploy with `Content-Type: application/zip` and the ZIP file as the HTTP request body:

```
POST /api/v1/sites/{site_id}/deploys
```

A deploy from a ZIP file will enter post-processing mode straight after being created.

While we generally recommend using file digests, you can use the ZIP file method straight from the command line with cURL:

```bash
curl -H "Content-Type: application/zip" \
     -H "Authorization: Bearer YOUR_OAUTH2_ACCESS_TOKEN" \
     --data-binary "@website.zip" \
     https://api.netlify.com/api/v1/sites/mysite.netlify.app/deploys
```

### Create and deploy at once

When creating a new site, you can include a file digest or a ZIP file straight away, to save an HTTP request.

The following will create a new site and deploy it from a ZIP file:

```bash
curl -H "Content-Type: application/zip" \
     -H "Authorization: Bearer YOUR_OAUTH2_ACCESS_TOKEN" \
     --data-binary "@website.zip" \
     https://api.netlify.com/api/v1/sites
```

### Poll for deploy state

You can poll the deploy to check the state:

```
GET /api/v1/deploys/{deploy_id}
```

```json
{ "id": "1234", "state": "ready" }
```

Once the state changes to `ready`, the deploy is live.

### Draft deploys

When creating a new deploy, you can set `"draft": true` to mark the deploy as a draft deploy.

A draft deploy works like a normal deploy, but it won't change the current published deploy of the site when it's done processing.

## Commonly used endpoints

This section describes usage for some popular endpoints.

We also have an [OpenAPI reference for the Netlify API](https://open-api.netlify.com) that you can explore.

Visit our Forums for more tips and conversation about [understanding and using Netlify's API](https://answers.netlify.com/t/common-issue-understanding-and-using-netlifys-api/160).

### Sites

The `/sites` endpoint allows you to access sites deployed on Netlify.

### Tip - Trying to manage your site's environment variables?

To update or retrieve your site's environment variables, leverage the [environment variables](#environment-variables) endpoints. The `/sites` endpoint does not support environment variables.

#### Get sites

`GET /api/v1/sites` returns all sites you have access to.

```json
[
  {
    "id": "3970e0fe-8564-4903-9a55-c5f8de49fb8b",
    "premium": false,
    "claimed": true,
    "name": "synergy",
    "custom_domain": "www.example.com",
    "url": "http://www.example.com",
    "admin_url": "https://api.netlify.com/sites/synergy",
    "screenshot_url": null,
    "created_at": "2013-09-17T05:13:08Z",
    "updated_at": "2013-09-17T05:13:19Z",
    "user_id": "51f60d2d5803545326000005"
  }
]
```

#### Get site

`GET /api/v1/sites/{site_id}` returns the specified site.

### Note - About site IDs

- You can find a value for `{site_id}` by visiting the Netlify UI at 
### NavigationPath Component:

Project configuration > General > Project details > Project information
 and copying **Project ID**, which is the UI label for `site_id`. The same value is returned as `id` when you [create a site](#create-site) or [get a list of sites](#get-sites), and it's the value the `NETLIFY_SITE_ID` environment variable expects.
- Whenever the API requires a `{site_id}`, you can either use the `id` of a site obtained through the API, or the domain of the site (for example, `mysite.netlify.app` or `www.example.com`). These two are interchangeable whenever they're used in API paths.

`GET /api/v1/sites/3970e0fe-8564-4903-9a55-c5f8de49fb8b` returns the site with a matching `id`.

`GET /api/v1/sites/www.example.com` returns the site matching the domain `www.example.com`.

```json
{
  "id": "3970e0fe-8564-4903-9a55-c5f8de49fb8b",
  "premium": false,
  "claimed": true,
  "name": "synergy",
  "custom_domain": "www.example.com",
  "notification_email": "me@example.com",
  "url": "http://www.example.com",
  "admin_url": "https://api.netlify.com/sites/synergy",
  "screenshot_url": null,
  "created_at": "2013-09-17T05:13:08Z",
  "updated_at": "2013-09-17T05:13:19Z",
  "user_id": "51f60d2d5803545326000005"
}
```

#### Create site

`POST /api/v1/sites` creates a new site. By default the site will be created in your personal team.

When creating a site, you can set the following properties:

- `name`: the name of the site (**mysite**.netlify.app)
- `custom_domain`: the custom domain of the site (www.example.com)
- `password`: password protect the site
- `force_ssl`: will force SSL on the site if SSL is enabled
- `processing_settings`: sets the Pretty URLs post processing setting:
  ```json
  {
    "html": { "pretty_urls": true }
  }
  ```
- `repo`: configures continuous deployment. It's a bit complicated to create a `repo` object so please visit our Forums for a verified Support Guide on [linking a repository using the API](https://answers.netlify.com/t/common-issue-linking-a-repository-via-api/121).

#### Create site in team

`POST /api/v1/{account_slug}/sites/` creates a new site in a specific team. It takes the same parameters as when creating a site.

#### Update site

`PATCH /api/v1/sites/{site_id}` updates some attributes on a site.

`PUT /api/v1/sites/{site_id}` updates some attributes on a site.

This lets you update a site. It takes all the same parameters as when creating a site.

If you do a PUT request to a site with `Content-Type: application/zip` and a zipped website in the HTTP request body, it works exactly like creating a new deploy for the site based on a ZIP file.

#### Provision SSL for a site

`POST /api/v1/sites/{site_id}/ssl` activates SSL for a site.

The site must have a custom domain with DNS records configured to point to Netlify's infrastructure.

Any domain aliases with valid DNS records will also be included in the SSL certificate for the site.

This endpoint manually triggers SSL provisioning for a site's custom domains. Once SSL provisioning is successful, the domain will be served over HTTPS.

#### Delete site

`DELETE /api/v1/sites/{site_id}` permanently deletes a site.

This will return `200 OK`.

### Site metadata

Each site has a metadata object. The properties of the metadata object can be used within the [snippets](/api-and-cli-guides/api-guides/get-started-with-api#snippets) for a site by using the [Liquid](https://github.com/Shopify/liquid) template syntax.

#### Get metadata

`GET /api/v1/sites/{site_id}/metadata` gets the metadata for a site.

```json
{
  "my_meta_key": "my_meta_value"
}
```

#### Update metadata

`PUT /api/v1/sites/{site_id}/metadata` replaces the metadata object with a new metadata object.

### Environment variables

The [environment variables API endpoints](https://open-api.netlify.com/#tag/environmentVariables) allow you to access and set both site and shared environment variables. Environment variable changes require a build and deploy to take effect.

#### Get environment variables

`GET /api/v1/accounts/{account_id}/env` returns all environment variables for a team or site. The list will only include shared environment variables if the request is made by a Team Owner.

`GET /api/v1/accounts/{account_id}/env/{key}` returns an individual environment variable for a team or site.

### Note - About account IDs

- You can find a value for `{account_id}` by querying `GET /api/v1/accounts/{account_slug}`. The slug is available in the Netlify UI at 
### NavigationPath Component:

Team settings > General > Team details > Team information
. An account in the Netlify REST API is equivalent to a team in the UI.
- Whenever the API requires an `{account_id}`, you can substitute `{account_slug}`. These two are interchangeable whenever they're used in API paths.

#### Create and update environment variables

`POST /api/v1/accounts/{account_id}/env` creates site or shared environment variables with the specified scopes and contextual values. An environment variable's contextual values are the different values set for use in each [deploy context](/deploy/deploy-overview#deploy-contexts).

`PUT /api/v1/accounts/{account_id}/env/{key}` updates an existing environment variable by replacing all of its values with the values provided with this request.

`PATCH /api/v1/accounts/{account_id}/env/{key}` updates or creates a new value for an existing environment variable.

#### Delete environment variables

`DELETE /api/v1/accounts/{account_id}/env/{key}` deletes an environment variable and all of its values.

`DELETE /api/v1/accounts/{account_id}/env/{key}/value/{id}` deletes a specific environment variable value.

### Files

All files deployed by Netlify can be read through the API. Where the public URL of a file will serve the processed version for HTML pages, the files accessed through the API are the original uploaded files.

Netlify is based on a concept of atomic deploys. This means you never work on individual files. If you want to change a file, you do a new deploy with a new version of the site. To delete a file, you create a new deploy without the file. The file digest based deployment method means that these operations are fast and low-cost. Atomic deploys guarantees that your site is never in an inconsistent state where some files are being uploaded and where users might get HTML files that are not in sync with the CSS, image files, etc.

#### Get files

`GET /api/v1/sites/{site_id}/files` returns a list of all the files in the current deploy.

```json
[
  {
    "id": "/index.html",
    "path": "/index.html",
    "sha": "20828dcdf2cd07e5980fe52759101591bf5014ab",
    "mime_type": "text/html",
    "size": 27232
  }
]
```

#### Get file

`GET /api/v1/sites/{site_id}/files/{file_path}` returns the file.

```json
{
  "id": "/index.html",
  "path": "/index.html",
  "sha": "20828dcdf2cd07e5980fe52759101591bf5014ab",
  "mime_type": "text/html",
  "size": 27232
}
```

You can get the raw contents of the file by using the custom media type `application/vnd.bitballoon.v1.raw` as the `Content-Type` of your HTTP request.

### Deploys

You can access all deploys for a specific site.

#### Get deploys

`GET /api/v1/sites/{site_id}/deploys` returns a list of all deploys for a site.

```json
[
  {
    "id": "52465f435803544542000001",
    "premium": false,
    "claimed": true,
    "name": "synergy",
    "custom_domain": "www.example.com",
    "notification_email": "me@example.com",
    "url": "http://www.example.com",
    "deploy_url": "http://52465f435803544542000001.some-site.netlify.app",
    "admin_url": "https://api.netlify.com/sites/synergy",
    "screenshot_url": null,
    "created_at": "2013-09-17T05:13:08Z",
    "updated_at": "2013-09-17T05:13:19Z",
    "user_id": "51f60d2d5803545326000005",
    "state": "old"
  }
]
```

#### Get deploy

`GET /api/v1/sites/{site_id}/deploys/{deploy_id}` returns a specific deploy.

```json
{
  "id": "52465f435803544542000001",
  "premium": false,
  "claimed": true,
  "name": "synergy",
  "custom_domain": "www.example.com",
  "notification_email": "me@example.com",
  "url": "http://www.example.com",
  "deploy_url": "http://52465f435803544542000001.some-site.netlify.app",
  "admin_url": "https://api.netlify.com/sites/synergy",
  "screenshot_url": null,
  "created_at": "2013-09-17T05:13:08Z",
  "updated_at": "2013-09-17T05:13:19Z",
  "user_id": "51f60d2d5803545326000005",
  "state": "old"
}
```

#### Restore deploy (rollback)

`POST /api/v1/sites/{site_id}/deploys/{deploy_id}/restore` restores an old deploy and makes it the live version of the site.

```json
{
  "id": "52465f435803544542000001",
  "premium": false,
  "claimed": true,
  "name": "synergy",
  "custom_domain": "www.example.com",
  "notification_email": "me@example.com",
  "url": "http://www.example.com",
  "deploy_url": "http://52465f435803544542000001.some-site.netlify.app",
  "admin_url": "https://api.netlify.com/sites/synergy",
  "screenshot_url": null,
  "created_at": "2013-09-17T05:13:08Z",
  "updated_at": "2013-09-17T05:13:19Z",
  "user_id": "51f60d2d5803545326000005",
  "state": "current"
}
```

### Snippets

Snippets are code snippets that are injected into every HTML page of the website, either right before the closing `head` tag or right before the closing `body` tag.

Each snippet can specify code for all pages and code that gets injected into "Thank you" pages shown after a successful form submission.

#### Get snippets

`GET /api/v1/sites/{site_id}/snippets` gets a list of snippets specific to a site.

```json
[
  {
    "id": 0,
    "title": "Test",
    "general": "\u003Cscript\u003Ealert(\"Hello\")\u003C/script\u003E",
    "general_position": "head",
    "goal": "",
    "goal_position": "footer"
  }
]
```

The `general` property is the code that will be injected right before either the head or body end tag. The `general_position` can be `head` or `footer` and determines whether to inject the code in the head element or before the closing body tag.

The `goal` property is the code that will be injected into the "Thank you" page after a form submission. `goal_position` determines where to inject this code.

#### Get snippet

`GET /api/v1/sites/{site_id}/snippets/{snippet_id}` gets a specific snippet.

```json
{
  "id": 0,
  "title": "Test",
  "general": "\u003Cscript\u003Ealert(\"Hello\")\u003C/script\u003E",
  "general_position": "head",
  "goal": "",
  "goal_position": "footer"
}
```

#### Add snippet

`POST /api/v1/sites/{site_id}/snippets` adds a new snippet to a site.

#### Update snippet

`PUT /api/v1/sites/{site_id}/snippets/{snippet_id}` replaces a snippet.

#### Delete snippet

`DELETE /api/v1/sites/{site_id}/snippets/{snippet_id}` deletes a snippet.

### Forms

You can access all [Netlify Forms](/manage/forms/setup) metadata and submissions for a site.

#### Get forms

`GET /api/v1/sites/{site_id}/forms` returns a list of all forms for a site, including metadata about each form, but not including form submissions.

```json
[
  {
    "id": "ac0865cc46440b1e64666f520e8d88d670c8a2f6",
    "site_id": "0d3a9d2f-ef94-4380-93df-27ee400e2048",
    "name": "Landing Page",
    "paths": ["/index"],
    "submission_count": 3,
    "fields": [
      { "name": "name", "type": "text" },
      { "name": "email", "type": "email" },
      { "name": "phone", "type": "text" },
      { "name": "company", "type": "text" },
      { "name": "website", "type": "url" },
      { "name": "number_of_employees", "type": "select" }
    ],
    "created_at": "2013-09-18T20:26:19Z"
  }
]
```

#### Get verified submissions

`GET /api/v1/sites/{site_id}/submissions` returns a list of verified form submissions across all forms for a specific site.

`GET /api/v1/forms/{form_id}/submissions` returns a list of verified form submissions for a specific form.

```json
[
  {
    "id": "5231110b5803540aeb000019",
    "number": 13,
    "title": null,
    "email": "test@example.com",
    "name": "Mathias Biilmann",
    "first_name": "Mathias",
    "last_name": "Biilmann",
    "company": "Netlify",
    "summary": "Hello, World",
    "body": "Hello, World",
    "data": {
      "email": "test@example.com",
      "name": "Mathias Biilmann",
      "ip": "127.0.0.1"
    },
    "created_at": "2013-09-12T00:55:39Z",
    "site_url": "http://synergy.netlify.app"
  }
]
```

#### Get spam submissions

To get spam submissions, add a `state=spam` query parameter to the URL:

`GET /api/v1/sites/{site_id}/submissions?state=spam` returns a list of spam form submissions across all forms for a specific site.

`GET /api/v1/forms/{form_id}/submissions?state=spam` returns a list of spam form submissions for a specific form.

#### Change submission state

You can change the state of a submission from spam to verified or vice versa.

`PUT /api/v1/submissions/{submission_id}/spam` marks the submission as spam.

`PUT /api/v1/submissions/{submission_id}/ham` marks the submission as verified.

#### Delete submissions

`DELETE /api/v1/submissions/{submission_id}` removes a form submission.

#### Delete form

`DELETE /api/v1/sites/{site_id}/forms/{form_id}` removes a form and any existing submissions to it.

Future submissions to the form will result in a 404 error, and previous submissions will no longer be available.

### Hooks

Netlify can trigger webhooks, send email notifications, or send Slack messages on certain events.

The `/hooks` endpoint lets you control the hooks for your site.

#### Get hook types

`GET /api/v1/hooks/types` returns a list of types of hooks that you can configure on Netlify.

```json
[
  {
    "name": "url",
    "fields": [
      {
        "name": "url",
        "options": {
          "type": "string",
          "title": "URL to notify"
        }
      }
    ],
    "events": ["submission_created", "deploy_created", "deploy_failed"]
  }
]
```

Each type has a series of fields that you need to set to create a new hook, and a list of events that can trigger them.

#### Get hooks for a site

`GET /api/v1/hooks?site_id={site_id}` returns a list of a hooks defined for a specific site.

```json
[
  {
    "id": "5636b7a00d61eec2d6001004",
    "site_id": "0d3a9d2f-ef94-4380-93df-27ee400e2048",
    "type": "email",
    "event": "submission_created",
    "data": { "email": "test@example.com" },
    "created_at": "2015-10-20T21:51:51Z",
    "updated_at": "2015-10-20T21:51:51Z"
  }
]
```

#### Create hook

`POST /api/v1/hooks` creates a new hook.

An example request body for an email hook for a specific form in your site would be formatted like this:

```json
{
  "site_id": "0d3a9d2f-ef94-4380-93df-27ee400e2048",
  "form_id": "5235a7a00d61eec2d6001302",
  "type": "email",
  "event": "submission_created",
  "data": { "email": "test@example.com" }
}
```

`form_id` is optional and links the hook to a specific form within your site. You can also use `form_name` with the value of the `name` attribute of the form of your site as an alternative to `form_id`.

#### Delete hook

`DELETE /api/v1/hooks/{hook_id}` removes a hook permanently.

Note, for outgoing webhooks, returning a `410 Gone` status code from the URL endpoint will trigger a deletion of the hook.
