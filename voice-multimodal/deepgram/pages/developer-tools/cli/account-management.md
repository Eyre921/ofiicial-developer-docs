---
title: "Account Management Commands"
source: https://developers.deepgram.com/developer-tools/cli/account-management.md
path: developer-tools/cli/account-management
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Account Management Commands

Account commands are flag-based: the action is a flag, not a subcommand. Run `dg keys --help`, `dg projects --help`, or `dg members --help` for the full set.

## Projects

### List Projects

```shell
dg projects --list
```

### Switch Project

```shell
dg projects --set-default <project-id>
dg projects --current
```

## API Keys

### List Keys

```shell
dg keys --list
```

### Create Key

```shell
dg keys --create --comment "ci-runner"
dg keys --create --comment "production" --scopes member --tags prod
```

`--scopes` takes comma-separated scope names and defaults to `member`. See [Working With Roles & API Scopes](/guides/deep-dives/working-with-roles) for what each scope grants.

### Delete Key

```shell
dg keys --delete <key-id>
```

Use `--dry-run` to preview:

```shell
dg keys --delete <key-id> --dry-run
```

## Team Members

### List Members

```shell
dg members --list
dg members --invites   # Pending invites
```

### Invite Member

```shell
dg members --invite user@example.com --scope admin
```

Available scopes: `owner`, `admin`, `member`. See [Working With Roles & API Scopes](/guides/deep-dives/working-with-roles).

### Remove Member

```shell
dg members --remove <member-id>
dg members --revoke-invite user@example.com
```

## Usage

### View Usage

```shell
dg usage
dg usage --start-date 2024-01-01 --end-date 2024-01-31
dg usage --current-month
```

### Export Usage

`-o` belongs to `dg` itself, so it goes before the subcommand name:

```shell
dg -o json usage > usage.json
dg -o csv usage > usage.csv
```

## Billing

### View Balance

```shell
dg billing
dg billing --balances
```

## Direct API Access

Use `dg api` to call any Deepgram API endpoint. The endpoint is positional; set the method with `-X` and body fields with `-f`:

```shell
dg api /v1/projects
dg api -X POST /v1/listen -f url=https://example.com/audio.mp3
```

Authentication is handled automatically.
