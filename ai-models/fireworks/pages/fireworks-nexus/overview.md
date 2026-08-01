---
title: "Overview"
source: https://docs.fireworks.ai/fireworks-nexus/overview
path: fireworks-nexus/overview
---

Fireworks Nexus — connect agent harnesses to open models, route intelligently, and control spend per seat

[Fireworks Nexus](https://fireworks.ai/nexus) is the open-weight intelligence layer for agentic coding. It connects the harnesses your teams already use to Fireworks inference, routes each request to the right model, and gives admins per-seat cost controls — without replacing your workflows.

You can adopt Nexus as a full platform or use its parts independently. Many teams start with [FireConnect](/ecosystem/fireconnect/overview) or [FireRouter](/ecosystem/firerouter/overview) on a standard Fireworks API key before rolling out seat-level controls.

## How Nexus fits together

| Component                  | What it does                                                                                                                        | Docs                                                    |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **FireConnect**            | One-command CLI that routes Claude Code, OpenCode, Codex, Pi, Cursor, VS Code, and Deep Agents through Fireworks                    | [FireConnect overview](/ecosystem/fireconnect/overview) |
| **FireRouter**             | Managed router that sends simple work to open models and passes hard requests to closed-source models (for example Claude Opus 4.8) | [FireRouter overview](/ecosystem/firerouter/overview)   |
| **Per-user usage limits**  | Account-wide and per-user spending caps on serverless inference                                                                     | [Usage limits](/fireworks-nexus/usage-limits)           |
| **[Fire Pass](/firepass)** | Separate invite-only promotion for personal, non-production coding with included open-weight models                                 | [Fire Pass setup](/firepass)                            |

<Note>
  **Fire Pass is not Nexus.** Fire Pass is an experimental promotion aimed at individual developers and VIP invites. Nexus is the team control plane for connecting harnesses, intelligent routing, and per-seat spend limits. Both can use FireConnect, but they serve different audiences.
</Note>

## Typical paths

<Steps>
  <Step title="Connect a harness">
    Install [FireConnect](/ecosystem/fireconnect/overview#install), sign in, and run `fireconnect <harness> on`. This points your coding tool at Fireworks with sensible model defaults.
  </Step>

  <Step title="Add intelligent routing (optional)">
    Enable [FireRouter](/ecosystem/firerouter/overview) when you want automatic cost optimization — simple prompts stay on open models, hard prompts pass through to closed-source models you BYOK.
  </Step>

  <Step title="Control spend per seat (optional)">
    For team accounts, enable [per-user usage limits](/fireworks-nexus/usage-limits) to cap serverless spend per developer and block overages until the billing period resets.
  </Step>
</Steps>

## Use components on their own

Nexus is modular. You do not need every piece to get value:

* **FireConnect only** — route harnesses to Fireworks open models with a standard API key (`fw_...`). No FireRouter or seat limits required.
* **FireRouter only** — call the `firerouter` model directly through the [Fireworks inference API](/tools-sdks/openai-compatibility), or enable it in FireConnect with `--model firerouter`.
* **Usage limits only** — cap serverless spend per user on supported models without changing how harnesses connect.

<Info>
  FireRouter and FireConnect are available on self-serve (PLG) today. Per-user usage limits require a team account — reach out to your Fireworks contact to enable them.
</Info>

## Quick links

<CardGroup>
  <Card title="FireConnect" icon="plug" href="/ecosystem/fireconnect/overview">
    Install the CLI and route Claude Code, OpenCode, Codex, and more
  </Card>

  <Card title="FireRouter" icon="route" href="/ecosystem/firerouter/overview">
    Automatic routing between open and closed-source models
  </Card>

  <Card title="Usage limits" icon="gauge" href="/fireworks-nexus/usage-limits">
    Per-user spending caps for serverless inference
  </Card>

  <Card title="Fire Pass" icon="ticket" href="/firepass">
    Invite-only promotion for personal agentic coding
  </Card>
</CardGroup>

## Learn more

* [Fireworks Nexus on the web](https://fireworks.ai/nexus)
* [Fireworks Nexus blog post](https://fireworks.ai/blog/fireworks-nexus)
