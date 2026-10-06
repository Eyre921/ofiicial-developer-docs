---
title: "Proposals and validation"
source: https://elevenlabs.io/docs/eleven-agents/operate/architect/proposals.md
path: docs/eleven-agents/operate/architect/proposals
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Proposals and validation

## Overview

When ElevenAgents Architect finishes a change, it hands it to you as a **proposal**: a branch that holds the change, tests that show it works, and a [merge proposal](/docs/eleven-agents/operate/merge-proposals) asking for that branch to be merged into `main`. This page explains how each part works, where to find it, and how a proposal moves from a conversation to live traffic.

## What a proposal is

A proposal is built from the existing [versioning](/docs/eleven-agents/operate/versioning) model:

| Part           | What it is                                                                                                                                                            |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Branch         | A branch Architect created for the change, so `main` and live callers are unaffected while you work.                                                                  |
| Draft          | Architect's edits, staged in your unpublished draft on that branch.                                                                                                   |
| Version        | When you publish the draft, it becomes a new version on the branch.                                                                                                   |
| Tests          | The tests Architect wrote for the change, attached to the agent and run against the branch.                                                                           |
| Merge proposal | A request to merge the branch into `main` (or another branch you choose), with a description of the change, the tests that were run, and what reviewers should check. |

The merge proposal is a standard ElevenAgents merge proposal, the same kind a teammate opens by hand. It is not a separate object type.

A merge proposal covers exactly one source branch and one target branch, so one proposal holds one candidate solution. To compare alternatives, ask Architect to put each one on its own branch. Each branch then gets its own proposal, and you can split traffic between them as an [experiment](/docs/eleven-agents/operate/experiments).

> **Note**
>
> Architect acts as you, so a merge proposal it opens is recorded under your name as the author. No
> field records that Architect created it. Mention it in the proposal description if your team wants
> to know.

## How a proposal is created

Architect creates a proposal when you ask it to fix or improve something, or when you hand it a failing test, a Spotlight finding, or a triage ticket. The full sequence, with the tools Architect calls at each step, is in the [worked example](/docs/eleven-agents/operate/architect/how-it-works#worked-example-improving-refund-resolutions). In short:

1. Architect investigates, creates a branch, and stages the change in your draft on that branch.
2. Architect writes tests and simulations for the change and runs them in the conversation, before showing you the result.
3. Architect opens the publish dialog. You review the diff and select **Publish**, which commits the change as a new version on the branch.
4. Architect opens a merge proposal into `main`, writing its description from the branch's actual commits and test runs.
5. Architect offers to send a small share of live traffic to the branch while the proposal is reviewed. This needs your approval.

You can stop at any step. A branch with a published version but no merge proposal is still useful: you can test it yourself, or open a proposal later.

### Validation inside the conversation

Architect writes and runs tests as part of building the change, not as a separate step you start afterward. For a fix, a useful pattern is to show that the new tests fail without the change and pass with it. Architect can run the same tests against the original branch and against the draft that contains the change.

Architect doesn't run this before-and-after check on every change automatically. Ask for it when it matters, for example: "Show me the new simulation failing on main and passing on the branch, then open a proposal."

A test **passes** when every success condition is met. For an LLM test, the agent's response satisfies the success criteria. For a tool-call test, the expected tool is called with the expected parameters. For a simulation, the simulated conversation meets its success conditions. To check for flaky results, ask Architect to run tests several times. It can repeat each test up to 50 times and report the pass rate.

See [Testing](/docs/eleven-agents/customization/agent-testing) for how each test type is defined.

## Where to find proposals

Open the agent, then go to **Version Control** > **Proposals**. The list can be filtered by status, by author (**Created by**), and by reviewer (**Awaiting review from**, **Reviewed by**). A proposal Architect opened in your conversation is listed with you as the author.

Architect also returns a link to the proposal in the conversation as soon as it creates it.

![Proposals list on the Branches page](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/bfdb23ad1edb31c89c2ff2a137fa3028bf3f9fbcf31e236de142e207b5d54cd0/assets/images/agents/architect-proposals-list.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T095016Z&X-Amz-Expires=604800&X-Amz-Signature=d8e0f3a15e544352869b6da16f4aa935df1a51afbf2a52f14f98c45d1b83bdf5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Anatomy of a proposal

A proposal's page shows the source and target branches, its status, whether it can be merged, and how far the source branch is behind or ahead of the target. It has these tabs:

#### Overview

The description, an activity timeline of commits on the source branch, reviews, and comments, and a comment box. The sidebar shows reviewers, recommended reviewers, and any linked triage ticket.

A description Architect writes always has three sections: **Summary** (each meaningful change and why), **Testing** (which tests were run and their results, or a statement that none were run), and **How to review** (what to focus on, and a test to run or conversation to try).

![Overview tab of a merge proposal](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/569eccd1750f90cd5ec8121411e8effd3a38e924e0f03f06f6216a9fcc160e08/assets/images/agents/architect-proposal-overview.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T095016Z&X-Amz-Expires=604800&X-Amz-Signature=3b26ecb6b79b4a8a3c932d125c21e1ffdc571e2dd7192b25d9cfb077c333e5c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Changes

The configuration diff: what the target branch will look like after the merge, compared with its current state. If both branches changed the same field, a **Conflicts** view lists each conflict and which side wins.

After the proposal is merged, this tab shows the target branch before and after the merge.

![Changes tab of a merge proposal](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/cd06c0f93240d7c973101b896599542290437a6dcbfa6d288a25db0c1bfcd566/assets/images/agents/architect-proposal-changes.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T095016Z&X-Amz-Expires=604800&X-Amz-Signature=229ae54f85b73af33e1ba1e6cfa4cc88f5b3e28ac48562eb5139b082d5564426&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Test runs

The pass rate and test run history for the source branch, including the runs Architect started in the conversation. Switch to the target branch to compare its pass rate. Select **Run tests** to run every attached test on either branch again, optionally several times each.

Test runs are linked to the branch, not to the proposal. Merging does not require tests to pass. Reviewers decide based on what the tab shows.

![Test runs tab of a merge proposal](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/58e28b31cb3408fe5bf8e9193f4a4edb5e716e6023c56f29d5a4f924c70a0f7a/assets/images/agents/architect-proposal-test-runs.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T095016Z&X-Amz-Expires=604800&X-Amz-Signature=0a2af409f1333afb07b196cd9f64f5550a1c2fe47ed9def42fc2b70a421fe74d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Conversations

Every conversation that ran on the source branch, including live traffic sent there by a traffic split. Select a conversation to open its transcript. While a branch is on a gradual rollout, this is where you watch real callers use the change.

![Conversations tab of a merge proposal](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/f6345ff5beaee9a22732c7322995a7e889245cda7901682ab390790ef3849690/assets/images/agents/architect-proposal-conversations.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T095016Z&X-Amz-Expires=604800&X-Amz-Signature=36eb04fb579c05aaf11864a6cc2cede1b81d4d9a5059afb7a71415e90d9ea83c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Reviewing and merging

### Statuses

A merge proposal has one of these statuses:

| Status | Meaning                                                                                                                           |
| ------ | --------------------------------------------------------------------------------------------------------------------------------- |
| Open   | Waiting for review or merge.                                                                                                      |
| Merged | The branch was merged into the target.                                                                                            |
| Closed | Withdrawn by its author, rejected by someone else, or closed because its branch was archived. Closed proposals can't be reopened. |

While a proposal is open, each reviewer's latest review is either **Approved** or **Changes requested**. There are no separate "tested" or "ready for review" statuses. Test results are shown on the **Test runs** tab instead.

Reviews and comments appear in the activity timeline on the **Overview** tab, alongside each new version committed to the source branch.

![Activity timeline of a merge proposal](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/522012341d0089ff418032a34bae6653d2b883934b64a0b6a12de887646b2f5f/assets/images/agents/architect-proposal-activity.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T095016Z&X-Amz-Expires=604800&X-Amz-Signature=d3bbbab9061cff7f8865bfe97746fa3c1da3b81658215d6cfdc3c3d5b5f0a214&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Who can approve and merge

* Anyone with editor access to the agent can review a proposal, except its author. Because Architect acts as you, you can't approve a proposal Architect opened in your conversation. A teammate has to.
* A proposal can be merged once it has at least one approval from someone other than the author and no reviewer's latest review is **Changes requested**. Workspace admins can merge without an approval.
* Merging into a [protected branch](/docs/eleven-agents/operate/versioning) requires admin permissions, or an approval from an admin.

Architect can't approve, comment on, merge, or close a merge proposal. Those steps are always done by people. See [Merge proposals](/docs/eleven-agents/operate/merge-proposals) for the full review rules.

> **Warning**
>
> Architect can merge a branch directly, without a proposal, when you ask it to and your role allows
> the merge. In **Approval required** mode it asks first. In **Auto-approve** mode it does not. Use
> branch protection on `main` if every change must go through a reviewed proposal.

### What happens on merge

There's no separate publish step after a merge. Merging writes a new version on the target branch, and that version serves live traffic straight away for whatever share of traffic the target receives. When the target is `main` and no traffic split is set, that means all callers.

Merging also:

* Moves any live traffic share the source branch had to the target.
* Archives the source branch by default.
* Closes any other open proposal from the same branch.
* Resolves the linked triage ticket, if there is one.

## Gradual rollout

Before a proposal is merged, you can send a share of live traffic to its branch so real callers exercise the change.

#### Start the split

Ask Architect, for example "Send 5% of traffic to this branch." Architect tells you the full
resulting split, including `main`'s share, and asks for approval before applying it. You can
also set it yourself: in **Version Control** > **Branches**, select **Deploy** on the branch.

#### Watch the results

Open the proposal's **Conversations** tab to read conversations on the branch, or ask Architect
to compare the branch's results with `main`'s.

#### Promote or roll back

To promote, merge the proposal. The branch's traffic share moves to `main` with it. To roll
back, ask Architect to set the branch's share to 0%, or edit the deployment yourself. Live
traffic returns to `main` immediately.

Traffic shares must always total 100%, and routing is deterministic per conversation. Changing the share of a protected branch, including taking traffic from a protected `main`, requires an admin. See [Traffic deployment](/docs/eleven-agents/operate/versioning#traffic-deployment).

## Proactive proposals

> **Note**
>
> Architect produces proposals when you ask it to, or when you hand it a failing test, a Spotlight
> finding, an alert, or a triage ticket. It doesn't yet scan your agents on a schedule or open
> proposals on its own.

The proactive path today is [Spotlight](/docs/eleven-agents/dashboard/spotlight) followed by a hand-off. Spotlight watches your agent's conversations continuously. It produces a weekly summary with suggested investigations, raises real-time alerts, and recommends configuration changes. To turn a Spotlight finding into a proposal:

#### Open Spotlight

Open the agent. Its overview page is Spotlight.

#### Pick a finding

Open the weekly summary and review **Suggested next steps**, or open a real-time alert.

#### Hand it to ElevenAgents Architect

Select **Open in Architect** on a suggestion, **Analyze with Architect** on the summary, or
**Investigate with Architect** on an alert. Architect receives the finding and is instructed to
verify it against real conversations, and to identify which branch is affected, before
suggesting a change.

#### Ask for a proposal

Review Architect's findings. If you agree with the root cause, ask it to fix the problem on a
branch, test the fix, and open a proposal.

Triage tickets work the same way. Your live agent can [flag issues for review](/docs/eleven-agents/customization/tools/system-tools/flag-issue-for-review) during conversations, and **Discuss with Architect** on a ticket starts an investigation of it.

Scheduled automations, with reports delivered to an Architect inbox, are in development. The **Inbox** tab on the Architect page is a placeholder for them.
