---
title: "Notion connections"
source: https://developers.notion.com/guides/get-started/overview
path: guides/get-started/overview
---

Compare internal connections, public connections, and personal access tokens.

## What is a Notion connection?

A [connection](https://www.notion.com/help/add-and-manage-connections-with-the-api) gives an app access to content in a Notion workspace. For example, a connection can add tasks to a database or post a comment on a page. You can also call the same API as yourself with a personal access token.

![A connection links a Notion workspace to tools that a team uses.](https://mintcdn.com/notion-demo/LHm9qfrJYJOPRxs6/images/docs/0f06356-notion_overview.jpg?fit=max\&auto=format\&n=LHm9qfrJYJOPRxs6\&q=85\&s=ab31886c0c84514c8db8a2801d4fffe4)

## Connection types

Use an [internal connection](/guides/get-started/internal-connections) for a team automation in one workspace. A [public connection](/guides/get-started/public-connections#installation-scope) uses OAuth so other people can install your app. A [personal access token](/guides/get-started/personal-access-tokens) runs a script or tool with your own access.

> [!NOTE]
>
> Public connections must undergo a Notion security review before being [listed on the Marketplace](/guides/get-started/marketplace-listing). You can create and use a public connection without listing it.

### Comparison

| Feature | Internal connections | Public connections | Personal access tokens |
| :- | :- | :- | :- |
| Best for | Team-owned automations in one workspace. | Apps or services used by many Notion users or workspaces. | User-owned scripts, CLI workflows, Workers, and trusted tools. |
| Installation scope | Single workspace. | Any workspace, or a specific set of workspaces chosen at creation time. Scope can't change after creation. | One user in one workspace. |
| User access | Only members of the workspace where it's installed. | Any user in a workspace where the connection is allowed to install. | The member who created the token. |
| Content access | Granted directly to the connection, not tied to any specific user. | Users choose which pages to share during the OAuth flow or via the Add connections menu. | Uses the creator's Notion permissions; pages do not need to be shared with a bot. |
| Authentication | Internal connection API token. | OAuth 2.0. | Static bearer token. |

> [!NOTE]
>
> **Looking for SCIM or SAML SSO?**
>
> Enterprise identity management (user provisioning, group management, and Single Sign-On) is covered in Notion's Help Center, not in these API docs.
>
> > [card] [Provision users and groups with SCIM](https://www.notion.com/help/provision-users-and-groups-with-scim)
>
> > [card] [SAML SSO configuration](https://www.notion.com/help/saml-sso-configuration)

## Shared concepts

### Capabilities

[Capabilities](/reference/capabilities) control which operations a connection or token can perform, such as reading content or adding comments.

> [card] [Pages](/guides/data-apis/working-with-page-content)
>
> Create, update, and retrieve page content.

> [card] [Databases](/guides/data-apis/working-with-databases)
>
> Create a database and find its data sources.

> [card] [Views](/guides/data-apis/working-with-views)
>
> Create and configure database views programmatically.

> [card] [Data sources](/reference/data-source)
>
> Manage data sources, properties, entries, and schemas.

> [card] [File uploads](/guides/data-apis/working-with-files-and-media)
>
> Upload and attach files to pages and databases.

> [card] [Comments](/guides/data-apis/working-with-comments)
>
> Handle page and inline comments.

> [card] [Content queries](/reference/post-search)
>
> Find pages and data sources by title.

> [card] [Users](/reference/user)
>
> Read user profiles available to your connection.

### Content access

Connections must have access to pages and databases before they can interact with them. The mechanism differs by type:

* **Internal connections** can be granted access in two ways: the connection owner can add pages directly from the **Content access** tab in the Developer portal, or workspace members can share pages via the **Add connections** menu in Notion.
* **Public connections** use the OAuth page picker, where users select which pages to grant access to during the authorization flow.
* **Personal access tokens** use the token creator's existing Notion permissions. If the creator can access a page in Notion, a PAT with the right capabilities can access it through the API.

See the [Internal connections](/guides/get-started/internal-connections), [Public connections](/guides/get-started/public-connections), and [Personal access tokens](/guides/get-started/personal-access-tokens) guides for specifics on how content access works for each type.

### Webhooks

Connections can subscribe to real-time events — like page updates, property changes, and new comments — via webhooks. This allows your connection to react to changes in Notion without polling the API. See the [Webhooks guide](/reference/webhooks) for details on setting up webhook subscriptions.

## Getting started

Follow the [API quickstart](/guides/get-started/quick-start) to create a private page. If you’re building a public connection, see how to [authorize users](/guides/get-started/authorization), [store credentials](/guides/get-started/handling-api-keys), and [set up content for new users](/guides/get-started/preparing-for-users).

## Resources

> [card] [API reference](/reference/intro)

> [card] [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js)

> [card] [Starter templates](https://github.com/makenotion/notion-sdk-typescript-starter)

> [card] [Postman collection](https://www.postman.com/notionhq/notion-s-api-workspace/collection/52041987-03f70d8f-b6e5-4306-805c-f95f7cdf05b9)

> [card] [FAQs](/page/frequently-asked-questions)

> [card] [Notion Devs Slack](https://join.slack.com/t/notiondevs/shared_invite/zt-3u9oid9q8-HLUBmMVWYK~g9HFo4U4raA)
