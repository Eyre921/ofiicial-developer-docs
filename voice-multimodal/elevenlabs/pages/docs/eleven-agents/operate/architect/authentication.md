---
title: "Authentication, approvals, and drafts"
source: https://elevenlabs.io/docs/eleven-agents/operate/architect/authentication.md
path: docs/eleven-agents/operate/architect/authentication
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Authentication, approvals, and drafts

## How Architect authenticates

Architect does not use a separate service account or act as a different identity. It runs inside your logged-in session: every read or write it performs, from fetching an agent's configuration to updating a prompt or creating a branch, goes through the same authenticated requests the rest of the dashboard uses, under your account and your workspace permissions.

This means Architect can only do what you are already allowed to do. If your role doesn't permit merging into the main branch, or a resource hasn't been shared with you, Architect can't do it either.

## Approval modes

Every Architect conversation runs in one of three modes, switchable from the composer:

| Mode                        | Behavior                                                                                                                                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Approval required (default) | Before running a tool that changes something, Architect shows you exactly what will change and waits for you to approve or reject it.                                                      |
| Auto-approve                | Skips that confirmation step for gated tools, including higher-risk actions like merging a branch or discarding a draft. Use it once you're confident about the changes you're asking for. |
| Plan                        | Architect researches first, writes a plan, and only starts editing after you approve the plan.                                                                                             |

Reads, such as listing tools or fetching an agent's current configuration, never require approval in any mode. A tool you've already approved once earlier in the same conversation is treated as trusted and won't ask again until you start a new conversation.

## Drafts, publishing, and merging

Changes to an agent's configuration, prompt, workflow, tools, tests, or knowledge base are staged as an unpublished draft on the branch you're working on. Nothing Architect does takes effect for live callers until you publish it.

* Ask Architect what it has changed so far to see the current draft compared to what's published.
* Architect can open the publish dialog for you, but it cannot click publish itself. You review the diff and confirm.
* After publishing, you can keep iterating: ask Architect for more changes, review, and publish again, as many rounds as you need.

### Branches

For larger changes, work on a separate branch instead of directly on the one that's live. Architect can create branches, list them, and adjust traffic splits across active branches, which must always sum to 100%.

When you're ready to bring a branch's changes into `main`, ask Architect to merge it. Architect shows a merge preview first, and the merge itself still requires your approval, even in auto-approve mode. Merging into `main` may require admin permissions, and a branch with an unsaved draft must be saved or discarded before it can be merged or switched away from.
