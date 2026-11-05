---
title: "Page property items"
source: https://developers.notion.com/reference/property-item-object
path: reference/property-item-object
---

Reference for single property items, paginated values, and rollup results.

## Overview

[Retrieve a page property item](/reference/retrieve-a-page-property) reads one property on one page. It returns either a `property_item` object or a `list` of property items. The type determines the response shape.

The [page property values reference](/reference/page-property-values) defines each value type. Its examples include a Property item tab. This page defines the response wrapper and pagination rules.

## Common fields

| Field | Type | Meaning |
| :- | :- | :- |
| `object` | String | Always `property_item` for an individual item. |
| `id` | String | The property ID, shared by all items in that property. It is not a unique item ID. |
| `type` | String | The property type. |
| Key matching `type` | Varies | A single value of that type. |

A property’s `id` stays the same when its name changes. IDs can be short strings or UUIDs. The Name property always has the ID `title`.

Responses use URL-encoded property IDs, such as `f%5C%5C%3Ap`. Pass the returned ID as-is to the SDK or in an API path. Don’t encode it a second time. You can also use a property ID as a key in a request’s `properties` object.

## Response shape by type

Single-item responses use the same value shape as page responses. Follow a type link for its fields, write rules, and JSON examples.

| Type | Response |
| :- | :- |
| [`button`](/reference/page-property-values#button) | One property item. |
| [`checkbox`](/reference/page-property-values#checkbox) | One property item. |
| [`created_by`](/reference/page-property-values#created-by) | One property item. |
| [`created_time`](/reference/page-property-values#created-time) | One property item. |
| [`date`](/reference/page-property-values#date) | One property item. |
| [`email`](/reference/page-property-values#email) | One property item. |
| [`files`](/reference/page-property-values#files) | One property item. |
| [`formula`](/reference/page-property-values#formula) | One property item. |
| [`last_edited_by`](/reference/page-property-values#last-edited-by) | One property item. |
| [`last_edited_time`](/reference/page-property-values#last-edited-time) | One property item. |
| [`multi_select`](/reference/page-property-values#multi-select) | One property item. |
| [`number`](/reference/page-property-values#number) | One property item. |
| [`people`](/reference/page-property-values#people) | A paginated list; each item contains one user object. |
| [`phone_number`](/reference/page-property-values#phone-number) | One property item. |
| [`place`](/reference/page-property-values#place) | One property item. |
| [`relation`](/reference/page-property-values#relation) | A paginated list; each item contains one page reference. |
| [`rich_text`](/reference/page-property-values#rich-text) | A paginated list; each item contains one rich text object. |
| [`rollup`](/reference/page-property-values#rollup) | A paginated list with metadata in `property_item.rollup`. |
| [`select`](/reference/page-property-values#select) | One property item. |
| [`status`](/reference/page-property-values#status) | One property item. |
| [`title`](/reference/page-property-values#title) | A paginated list; each item contains one rich text object. |
| [`unique_id`](/reference/page-property-values#unique-id) | One property item. |
| [`url`](/reference/page-property-values#url) | One property item. |
| [`verification`](/reference/page-property-values#verification) | One property item. |

## Status

Status is a single property item. The response is not wrapped in a property name or a `properties` object.

> [tab] Schema
>
> ```json Schema theme={null}
> {
>   "Status": {
>     "id": "stat",
>     "name": "Status",
>     "description": null,
>     "type": "status",
>     "status": {
>       "default_option": "In progress",
>       "options": [
>         {
>           "id": "330aeafb-598c-4e1c-bc13-1148aa5963d3",
>           "name": "In progress",
>           "color": "blue",
>           "description": null
>         }
>       ],
>       "groups": [
>         {
>           "id": "b9d42483-e576-4858-a26f-ed940a5f678f",
>           "name": "To-do",
>           "color": "gray",
>           "option_ids": []
>         },
>         {
>           "id": "cf4952eb-1265-46ec-86ab-4bded4fa2e3b",
>           "name": "In progress",
>           "color": "blue",
>           "option_ids": [
>             "330aeafb-598c-4e1c-bc13-1148aa5963d3"
>           ]
>         },
>         {
>           "id": "4fa7348e-ae74-46d9-9585-e773caca6f40",
>           "name": "Complete",
>           "color": "green",
>           "option_ids": []
>         }
>       ]
>     }
>   }
> }
> ```

> [tab] Page value
>
> ```json Page value theme={null}
> {
>   "Status": {
>     "id": "stat",
>     "type": "status",
>     "status": {
>       "id": "330aeafb-598c-4e1c-bc13-1148aa5963d3",
>       "name": "In progress",
>       "color": "blue"
>     }
>   }
> }
> ```

> [tab] Page write
>
> ```json Page write theme={null}
> {
>   "properties": {
>     "Status": {
>       "status": {
>         "name": "In progress"
>       }
>     }
>   }
> }
> ```

> [tab] Property item
>
> ```json Property item theme={null}
> {
>   "object": "property_item",
>   "id": "stat",
>   "type": "status",
>   "status": {
>     "id": "330aeafb-598c-4e1c-bc13-1148aa5963d3",
>     "name": "In progress",
>     "color": "blue"
>   }
> }
> ```

## Paginated values

`title`, `rich_text`, `people`, and `relation` always return a list, even if there is only one item. Empty values return `results: []`. Multi-select and files return a single property item whose value is an array.

| Field | Type | Meaning |
| :- | :- | :- |
| `object` | String | `list`. |
| `type` | String | `property_item`. |
| `results` | Array | The property items in this response. |
| `has_more` | Boolean | Whether another page of results exists. |
| `next_cursor` | String or `null` | Pass this as `start_cursor` in the next request. |
| `property_item` | Object | Metadata for the property being retrieved. |
| `property_item.id` | String | The requested property ID. |
| `property_item.type` | String | The requested property type. |
| `property_item.next_url` | String or `null` | The URL for the next request. This field is nested, not top-level. |
| `property_item.{type}` | Object | Empty for the four list types above. Rollups include a result or calculation state. |

The metadata under `property_item` is not an individual result and has no `object` field. For a relation item, the nested `relation.id` identifies the related page; the item’s own `id` identifies the property.

```json First page of a relation, with page_size=1 theme={null}
{
  "object": "list",
  "results": [
    {
      "object": "property_item",
      "id": "proj",
      "type": "relation",
      "relation": { "id": "dd456007-6c66-4bba-957e-ea501dcda3a6" }
    }
  ],
  "next_cursor": "opaque-cursor",
  "has_more": true,
  "type": "property_item",
  "property_item": {
    "id": "proj",
    "next_url": "https://api.notion.com/v1/pages/60bdc8bd-3880-44b8-a9cd-8a145b3ffbd7/properties/proj?start_cursor=opaque-cursor&page_size=1",
    "type": "relation",
    "relation": {}
  }
}
```

Continue with `next_cursor` until `has_more` is `false`. In the final response, `next_cursor` and `prope# Authentication
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

> [!NOTE]
>
> `ntn login` requires full workspace membership. [Guests](https://www.notion.com/help/whos-who-in-a-workspace) and [restricted members](https://www.notion.com/help/whos-who-in-a-workspace) cannot log in with the Notion CLI. If you need CLI access, ask a workspace admin to upgrade your role. See [Personal access tokens](/guides/connections-and-tokens/personal-access-tokens) for more on who can create tokens.

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

For unattended use, authenticate with a [personal access token](/guides/connections-and-tokens/personal-access-tokens) (PAT) by exporting it as `NOTION_API_TOKEN`:

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

| Variable | Purpose |
| :- | :- |
| `NOTION_API_TOKEN` | When this is set, it'll take precedence over `ntn login`'s keychain entry. Handy for scripts and CI. |
| `NOTION_WORKSPACE_ID` | Override the default workspace for a single command. |
| `NOTION_KEYRING` | Set to `0` to use file-based storage instead of the OS keychain. |
| `NOTION_HOME` | Override the config directory. |
| `NOTION_ENV` | Same as `--env`. Rarely needed. |

Run `ntn login --help` for the full list.

## Next steps

> [card] [Workers quickstart](/workers/get-started/quickstart)
>
> Create and deploy your first Notion Worker.

> [card] [API requests](/cli/guides/api-requests)
>
> Make Notion API requests from the terminal.

> [card] [Command reference](/cli/reference/commands)
>
> Full reference for every ntn command.

> [card] [Personal access tokens](/guides/connections-and-tokens/personal-access-tokens)
>
> Create tokens for scripts and CI.
