---
title: "Deploy Coding Agents Across Your Company without handing out API keys"
source: https://openrouter.ai/docs/cookbook/coding-agents/deploy-coding-agents.md
path: docs/cookbook/coding-agents/deploy-coding-agents
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Coding Agents Across Your Company without handing out API keys

> Deploy Claude Code, Codex and other coding agents to managed machines with MDM, with OIDC sign-in instead of saved API keys

Beta

Coding agents like Claude Code and Codex usually run on an API key saved in a config file on each engineer's laptop. Those keys are what malicious npm and PyPI packages look for, and each one is another key IT has to hand out, track and rotate. In this guide, you'll learn how to set up your mobile device management (MDM) tool to roll out [Ori Harness](https://openrouter.ai/docs/guides/ori/harness.md) and one policy to every engineer's machine. Engineers will be able to sign in from their terminal and run their coding agents without a saved API key.

**Goal:** Keep long-lived OpenRouter API keys off your engineers' machines. Use your MDM to roll out Ori with a policy that only allows OpenID Connect (OIDC) sign-in, only accepts keys from your organization, and only launches the agents you approve.

**Outcome:** Engineers sign in to Ori from their terminal and run Claude Code, Codex and other agents without saving an OpenRouter API key. You test the policy on one machine before your MDM pushes it to everyone.

> [!TIP]
>
> Want to get started faster? Copy this prompt into a coding agent on the machine you want to test on. Claude Code, Codex, Ori Code or any agent that can run shell commands will work.

## Why deploy coding agents through Ori

With OIDC sign-in, engineers use their own OpenRouter account instead of an API key. Nobody has to create, share or rotate keys, and no key sits on a laptop working until someone remembers to revoke it. Ori keeps a sign-in session and gives each agent access tokens that expire after about 24 hours, so a leaked token stops working on its own.

IT also gets one tool to manage instead of one per agent. You deploy and configure Ori, and Ori sets up each agent it launches. Engineers can't loosen the policy from a shell, a project or a flag. Since requests made with Ori's credentials go through your OpenRouter organization, its model allowlists, provider settings and spend limits apply to all of them.

## Prerequisites

* **Your OpenRouter organization ID**, from the Org ID field in [Settings > Preferences](https://openrouter.ai/settings/preferences). To restrict Ori to one workspace, you also need its ID from the workspace's [Settings](https://openrouter.ai/workspaces/default/settings) page.
* **An MDM** that can write macOS managed preferences or push files to `/etc/ori` (Linux) and `C:\ProgramData\ori` (Windows)
* **Ori 0.16.0 or later** on every machine before the policy arrives
* **A Business or Enterprise plan**, only if you want to pin requests to a US or EU region

## 1. Install Ori

Deploy Ori before the policy, because older releases don't recognize some of these settings. To control which version runs, add `ORI_DISABLE_UPDATES` to the policy, or set `ORI_MINIMUM_VERSION` to block anything older than a given release.

## 2. Write the policy

This policy makes OIDC the only way to sign in, only accepts keys from your organization and workspace, and only allows Claude Code and Codex. Replace the two `YOUR_…` values. Leave out `ORI_REQUIRED_WORKSPACE_ID` to allow any workspace in the organization.

```json theme={null}
{
  "env": {
    "ORI_DISABLE_OAUTH_LOGIN": "1",
    "ORI_DISABLE_API_KEY_LOGIN": "1",
    "ORI_DISABLE_ENV_KEY_LOGIN": "1",
    "ORI_REQUIRE_LOGIN": "1",
    "ORI_REQUIRED_ORGANIZATION_ID": "YOUR_OPENROUTER_ORGANIZATION_ID",
    "ORI_REQUIRED_WORKSPACE_ID": "YOUR_OPENROUTER_WORKSPACE_UUID",
    "ORI_ENABLED_HARNESSES": "claude,codex"
  }
}
```

For macOS MDM, the same policy as `com.openrouter.ori.plist`:

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>ORI_DISABLE_OAUTH_LOGIN</key>
    <true/>
    <key>ORI_DISABLE_API_KEY_LOGIN</key>
    <true/>
    <key>ORI_DISABLE_ENV_KEY_LOGIN</key>
    <true/>
    <key>ORI_REQUIRE_LOGIN</key>
    <true/>
    <key>ORI_REQUIRED_ORGANIZATION_ID</key>
    <string>YOUR_OPENROUTER_ORGANIZATION_ID</string>
    <key>ORI_REQUIRED_WORKSPACE_ID</key>
    <string>YOUR_OPENROUTER_WORKSPACE_UUID</string>
    <key>ORI_ENABLED_HARNESSES</key>
    <string>claude,codex</string>
</dict>
</plist>
```

```bash theme={null}
plutil -lint com.openrouter.ori.plist
```

Never put an API key or any other credential in a policy.

| Setting | What it does |
| - | - |
| `ORI_DISABLE_OAUTH_LOGIN` | Turns off the older browser sign-in, which saves an API key. |
| `ORI_DISABLE_API_KEY_LOGIN` | Turns off pasting an API key into `ori login`. |
| `ORI_DISABLE_ENV_KEY_LOGIN` | Ignores an `OPENROUTER_API_KEY` in the environment. |
| `ORI_REQUIRE_LOGIN` | Refuses any credential `ori login` didn't create, such as an exported key or one in a project `.env` file. |
| `ORI_REQUIRED_ORGANIZATION_ID` | Refuses any key outside your organization, including personal keys. Ori checks with OpenRouter before it uses or saves a key. |
| `ORI_REQUIRED_WORKSPACE_ID` | Refuses any key outside one workspace. |
| `ORI_ENABLED_HARNESSES` | The agents engineers can launch. Every other launcher is hidden and refuses to start, including ones added in later releases. |

Optional:

| Setting | What it does |
| - | - |
| `ORI_REQUIRED_REGION` | `us` or `eu` sends every Ori request through that OpenRouter data region. Business and Enterprise plans only; other plans get a 403 on every request. |
| `ORI_CREDENTIAL_STORAGE` | `protected` keeps sign-ins in the macOS Keychain or the Linux Secret Service instead of files in the home directory. Hold off on macOS until Ori releases are signed. Until then, macOS asks for a Keychain password after every Ori update, and agent tools running under `ori claude` can fail. |
| `ORI_KEY_LIMIT`, `ORI_KEY_LIMIT_RESET` | Every key Ori uses must have a credit limit at or below this amount, in USD. Keys with no limit are refused. The reset setting sets how often the limit resets (`daily`, `weekly`, `monthly`). |
| `ORI_ENABLED_COMMANDS` | Limits which top-level `ori` commands run. |

## 3. Test it on one machine

Write the policy as a machine file, sign in, and check the result. If the machine already has a policy file, back it up first. Replace the IDs with your own, and delete the `ORI_REQUIRED_WORKSPACE_ID` line if you don't restrict Ori to one workspace. On macOS and Linux:

```bash theme={null}
sudo mkdir -p /etc/ori
sudo tee /etc/ori/config.json > /dev/null <<'JSON'
{
  "env": {
    "ORI_DISABLE_OAUTH_LOGIN": "1",
    "ORI_DISABLE_API_KEY_LOGIN": "1",
    "ORI_DISABLE_ENV_KEY_LOGIN": "1",
    "ORI_REQUIRE_LOGIN": "1",
    "ORI_REQUIRED_ORGANIZATION_ID": "YOUR_OPENROUTER_ORGANIZATION_ID",
    "ORI_REQUIRED_WORKSPACE_ID": "YOUR_OPENROUTER_WORKSPACE_UUID",
    "ORI_ENABLED_HARNESSES": "claude,codex"
  }
}
JSON
ori login --oidc
ori auth
ori doctor
```

On Windows, from an administrator PowerShell:

```powershell theme={null}
New-Item -ItemType Directory -Force -Path 'C:\ProgramData\ori' | Out-Null
$policy = @'
{
  "env": {
    "ORI_DISABLE_OAUTH_LOGIN": "1",
    "ORI_DISABLE_API_KEY_LOGIN": "1",
    "ORI_DISABLE_ENV_KEY_LOGIN": "1",
    "ORI_REQUIRE_LOGIN": "1",
    "ORI_REQUIRED_ORGANIZATION_ID": "YOUR_OPENROUTER_ORGANIZATION_ID",
    "ORI_REQUIRED_WORKSPACE_ID": "YOUR_OPENROUTER_WORKSPACE_UUID",
    "ORI_ENABLED_HARNESSES": "claude,codex"
  }
}
'@
[System.IO.File]::WriteAllText('C:\ProgramData\ori\config.json', $policy)
ori login --oidc
ori auth
ori doctor
```

`ori login --oidc` opens OpenRouter's approval page. If you're already signed in to OpenRouter, approving takes one click and you're back in the terminal. `ori auth` shows the account, the required organization and workspace and whether the key matches, and which administrator source set each value. For a script, `ori auth --json` reports `data.policyStatus` as `compliant` when the key meets the policy. `ori doctor` lists any setting Ori ignored because a user, project or shell set it.

## 4. Deliver the policy

* **macOS:** upload `com.openrouter.ori.plist` as a custom-settings payload for the `com.openrouter.ori` domain in Jamf, Kandji, Intune or any MDM that writes managed preferences. This source takes priority over everything else, with one exception: if a Mac already has a per-user `com.openrouter.ori` profile, that profile replaces this one for ordinary settings such as the sign-in switches and the allowed agents. Remove the per-user profile or add the same settings to it.
* **Linux:** push `/etc/ori/config.json` with your configuration management.
* **Windows:** push `C:\ProgramData\ori\config.json`.

If the policy is malformed, contradicts itself or can't be read, Ori won't use any key until it's fixed.

## 5. Have engineers sign in

Send engineers this prompt to paste into their coding agent:

```txt theme={null}
Switch my Ori sign-in to OpenRouter OIDC so no OpenRouter API key is saved on this machine. Use these as the source of truth:
- Rollout guide: https://openrouter.ai/docs/cookbook/coding-agents/deploy-coding-agents
- Ori configuration reference: https://openrouter.ai/docs/guides/ori/configuration

Never print, copy or paste a key or token.

1. Run ori --version. If it's older than 0.16.0, run ori update. If ori update says my organization manages the installation, stop and tell me to ask IT.
2. Run ori auth and tell me how I'm signed in now.
3. Run ori logout --all to remove my saved sign-ins, then run ori login --oidc. It opens an OpenRouter approval page. Tell me to approve it, and wait. If a browser can't open here, run ori login --oidc --no-browser and give me the link.
4. Run ori doctor. If it finds OPENROUTER_API_KEY set in a shell startup file, show me the file and line number, with the key value hidden, and after I confirm, run ori doctor --fix to remove it.
5. If I use Claude Code or Claude Desktop (macOS), run ori harness setup claude. On Windows, run ori claude instead. If I use Codex or Codex Desktop, run ori harness setup codex.
6. Run ori auth again and confirm I'm signed in with the OIDC session.

Check your work:
- ori auth shows an OIDC sign-in.
- No OPENROUTER_API_KEY is left in my shell startup files.
- My agent starts through Ori.
- Remind me to delete any OpenRouter API keys I no longer need at https://openrouter.ai/settings/keys. Removing them from this machine doesn't delete them.
```

Or they can run it by hand:

```bash theme={null}
ori logout --all
ori login --oidc
ori harness setup claude   # Claude Code, and Claude Desktop (macOS). On Windows, run ori claude instead.
ori harness setup codex    # Codex and Codex Desktop
```

## 6. Roll out in rings

1. Deploy Ori 0.16.0 or later to a pilot group, without the policy.
2. Add the policy for the pilot group. Have them sign in with OIDC, launch each allowed agent, and run `ori auth`.
3. Confirm their requests show up in your OpenRouter activity under the right workspace.
4. Expand to the rest of the company in stages.

To roll back, unassign the profile and delete any machine file left from the pilot. If you backed up an earlier policy file, restore it.

```bash theme={null}
sudo rm /etc/ori/config.json
```

## Check your work

* `ori auth --json` reports `data.policyStatus` as `compliant` on a pilot machine
* `ori login` without `--oidc` no longer offers a way to paste or save an API key
* An exported `OPENROUTER_API_KEY` is ignored
* A key from outside your organization is refused
* An agent that isn't in `ORI_ENABLED_HARNESSES` is hidden and refuses to start
* Pilot requests show up under the right workspace in OpenRouter

## What this doesn't cover

* Turning off a sign-in method doesn't delete keys it already saved. The organization requirement refuses keys from anyone else, and `ori logout --all` removes them from the machine, but they keep working at OpenRouter until someone deletes them at [openrouter.ai/settings/keys](https://openrouter.ai/settings/keys).
* The policy covers the credential Ori gives the agents it launches. An engineer who runs `claude` directly with their own Anthropic account isn't covered.
* Someone who steals an access token, or reads the session and its key from disk on today's unsigned releases, can use it for about 24 hours. Revoking the sign-in stops new tokens, not ones already issued.
* Engineers on personal machines can use the engineer prompt with the same organization and workspace, so OpenRouter's server-side settings still apply to them. The device policy doesn't.

## FAQ

### Can I deploy Claude Code and Codex to every engineer without giving them API keys?

Yes. Deploy Ori with your MDM and push a policy that turns off API-key sign-in. Engineers run `ori login --oidc` from their terminal, then `ori claude` or `ori codex`. Ori passes each agent a short-lived access token from their OpenRouter sign-in, so nobody saves an OpenRouter API key.

### Which MDMs does this work with?

Any MDM that can write macOS managed preferences for the `com.openrouter.ori` domain, or push a file to `/etc/ori/config.json` on Linux and `C:\ProgramData\ori\config.json` on Windows. That includes Jamf, Kandji and Intune.

### Does OIDC sign-in remove every credential from the laptop?

No. Ori still keeps an OIDC session on the machine. It limits what a stolen credential is worth, because access tokens expire after about 24 hours, unlike an API key that works until someone revokes it. Until Ori releases are signed, a malicious package that can read the home directory can still use that session until it expires.

### Do I need an Enterprise plan?

No. OIDC sign-in is in beta and available to every OpenRouter account. Only pinning requests to a US or EU region needs a Business or Enterprise plan.

### What happens to API keys engineers already saved?

Ori doesn't delete them. With the organization requirement, Ori refuses keys from outside your organization, and `ori logout --all` removes saved keys from the machine. Delete the old keys at [openrouter.ai/settings/keys](https://openrouter.ai/settings/keys) so they stop working.

## Next steps

* Read the [Ori overview](https://openrouter.ai/docs/guides/ori/harness.md)
* See every setting in [Ori configuration](https://openrouter.ai/docs/guides/ori/configuration.md)
* Set up [Claude Desktop with OpenRouter Sign-In](https://openrouter.ai/docs/cookbook/coding-agents/claude-desktop-oidc), a separate OIDC integration that doesn't use Ori (beta)

