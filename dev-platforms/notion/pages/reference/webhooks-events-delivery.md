---
title: "Event types & delivery"
source: https://developers.notion.com/reference/webhooks-events-delivery
path: reference/webhooks-events-delivery
---

Learn about the different event types and how they are delivered to your connection.

Webhooks currently notify you about changes to pages and databases — such as when a new page is created, a title is updated, or someone changes a database schema. The events themselves do not contain the full content that changed. Instead, the webhook acts as a signal that something changed, and it’s up to your connection to follow up with a call to the Notion API to retrieve the latest content.

For example, let’s say a user updates the title of a page. You’ll receive a `page.content_updated` webhook event with the ID of the page that changed. From there, your connection can use the [retrieve a page endpoint](/reference/retrieve-a-page) to fetch the latest page content — including the new title.

<Info>
  For detailed payload schemas for each webhook event type, see the [Webhook events](/reference/webhooks/page-created) API reference.
</Info>

## Event types

### Event properties

**All webhook event types share the following shape of properties:**

| **Field**         | **Type** | **Description**                                                                                                                                                                                                                                                                                                                                              |
| :---------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`              | UUID     | The unique ID of the webhook event                                                                                                                                                                                                                                                                                                                           |
| `timestamp`       | String   | ISO 8601 formatted time at which the event occurred. This field can be used to order events on your side                                                                                                                                                                                                                                                     |
| `workspace_id`    | UUID     | The workspace ID where the event originated from                                                                                                                                                                                                                                                                                                             |
| `subscription_id` | UUID     | The ID of the webhook subscription                                                                                                                                                                                                                                                                                                                           |
| `integration_id`  | UUID     | Associated connection ID the subscription is set up with                                                                                                                                                                                                                                                                                                     |
| `type`            | String   | Type of the event, e.g. `page.created`                                                                                                                                                                                                                                                                                                                       |
| `authors`         | Array    | Array of objects with the ID (`id`) and type (`type`) of the author who performed the action. `type` can be `"person"`, `"bot"`, or `"agent"`. Typically an array of length 1; can be more for aggregated events. See [bot](/reference/user#bots) or [person](/reference/user#people) for details retrievable by ID in the [Users API](/reference/get-user). |
| `accessible_by`   | Array    | Array of objects with the ID (`id`) and type (`type`) of each accessible bot and user who owns the bot connection to the `integration_id` and has access to the webhook's `entity`. Only for public connections. `type` can be `"person"` or `"bot"`.                                                                                                        |
| `attempt_number`  | number   | Attempt number (1-8) of the current event delivery                                                                                                                                                                                                                                                                                                           |
| `entity`          | Object   | ID (`id`) and type (`type`) of the object that triggered the event. `type` can be `"page"`, `"block"`, or `"database"`.                                                                                                                                                                                                                                      |
| `data`            | Object   | Additional, event-specific data.                                                                                                                                                                                                                                                                                                                             |

### Supported webhook event types

Notion currently supports the following webhook event types. Each event represents a meaningful change to content in a workspace — such as the creation of a page, a schema update, or a new comment.

<Note>
  **More event types may be added in the future**

  If Notion supports additional event types or resources, your subscription won't update automatically to receive them.

  To subscribe to more event types or change the existing types your endpoint is receiving, update your subscription in the connection page's **Webhooks** tab.
</Note>

Below, you’ll find the list of available type values, a short description of what each event represents, and whether the event is aggregated. Aggregated events group multiple changes into a single notification to reduce noise and improve efficiency.

| Type                          | Description                                                                                                                                                 | Is aggregated? |
| :---------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------- |
| `page.content_updated`        | Triggered when the content of a page changes — for example adding or removing a block on the page.                                                          | Yes            |
| `page.created`                | Triggered when a new page is created.                                                                                                                       | Yes            |
| `page.deleted`                | Triggered when a page is moved to the trash.                                                                                                                | Yes            |
| `page.locked`                 | Triggered when a page is locked from editing.                                                                                                               | No             |
| `page.moved`                  | Triggered when a page is moved to another location.                                                                                                         | Yes            |
| `page.properties_updated`     | Triggered when a page's property is updated.                                                                                                                | Yes            |
| `page.undeleted`              | Triggered when a page is restored from the trash.                                                                                                           | Yes            |
| `page.unlocked`               | Triggered when a page is unlocked                                                                                                                           | No             |
| `database.content_updated`    | Triggered when a database's content is updated— for example, adding or removing a child page. <br /> <br />**Deprecated** in 2025-09-03 API version.        | Yes            |
| `database.created`            | Triggered when a new database is created.                                                                                                                   | Yes            |
| `database.deleted`            | Triggered when a database is moved to the trash.                                                                                                            | Yes            |
| `database.moved`              | Triggered when a database is moved to another location.                                                                                                     | Yes            |
| `database.schema_updated`     | Triggered when a database's schema is updated — for example, adding or removing a database property. <br /> <br />**Deprecated** in 2025-09-03 API version. | Yes            |
| `database.undeleted`          | Triggered when a database is restored from the trash.                                                                                                       | Yes            |
| `data_source.content_updated` | Triggered when a data source's content is updated— for example, adding or removing a child page. <br /> <br />**New** in 2025-09-03 API version.            | Yes            |
| `data_source.created`         | Triggered when a new data source is created within an existing database. <br /> <br />**New** in 2025-09-03 API version.                                    | Yes            |
| `data_source.deleted`         | Triggered when a data source is moved to the trash. <br /> <br />**New** in 2025-09-03 API version.                                                         | Yes            |
| `data_source.moved`           | Triggered when a data source is moved to another database. <br /> <br />**New** in 2025-09-03 API version.                                                  | Yes            |
| `data_source.schema_updated`  | Triggered when a data source's schema is updated — for example, adding or removing a database property. <br /> <br />**New** in 2025-09-03 API version.     | Yes            |
| `data_source.undeleted`       | Triggered when a data source is restored from the trash. <br /> <br />**New** in 2025-09-03 API version.                                                    | Yes            |
| `comment.created`             | Triggered when a new comment or suggested edit is added to a page or block                                                                                  | No             |
| `comment.deleted`             | Triggered when a comment is deleted.                                                                                                                        | No             |
| `comment.updated`             | Triggered when a comment is edited.                                                                                                                         | No             |

<Info>
  **What does “aggregated” mean?**

  For high-frequency events like `page.content_updated`, Notion batches changes that occur within a short time window into a single webhook event. Events such as `page.created`, `page.deleted`, `page.undeleted` occur in quick succession, you may only recieve the most meaningful result event -- or none at all if the state returns to its original one.

  Event aggregration helps reduce redundant calls and improves reliability. Aggregated events may have a slight delivery delay (typically under one minute).
</Info>

## Event delivery

Events should be delivered within 5 minutes of their occurrences. Most should be be delivered within a minute. Here are a few things to keep in mind when consuming webhook events.

### Event aggregation

Certain events that occur frequently, like page.content\_updated, are aggregated by their entity within a brief time window. As a result, there may be a slight delay between the first occurrence of an event and its delivery to your webhook URL.

### Event ordering

Events may arrive in a different order than they occurred. If event ordering is critical for your workflows, use the event's timestamp field to reorder them. Also, webhook events may not show the most current state of the data. We strongly recommend fetching the latest data from the API.

### Delivery retries

W# Authentication
Source: https://developers.notion.com/cli/get-started/authentication

Log in to your Notion workspace and manage CLI credentials.

## Log in

Authenticate with your Notion workspace:

```bash theme={null}
ntn login
```

This opens your browser to an authorization page. Confirm that the code in the browser matches the code printed in your terminal before approving. This prevents another page from completing the login in your name.

Your workspace-scoped token will be stored securely in your system's keychain.

If you've already logged in to one or more workspaces, you can pick existing workspace to switch the default, or pick **Authenticate with new workspace** to start a fresh browser flow and add another workspace.

<Note>
  `ntn login` requires full workspace membership. [Guests](https://www.notion.com/help/whos-who-in-a-workspace) and [restricted members](https://www.notion.com/help/whos-who-in-a-workspace) cannot log in with the Notion CLI. If you need CLI access, ask a workspace admin to upgrade your role. See [Personal access tokens](/guides/get-started/personal-access-tokens) for more on who can create tokens.
</Note>

## Log in without a browser

On a remote machine, container, or CI runner that can't open a browser, use `--no-browser` to get a two-step login flow:

1. Run `ntn login --no-browser`. It prints a URL, a verification code, and a `ntn login poll` command.
2. Open the URL in any browser, sign in, and confirm the verification code.
3. Run `ntn login poll` on the original machine to redeem the token.

`ntn login` also falls back to this flow automatically when it detects there is no terminal (e.g. piped input).

Login sessions expire after a short window. If polling fails because the session expired, run `ntn login` again to start over.

For unattended use (CI, scripts, bots), prefer a [personal access token](#use-a-personal-access-token) instead.

## Target a specific workspace

To run a single command against a non-default workspace without switching defaults, set `NOTION_WORKSPACE_ID`:

```bash theme={null}
NOTION_WORKSPACE_ID=<workspace-id> ntn api v1/users/me
```

Workspace IDs are listed in the output of `ntn debug`.

## Use a personal access token

For unattended use, authenticate with a [personal access token](/guides/get-started/personal-access-tokens) (PAT) by exporting it as `NOTION_API_TOKEN`:

```bash theme={null}
export NOTION_API_TOKEN=ntn_xxx...
ntn api v1/users/me
```

`NOTION_API_TOKEN` takes precedence over anything stored in the keychain, so the same shell can mix `ntn login`-based commands and PAT-based commands depending on what's exported.

## Inspect your session

```bash theme={null}
ntn doctor
```

## Log out

```bash theme={null}
ntn logout
```

This forgets every cached workspace, deletes each one's token from the keychain, and clears the default workspace. The `config.json` and `workspaces.json` files themselves stay in place — run `ntn login` to repopulate them.

## Where credentials are stored

Tokens live in your OS credential store (Keychain on macOS, Secret Service on Linux) under the service name `notion-cli`, with the workspace ID as the account.

Two files sit alongside them in the CLI config directory:

* `config.json` — CLI version, default workspace per, and the optional `keyring` toggle.
* `workspaces.json` — cached workspace IDs and names for the interactive picker.

The config directory is `NOTION_HOME` if set, otherwise `$XDG_CONFIG_HOME/notion`, `$HOME/.config/notion`, or `$HOME/.notion` as fallbacks.

### Opt out of the OS keychain

On systems without a usable keychain, `ntn login` fails with a keychain error. Common examples include Docker containers, CI runners, SSH sessions to a Linux server, etc.

Set `NOTION_KEYRING=0` to store tokens in plain JSON at `auth.json` in the config directory instead. Treat that file like any other secret.

```bash theme={null}
NOTION_KEYRING=0 ntn login
```

To make it permanent, set `"keyring": false` in `config.json`. The env var always wins.

## Environment variables

| Variable              | Purpose                                                                                              |
| :-------------------- | :--------------------------------------------------------------------------------------------------- |
| `NOTION_API_TOKEN`    | When this is set, it'll take precedence over `ntn login`'s keychain entry. Handy for scripts and CI. |
| `NOTION_WORKSPACE_ID` | Override the default workspace for a single command.                                                 |
| `NOTION_KEYRING`      | Set to `0` to use file-based storage instead of the OS keychain.                                     |
| `NOTION_HOME`         | Override the config directory.                                                                       |
| `NOTION_ENV`          | Same as `--env`. Rarely needed.                                                                      |

Run `ntn login --help` for the full list.

## Next steps

<CardGroup>
  <Card title="Workers quickstart" icon="rocket" href="/workers/get-started/quickstart">
    Create and deploy your first Notion Worker.
  </Card>

  <Card title="API requests" icon="terminal" href="/cli/guides/api-requests">
    Make Notion API requests from the terminal.
  </Card>

  <Card title="Command reference" icon="book-open" href="/cli/reference/commands">
    Full reference for every ntn command.
  </Card>

  <Card title="Personal access tokens" icon="key" href="/guides/get-started/personal-access-tokens">
    Create tokens for scripts and CI.
  </Card>
</CardGroup>
