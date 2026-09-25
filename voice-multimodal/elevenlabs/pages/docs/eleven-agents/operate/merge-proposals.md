---
title: "Merge proposals"
source: https://elevenlabs.io/docs/eleven-agents/operate/merge-proposals.md
path: docs/eleven-agents/operate/merge-proposals
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Merge proposals

## Overview

A merge proposal records a request to merge one [branch's](/docs/eleven-agents/operate/versioning#branches) changes into another and lets a teammate review the diff before that happens. Anyone with edit access to the agent can open a proposal, even into a branch they cannot merge into themselves. Merging the proposal still requires write access to the target branch, so a proposal is how a change reaches a protected branch without giving every contributor merge rights on it.

> **Note**
>
> Merge proposals add an optional review step on top of [merging branches directly](/docs/eleven-agents/operate/versioning#merging-branches). Merge directly when you have
> write access to the target branch and don't need a second opinion. Open a proposal when you want
> one reviewed first, or when the target branch is protected and you don't have write access to it.

## Availability

Merge proposals are in alpha. When several branches of an agent are in progress at once, it becomes hard to track which ones are ready and safe to merge. Merge proposals give a team one place to review and discuss a branch's changes, compare test pass rates between branches, and look at the branch's latest conversations.

The alpha is a first step toward a CI/CD-style workflow for agents, similar to pull requests on GitHub. Planned additions over the coming weeks include:

* Required tests that must pass before a proposal can be merged.
* Requesting approvals from specific reviewers.
* Configuring owners for different parts of an agent.

## Proposal lifecycle

Every proposal has one of these statuses:

| Status | Meaning                                                                                                            |
| ------ | ------------------------------------------------------------------------------------------------------------------ |
| Open   | Waiting for review or merge.                                                                                       |
| Merged | The source branch's changes were merged into the target branch.                                                    |
| Closed | Withdrawn by the author, rejected by someone else, or closed automatically because the source branch was archived. |

While a proposal is open, reviewers leave one of these verdicts. A reviewer's latest verdict replaces any earlier one from that same reviewer:

| Review state      | Meaning                                                           |
| ----------------- | ----------------------------------------------------------------- |
| Approved          | The reviewer is satisfied with the changes.                       |
| Changes requested | The reviewer wants something addressed before this can be merged. |

## Opening a proposal

Open a proposal from the branch whose changes you want reviewed:

#### From the branch list

In the agent's **Branches** tab, open the options menu on the source branch and select **Open
merge proposal**.

![Open merge proposal option in a branch's options menu](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/5216047fc93408959d31bba118e0f0e8853129da106a9d75c00d57a2307e33e0/assets/images/agents/merge-proposal-open-from-branch-list.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260925%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260925T233147Z&X-Amz-Expires=604800&X-Amz-Signature=8e0fa19b45d1515ab20101f531c252c5403c3b9b879dec62d312d655ebc0409f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### From the Proposals tab

In the agent's **Branches > Proposals** tab, select the source branch, then click **Create
proposal**.

![Proposals tab on an agent's Branches page](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/bfdb23ad1edb31c89c2ff2a137fa3028bf3f9fbcf31e236de142e207b5d54cd0/assets/images/agents/merge-proposals-list.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260925%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260925T233147Z&X-Amz-Expires=604800&X-Amz-Signature=041944e374df12282745cadf9cf4316c1ea5612e1f54b1040cc753708bbd0e27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Give the proposal a title, an optional description, and pick a target branch from the agent's other non-archived branches. Opening a proposal does not change either branch; it only records the request.

> **Note**
>
> A source and target branch pair can have at most one open proposal at a time. Close the existing
> one before opening another between the same two branches.

## Reviewing a proposal

A proposal's page has these tabs:

#### Overview

The description, review history, and a form for leaving a review.

![Overview tab of a merge proposal](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/44894b2d2cbb79aeff99813f83d5832ab4a9e6ff44796c772e3681c69120b04c/assets/images/agents/merge-proposal-overview.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260925%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260925T233147Z&X-Amz-Expires=604800&X-Amz-Signature=a30e7419d59ba3c77a6c1af9a9fa0cec04248dfe917587b448035913e5fe0a34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Changes

A diff between the source and target branch configurations.

![Changes tab of a merge proposal](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/968126763b1bb7e5bf57ad68ee334d5d5bc64b43a7ce3006184a462ce0c3d929/assets/images/agents/merge-proposal-changes.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260925%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260925T233147Z&X-Amz-Expires=604800&X-Amz-Signature=260f7c395560fadf6261baa0e5a110e7bbc3c986513901beef69b373436ee9dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Test runs

The source branch's test history, so reviewers can check it still passes before approving.

![Test runs tab of a merge proposal](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/a39354598b070cef39720159b84da10414d7b17820c8c71780ed2bd5a66a47fc/assets/images/agents/merge-proposal-test-runs.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260925%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260925T233147Z&X-Amz-Expires=604800&X-Amz-Signature=acb085e5c387bda3d3bd18727565ee6a2308606147c77924fd94b7d8dd690c9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Conversations

Recent conversations on the source branch.

![Conversations tab of a merge proposal](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/c37286e50107428225c57804a8bc8e09fe364b1ad6dc6cf582084dd8c52a6565/assets/images/agents/merge-proposal-conversations.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260925%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260925T233147Z&X-Amz-Expires=604800&X-Amz-Signature=5cb8056c45b49f49df8b12ccb4d2efc764396ef5f33e6b4b0da600abe0949174&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Anyone with edit access to the agent, other than the proposal's own author, can leave a review with an optional comment. Comments support markdown.

## Merging a proposal

Merging a proposal performs the same [branch merge](/docs/eleven-agents/operate/versioning#merging-branches) as merging directly, including [conflict resolution](/docs/eleven-agents/operate/versioning#resolving-merge-conflicts) and the option to archive the source branch afterward. Before it can be merged, a proposal must meet these requirements:

* The merging user has write access to both the source and target branches. On a [protected branch](/docs/eleven-agents/operate/versioning), that means being a workspace admin.
* No reviewer's latest verdict is "changes requested". A reviewer who requested changes must approve before the proposal can be merged.
* The proposal has at least one approval from someone other than its author. Workspace admins can merge without this approval.

Merging a proposal automatically closes any other open proposal for the same source branch, since its changes have now moved on.

## Closing a proposal

A proposal can be closed without merging at any point while it's open. The author and reviewers can edit its title and description up until it's closed.

* The author closing their own proposal records it as **withdrawn**.
* Anyone else closing it records it as **rejected**.
* Archiving the source branch closes any open proposal from or to it automatically, recorded as **branch\_archived**.

## Merge proposals and Architect

[Architect](/docs/eleven-agents/operate/architect) has read access to an agent's branches when you [ask it about branches, versions, and merges](/docs/eleven-agents/operate/architect/how-it-works#what-architect-can-see), so it can help you understand a proposal's diff or summarize open reviews in a conversation.

## Next steps

#### [Versioning](/docs/eleven-agents/operate/versioning)

Branches, versions, and direct merging.

#### [Architect](/docs/eleven-agents/operate/architect)

The assistant built into ElevenAgents for iterating on an agent.

#### [Triage](/docs/eleven-agents/operate/triage)

Review conversation issues flagged for follow-up.

#### [Experiments](/docs/eleven-agents/operate/experiments)

Run A/B tests using branches and traffic deployment.
