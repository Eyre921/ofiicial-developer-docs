---
title: "OAuth integrations"
source: https://developers.notion.com/guides/connections-and-tokens/oauth-integrations/overview
path: guides/connections-and-tokens/oauth-integrations/overview
---

Build an internal tool for your Notion workspaces where each user authorizes their own access.

Use an OAuth integration when your internal tool needs to act on behalf of each person who uses it. Each user authorizes the app separately and grants it access to content. Your app uses an access token tied to that user.

For example, a tool that helps teammates work with their own project pages can ask each person to connect their Notion account. A shared automation that updates one team tracker can use an [internal connection](/guides/connections-and-tokens/internal-connections), with access granted to the connection independently of any one person.

Both options can serve internal tools. Choose OAuth when access needs to be authorized by each user, and an internal connection when the tool should use shared connection access.

## Installation scope

Choose **Or select 1 or more workspaces** when creating your integration. Only those workspaces can install it, and it cannot be listed on the Marketplace. To make your app available to any workspace, create a [public integration](/guides/connections-and-tokens/public-integrations/overview).

Installation scope cannot be changed after creation. If you later need to make the app available to any workspace, create a new integration.

## Create an OAuth integration

**1. Open the Developer portal**

Go to the [Developer portal](https://app.notion.com/developers/connections). In the **Build** section, select **Connections**. This is also where you create OAuth integrations limited to selected workspaces.

**2. Configure your integration**

Select **Create new connection**. Enter the connection name, development workspace, and [redirect URIs](https://www.oauth.com/oauth2-servers/redirect-uris/). Choose **Or select 1 or more workspaces**, select the workspaces, and choose the [capabilities](/reference/capabilities) your app needs.

**3. Get your OAuth credentials**

Open the **Configuration** tab to find your **OAuth client ID** and **OAuth client secret**. Use them to implement the [OAuth authorization flow](/guides/authorization/overview#public-connection-authorization-overview).

## How users authorize your app

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

## Next steps

> [card] [Set up OAuth authorization](/guides/authorization/overview)
>
> Implement the authorization flow and exchange codes for access tokens.

> [card] [Set up content for users](/guides/connections-and-tokens/oauth-integrations/preparing-for-users)
>
> Create pages and databases after a user authorizes your app. This works for both scoped and public integrations.
