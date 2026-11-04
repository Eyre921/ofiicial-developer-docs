---
title: "Flag issue for review"
source: https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/flag-issue-for-review.md
path: docs/eleven-agents/customization/tools/system-tools/flag-issue-for-review
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Flag issue for review

## Overview

The **Flag issue for review** tool lets your conversational agent silently raise an [issue](/docs/eleven-agents/operate/triage) mid-conversation about something it cannot handle well — an ambiguous request, a policy question it isn't confident about, or a failed tool call — without telling the caller and without ending the conversation.

> **Note**
>
> This tool was previously named **Request help**. The old name suggested a human would join the
> call, which isn't what it does: it only opens an issue for someone to review afterward. It has
> been renamed to **Flag issue for review** in both the tool and its dashboard label, to make that
> behavior clearer. Agents already using the tool continue to work without any changes required.

## Functionality

* **Add the tool**: add it to your agent's configuration, the same way you would add [End call](/docs/eleven-agents/customization/tools/system-tools/end-call) or [Skip turn](/docs/eleven-agents/customization/tools/system-tools/skip-turn).
* **Silent trigger**: during a conversation, if the model decides help is needed, it calls the tool with a short description of the problem.
* **Issue creation**: calling the tool opens an issue with that description and a link back to the conversation. The issue appears in the agent's [Issues](/docs/eleven-agents/operate/triage) tab, where you or ElevenAgents Architect can review it.
* **Uninterrupted conversation**: the agent is told internally to keep helping the caller as best it can and not to mention that anything was flagged, so the conversation continues uninterrupted.

![Flag issue for review enabled in system
tools](/docs/_fern-files/_img/428092adaaf445254c89c54bc09904eb83fa7fe3a7ad41dad10546ce573de16e.webp)

## Availability

> **Warning**
>
> Flag issue for review is not available for agents or workspaces running in [Zero Retention Mode](/docs/eleven-agents/customization/privacy/zrm), or for on-premises deployments. Like the
> rest of the Issues feature, a flagged issue stores details from the conversation.

## Related resources

#### [Issues](/docs/eleven-agents/operate/triage)

Review and resolve flagged issues.

#### [ElevenAgents Architect](/docs/eleven-agents/operate/architect)

The assistant that helps you work through flagged issues.
