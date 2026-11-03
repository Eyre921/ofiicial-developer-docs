---
title: "Connections and tokens"
source: https://developers.notion.com/guides/connections-and-tokens/overview
path: guides/connections-and-tokens/overview
---

Compare personal access tokens, internal connections, OAuth integrations, and public integrations for your Notion app or automation.

Choose a personal access token, internal connection, OAuth integration, or public integration based on who will use your app and how it needs to access Notion.

## Choose the right option

> [card] [Automate your own work](/guides/connections-and-tokens/personal-access-tokens)
>
> Use a personal access token for scripts, tools, and Workers that run with your Notion permissions.

> [card] [Build a shared workspace tool](/guides/connections-and-tokens/internal-connections)
>
> Use an internal connection for tools your team shares, with access granted to the connection independently of any one person.

> [card] [Build an app for your workspaces](/guides/connections-and-tokens/oauth-integrations/overview)
>
> Use an OAuth integration for internal tools where each person authorizes their own access. Your app acts on behalf of the user who connects it.

> [card] [Build an app for any workspace](/guides/connections-and-tokens/public-integrations/overview)
>
> Use a public integration so users in any workspace can authorize your app through OAuth. You can also apply to list it on the Marketplace.

## Compare the options

OAuth integrations and public integrations use the same OAuth authorization flow. Here, **OAuth integrations** are limited to selected workspaces, while **public integrations** are available to any workspace.

| | Personal access token | Internal connection | OAuth integration | Public integration |
| :- | :- | :- | :- | :- |
| Workspace scope | One workspace. | One workspace. | Workspaces you select when creating the integration. | Any workspace. |
| Whose access does it use? | Yours. | The connection’s own access, shared by the tool. | Each user’s separately authorized access. | Each user’s separately authorized access. |
| Content access | Uses your existing page permissions. | Uses permissions granted to the connection. | Users grant access during authorization. | Users grant access during authorization. |
| Authentication | A token you create for yourself. | An API token for the connection. | Access tokens obtained through OAuth. | Access tokens obtained through OAuth. |
| Marketplace listing | Not eligible. | Not eligible. | Not eligible. | Optional, subject to review. |

## Shared concepts

### Capabilities

[Capabilities](/reference/capabilities) determine which operations a connection or token can perform, such as reading pages, updating databases, or adding comments. Choose the capabilities your app needs.

### Content access

Capabilities and content access work together: permission to update pages does not grant access to every page. A personal access token uses your existing permissions. An internal connection needs content access granted to it. For OAuth integrations and public integrations, each user grants access during authorization. To share content:

* **Internal connections:** Add the page or database in the Developer portal’s **Content access** tab, or open it in Notion and use **Add connections**. See [Granting page access](/guides/connections-and-tokens/internal-connections#granting-page-access) for the steps.
* **OAuth integrations and public integrations:** Each user selects pages in the OAuth page picker when authorizing the app. Selecting a parent page also grants access to its child pages. See [Selecting pages during authorization](/guides/authorization/overview#select-pages-to-share).
* **Personal access tokens:** No separate sharing step is needed. The token uses its creator’s existing permissions, limited by its capabilities.

### Webhooks

Internal connections, OAuth integrations, and public integrations can subscribe to [webhooks](/reference/webhooks) to respond to changes such as page updates and new comments. Use these when your app needs to react to changes without repeatedly checking the API.

## Getting started

Try the [Quickstart](/guides/notion-api/quick-start) to create a page with a personal access token. For setup instructions and permissions, choose one of the guides above.

See [Authorization](/guides/authorization/overview) for token authentication and OAuth flows, and [API credential security](/guides/authorization/credential-security) for storing and protecting credentials.

## Resources

> [card] [API reference](/reference/intro)

> [card] [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js)

> [card] [Starter templates](https://github.com/makenotion/notion-sdk-typescript-starter)

> [card] [Postman collection](https://www.postman.com/notionhq/notion-s-api-workspace/collection/52041987-03f70d8f-b6e5-4306-805c-f95f7cdf05b9)

> [card] [FAQs](/page/frequently-asked-questions)

> [card] [Notion Devs Slack](https://join.slack.com/t/notiondevs/shared_invite/zt-3u9oid9q8-HLUBmMVWYK~g9HFo4U4raA)

> [!NOTE]
>
> **Looking for SCIM or SAML SSO?**
>
> Enterprise identity management (user provisioning, group management, and Single Sign-On) is covered in Notion's Help Center, not in these API docs.
>
> > [card] [Provision users and groups with SCIM](https://www.notion.com/help/provision-users-and-groups-with-scim)
>
> > [card] [SAML SSO configuration](https://www.notion.com/help/saml-sso-configuration)
