---
title: "Provider Keys"
source: https://docs.fireworks.ai/nexus/provider-keys
path: nexus/provider-keys
---

Connect an Anthropic, OpenAI, or Amazon Bedrock Provider Key once so Nexus Auto can call closed models without developers sending the key.

* Only account admins can connect, replace, or remove a key.
* A connected key works in every coding harness, including Cursor IDE, the Copilot App, and Claude Desktop.
* Fireworks encrypts keys at rest and never shows them in full again.
* Every [Nexus plan](/nexus/plans) includes Provider Keys: Pro, Team, and Enterprise. A developer can also use their own key, saved with [`nexus auto`](/nexus/auto#nexus-cli) or sent as a request header.

- On accounts without Provider Keys, send the Anthropic or OpenAI key with each request. See [APIs and SDKs](/nexus/apis-and-sdks#credentials) or [LLM Gateways](/nexus/llm-gateways#provide-closed-model-credentials). In coding harnesses, a developer can save their own key with `nexus auto --anthropic-api-key` or `--openai-api-key`. See [which harnesses send a saved key](/nexus/auto#nexus-cli).
- A key a developer saves with `nexus auto` takes precedence over the Provider Key for that provider.
- `nexus login` stores only the developer's Fireworks credential. The provider key stays with the account, so admins never hand it to developers.
- IAM role ARNs are non-secret identifiers.
- The admin-only rule applies to the dashboard, the API, and `firectl`.

## Supported providers

| Provider | What you connect |
| - | - |
| Anthropic | API key |
| OpenAI | API key |
| Amazon Bedrock | [API key or IAM role](/nexus/provider-keys/bedrock), plus a region and model ID for each model |

| Provider | Dashboard | API and `firectl` |
| - | - | - |
| Anthropic | Yes | Yes |
| OpenAI | Yes | Yes |
| Amazon Bedrock | Yes | Yes |
| Grok | No | When enabled for the account |

* **One active key per provider:** an account can upload several keys for one provider, but only one is active for routing at a time.
* **Bedrock also needs routes:** a Bedrock key alone serves no traffic. Each model sent through AWS needs a Bedrock model ID and region.

## Connect a key

**1. Open Provider Keys**

Open [Provider Keys](https://nexus.fireworks.ai/settings/provider-keys) in Nexus settings.

**2. Connect a provider**

Click **Connect** next to Anthropic, OpenAI, or Amazon Bedrock, and paste your key. For Bedrock, follow [Amazon Bedrock Setup](/nexus/provider-keys/bedrock).

The provider shows **Connected**, and requests start using the key within a minute.

![Connecting a provider key from the Provider Keys page in Settings](https://mintcdn.com/fireworksai/nxZpB0vMV5GibTdM/images/fireworks-nexus/provider-keys/connect-a-key.gif?s=0203955982120c703d29dfde345f3006)

* For Anthropic or OpenAI, paste the key and click **Connect**. A confirmation appears once it's saved.
* For Amazon Bedrock, choose an IAM role or API key, then select models. After the card connects, fill in each model's Bedrock model ID and region, then click **Save**. Bedrock traffic starts only after the model routes are saved.
* Requests typically begin using the key 30 to 60 seconds after connecting.

Each provider is always in one of these states:

| State | What it means |
| - | - |
| **Connected** | The key is active for Nexus Auto requests to that provider |
| **Connecting** | A new binding is propagating |
| **Disconnecting** | A binding removal is propagating |
| **Not connected** | No key is set for this provider |

Developers can check the Anthropic and OpenAI states with `nexus auto`. It lists each Provider Key next to the keys saved on their machine:

| `nexus auto` shows | What it means |
| - | - |
| **Connected, covers every harness** | The Provider Key is active. A masked preview may follow **Connected** |
| **Connecting** or **Disconnecting** | A change is propagating |
| **Not connected** | No Provider Key is set for this provider |
| **Not enabled on this account** | Provider Keys isn't turned on for this account. Nexus accounts include it. For a Fireworks platform account, [contact us](https://fireworks.ai/contact) |
| **Sign in to see status** | Run `nexus login` first |
| **Key rejected: sign in again** | The stored Fireworks key was rejected. Run `nexus login` |
| **Couldn't check just now** | Nexus CLI couldn't read the status. Try again later |

## Replace or remove a key

Open the menu on a connected provider:

* **Replace** swaps in a new key. Bedrock routes stay in place.
* **Remove** disconnects the provider. For Bedrock, this also deletes its routes.

![Replacing the key value for a connected provider](https://mintcdn.com/fireworksai/nxZpB0vMV5GibTdM/images/fireworks-nexus/provider-keys/update-a-key.gif?s=e920c9a4d139210db5da7d201b54d170)

* Replace accepts a new API key or IAM role ARN for that provider.
* Changes typically propagate within 30 to 60 seconds. The provider may briefly show **Connecting** or **Disconnecting**.

## Manage keys with `firectl`

`firectl` is the older way to manage Provider Keys and remains supported for existing scripts. For new setups, use [Provider Keys](https://nexus.fireworks.ai/settings/provider-keys) in Nexus settings.

| Task | Command |
| - | - |
| Upload a key | `firectl provider-key upload --provider-type PROVIDER --from-file PATH` |
| Make it active | `firectl provider-key-binding bind PROVIDER KEY_ID` |
| Check status | `firectl provider-key-binding list` |
| Remove | `firectl provider-key-binding unbind PROVIDER`, then `firectl provider-key delete KEY_ID` |

If you haven't used `firectl` before, start with [Getting started](/tools-sdks/firectl/firectl).

`firectl provider-key` manages stored keys and `firectl provider-key-binding` chooses which key is active for routing. `firectl auto-provider-key` is an alias. `unbind` stops routing from using a key without deleting it, so it can be bound again without re-uploading.

| Action | Step | Command |
| - | - | - |
| **Connect or replace** | Upload a key | `firectl provider-key upload --provider-type PROVIDER --api-key $PROVIDER_KEY` / `--from-file PATH` |
| | Upload a Bedrock IAM role | `firectl provider-key upload --provider-type bedrock --aws-iam-role-arn ROLE_ARN` |
| | Use the key | `firectl provider-key-binding bind PROVIDER KEY_ID` |
| | Use a Bedrock key | `firectl provider-key-binding bind bedrock KEY_ID --routes-file=./routes.json` |
| **Check status** | Check stored keys | `firectl provider-key list` / `firectl provider-key list --provider-type PROVIDER` |
| | Check keys in routing | `firectl provider-key-binding list` or `firectl provider-key-binding get PROVIDER` |
| **Remove** | Stop using a key (but keep stored) | `firectl provider-key-binding unbind PROVIDER` |
| | Delete (unbind first) | `firectl provider-key delete KEY_ID` |

### Add or replace a key

`upload` stores a key but does not make it active for routing. Use `bind` to make it active. `--provider-type` is required and accepts `anthropic`, `openai`, `grok`, or `bedrock`.

For Anthropic or OpenAI, pass an environment variable to `--api-key`. This keeps the value out of shell history:

```bash wrap theme={null}
firectl provider-key upload --provider-type anthropic --api-key $ANTHROPIC_KEY
firectl provider-key-binding bind anthropic KEY_ID
```

Or point at a file with `--from-file`. The file holds only the raw key, with no JSON or quotes. `firectl` trims surrounding whitespace:

```bash wrap theme={null}
firectl provider-key upload --provider-type anthropic --from-file ./anthropic.key
```

On a shared or multi-user machine, prefer `--from-file`. The shell expands `$ANTHROPIC_KEY` before `firectl` starts, so `--api-key` keeps the key out of shell history but still exposes it in the process list (`ps`) while the command runs. `--from-file` passes only the path.

To rotate a provider, upload the new key and bind that key's ID. The old key stays stored until it is deleted.

For Amazon Bedrock, upload an API key with `--from-file` or an IAM role with `--aws-iam-role-arn`, then bind with `--routes-file`. Omitting `--routes-file` binds an empty route set, which serves no Bedrock traffic and replaces any existing routes. See [Amazon Bedrock Setup](/nexus/provider-keys/bedrock#manage-with-firectl).

### Check status

```bash wrap theme={null}
# Keys you have uploaded (vault). One provider can have several.
firectl provider-key list
firectl provider-key list --provider-type openai
firectl provider-key list -o json

# Which key is live for each provider (Connected / Connecting / Disconnecting / Not connected)
firectl provider-key-binding list
firectl provider-key-binding list --provider-type openai
firectl provider-key-binding get openai
```

`provider-key list` shows each stored key's ID, provider, credential type, preview, and display name. API key previews are masked; IAM role previews show the full non-secret role ARN. `provider-key-binding list` and `get` show each provider's connection state, credential type, and active `PROVIDER_KEY` resource name. For Bedrock, also confirm that `routes` lists every model to send through AWS.

### Delete a key

Use the key ID or full resource name from `upload` or `provider-key list`. If that key is live for the provider, unbind it first. The key stays stored until it is deleted.

```bash wrap theme={null}
# If this key is currently in use
firectl provider-key-binding unbind openai
firectl provider-key delete KEY_ID
```

## Key behavior and security

* **A key sent with a request wins.** If a request includes its own provider key, Nexus uses that key instead of the stored one.
* **Keys stay private.** The dashboard and API show only the provider, state, a masked preview, and dates for each key.

- Request-level credentials take precedence when the client supports sending them.
- After a key is connected, replaced, or removed, allow 30 to 60 seconds for the change to reach requests.
- The full API key is stored securely and never returned. An IAM role ARN is a non-secret identifier and is returned as the credential preview.
