---
title: "Public connections"
source: https://developers.notion.com/guides/get-started/public-connections
path: guides/get-started/public-connections
---

Learn how public connections work, how users authorize them, and how to create one.

## What is a public connection?

A public connection is an OAuth connection that users install into their Notion workspaces. Unlike [internal connections](/guides/get-started/internal-connections), which are scoped to a single workspace with a static token, public connections follow the [OAuth 2.0](https://oauth.net/2/) protocol: each user who authorizes the connection receives their own access token, scoped to their workspace.

When you create a public connection, you also choose its [installation scope](#installation-scope) — either **Any workspace** (Marketplace-eligible) or **Selected workspaces only** (not Marketplace-eligible).

If you only need a token for your own scripts, CLI workflows, Workers, or trusted tools, use a [personal access token](/guides/get-started/personal-access-tokens). PATs also act as one Notion user, but they do not provide an OAuth install flow for other users.

This guide covers:

* How public connections differ from internal connections
* How installation scope controls who can install your connection
* How users authorize a public connection via OAuth
* How to create a public connection in the Developer portal

## How public connections differ from internal connections

The key differences come down to scope, identity, and how access is granted:

* **Scope:** Internal connections work in one workspace; public connections can install into many. [Installation scope](#installation-scope) controls which workspaces are eligible.
* **Identity:** Internal connections operate as their own bot user with permissions independent of any specific person. Public connections act on behalf of the individual user who authorized them — the access token is tied to that user. [Personal access tokens](/guides/get-started/personal-access-tokens) are also tied to one user, but they are created directly by that user instead of through OAuth.
* **Page access:** Internal connections require workspace members to manually share pages via the "Add connections" menu. Public connections use the OAuth page picker, where users choose which pages to grant access to during the authorization flow.

For a full comparison, see the [comparison table](/guides/get-started/overview#comparison) in the Overview.

## Installation scope

Every public connection has an **installation scope** that controls which workspaces can install it. You pick the scope when you create the connection.

| Scope                    | Who can install                                  | Marketplace eligible |
| :----------------------- | :----------------------------------------------- | :------------------- |
| Any workspace            | Any Notion user, in any workspace.               | Yes                  |
| Selected workspaces only | Only the workspaces you select at creation time. | No                   |

<Warning>
  Installation scope is set once, at creation time, and can't be changed afterward. If you pick **Selected workspaces only** and later want to list on the Marketplace, create a new connection.
</Warning>

## How users authorize a public connection

When a user wants to use your public connection, they go through an OAuth authorization flow:

<Steps>
  <Step>
    The user visits the connection's authorization URL. Find this URL in the **Configuration** tab of your connection in the Developer portal.
  </Step>

  <Step>
    Notion presents a prompt describing the connection's [capabilities](/reference/capabilities) — what it will be able to do in the user's workspace.
  </Step>

  <Step>
    The user selects which pages to grant the connection access to using the page picker.
  </Step>

  <Step>
    After the user approves, Notion redirects them to your redirect URI with a temporary authorization code.
  </Step>

  <Step>
    Your connection exchanges the code for an access token, which is used for all subsequent API requests on behalf of that user.
  </Step>
</Steps>

Public connections can also offer a Notion template during the auth flow. If configured, users can choose to duplicate the template into their workspace instead of selecting existing pages. See the [Authorization guide](/guides/get-started/authorization#prompt-for-a-connection-with-a-notion-template-option) for details on configuring templates.

<Note>
  After a user authorizes a public connection, only that user can interact with the connection in their workspace. If multiple members in a workspace want to use the same public connection, each user needs to complete the authorization flow individually.
</Note>

## Creating a public connection

<Steps>
  <Step>
    Navigate to the <a href={developerConnectionsUrl}>Developer portal</a>.
  </Step>

  <Step>
    In the **Build** section of the sidebar, select **Public connections**.
  </Step>

  <Step>
    Click **Create new connection** and fill in the required fields, including:

    * Connection name and development workspace
    * [Redirect URI(s)](https://www.oauth.com/oauth2-servers/redirect-uris/) for the OAuth flow
    * [Installation scope](#installation-scope) — choose **Any workspace** or **Selected workspaces only** (if you pick the latter, select the workspaces from the list that appears)
    * Connection [capabilities](/reference/capabilities) (read content, update content, insert content, etc.)
  </Step>

  <Step>
    After creation, visit the **Configuration** tab to retrieve your **OAuth client ID** and **OAuth client secret**. The client ID identifies your connection to Notion during the OAuth flow, and the client secret proves your connection is who it claims to be. Both are required when your server exchanges the authorization code for an access token. See the [Authorization guide](/guides/get-started/authorization) for the full implementation.
  </Step>
</Steps>

<Note>
  Marketplace listing details (such as descriptions, categories, and images) are managed separately through the **Listings** section. See [List on the Marketplace](/guides/get-started/marketplace-listing) for details.
</Note>

## Next steps

<CardGroup>
  <Card title="Set up OAuth authorization" icon="lock" href="/guides/get-started/authorization">
    Implement the full OAuth 2.0 flow for your public connection.
  </Card>

  <Card title="Preparing for users" icon="wand-magic-sparkles" href="/guides/get-started/preparing-for-users">
    Automate user onboarding after they install your connection.
  </Card>
</CardGroup>
