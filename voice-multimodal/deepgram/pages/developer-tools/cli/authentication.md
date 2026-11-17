---
title: "Authentication"
source: https://developers.deepgram.com/developer-tools/cli/authentication.md
path: developer-tools/cli/authentication
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Authentication

## Interactive login

```shell
dg login
```

`dg login` opens a Deepgram sign-in page and shows a one-time code to confirm. It stores a time-limited Deepgram credential in your operating system keyring, or in the deepctl config file when no keyring is available.

The keyring entry is service `com.deepgram.dx.deepctl`, account `api-key.<profile>`, which helps when you troubleshoot a headless Linux machine.

After a successful login, `dg login` offers to install the Deepgram skills; see [Skills](/developer-tools/cli/skills).

### Finish login from an agent session

`dg login --complete` finishes a browser device-flow login you started elsewhere: approve the sign-in in your browser, then run `dg login --complete` from an AI-agent session or script to pick up the resulting credential. This is a separate path from `dg login --api-key` below, with its own checks before it stores a key.

### Credential expiry

* When the credential expires and no `--api-key` or `DEEPGRAM_API_KEY` supplies another key, commands stop with ``Your Deepgram credential has expired. Run `dg login` again.``; run `dg login` to get a new credential.
* When `DEEPGRAM_API_KEY` is set, the CLI skips an expired browser credential and uses the environment key without the message.
* `dg whoami` prints an `Expires:` line, and `dg -o json whoami` reports `credential_expires_at`.
* Upgrading from a CLI release before 0.4.0 needs one `dg login` for browser-login sessions.
* For CI, use `DEEPGRAM_API_KEY`. Keys stored with `dg login --api-key` and keys in `DEEPGRAM_API_KEY` carry no CLI-side expiry; such a key lasts until it is deleted or reaches its own expiration date.

## Store a key without the browser

On a machine with no browser, set `DEEPGRAM_API_KEY` as the next section shows; every command reads it, so nothing needs storing. To store a key with a profile instead, pass it to `dg login`:

```shell
dg login --api-key YOUR_API_KEY --project-id YOUR_PROJECT_ID
```

A key typed on the command line stays in your shell history and is visible in process listings while the command runs.

A real key is accepted outright; `-f` (`--force-write`) is no longer needed just to get past a key-format check. The CLI checks the project ID against the key:

* If the API reports the project ID as not found, `dg login` prints `Warning: Project ID '<id>' not found. API key will still be stored.`, stores the key without the project ID, and exits `0`. Its summary still shows the ID you passed; run `dg whoami` to see the stored project ID.
* If the key is invalid (`401`) or cannot access the project (`403`), the login fails with exit code `1` and stores nothing.

If `DEEPGRAM_API_KEY` is already set in your shell, `dg login --api-key` stops instead of silently saving a profile that would be used ahead of it: it prints `ERROR: DEEPGRAM_API_KEY is set, and logging in saves a profile that dg will use instead of it.`, exits `1` with `confirmation_required`, and stores nothing unless you add `--yes`.

On `dg login`, `-p` is `--project-id` and `-k` is `--api-key`; on the root `dg`, `-p` is `--profile`.

## Environment variable

For scripts and CI/CD, set your API key as an environment variable:

```shell
export DEEPGRAM_API_KEY=YOUR_API_KEY
dg listen audio.mp3
```

## API key flag

The global `--api-key` flag supplies a key for one command and overrides every other credential:

```shell
dg --api-key YOUR_API_KEY listen audio.mp3
```

The flag leaves the key in your shell history and in process listings while the command runs. For a key you keep, use `dg login` or `DEEPGRAM_API_KEY`.

When more than one credential is present, the CLI picks one by a fixed order; [Configuration & Environment](/developer-tools/cli/configuration) lists it. `dg whoami` shows which credential the CLI is using and where it came from.

## Named profiles

Use multiple API keys with named profiles:

```shell
# Store a credential under each profile name
dg login --profile production
dg login --profile development

# Use a specific profile for one command (-p is the short form)
dg --profile production listen audio.mp3
dg -p production listen audio.mp3
```

Each profile holds its own keyring credential (when available) and configuration values. `dg login --profile development` also makes `development` the active profile, so later commands use it until you switch.

```shell
# List every profile
dg profiles --list
# Show the active profile
dg profiles --current
# Make another profile active
dg profiles --switch production
```

On a machine with no system keyring, `dg profiles --switch` stops with `Error accessing credentials:`; pass `--profile <name>` on each command instead.

`dg profiles --list` shows each profile that has a stored key by its last 4 characters (the same masking as `dg whoami`'s `api_key_masked`), never the raw value.

## Log out

```shell
# Clear the active profile's credentials
dg logout
# Clear one profile's credentials
dg logout --profile development
# Clear every profile's credentials
dg logout --all
# Clear credentials but keep each profile's project ID and base URL
dg logout --all --keep-config
```

Run `dg logout --help` for each flag's exact behaviour.

## Check Auth Status

```shell
dg whoami
dg whoami --profile production
```

`dg whoami` reports the active profile (or the one `--profile` names), a masked API key, its credential source, and the configured project ID. The credential source is one of `system keyring`, `config file`, `DEEPGRAM_API_KEY (env)`, or `not set`. `dg -o json whoami` returns the fields `authenticated`, `profile`, `api_key_masked`, `key_source`, `project_id`, `base_url`, and `credential_expires_at`.

## CI/CD usage

Set `DEEPGRAM_API_KEY` from your CI secret store:

```yaml
# Example GitHub Actions
- name: Transcribe audio
  env:
    DEEPGRAM_API_KEY: ${{ secrets.DEEPGRAM_API_KEY }}
    DEEPCTL_TELEMETRY_DISABLED: "1" # turn off telemetry
  run: dg -o json listen audio.mp3 > transcript.json
```
