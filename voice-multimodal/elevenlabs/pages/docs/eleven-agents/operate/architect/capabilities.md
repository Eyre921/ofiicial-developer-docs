---
title: "What ElevenAgents Architect can change"
source: https://elevenlabs.io/docs/eleven-agents/operate/architect/capabilities.md
path: docs/eleven-agents/operate/architect/capabilities
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# What ElevenAgents Architect can change

## Overview

ElevenAgents Architect's capabilities come from a fixed set of tools. This page lists them by area, and for each area answers three questions:

* **What can Architect read?**
* **What can it change, and where does the change land?** Changes land in one of two places:
  * **Draft**: staged in your unpublished draft on a branch. Nothing reaches live callers until you publish the draft.
  * **Workspace**: applied immediately to a resource shared across the workspace, such as a tool or a knowledge base document.
* **Does it ask first?** This column describes the default **Approval required** mode. In **Auto-approve** mode, Architect does not ask before any action. See [Approval modes](/docs/eleven-agents/operate/architect/authentication#approval-modes).

Every action also runs as you: Architect can only do what your own role allows. See [Permissions, approvals, and drafts](/docs/eleven-agents/operate/architect/authentication).

## Agent configuration

| Area                                                        | Reads                                      | Changes                                                                   | Lands in | Asks first                                                             |
| ----------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------- | -------- | ---------------------------------------------------------------------- |
| System prompt and first message                             | Yes                                        | Edit, append, or rewrite                                                  | Draft    | No                                                                     |
| Voice, LLM, language, turn-taking, and other agent settings | Yes, including available LLMs and voices   | Any setting in the agent's configuration                                  | Draft    | No                                                                     |
| [Guardrails](/docs/eleven-agents/best-practices/guardrails) | Yes                                        | Add, edit, or remove guardrails                                           | Draft    | No                                                                     |
| Evaluation criteria and data collection                     | Yes                                        | Add, edit, or remove                                                      | Draft    | No                                                                     |
| [Procedures](/docs/eleven-agents/customization/procedures)  | Yes, and search                            | Create and edit. Procedures are compiled automatically after each change. | Draft    | No                                                                     |
|                                                             |                                            | Delete                                                                    | Draft    | Yes                                                                    |
| Workflow                                                    | Yes                                        | Add, update, connect, and delete nodes and edges                          | Draft    | No                                                                     |
| Attached tools, knowledge base documents, and tests         | Yes                                        | Attach or detach                                                          | Draft    | No                                                                     |
| System tools, such as end call and transfer                 | Yes                                        | Enable, disable, and configure                                            | Draft    | No                                                                     |
| Draft                                                       | Yes, including what differs from published | Discard the draft                                                         | Draft    | Yes                                                                    |
|                                                             |                                            | Publish                                                                   | —        | Cannot. Architect opens the publish dialog and you select **Publish**. |

## Workspace resources

| Area                                 | Reads                                         | Changes                                                                               | Lands in                              | Asks first                                         |
| ------------------------------------ | --------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------- | -------------------------------------------------- |
| Webhook, client, and code tools      | Yes, including recent failures and dependents | Create and update. Code tools require an Enterprise plan.                             | Workspace                             | Yes                                                |
|                                      |                                               | Delete                                                                                | Workspace                             | Yes                                                |
| MCP servers                          | Tools attached to the agent                   | Cannot create, edit, or delete                                                        | —                                     | —                                                  |
| Knowledge base                       | Yes, including search and RAG queries         | Create a text or URL document                                                         | Workspace                             | Only if it goes in a folder or syncs automatically |
|                                      |                                               | Crawl a site, create folders, move items, rename or replace a document                | Workspace                             | Yes                                                |
|                                      |                                               | Index a document for RAG                                                              | Workspace                             | No                                                 |
|                                      |                                               | Delete a document or folder                                                           | —                                     | Cannot                                             |
| Tests and simulations                | Yes, including runs, results, and failures    | Create LLM, tool-call, and simulation tests, or generate one from a real conversation | Workspace, attached through the draft | No                                                 |
|                                      |                                               | Update or delete a test, create a test folder                                         | Workspace                             | Yes                                                |
|                                      |                                               | Run tests, including repeated runs to check for flakiness                             | —                                     | No                                                 |
| Voices                               | Yes, and search                               | Add a voice to the workspace                                                          | Workspace                             | No                                                 |
| Secrets                              | Names only, never values                      | Cannot create, edit, or delete                                                        | —                                     | —                                                  |
| Phone numbers                        | Yes                                           | Place a test call through Twilio or SIP                                               | Live call                             | Yes                                                |
|                                      |                                               | Buy, import, assign, or delete                                                        | —                                     | Cannot                                             |
| Channels, integrations, and triggers | Yes                                           | Cannot change                                                                         | —                                     | —                                                  |

A test Architect creates exists in the workspace straight away, but it only joins the agent's test suite when you publish the draft that attaches it. Architect can still run it before you publish.

## Conversations, insights, and triage

| Area                                                 | Reads                                                                                                                       | Changes                                | Asks first |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ---------- |
| Conversations and transcripts                        | List, count, filter, literal and semantic search, summaries, full detail, and in-depth analysis of individual conversations | Cannot change                          | —          |
| Spotlight, topics, and insight reports               | Yes, including the values shown on dashboard charts                                                                         | Can set dashboard filters on screen    | No         |
| Real-time alerts                                     | Yes                                                                                                                         | Cannot change                          | —          |
| [Triage tickets](/docs/eleven-agents/operate/triage) | Yes                                                                                                                         | Comment                                | No         |
|                                                      |                                                                                                                             | Change status, for example to resolved | Yes        |

## Branches, proposals, and deployment

| Area                                                            | Reads                                                              | Changes                                               | Asks first |
| --------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------- | ---------- |
| [Branches and versions](/docs/eleven-agents/operate/versioning) | Yes, including history, diffs between versions, and merge previews | Create a branch                                       | No         |
|                                                                 |                                                                    | Rename, archive, or change protection                 | Yes        |
|                                                                 |                                                                    | Merge one branch into another                         | Yes        |
| [Merge proposals](/docs/eleven-agents/operate/merge-proposals)  | Yes                                                                | Open a proposal and request reviewers                 | No         |
|                                                                 |                                                                    | Approve, request changes, comment, merge, or close    | Cannot     |
| Traffic split                                                   | Yes                                                                | Change the share of live traffic each branch receives | Yes        |

Creating a branch or a merge proposal doesn't change what live callers experience, so Architect doesn't ask first. Merging into a branch that serves traffic, and changing the traffic split, both affect live callers immediately.

## Agents

| Area   | Reads                      | Changes                                                | Asks first |
| ------ | -------------------------- | ------------------------------------------------------ | ---------- |
| Agents | Every agent you can access | Create a new agent, or generate one from a description | No         |
|        |                            | Create an agent from a template                        | Yes        |
|        |                            | Archive an agent                                       | Yes        |

Architect can't permanently delete an agent. Its delete action archives the agent instead.

## Interface actions

In addition to its agent-building tools, Architect can act on the page you are viewing: navigate to a page, highlight a control, fill in form fields, click buttons, and switch branches or dashboard filters. It uses these to walk you through the dashboard, for example when you ask how to invite a teammate. These actions don't ask for approval. They can only do what you could do on that page yourself.

## One agent or many

Architect isn't limited to the agent you have open. It works on that agent by default, but it can read and edit any agent you have access to, and compare agents across the workspace. Open the workspace Architect page (**Agents** > **Architect**) for questions that span agents, such as "Which of my agents have no guardrails?"

When a single chat stages edits on more than one branch of an agent, Architect must say which branch each later edit is for.

## What ElevenAgents Architect cannot do

Architect has no tools for these actions:

* Publish a draft. You always publish.
* Approve, review, or merge a merge proposal.
* Permanently delete an agent, a branch, a knowledge base document, a phone number, or a secret.
* Create or edit MCP servers, secrets, integrations, channels, or alerts.
* Buy, import, or assign phone numbers.
* Read secret values.
* Manage workspace members, roles, billing, or API keys through a dedicated tool. It can open those pages and walk you through them using the interface actions below.
* Bypass your permissions. Architect is subject to every restriction on your account, including [branch protection](/docs/eleven-agents/operate/versioning).
