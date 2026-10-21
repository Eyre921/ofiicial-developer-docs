---
title: "Provider Keys"
source: https://docs.fireworks.ai/nexus/provider-keys
path: nexus/provider-keys
---

Connect an Anthropic, OpenAI, or Amazon Bedrock Provider Key once so Nexus Auto can call closed models without developers sending the key.

Connect an Anthropic, OpenAI, or [Amazon Bedrock](/nexus/provider-keys/bedrock) key once to let [Nexus Auto](/nexus/auto) call closed models. After that, developers and gateways authenticate with only their Fireworks API key. When Nexus Auto selects a closed model, Fireworks sends the request with the stored provider credential.

> [!NOTE]
>
> Provider Keys is not yet available on every account. If **Provider Keys**
> does not appear in [Settings](https://app.fireworks.ai/settings/provider-keys),
> [contact the Fireworks team](https://fireworks.ai/demo-request) to enable it.
> Self-serve setup is coming soon.

Until then, send a per-request Anthropic or
OpenAI header from [APIs and SDKs](/nexus/apis-and-sdks#credentials) or
[LLM Gateways](/nexus/llm-gateways#provide-closed-model-credentials). For
coding harnesses, review local support in
[Which harnesses can send provider keys](/nexus/auto#nexus-cli).

Nexus CLI configures the developer's Fireworks credential through `nexus login`. The provider key stays with the account, so it is never distributed to developers or pasted into a chat. Fireworks encrypts API keys at rest and never shows them in full again. IAM role ARNs are non-secret identifiers.

> [!TIP]
>
> **Admin:** connect the provider key once. **Developer:** run
> `nexus login`. **Request:** send only the Fireworks API key.

> [!NOTE]
>
> Nexus Auto support varies by harness. See
> [Which harnesses can send provider keys](/nexus/auto#nexus-cli) for current support.

> [!NOTE]
>
> Provider Keys is an account-admin-only feature. You must be an account admin
> to connect, replace, or remove a key, whether from the dashboard or through
> `firectl`.

## Check provider support and connection states

Provider Keys supports these providers:

| Provider | Dashboard | API and `firectl` | What you connect |
| - | - | - | - |
| Anthropic | Yes | Yes | API key |
| OpenAI | Yes | Yes | API key |
| Amazon Bedrock | Yes | Yes | API key or IAM role |
| Grok | No | When enabled for your account | API key |

* **One active key per provider:** You can upload several keys for one provider, but only one can be active for routing at a time.
* **Bedrock also needs routes:** a Bedrock key is not enough. Each model you want to send through your AWS account needs a Bedrock model ID and region. See [Amazon Bedrock Setup](/nexus/provider-keys/bedrock).

Each provider is always in one of these states:

| State | What it means |
| - | - |
| **Connected** | The key is active for Nexus Auto requests to that provider |
| **Connecting** | A new binding is propagating |
| **Disconnecting** | A binding removal is propagating |
| **Not connected** | No key is set for this provider. |

## Connect a key in the dashboard

Connect a Provider Key from **Settings** without using a terminal. You can open [Provider Keys](https://app.fireworks.ai/settings/provider-keys) directly.

**1. Open Provider Keys**

Open **Settings** and go to **Provider Keys**, or open the [Provider Keys page](https://app.fireworks.ai/settings/provider-keys) directly.

**2. Connect a provider**

Find the provider you want (Anthropic, OpenAI, or Amazon Bedrock) and click **Connect**.

**3. Paste your key**

For Anthropic or OpenAI, paste your key and click **Connect**. You will see a confirmation once it is saved.

For Amazon Bedrock, choose an IAM role or API key, then select models. After the card connects, fill in each model's Bedrock model ID and region, then click **Save**. Full steps are in [Amazon Bedrock Setup](/nexus/provider-keys/bedrock).

The provider then shows **Connected**. Requests typically begin using the key within 30–60 seconds of connecting it. Bedrock traffic starts only after the model routes are saved.

![Connecting a provider key from the Provider Keys page in Settings](https://mintcdn.com/fireworksai/nxZpB0vMV5GibTdM/images/fireworks-nexus/provider-keys/connect-a-key.gif?s=0203955982120c703d29dfde345f3006)

## Replace or remove a key

Open the menu on any connected provider to:

* **Replace:** swap in a new API key or IAM role ARN for that provider. Bedrock routes stay in place when you update only that value.

![Replacing the key value for a connected provider](https://mintcdn.com/fireworksai/nxZpB0vMV5GibTdM/images/fireworks-nexus/provider-keys/update-a-key.gif?s=e920c9a4d139210db5da7d201b54d170)

* **Remove:** remove the key. For Bedrock, this also deletes every Bedrock route.

![Removing a connected provider key](https://mintcdn.com/fireworksai/nxZpB0vMV5GibTdM/images/fireworks-nexus/provider-keys/remove-a-key.gif?s=4e160de51c5d7645e5bf09ff9c4aedfb)

Changes typically propagate within 30–60 seconds. The provider may briefly show **Connecting** or **Disconnecting**.

## Manage keys with `firectl`

You can also connect, replace, remove, and inspect Provider Keys with `firectl`. Use `firectl provider-key` to manage stored keys and `firectl provider-key-binding` to choose which key is active for routing. `firectl auto-provider-key` is an alias.

The CLI can also stop using a key for routing without deleting it (`provider-key-binding unbind`). The key remains stored, so you can bind it again without re-uploading it.

> [!TIP]
>
> First time using `firectl`? Follow [Getting started](/tools-sdks/firectl/firectl) to install it.

| Action | Step | Command |
| - | - | - |
| **Connect or replace** | Upload a key | `firectl provider-key upload --provider-type PROVIDER --api-key $PROVIDER_KEY` / `--from-file PATH` |
| | Upload a Bedrock IAM role | `firectl provider-key upload --provider-type bedrock --aws-iam-role-arn ROLE_ARN` |
| | Use the key | `firectl provider-key-binding bind PROVIDER KEY_ID` |
| | Use a Bedrock key | `firectl provider-key-binding bind bedrock KEY_ID --routes-file=./routes.json` |
| **Check status** | Check stored keys | `firectl provider-key list` / `firectl provider-key list --provider-type PROVIDER` |
| | Check keys in routing | `firectl provider-key-binding list` or `firectl provider-key-binding get PROVIDER` |
| **Remove** | Stop using a key (but keep stored) | `firectl provider-key-binding unbind PROVIDER` |
| | Delete (needs to stop first) | `firectl provider-key delete KEY_ID` |

### Add or replace a key

`upload` stores a key but does not make it active for routing. Use `bind` to make it active. `--provider-type` is required and accepts `anthropic`, `openai`, `grok`, or `bedrock`.

For the quickest Anthropic or OpenAI setup, pass an environment variable to `--api-key`. This keeps the value out of your shell history:

```bash wrap theme={null}
firectl provider-key upload --provider-type anthropic --api-key $ANTHROPIC_KEY
firectl provider-key-binding bind anthropic KEY_ID
```

You can also point at a file with `--from-file`. The file should hold only the raw key, with no JSON or quotes. `firectl` trims surrounding whitespace:

```bash wrap theme={null}
firectl provider-key upload --provider-type anthropic --from-file ./anthropic.key
```

> [!NOTE]
>
> On a shared or multi-user machine, prefer `--from-file`. The shell expands
> `$ANTHROPIC_KEY` before `firectl` starts, so `--api-key` keeps the key out of
> your shell history but still exposes it in the process list (`ps`) while the
> command runs. `--from-file` passes only the path.

To rotate a provider, upload the new key and bind that key's ID. The old key stays stored until you delete it.

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

`provider-key list` shows each stored key's ID, provider, credential type, preview, and display name. API key previews are masked; IAM role previews show the full non-secret role ARN. `provider-key-binding list` and `get` show each provider's connection state, credential type, and active `PROVIDER_KEY` resource name. For Bedrock, also confirm that `routes` lists every model you intend to send through AWS.

### Delete a key

Use the key ID or full resource name from `upload` or `provider-key list`. If that key is live for the provider, unbind it first. Unbind stops routing from using it; the key stays stored until you delete it.

```bash wrap theme={null}
# If this key is currently in use
firectl provider-key-binding unbind openai
firectl provider-key delete KEY_ID
```

## Key behavior and security

* **Request-level credentials take precedence when supported.** If a request includes a provider key, that key is used and the stored one is skipped.
* **Changes are not instant.** After you connect, replace, or remove a key, allow 30–60 seconds for the change to reach requests.
* **Your API key stays private.** The full API key is stored securely and never returned. For API keys, the dashboard and API only show the provider, state, masked preview, and dates. An IAM role ARN is a non-secret identifier and is returned as the credential preview.
