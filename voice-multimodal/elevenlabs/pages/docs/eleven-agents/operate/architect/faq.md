---
title: "Limitations and FAQ"
source: https://elevenlabs.io/docs/eleven-agents/operate/architect/faq.md
path: docs/eleven-agents/operate/architect/faq
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Limitations and FAQ

## Known limitations

* **No scheduled or background work yet.** ElevenAgents Architect only works while you're in a conversation with it. It doesn't yet scan agents on a schedule, send reports, or open proposals on its own. Scheduled automations are coming soon. See [Proactive proposals](/docs/eleven-agents/operate/architect/proposals#proactive-proposals) for the current path from Spotlight to a proposal.
* **It can't review merge proposals.** Architect can open a proposal and suggest reviewers, but approving, commenting, merging, and closing are done by people.
* **Some resources are read-only to Architect.** It can't manage MCP servers, secrets, integrations, channels, alerts, or phone number assignments. See [What Architect can't do](/docs/eleven-agents/operate/architect/capabilities#what-architect-cannot-do).
* **Dashboards aren't saved.** A dashboard built in the chat keeps its data only in the browser tab where it was built.
* **Chats are private.** You can't share an Architect chat with a teammate. Share the result instead, such as a merge proposal or a triage ticket comment.

## FAQ

#### What's the difference between Spotlight and Architect?

Spotlight observes and recommends: it monitors your agent's conversations and surfaces
summaries, suggested investigations, alerts, and recommendations. Architect builds and fixes: it
investigates a question or a Spotlight finding, changes the agent, tests the change, and
prepares it for your review. Spotlight cards hand off to Architect with **Analyze with
Architect** and **Investigate with Architect**.

#### Can Architect change my live agent without me knowing?

Not through the agent's configuration. Architect stages configuration changes in your draft, and
only you can publish a draft. In the default **Approval required** mode, it also asks before
actions that affect live traffic or shared resources, such as merging a branch, changing the
traffic split, or updating a tool. In **Auto-approve** mode it doesn't ask before those actions,
so use that mode only for work you are confident about. See [Permissions, approvals, and drafts](/docs/eleven-agents/operate/architect/authentication).

#### Where do I find the proposal Architect made?

Open the agent and go to **Version Control** > **Proposals**. Architect also posts a link to the
proposal in the conversation. The proposal lists you as its author, because Architect acts as
you.

#### Why can't I approve a proposal Architect opened for me?

Architect acts as you, so you are the proposal's author, and authors can't review their own
proposals. A teammate with editor access has to approve it. Workspace admins can merge without
an approval.

#### Does merging a proposal deploy it?

Yes. There's no separate publish step after a merge. The merged version serves live traffic
immediately for whatever share of traffic the target branch receives. See [What happens on merge](/docs/eleven-agents/operate/architect/proposals#what-happens-on-merge).

#### Can Architect work on more than one agent?

Yes. It works on the agent you have open by default, but it can read and edit any agent you have
access to. Use the workspace Architect page (**Agents** > **Architect**) for questions that span
agents.

#### Can Architect do something my role doesn't allow?

No. Architect runs as you, with your permissions. If you can't edit an agent or merge into a
protected branch, neither can Architect.

#### Does Architect test its changes before showing them to me?

Architect writes tests and simulations and runs them in the conversation as part of building a
change, before it asks you to publish. To be certain a fix is verified, ask Architect to show
the new tests failing without the change and passing with it. Results also appear on the
proposal's **Test runs** tab.

#### Can I talk to Architect out loud?

Yes. In an open chat with an empty composer, select **Talk to agent** to start a voice
conversation. You can also dictate messages in any composer by holding <kbd>Cmd</kbd>/
<kbd>Ctrl</kbd>+<kbd>.</kbd>.

#### Is Architect the same as the ElevenLabs MCP server?

No, but they call the same APIs. Architect runs in the dashboard, stages changes in drafts, and
uses its own approval modes. The MCP server lets external assistants such as Claude and Cursor
manage your agents, applies changes directly, and relies on your client's tool approvals. See
[Claude, Cursor, and other AI assistants](/docs/eleven-agents/operate/architect/external-assistants).

#### How much does Architect cost?

Architect is free during the alpha, which runs through October 2026. Usage doesn't count against
your workspace's agent minutes or LLM cost. Check the [pricing page](https://elevenlabs.io/pricing) for terms after the alpha ends.

#### How do I give feedback on Architect?

Rate a response with the thumbs up or down under it, use **Feedback** in the sidebar chat header
to rate the session, or type `/feedback` in the sidebar chat.
