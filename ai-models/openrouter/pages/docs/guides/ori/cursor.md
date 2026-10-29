---
title: "Ori Cursor"
source: https://openrouter.ai/docs/guides/ori/cursor.md
path: docs/guides/ori/cursor
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Ori Cursor

> Point the Cursor desktop app at OpenRouter with one setup command, and go back with one reset

Ori Cursor points the Cursor desktop app (IDE) at OpenRouter. It is part of [Ori Harness](https://openrouter.ai/docs/guides/ori/harness.md). Setup changes Cursor's OpenAI API key setting to use OpenRouter and adds your organization's models to Cursor's model picker. It's available in Ori 0.16.0 and later.

## Set up Cursor

1. Save an OpenRouter API key with `ori login` or `ori login --with-key`. Setup doesn't accept an OpenRouter OIDC sign-in. See [Saved API key only](#saved-api-key-only).
2. On Linux and Windows, close Cursor. On macOS, setup quits Cursor and opens it again for you.
3. Run setup:

```sh theme={null}
ori harness setup cursor
```

Setup prints a warning that Cursor sends your key and every request through its own servers before they reach OpenRouter.

## Go back to your own Cursor setup

Run reset to remove the OpenRouter key and models and put back your previous Cursor settings. On Linux and Windows, close Cursor first.

```sh theme={null}
ori harness reset cursor
```

## Limits

Cursor has no way to ask Ori for a fresh credential, so Ori writes one static key into Cursor's settings. The first three limits come from that, and they apply only to Cursor. Codex, Claude, Droid, and Pi get their credential from Ori on each request.

### Saved API key only

Cursor stores one static key. If you signed in with OpenRouter OIDC (`ori login --oidc`), setup stops with `ORI_CLI_HARNESS_CREDENTIAL_UNSUPPORTED`, because an OIDC access token expires.

### Requests go through Cursor

Cursor sends your key and every request through its own servers before they reach OpenRouter.

### Logout doesn't remove the key

`ori logout` leaves the key in Cursor. Run `ori harness reset cursor` to remove it.

### Fixed model list

Setup writes your organization's model list once. If your organization changes which models it allows, run `ori harness setup cursor` again. Factory Droid setup has the same limit.

## Not available yet

* **Cursor CLI:** Setup doesn't cover the Cursor CLI (`cursor-agent`).
* **Launching from Ori:** There is no `ori cursor` command. Open Cursor as usual after setup.
* **Automatic restart on Linux and Windows:** Setup and reset stop with `ORI_CLI_HARNESS_ALREADY_RUNNING` while Cursor is running. Close Cursor and run the command again.

