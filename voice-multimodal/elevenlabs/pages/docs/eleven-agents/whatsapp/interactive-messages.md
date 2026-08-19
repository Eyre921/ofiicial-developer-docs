---
title: "Interactive messages"
source: https://elevenlabs.io/docs/eleven-agents/whatsapp/interactive-messages.md
path: docs/eleven-agents/whatsapp/interactive-messages
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Interactive messages

## Overview

Instead of asking the user to type an answer, your agent can send WhatsApp **interactive messages**: up to three tappable reply buttons, or a list of up to ten options. The user's tap comes back as their next message, and the agent sees exactly which option was chosen.

Interactive messages work in active WhatsApp message conversations only. They are sent by the agent through two integration tools:

* **Send Interactive Buttons** — up to three reply buttons, for small sets of choices.
* **Send Interactive List** — a tappable list of options grouped into sections, for more than three choices.

Source: [Meta's guide to WhatsApp interactive messages](https://developers.facebook.com/docs/whatsapp/guides/interactive-messages/).

## Enabling the tools

#### Add the WhatsApp integration

Import your WhatsApp business account ([instructions](/docs/eleven-agents/whatsapp)), then go to
the [Integrations page](https://elevenlabs.io/app/agents/integrations), click the ***Add
integration*** button, select WhatsApp and connect your account.

#### Add the tools

Go to the [Tools page](https://elevenlabs.io/app/agents/tools), click the ***Add integration
tool*** button, select the WhatsApp integration, and add the ***Send Interactive Buttons*** and
***Send Interactive List*** tools.

If you have imported more than one WhatsApp account, each has its own WhatsApp integration.
Make sure you add the tools from the integration connected to the account your agent uses —
tools added from a different account's integration will not work for this agent's
conversations.

#### Attach the tools to your agent

Add the tools in your agent configuration. The tools always message the user of the live
conversation — the agent chooses the content, never the recipient.

## Send interactive buttons

**Send Interactive Buttons** presents one to three choices in the current WhatsApp message conversation.

| Parameter     | Required | Description                                                    |
| ------------- | -------- | -------------------------------------------------------------- |
| `body_text`   | Yes      | Message shown above the buttons. Max 1024 characters.          |
| `buttons`     | Yes      | One to three buttons, in display order. Titles must be unique. |
| `footer_text` | No       | Small print shown below the buttons. Max 60 characters.        |

Each button has:

| Field   | Required | Description                                                                  |
| ------- | -------- | ---------------------------------------------------------------------------- |
| `id`    | Yes      | Identifier reported back when the user taps this button. Max 256 characters. |
| `title` | Yes      | Button label. Max 20 characters.                                             |

## Send an interactive list

**Send Interactive List** presents options grouped into sections in the current WhatsApp message conversation. The user opens the list and selects a row.

| Parameter     | Required | Description                                                                                 |
| ------------- | -------- | ------------------------------------------------------------------------------------------- |
| `body_text`   | Yes      | Message shown above the list. Max 4096 characters.                                          |
| `button_text` | Yes      | Label of the button that opens the list. Max 20 characters.                                 |
| `sections`    | Yes      | One to 10 groups of options. A list can contain up to 10 rows across all sections combined. |
| `header_text` | No       | Heading shown above the message body. Max 60 characters.                                    |
| `footer_text` | No       | Small print shown below the list. Max 60 characters.                                        |

Each section has:

| Field   | Required | Description                         |
| ------- | -------- | ----------------------------------- |
| `title` | Yes      | Section heading. Max 24 characters. |
| `rows`  | Yes      | One to 10 options in this section.  |

Each row has:

| Field         | Required | Description                                                                |
| ------------- | -------- | -------------------------------------------------------------------------- |
| `id`          | Yes      | Identifier reported back when the user picks this row. Max 200 characters. |
| `title`       | Yes      | Row label. Max 24 characters.                                              |
| `description` | No       | Secondary text shown under the row label. Max 72 characters.               |

If the agent produces content over a limit, the tool call fails and the agent is told why, so it can retry with shorter content.

## Prompting the agent

Tell the agent in the system prompt when to offer choices. For example:

```text
When you need the user to pick from a fixed set of options (appointment slots,
product variants, yes/no confirmations), use the Send Interactive Buttons tool
for up to 3 options or the Send Interactive List tool for more. Keep option
titles short. Do not use interactive messages for open-ended questions.
```

### Optional: Add a procedure to steer the agent's tool use

Giving the agent the tools is half the work — a [procedure](/docs/eleven-agents/customization/procedures) tells it how to operate them well.

The procedure below is a template, not a drop-in. After copying it, make it yours: adjust the
trigger to your flows, keep only the tools your agent actually has, and rewrite the option
examples and rules to match your use case.

#### Copy the sample procedure

```markdown
---
name: Offer choices with interactive messages
trigger: The user must pick from a fixed set of known options in a WhatsApp message conversation, such as appointment slots, product variants, or order confirmations.
---

Offer the options as an interactive message instead of asking the user
to type an answer.

1. Check which interactive tools you have. Prefer Send Interactive
   Buttons for 2–3 options and Send Interactive List for 4–10. If only
   one of the two is available, use it for any option count that fits its
   limits; if no interactive tool fits, ask the question in plain text.
   Never present more than 10 options; narrow them down with a question
   first.
2. Write a body_text that asks one clear question. Do not stack multiple
   questions into one interactive message.
3. Give every option a stable, machine-readable id (for example
   slot_2026-08-20_10am) and a short human title — 20 characters for
   buttons, 24 for list rows.
4. For lists, group related rows into titled sections, and add a
   description to a row only when its title alone is ambiguous.
5. Send the message with the tool, then wait for the user's reply. Do not
   send a second interactive message before the user responds to the first.
6. Treat the reply as the user's choice. Confirm it back in one short line
   and continue the flow.

Rules:

- Never use interactive messages for open-ended questions.
- When the fixed options may not cover everyone, include a final option
  such as "Something else" and follow up with a free-text question.
- If the tool call fails because content exceeds a limit, shorten titles
  and descriptions and retry once.
- If the user types an answer instead of tapping, accept it — do not
  re-send the options.
```

## Constraints

* Interactive messages can only be sent in **message** conversations — not during WhatsApp voice calls, and not on other channels.
* WhatsApp Flows (interactive forms) are not supported. If a user responds with a Flow reply, it is not passed to the agent.
* Interactive messages are session messages: they can only be sent inside an active conversation, not as the first outbound contact. Use [message templates](/docs/eleven-agents/whatsapp/outbound) to start conversations.
