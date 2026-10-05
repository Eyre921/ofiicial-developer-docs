---
title: "Permissions, approvals, and drafts"
source: https://elevenlabs.io/docs/eleven-agents/operate/architect/authentication.md
path: docs/eleven-agents/operate/architect/authentication
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Permissions, approvals, and drafts

## How ElevenAgents Architect authenticates

Architect doesn't use a separate service account or act as a different identity. In the ElevenLabs dashboard, its tools run in your browser, inside your signed-in session. Every read or write it performs, from fetching an agent's configuration to creating a branch, is an ordinary request made as you, under your workspace permissions.

This has three consequences:

* **Architect can only do what you can do.** If you can't edit an agent, Architect can read it but can't stage changes to it. If your role doesn't allow merging into a protected branch, Architect can't merge into it either.
* **Its work is recorded under your name.** Versions you publish, branches, and merge proposals Architect creates show you as the author. Nothing marks them as created by Architect.
* **Different users get different results.** Two teammates asking Architect for the same change can get different outcomes if their roles differ.

> **Note**
>
> This page describes Architect in the ElevenLabs dashboard, which is the only place Architect runs
> today. Architect is coming to other surfaces, such as Slack, but that isn't available yet. On
> every surface, Architect will keep the same model: it authenticates as the person it is talking to
> and acts with that person's permissions.

## What each role allows

Agent access roles apply to Architect exactly as they apply to you in the dashboard.

| Your access to the agent | What Architect can do for you                                                                                                                                     |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Viewer                   | Read the configuration, conversations, tests, branches, and proposals. Investigate and recommend changes, but not stage them.                                     |
| Editor                   | Everything a viewer can, plus stage changes in drafts, create branches, write and run tests, open merge proposals, and merge into branches that aren't protected. |
| Workspace admin          | Everything an editor can, plus merge into protected branches and change the traffic share of protected branches.                                                  |

Workspace-level resources, such as tools, knowledge base documents, and tests, follow their own sharing permissions. See [What Architect can change](/docs/eleven-agents/operate/architect/capabilities) for which actions apply to the agent and which to the workspace.

## Approval modes

Every Architect conversation runs in one of three modes. Switch modes from the pill in the composer, or press <kbd>Shift</kbd>+<kbd>Tab</kbd> to cycle through them.

| Mode                            | Behavior                                                                                                                                                                                                       |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approval required** (default) | Architect asks before actions that affect live traffic or shared resources. It shows exactly what will change and waits for you to approve or reject.                                                          |
| **Auto-approve**                | Architect doesn't ask before any action, including merging a branch, changing the traffic split, discarding a draft, archiving an agent, or placing a test call. Use it only for work you are confident about. |
| **Plan**                        | Architect researches with read-only tools, writes a plan, and waits for you to approve the plan before changing anything. After you approve, actions are gated as in Approval required mode.                   |

Your choice of mode is remembered in your browser. There is no workspace setting that enforces a mode for everyone. To require review for every change to a live agent, protect its `main` branch so changes have to go through an approved [merge proposal](/docs/eleven-agents/operate/merge-proposals).

### Which actions ask first

In **Approval required** mode, Architect stages changes to the agent's configuration in your draft without asking, because a draft never affects live callers. It asks before:

* Changes that take effect immediately for live callers: merging a branch and changing the traffic split.
* Changes to shared workspace resources: creating, updating, or deleting tools, updating or deleting tests, and most knowledge base changes.
* Destructive actions: discarding a draft, deleting a procedure, archiving an agent or branch.
* Real-world actions: placing a test phone call.

Reads never ask. The approval prompt marks deletes that can't be undone with a **Permanent** label. The full list of what asks first is in [What Architect can change](/docs/eleven-agents/operate/architect/capabilities).

Three steps always need you, in every mode:

* **Publishing a draft.** Architect opens the publish dialog, and you select **Publish**.
* **Approving a plan** in Plan mode.
* **Deciding what to do with an existing draft.** If the branch already has a draft that Architect didn't create in this chat, including unsaved edits in the editor, Architect stops and asks whether to keep it or discard it before staging anything.

### Trusting a tool for the session

The approval prompt has a **Trust these tools this session** checkbox. When you select it, later calls to the same tools in that session run without asking. Trust ends when you start a new conversation. If you don't respond to an approval prompt within about two minutes, the request expires and Architect doesn't run the action.

## Drafts, versions, and branches

Architect uses the same [versioning](/docs/eleven-agents/operate/versioning) model as the rest of ElevenAgents.

| Concept | What it is                                                                        | How Architect uses it                                                                                                     |
| ------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Draft   | Your unpublished changes on one branch. Each user has their own draft per branch. | Every configuration edit Architect makes is staged here. The chat shows a staged changes panel with **Review & publish**. |
| Version | An immutable snapshot, created when a draft is published.                         | You publish. Architect can't. On a protected branch, the dialog offers to publish to a new branch instead.                |
| Branch  | A named line of versions. Live traffic is routed to branches by percentage.       | Architect creates a branch for changes that need review, so `main` is unaffected until the branch is merged.              |

"Nothing goes live without your approval" has a precise meaning:

* Changes to an agent's configuration are staged in a draft and reach live callers only after you publish, on a branch that serves traffic.
* In **Approval required** mode, actions that affect live traffic or shared resources wait for your approval.
* In **Auto-approve** mode, Architect still can't publish, but it can merge branches and change traffic splits without asking, within your permissions.

Some changes outside the agent configuration take effect in the workspace as soon as they're made, such as creating a tool or a knowledge base document. They don't affect the agent's behavior until it uses them, which happens when you publish a draft that attaches them. Workspace resources already attached to live agents are the exception: updating a tool that a live agent uses changes that agent straight away. Architect asks before updating tools in **Approval required** mode.

## Version history and reverting

Every published version records what changed and who published it.

* **See what changed**: in **Version Control** > **Branches**, open a branch's **Version history**. Compare any version with the previous one or with the live version. Or ask Architect, for example "What changed on main in the last week?" It reads the branch history and diffs versions for you.
* **See who changed it**: each version shows the user who published it. A change Architect made shows the user who was talking to it.
* **Revert**: select **Revert to this version** in the version history. Reverting doesn't remove history. It publishes the old configuration as a new version. You can also use `/rollback` to have Architect review recent changes and stage a revert for you to publish.
