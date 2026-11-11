---
title: "Public integrations"
source: https://developers.notion.com/guides/connections-and-tokens/public-integrations/overview
path: guides/connections-and-tokens/public-integrations/overview
---

Create an OAuth integration available to any Notion workspace, with the option to list it on the Marketplace.

## What is a public integration?

A public integration is an OAuth integration that users can install in any Notion workspace. The Developer portal also refers to these as public connections. Unlike [internal connections](/guides/connections-and-tokens/internal-connections), which are scoped to a single workspace with a static token, public connections follow the [OAuth 2.0](https://oauth.net/2/) protocol: each user who authorizes the connection receives their own access token, scoped to their workspace.

Choose **Any workspace** as the installation scope. If your app should only be available in specific workspaces, follow the [OAuth integrations guide](/guides/connections-and-tokens/oauth-integrations/overview).

If you only need a token for your own scripts, CLI workflows, Workers, or trusted tools, use a [personal access token](/guides/connections-and-tokens/personal-access-tokens). PATs also act as one Notion user, but they do not provide an OAuth install flow for other users.

This guide covers:

* How public connections differ from internal connections
* How installation scope controls who can install your connection
* How users authorize a public connection via OAuth
* How to create a public connection in the Developer portal

## How public integrations differ from internal connections

The key differences come down to scope, identity, and how access is granted:

* **Scope:** Internal connections work in one workspace; public connections can install into many. [Installation scope](#installation-scope) controls which workspaces are eligible.
* **Identity:** Internal connections operate as their own bot user with permissions independent of any specific person. Public connections act on behalf of the individual user who authorized them — the access token is tied to that user. [Personal access tokens](/guides/connections-and-tokens/personal-access-tokens) are also tied to one user, but they are created directly by that user instead of through OAuth.
* **Page access:** Internal connections can be granted access through the Developer portal’s **Content access** tab or the **Add connections** menu in Notion. See [Grant page access](/guides/connections-and-tokens/internal-connections#granting-page-access). Public connections use the OAuth page picker, where users choose which pages to grant access to during the authorization flow.

For a full comparison, see the [comparison table](/guides/connections-and-tokens/overview#comparison) in the Overview.

## Installation scope

For a public integration, choose **Any workspace** when you create it. This makes the integration eligible for Marketplace listing, subject to review. Listing is optional.

> [!WARNING]
>
> Installation scope is set once, at creation time, and can't be changed afterward. If you pick **Or select 1 or more workspaces** and later want to list on the Marketplace, create a new connection.

## How users authorize a public integration

When a user wants to use your OAuth integration, they go through an OAuth authorization flow:

**Step 1**

The user visits the connection's authorization URL. Find this URL in the **Configuration** tab of your connection in the Developer portal.

**Step 2**

Notion presents a prompt describing the connection's [capabilities](/reference/capabilities) — what it will be able to do in the user's workspace.

**Step 3**

The user selects which pages to grant the connection access to using the page picker.

**Step 4**

After the user approves, Notion redirects them to your redirect URI with a temporary authorization code.

**Step 5**

Your connection exchanges the code for an access token, which is used for all subsequent API requests on behalf of that user.

OAuth integrations can also offer a Notion template during the auth flow. If configured, users can choose to duplicate the template into their workspace instead of selecting existing pages. See the [Authorization guide](/guides/authorization/overview#prompt-for-a-connection-with-a-notion-template-option) for details on configuring templates.

> [!NOTE]
>
> After a user authorizes a OAuth integration, only that user can interact with the connection in their workspace. If multiple members in a workspace want to use the same OAuth integration, each user needs to complete the authorization flow individually.

## Create a public integration

**Step 1**

Navigate to the [Developer portal](https://app.notion.com/developers/connections).

**Step 2**

In the **Build** section of the sidebar, select **Connections**.

**Step 3**

Click **Create new connection** and fill in the required fields, including:

* Connection name and development workspace
* [Redirect URI(s)](https://www.oauth.com/oauth2-servers/redirect-uris/) for the OAuth flow
* [Installation scope](#installation-scope) — choose **Any workspace**
* Connection [capabilities](/reference/capabilities) (read content, update content, insert content, etc.)

**Step 4**

After creation, visit the **Configuration** tab to retrieve your **OAuth client ID** and **OAuth client secret**. The client ID identifies your connection to Notion during the OAuth flow, and the client secret proves your connection is who it claims to be. Both are required when your server exchanges the authorization code for an access token. See the [Authorization guide](/guides/authorization/overview) for the full implementation.

> [!NOTE]
>
> Marketplace listing details (such as descriptions, categories, and images) are managed separately through the **Listings** section. See [List on the Marketplace](/guides/connections-and-tokens/public-integrations/marketplace-listing) for details.

Public connections must undergo a Notion security review before being [listed on the Marketplace](/guides/connections-and-tokens/public-integrations/marketplace-listing). You can create and use a public connection without listing it.

## Next steps

> [card] [Set up OAuth authorization](/guides/authorization/overview)
>
> Implement the full OAuth 2.0 flow for your public connection.

> [card] [Set up content for users](/guides/connections-and-tokens/oauth-integrations/preparing-for-users)
>
> Automate user onboarding after they install your connection.
