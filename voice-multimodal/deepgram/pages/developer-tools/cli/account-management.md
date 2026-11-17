---
title: "Account management commands"
source: https://developers.deepgram.com/developer-tools/cli/account-management.md
path: developer-tools/cli/account-management
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Account management commands

> Deepgram CLI account management (Manage API): manage projects, API keys, team members, and usage with dg projects, dg keys, dg members, and dg usage.

Account commands take the action as a flag. Run `dg keys --help`, `dg projects --help`, or `dg members --help` for the full set.

## Projects

### Set a project first

Key, member, usage, billing, and request commands act on one project: run `dg projects --list`, then `dg projects --set-default <project-id>`, or export `DEEPGRAM_PROJECT_ID`. Without one they exit `1` with `Project ID is required for this command`. To target another project for one command, pass `-p` (`--project-id`) to `dg keys`, `dg members`, `dg usage`, `dg billing`, or `dg requests`.

```shell
# List the projects this key can reach, then set one as the default for later commands
dg projects --list
dg projects --set-default <project-id>
```

### List projects

```shell
dg projects --list
```

### Show, switch, and create projects

```shell
# Show one project's details
dg projects --show <project-id>
# Set the default project and confirm it
dg projects --set-default <project-id>
dg projects --current
# Create a project, optionally with a company name
dg projects --create "My New Project" --company "Example Inc"
```

## API keys

### List and show keys

```shell
# List every key in the project
dg keys --list
# List only active keys (or expired)
dg keys --list --status active
# Show one key's details
dg keys --show <key-id>
```

### Create Key

```shell
dg keys --create --comment "ci-runner"
dg keys --create --comment "production" --scopes member --tags prod
```

`--scopes` takes comma-separated scope names and defaults to `member`. See [Working with roles & API scopes](/guides/deep-dives/working-with-roles) for what each scope grants. Add `--dry-run` to preview a create without making the key.

`--ttl` sets the new key's time to live in seconds; `--expiration-date` takes an ISO date. A time-limited key suits a CI job:

```shell
# Create a key that expires in one hour and print only the secret
dg -o json keys --create --comment "CI" --ttl 3600 | jq -r '.created_key.key'
```

### Delete key

```shell
dg keys --delete <key-id> --yes
```

Without `--yes`, a non-interactive session (CI, an agent, a pipe) exits `1` with `Refusing to delete key ... without confirmation. Pass --yes to confirm.`; on a terminal, the CLI asks first.

Use `--dry-run` to preview:

```shell
dg keys --delete <key-id> --dry-run
```

## Team Members

### List members

```shell
dg members --list
# Pending invites
dg members --invites
```

If `dg members --list` fails with `validation errors for MemberInfo`, list members through the API: `dg api /v1/projects/<project-id>/members`.

### Invite Member

```shell
dg members --invite user@example.com --scope admin
```

`--scope` takes a role, for example `member` (the default) or `admin`. Available scopes: `owner`, `admin`, `member`. See [Working with roles & API scopes](/guides/deep-dives/working-with-roles). Add `--dry-run` to preview an invite without sending it.

### Remove Member

```shell
dg members --remove <member-id> --yes
dg members --revoke-invite user@example.com --yes
```

## Usage

### View usage

`dg usage` with no dates covers the current month. Replace each `YYYY-MM-DD` with a start and end date to choose a range; `-s` (`--start-date`) and `-e` (`--end-date`) also take ISO datetimes.

```shell
# Current month
dg usage
# A chosen range
dg usage --start-date YYYY-MM-DD --end-date YYYY-MM-DD
# Preset ranges
dg usage --current-month
dg usage --last-week
dg usage --last-month
# Totals only
dg usage --summary
```

### Export usage

```shell
dg -o json usage > usage.json
```

The JSON holds the per-period `buckets` alongside the totals.

## Billing

### View balance

```shell
dg billing
dg billing --balances
```

### Billing breakdown

```shell
# Break down a date range by line item
dg billing --breakdown --start YYYY-MM-DD --end YYYY-MM-DD --grouping line_item
```

`--grouping` takes `accessor`, `deployment`, `line_item`, or `tags`.

## Request history

`dg requests` lists the project's API requests, 10 per page by default. You can obtain up to 90 days of request logs; see [Logs & Usage Data](/docs/using-logs-usage).

```shell
# Failed transcription requests
dg requests --status failed --endpoint listen
# One request's details
dg requests --show <request-id>
# The last 24 hours, 50 at a time
dg requests --last-day --limit 50
```

| Option                       | Values                               |
| ---------------------------- | ------------------------------------ |
| `--status`                   | `succeeded`, `failed`                |
| `--endpoint`                 | `listen`, `read`, `speak`, `agent`   |
| `--method`                   | `sync`, `async`, `streaming`         |
| `--limit`                    | Results per page (default `10`)      |
| `--page`                     | Page number                          |
| `--start-date`, `--end-date` | `YYYY-MM-DD`                         |
| `--last-day`, `--last-week`  | The last 24 hours or the last 7 days |
| `--show`                     | One request's details by ID          |

## Models

`dg models` lists the models your key can use, with each model's canonical name, ID, languages, and architecture, and flags deprecated models.

```shell
# Speech-to-text models
dg models --type stt
# Text-to-speech models
dg models --type tts
# Include outdated model versions
dg models --include-outdated
```

`-t` is the short form of `--type`, which takes `stt` or `tts`. `dg models --type tts` and `dg speak --list-voices` list the Aura-2 voices. For Flux TTS voices, see [Flux TTS Voices & Languages](/docs/flux-tts/voices).

## Direct API Access

`dg api` calls any Deepgram API endpoint with your stored credentials. The endpoint is positional; `-X` sets the method and `-f` sets body fields:

```shell
dg api /v1/projects
dg api -X POST /v1/listen -f url=https://example.com/audio.mp3
```

* `--jq EXPR` applies a jq filter to the response and needs `jq` on your PATH, for example `dg api /v1/projects --jq '.projects[0].name'`.
* `--raw` prints the response without formatting.
* `-H` (`--header`) adds a header as `'Key: Value'`.
* `--input FILE` reads the request body from a file, or from stdin with `--input -`.
* `-f key=value` sends a string field, and `-f key:=json` sends raw JSON, for example `-f scopes:='["member"]'`.

`-o` works before the subcommand (`dg -o json usage`) or after it on most commands (`dg usage -o json`). On `dg speak`, `-o`/`--output` after the subcommand still sets the output file path but is deprecated; use `--out-file` instead. On `dg plugin` and `dg skills` subcommands, put `-o` before the subcommand.
