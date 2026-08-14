---
title: "Where can I locate the reason for my call failing?"
source: https://elevenlabs.io/docs/help-center/product/eleven-agents/where-can-i-locate-the-reason-for-my-call-failing.md
path: docs/help-center/product/eleven-agents/where-can-i-locate-the-reason-for-my-call-failing
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Where can I locate the reason for my call failing?

You can find all failed (and successful) calls on the Call History page.

Failed calls will display a red error message that explains why the call ended early or didn’t connect at all.

Here are a few common errors you might see:

* **Host elevenlabs.io is not allowed to connect to this agent**\
  This error usually occurs when the agent has an allowlist enabled, but the caller is using a
  shared link. Removing the allowlist will resolve this issue.
* **Missing required dynamic variables in **\_\_** : `{'dynamic variable name'}`**\
  This error typically appears when no transcript or call is generated. It means the caller didn’t
  configure a required dynamic variable correctly.
* **Agent has exceeded its daily call limit of**\
  The agent has a preset daily call limit. This error indicates that the call failed because the
  limit was exceeded.
* **Override is not allowed for this AI agent**\
  A simple error message indicating an attempt was made to override the prompt or other settings,
  but the override feature wasn’t enabled.
* **Missing dynamic variable after agent transfer**\
  This means a dynamic variable required by the transferred-to agent wasn’t available, causing the
  call to end.

If your call failed and no error message is displayed, please contact support by emailing us at [team@elevenlabs.io](mailto:team@elevenlabs.io).
