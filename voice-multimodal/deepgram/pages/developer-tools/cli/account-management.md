---
title: "Account Management Commands"
source: https://developers.deepgram.com/developer-tools/cli/account-management.md
path: developer-tools/cli/account-management
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Account Management Commands

## Projects

### List Projects

```shell
dg projects list
```

### Switch Project

```shell
dg projects use <project-id>
```

## API Keys

### List Keys

```shell
dg keys list
```

### Create Key

```shell
dg keys create "ci-runner"
dg keys create "production" --scope scopes.json
```

### Delete Key

```shell
dg keys delete <key-id>
```

Use `--dry-run` to preview:

```shell
dg keys delete <key-id> --dry-run
```

## Team Members

### List Members

```shell
dg members list
```

### Invite Member

```shell
dg members invite user@example.com --role admin
```

Available roles: `admin`, `member`, `viewer`

### Remove Member

```shell
dg members remove <member-id>
```

## Usage

### View Usage

```shell
dg usage
dg usage --start 2024-01-01 --end 2024-01-31
```

### Export Usage

```shell
dg usage -o json > usage.json
dg usage --format csv > usage.csv
```

## Billing

### View Balance

```shell
dg billing
```

## Direct API Access

Use `dg api` to call any Deepgram API endpoint:

```shell
dg api GET /v1/projects
dg api POST /v1/listen --data '{"url": "https://example.com/audio.mp3"}'
```

Authentication is handled automatically.
