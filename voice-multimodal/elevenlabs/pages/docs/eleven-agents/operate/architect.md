---
title: "Architect"
source: https://elevenlabs.io/docs/eleven-agents/operate/architect.md
path: docs/eleven-agents/operate/architect
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Architect

## Overview

Architect is the AI assistant built into ElevenAgents. Instead of changing every setting field by field, you describe what you want and Architect makes the edit for you, using the same configuration, workflow, tools, tests, and knowledge base APIs available in the dashboard.

Architect is one assistant with two placements:

* **Sidebar**: available across the whole ElevenLabs app from a floating button or sidebar. Use it to ask product questions, navigate the dashboard, and get help finding a setting.
* **Architect tab**: a full-screen view inside a specific agent, opened from that agent's page or from "Discuss", "Improve", or "Make with Architect" buttons. Here, Architect additionally reads and edits that agent's configuration, workflow, tools, tests, and knowledge base.

![Architect tab home screen](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/ed0d216d50539bce021442606fa5a8b82bd29b1596707571e2247081c399546d/assets/images/agents/architect-landing-page.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260926%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260926T113231Z&X-Amz-Expires=604800&X-Amz-Signature=d9862c6b1e6d86f62e65ccd9086ec820fd60664e51228eca595283788da4d4fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## What Architect is specialized for

Architect's primary job is helping you iterate on an agent you have already built: reviewing how it performed on real conversations, understanding what went wrong, and turning that into a concrete change to its prompt, workflow, tools, tests, or knowledge base. See [Triage](/docs/eleven-agents/operate/triage) for how this review loop works.

![Architect running an agent's test suite](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e3f2c99d7b123f8ef399f7a68ad326b96285a581dfe70fa1653784b8fb19b83d/assets/images/agents/architect-running-test.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260926%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260926T113231Z&X-Amz-Expires=604800&X-Amz-Signature=ebf6716a6d4f2ab35aea87ba6a66425b46d4cad49d4f045b2352b9debd5fe668&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Outside of a specific agent, Architect in the sidebar also answers general product questions and helps you navigate the dashboard.

## Pricing

Architect is available now in alpha and is free to use during the alpha period, which will run through October 2026. During the alpha, usage does not count against your workspace's agent minutes or LLM cost. Check the [pricing page](https://elevenlabs.io/pricing) for terms after the alpha ends.

## Privacy and data retention

> **Warning**
>
> Architect conversations are not covered by Zero Retention Mode (ZRM). Avoid sharing personal or
> sensitive information in messages to Architect.

For details on what ZRM does cover, see [Zero Retention Mode](/docs/eleven-agents/customization/privacy/zrm).

## Learn more

#### [How Architect works](/docs/eleven-agents/operate/architect/how-it-works)

What Architect can see, the tools it can use, and how it applies changes.

#### [Triage](/docs/eleven-agents/operate/triage)

Review conversation issues flagged for follow-up.

#### [Merge proposals](/docs/eleven-agents/operate/merge-proposals)

Ask for a branch's changes to be reviewed before they reach another branch.

#### [Flag issue for review](/docs/eleven-agents/customization/tools/system-tools/flag-issue-for-review)

Let a live agent raise a ticket for a problem it can't resolve.

#### [Customizing Architect](/docs/eleven-agents/operate/architect/customization)

Give Architect durable context and reusable prompts.

#### [Authentication, approvals, and drafts](/docs/eleven-agents/operate/architect/authentication)

How Architect acts on your behalf and stages changes safely.

#### [Claude, Cursor, and other AI assistants](/docs/eleven-agents/operate/architect/external-assistants)

Manage agents from outside the ElevenLabs dashboard.
