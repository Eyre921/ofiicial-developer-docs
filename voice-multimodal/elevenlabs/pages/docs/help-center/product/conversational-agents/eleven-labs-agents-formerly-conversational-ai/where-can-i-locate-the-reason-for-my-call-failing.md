---
title: "Where can I locate the reason for my call failing?"
source: https://elevenlabs.io/docs/help-center/product/conversational-agents/eleven-labs-agents-formerly-conversational-ai/where-can-i-locate-the-reason-for-my-call-failing.md
path: docs/help-center/product/conversational-agents/eleven-labs-agents-formerly-conversational-ai/where-can-i-locate-the-reason-for-my-call-failing
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Where can I locate the reason for my call failing?

You can find all failed (and successful) calls on the Call History page.

Failed calls will display a red error message that explains why the call ended early or didn’t connect at all.

Here are a few common errors you might see:

* <strong>
    Host elevenlabs.io is not allowed to connect to this agent
  </strong>
  <br />
  This error usually occurs when the agent has an allowlist enabled, but the caller is using a
  shared link. Removing the allowlist will resolve this issue.
* <strong>
    Missing required dynamic variables in \_\_\_\_\_\_ : \{‘dynamic variable name’}
  </strong>
  <br />
  This error typically appears when no transcript or call is generated. It means the caller didn’t
  configure a required dynamic variable correctly.
* <strong>
    Agent has exceeded its daily call limit of
  </strong>
  <br />
  The agent has a preset daily call limit. This error indicates that the call failed because the
  limit was exceeded.
* <strong>Override is not allowed for this AI agent</strong>
  <br />A simple error message indicating an attempt was made to override the prompt or other
  settings, but the override feature wasn’t enabled.
* <strong>
    Missing dynamic variable after agent transfer
  </strong>
  <br />
  This means a dynamic variable required by the transferred-to agent wasn’t available, causing the
  call to end.

If your call failed and no error message is displayed, please contact support by emailing us at [team@elevenlabs.io](mailto:team@elevenlabs.io).
