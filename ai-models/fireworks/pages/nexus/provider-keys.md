---
title: "Provider Keys"
source: https://docs.fireworks.ai/nexus/provider-keys
path: nexus/provider-keys
---

Connect an account-level Anthropic, OpenAI, or Amazon Bedrock Provider Key once, where available, so model routers can call closed families without developers sending the key.

Connect an Anthropic, OpenAI, or [Amazon Bedrock](/nexus/provider-keys/bedrock) key once to let [FireRouter](/nexus/firerouter) call closed models. After that, developers and gateways authenticate with only their Fireworks API key. When FireRouter selects a closed model, Fireworks sends the request with the stored provider credential.

<Note>
  Provider Keys is not yet available on every account. If **Provider Keys**
  does not appear in [Settings](https://app.fireworks.ai/settings/provider-keys),
  [contact the Fireworks team](https://fireworks.ai/demo-request) to enable it.
  Self-serve setup is coming soon. Until then, send a per-request Anthropic or
  OpenAI header from [APIs and SDKs](/nexus/apis-and-sdks#credentials) or
  [LLM Gateways](/nexus/llm-gateways#provide-closed-model-credentials). For
  coding harnesses, review local support in
  [Harness Compatibility](/nexus/harness-compatibility).
</Note>

FireConnect configures the developer's Fireworks credential through `fireconnect login`. The provider key stays with the account, so it is never distributed to developers or pasted into a chat. Fireworks encrypts it at rest and never shows it in full again.

<Tip>
  **Admin:** connect the provider key once. **Developer:** run
  `fireconnect login`. **Request:** send only the Fireworks API key.
</Tip>

<Note>
  Router availability in FireConnect varies by harness. See
  <a href="/nexus/harness-compatibility">Harness Compatibility</a> for current support.
</Note>

<Note>
  Provider Keys is an account-admin-only feature. You must be an account admin
  to connect, replace, or remove a key, whether from the dashboard or through
  `firectl`.
</Note>

## Check provider support and connection states

* **Providers:** The dashboard supports Anthropic, OpenAI, and Amazon Bedrock. The API and `firectl` support those providers, plus Grok when enabled for your account.
* **One active key per provider:** You can upload several keys for one provider, but only one can be active for routing at a time.
* **Bedrock also needs routes:** a Bedrock key is not enough. Each model you want to send through your AWS account needs a Bedrock model ID and region. See <a href="/nexus/provider-keys/bedrock">Amazon Bedrock</a>.

Each provider is always in one of these states:

| State             | What it means                                          |
| ----------------- | ------------------------------------------------------ |
| **Connected**     | The key is active for router requests to that provider |
| **Connecting**    | A new binding is propagating                           |
| **Disconnecting** | A binding removal is propagating                       |
| **Not connected** | No key is set for this provider.                       |

## Connect a key in the dashboard

Connect a Provider Key from **Settings** without using a terminal. You can open [Provider Keys](https://app.fireworks.ai/settings/provider-keys) directly.

<Steps>
  <Step title="Open Provider Keys">
    Open **Settings** and go to **Provider Keys**, or open the [Provider Keys page](https://app.fireworks.ai/settings/provider-keys) directly.
  </Step>

  <Step title="Connect a provider">
    Find the provider you want (Anthropic, OpenAI, or Amazon Bedrock) and click **Connect**.
  </Step>

  <Step title="Paste your key">
    For Anthropic or OpenAI, paste your key and click **Connect**. You will see a confirmation once it is saved.

    For Amazon Bedrock, paste the key and select models. After the card connects, fill in each model's Bedrock model ID and region, then click **Save**. Full steps are in <a href="/nexus/provider-keys/bedrock">Amazon Bedrock</a>.
  </Step>
</Steps>

The provider then shows **Connected**. Requests typically begin using the key within 30–60 seconds of connecting it. Bedrock traffic starts only after the model routes are saved.

<Frame>
  <img alt="Connecting a provider key from the Provider Keys page in Settings" />
</Frame>

## Replace or remove a key

Open the menu on any connected provider to:

* **Replace:** swap in a new key value for that provider. Bedrock routes stay in place when you update only the key.

<Frame>
  <img alt="Replacing the key value for a connected provider" />
</Frame>

* **Remove:** remove the key. For Bedrock, this also deletes every Bedrock route.

<Frame>
  <img alt="Removing a connected provider key" />
</Frame>

Changes typically propagate within 30–60 seconds. The provider may briefly show **Connecting** or **Disconnecting**.

## Manage keys with `firectl`

You can also connect, replace, remove, and inspect Provider Keys with `firectl`. Use `firectl provider-key` to manage stored keys and `firectl provider-key-binding` to choose which key is active for routing. `firectl firerouter-provider-key` is an alias.

The CLI can also stop using a key for routing without deleting it (`provider-key-binding unbind`). The key remains stored, so you can bind it again without re-uploading it.

<Tip>
  First time using `firectl`? Follow <a href="/tools-sdks/firectl/firectl">Getting started</a> to install it.
</Tip>

| Action                 | Step                               | Command                                                                                             |
| ---------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Connect or replace** | Upload a key                       | `firectl provider-key upload --provider-type PROVIDER --api-key $PROVIDER_KEY` / `--from-file PATH` |
|                        | Use the key                        | `firectl provider-key-binding bind PROVIDER KEY_ID`                                                 |
|                        | Use a Bedrock key                  | `firectl provider-key-binding bind bedrock KEY_ID --routes-file=./routes.json`                      |
| **Check status**       | Check stored keys                  | `firectl provider-key list` / `firectl provider-key list --provider-type PROVIDER`                  |
|                        | Check keys in routing              | `firectl provider-key-binding list` or `firectl provider-key-binding get PROVIDER`                  |
| **Remove**             | Stop using a key (but keep stored) | `firectl provider-key-binding unbind PROVIDER`                                                      |
|                        | Delete (needs to stop first)       | `firectl provider-key delete KEY_ID`                                                                |

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

<Note>
  On a shared or multi-user machine, prefer `--from-file`. The shell expands
  `$ANTHROPIC_KEY` before `firectl` starts, so `--api-key` keeps the key out of
  your shell history but still exposes it in the process list (`ps`) while the
  command runs. `--from-file` passes only the path.
</Note>

To rotate a provider, upload the new key and bind that key's ID. The old key stays stored until you delete it.

For Amazon Bedrock, upload with `--from-file` and bind with `--routes-file`. Omitting `--routes-file` binds an empty route set, which serves no Bedrock traffic and replaces any existing routes. See <a href="/nexus/provider-keys/bedrock#manage-with-firectl">Amazon Bedrock</a>.

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

`provider-key list` shows each stored key's ID, provider, masked preview, and display name. `provider-key-binding list` and `get` show each provider's connection state and active `key_id`. For Bedrock, also confirm that `routes` lists every model you intend to send through AWS.

### Delete a key

Use the `key_id` from `upload` or `provider-key list`. If that key is live for the provider, unbind it first. Unbind stops routing from using it; the key stays stored until you delete it.

```bash wrap theme={null}
# If this key is currently in use
firectl provider-key-binding unbind openai
firectl provider-key delete KEY_ID
```

## Key behavior and security

* **Request-level credentials take precedence when supported.** If a request includes a provider key, that key is used and the stored one is skipped.
* **Changes are not instant.** After you connect, replace, or remove a key, allow 30–60 seconds for the change to reach requests.
* **Your key stays private.** The full key is stored securely and never returned. The dashboard and API only show the provider, state, masked preview, and dates.
