---
title: "skill.md"
source: https://docs.x.com/tools/skill-md
path: tools/skill-md
---

skill.md is a structured capability summary that describes what AI agents can do with the X API, used by tools like agentskills.io to enable workflows.

The [`skill.md`](https://docs.x.com/skill.md) file follows the [agentskills.io specification](https://agentskills.io/specification) and describes what AI agents can *do* with the X API. While [`llms.txt`](/tools/llms-txt) is a directory of pages, `skill.md` is a capability summary — it lists specific actions, required inputs, and constraints so agents can use the API more reliably.

***

## What's included

* **Capabilities** — what agents can accomplish (search posts, create posts, manage users, etc.)
* **Skills** — specific actions organized by category with required parameters
* **Workflows** — step-by-step procedures for common tasks
* **Context** — background on authentication, rate limits, and architecture

```bash theme={null}
# Fetch the skill file
curl https://docs.x.com/skill.md
```

***

## Discovery endpoints

Agents can discover skill files programmatically via the well-known endpoints:

```bash theme={null}
# Discovery endpoint (agent-skills 0.2.0 spec)
curl https://docs.x.com/.well-known/agent-skills/index.json

# Original discovery format
curl https://docs.x.com/.well-known/skills/index.json
```

You can add X API capabilities to any agent that supports the [skills CLI](https://www.npmjs.com/package/skills):

```bash theme={null}
npx skills add https://docs.x.com
```
