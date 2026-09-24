---
title: "Flag issue for review"
source: https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/flag-issue-for-review.md
path: docs/eleven-agents/customization/tools/system-tools/flag-issue-for-review
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Flag issue for review

## Overview

The **Flag issue for review** tool lets your conversational agent silently raise a [triage ticket](/docs/eleven-agents/operate/triage) mid-conversation about something it cannot handle well — an ambiguous request, a policy question it isn't confident about, or a failed tool call — without telling the caller and without ending the conversation.

> **Note**
>
> This tool was previously named **Request help**. The old name suggested a human would join the
> call, which isn't what it does: it only opens a ticket for someone to review afterward. It is
> being renamed to **Flag issue for review** across the tool itself, its dashboard label, and
> related triage actions, to make that behavior clearer. Agents already using the tool continue to
> work without any changes required.

## Functionality

* **Add the tool**: add it to your agent's configuration, the same way you would add [End call](/docs/eleven-agents/customization/tools/system-tools/end-call) or [Skip turn](/docs/eleven-agents/customization/tools/system-tools/skip-turn).
* **Silent trigger**: during a conversation, if the model decides help is needed, it calls the tool with a short description of the problem.
* **Ticket creation**: calling the tool opens a triage ticket with that description and a link back to the conversation. The ticket appears in the agent's [triage queue](/docs/eleven-agents/operate/triage), where you or Architect can review it.
* **Uninterrupted conversation**: the agent is told internally to keep helping the caller as best it can and not to mention that anything was flagged, so the conversation continues uninterrupted.

![Flag issue for review enabled in system
tools](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/428092adaaf445254c89c54bc09904eb83fa7fe3a7ad41dad10546ce573de16e/assets/images/agents/flag-issue-for-review-enable.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260924%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260924T095248Z&X-Amz-Expires=604800&X-Amz-Signature=95ed470b92929e81d2c9bd0ae720227849d523d7fddb6b4d25e9545d67d27be8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Availability

> **Warning**
>
> Flag issue for review is not available for agents or workspaces running in [Zero Retention Mode](/docs/eleven-agents/customization/privacy/zrm), or for on-premises deployments. Like other
> triage functionality, flagging an issue creates a ticket that stores details from the
> conversation.

## Related resources

#### [Triage](/docs/eleven-agents/operate/triage)

Review and resolve flagged tickets.

#### [Architect](/docs/eleven-agents/operate/architect)

The assistant that helps you work through flagged tickets.
