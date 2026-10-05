---
title: "Starting a conversation"
source: https://elevenlabs.io/docs/eleven-agents/operate/architect/entry-points.md
path: docs/eleven-agents/operate/architect/entry-points
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Starting a conversation

## Overview

You can open ElevenAgents Architect from many places in ElevenAgents. Where you start a conversation decides the context Architect has from its first message. A conversation opened from a failed test already knows which tests failed. One opened from a Spotlight alert already knows which alert fired.

Architect runs in two placements:

* **Sidebar**: a panel available across the whole ElevenLabs app. It can see the page you are on and help you navigate it.
* **Architect tab**: a full-screen view, either for a single agent (**Agents** > your agent > **Architect**) or for the whole workspace (**Agents** > **Architect** in the left navigation).

Both placements have the same agent-building tools. The sidebar additionally sends Architect a snapshot of the page you are viewing. The full-screen tab adds a live plan panel when you use [Plan mode](/docs/eleven-agents/operate/architect/how-it-works#plan-mode).

## General entry points

These open Architect without specific context beyond the page you are on.

| Entry point          | Where                                                                                                                                 | What it passes                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Architect** button | The page header across ElevenAgents, and the header of detail panels for conversations, tools, and knowledge base items               | Opens the sidebar, or reopens your current chat. In the sidebar, Architect sees the page you are on.                                              |
| **Ask Architect**    | The floating composer at the bottom of ElevenAgents pages, on desktop                                                                 | Your typed message and any `@` references. It also shows suggested questions for the current page, which you can send with one click.             |
| Architect tab        | **Agents** > your agent > **Architect**                                                                                               | Your message, scoped to that agent. Suggested prompts are grouped by area: Agent, Procedures, Tools, Knowledge Base, Tests, Analysis, Guardrails. |
| Workspace Architect  | **Agents** > **Architect** in the left navigation                                                                                     | Your message, scoped to the whole workspace rather than one agent.                                                                                |
| Command palette      | Press <kbd>Cmd</kbd>+<kbd>K</kbd> (macOS) or <kbd>Ctrl</kbd>+<kbd>K</kbd> (Windows and Linux), type a request, and select **Ask "…"** | Your typed text as the first message. With an agent open, the palette also lists that agent's suggested prompts.                                  |
| Chat history         | The history list in the sidebar                                                                                                       | Reopens a previous chat with its message history.                                                                                                 |
| **Troubleshoot**     | The button on an error notification                                                                                                   | The error message, with a request to help resolve it.                                                                                             |

![Architect header button](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/d60a7dc0778e4b7743c84904e51ab0395a39508bf4cc2d5231e51a1605e0832e/assets/images/agents/architect-entry-header-button.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261005T230230Z&X-Amz-Expires=604800&X-Amz-Signature=e2078e91b65927e9a4854e85e99ef9ad35215464aaf9b85bf89ee9b6da415369&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Command palette](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/1e799dfc1c1600d78a2465dd6265cd2905d646f7b2b2dd7c5c9d81bb4195eea0/assets/images/agents/architect-entry-command-palette.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261005T230230Z&X-Amz-Expires=604800&X-Amz-Signature=22e4f0b3ccd77c5fa96c97036cf25871f8255887987d7ca422a641b1cbb60f62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Entry points with context

These entry points start a new conversation with a prepared first message and hidden context, so you don't have to explain the situation.

### Failed tests

When a test run has failures, **Fix with Architect** appears on the test run details and next to failing test groups. It offers three options:

* **Explain why this test failed** (or **Summarize why these tests failed** for several).
* **Suggest fixes to pass the test** (or **Suggest fixes to address the failures**). Architect groups fixes by root cause.
* **Start a new conversation**, with no context.

Architect receives the test run's invocation ID and the names of the failing tests. It reads the failure details, transcripts, and evaluation results itself with its test tools, so the answer reflects the full run.

![Failed test with Fix with
Architect](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/4233cb4faf8238cca926fbfdae052013e229777e693a2c8067751f7cca431f57/assets/images/agents/architect-entry-fix-with-architect.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261005T230230Z&X-Amz-Expires=604800&X-Amz-Signature=86ed0899525bf00eb51088e6f412af7011fce1dd4caa3c4141b7e202f1448ef9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Spotlight

[Spotlight](/docs/eleven-agents/dashboard/spotlight), the agent's overview page, hands findings to Architect from several cards.

| Card                  | Button                                                         | What Architect receives                                                                                                                                                                           |
| --------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Weekly summary        | **Analyze**, or **Analyze with Architect** in the full summary | The summary text and its date range. Architect is instructed to verify the summary's claims against real conversations first, and to work out which branch is affected, before proposing changes. |
| Suggested next steps  | **Open in Architect** on each suggestion                       | That suggested investigation, the context Spotlight gathered for it, and the weekly summary.                                                                                                      |
| Real-time alert       | **Investigate with Architect**, or **Investigate & fix**       | The alert's ID and what it monitors. Architect reads the alert, checks whether it is noise, and finds the affected branch before suggesting a fix.                                                |
| No tests attached     | **Add tests**                                                  | A request to set up the agent's first tests.                                                                                                                                                      |
| Convert to procedures | **Convert**                                                    | A request to convert the agent's system prompt into [procedures](/docs/eleven-agents/customization/procedures).                                                                                   |

Charts and metric tiles on Spotlight don't have their own Architect button. To ask about a specific chart, open Architect from the page header: in the sidebar, Architect can read the values on screen.

![Weekly summary](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e59d75a18fcad464fcbf92afc711eee6ef832ea86477190b6870d89cc0197aeb/assets/images/agents/architect-entry-spotlight-weekly-summary.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261005T230230Z&X-Amz-Expires=604800&X-Amz-Signature=a45330f6c04d2948d1a041efc2743e61d85e80541f050f81ac58cdd093ed524a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Alert card with Investigate with
Architect](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e71b18a2ac615b122870d69257575462ab416b154bc9d6d4bfd3d0864e1b81e9/assets/images/agents/architect-entry-spotlight-alert.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261005T230230Z&X-Amz-Expires=604800&X-Amz-Signature=b839f34b1fb5df9f12101f30e1b57f8a4d25e0057bd6084ec3d5b76d2731c134&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Triage tickets

In a [triage ticket](/docs/eleven-agents/operate/triage), select **Discuss with Architect**. Architect receives the conversation ID, the flagged issue or review comment, any comments on specific turns, and the ticket's discussion thread. It reads the transcript, explains what went wrong, suggests fixes, and offers to comment on the ticket and mark it resolved when you're done.

A ticket records every Architect chat started from it. Once you have started one, the button changes to **Continue in Architect** and **New Architect chat**. Chats stay private to the person who started them. In the triage list, a ticket with an Architect chat shows who dispatched Architect.

![Triage ticket with Architect](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/7327710426954b013a17073554ce183de64a322eeab78e458e30d9da6c0b470f/assets/images/agents/architect-entry-triage-ticket.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261005T230230Z&X-Amz-Expires=604800&X-Amz-Signature=152286f03f51b879b80e728766a8200fc4b26a8e84f83d5a5555706207d3ec27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Triage list with Architect](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/b4dccefa125d457ab5f5deedabd8be75255ce1ec2206607c172673a46492205a/assets/images/agents/architect-entry-triage-list.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261005T230230Z&X-Amz-Expires=604800&X-Amz-Signature=ee28c71255361cb4d8f51305a415d4d6bf050b623326ef6881bfc018824dacdd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Conversation transcripts

In a conversation's transcript, select **Analyze** on an agent message, or the **Analyze with Architect** icon in the history view. Architect receives the conversation ID and the text of that message, and explains why the agent responded the way it did.

![Analyze on an agent message](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3ba13985b69854baaa770393be1c2d654ad02a1c1e8001b73a46ecad04cb7b62/assets/images/agents/architect-entry-transcript-analyze.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261005T230230Z&X-Amz-Expires=604800&X-Amz-Signature=7d9ac0230351025edf5edcc69a859de1bd8d02e2675800065f1eb5ec58bf60b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Building an agent

* **Create with Architect**, in the new agent flow, starts a guided conversation: Architect asks about the job the agent has to do, one question at a time, then builds the agent and writes its [agent context](/docs/eleven-agents/operate/architect/customization#agent-context).
* **Draft with Architect**, in the **Add** menu on the procedures page, creates an empty procedure and asks Architect to write it.
* **Complete with Architect**, on each item of the Architect tab's deployment checklist, sends a request such as "Help me set up guardrails".
* **Set up with Architect**, on the agent context and preferences editors, runs the `/start` command.
* **Run**, on a saved prompt in the [prompt library](/docs/eleven-agents/operate/architect/customization#prompt-library), starts a conversation with that prompt.

### Suggestions after you act

After some actions, such as creating a test or a tool by hand, a notification may suggest a related request for Architect, for example "Look at my agent and suggest the 3 most important tests it should have, then write them for me." Select **Try Architect** to send it. Dismiss the suggestion to hide it.

## Referencing resources and commands

* Type `@` in the composer to reference a specific agent, tool, test, procedure, or knowledge base topic. Architect receives the referenced resource directly instead of searching for it.
* Type `/` to see slash commands, such as `/debug`, `/test`, `/review`, and `/dashboard`. See [How Architect works](/docs/eleven-agents/operate/architect/how-it-works#slash-commands) for the full list.
* Select **+** > **Use a saved prompt** to insert a prompt from your library.

## Keyboard shortcuts

| Shortcut                                             | Action                                                               |
| ---------------------------------------------------- | -------------------------------------------------------------------- |
| <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>K</kbd>          | Open the command palette and ask Architect.                          |
| Hold <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>.</kbd>     | Dictate a message. Release to stop.                                  |
| Hold <kbd>Space</kbd> in an empty composer           | Dictate a message.                                                   |
| <kbd>Shift</kbd>+<kbd>Tab</kbd>                      | Cycle the approval mode: Approval required, Auto-approve, and Plan.  |
| <kbd>Enter</kbd> / <kbd>Shift</kbd>+<kbd>Enter</kbd> | Send / insert a new line.                                            |
| <kbd>Esc</kbd>                                       | Cancel a dictated message before it sends, or collapse the composer. |

## Talking to ElevenAgents Architect

You can use your voice with Architect in two ways:

* **Dictation**: select the microphone in any Architect composer, or hold <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>.</kbd>. Your speech is transcribed into the composer and sent automatically after a short countdown, which you can cancel with <kbd>Esc</kbd>.
* **Voice conversation**: in an open chat with an empty composer, the send button becomes an audio button labeled **Talk to agent**. Select it to speak with Architect out loud. Architect answers in voice and keeps using its tools. Select **End conversation** to return to text.

Voice conversations are available in an open sidebar or full-screen chat. The floating composer and the Architect tab home page support dictation only.
