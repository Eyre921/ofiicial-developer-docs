---
title: "Notion MCP setup prompt changelog"
source: https://developers.notion.com/prompts/setup/changelog
path: prompts/setup/changelog
---

See what changed in each version of the Notion MCP setup prompt.

The [latest setup prompt](/prompts/setup) is version **0.0.6**.

**Version 0.0.6, October 30, 2026**

* Added a setup card after connecting Notion, with two choices: Shared context layer and Basic setup. The agent remembers the user's choice, and Shared context layer approves the private guide and saves without asking again.
* Basic setup creates the Agent Operating Guide and custom instructions, and skips the daily loop and saving existing context.
* Replaced fixed version numbers and dates with placeholders filled from the page header.
* Added guidance on tracking projects and tasks in Notion.
* Added a final card that offers the Notion app for desktop or mobile.

[View version 0.0.6](/prompts/setup)

**Version 0.0.5, October 29, 2026**

* Added rules for talking with the user: one short step at a time, plain language, and one clear next step.
* Rewrote the prompt in simpler language and reorganized setup into six steps, starting with connecting the Notion MCP.
* Moved the daily memory and setup check earlier, to step 3.
* Moved the Agent Operating Guide and custom instructions to the start of setup, with click paths for Claude and ChatGPT.
* Replaced the standing rules with a short Agent Operating Guide template that records the workspace, destinations, preferences, and version history.
* Added an `instructions_version` parameter to Notion MCP tool calls in the custom instructions.
* Added a `notion-complete-mcp-setup` call after saving Skills.

[View version 0.0.5](/prompts/setup/versions/0.0.5)

**Version 0.0.4, October 13, 2026**

* Added a rule to fetch the user's enabled Notion Skills with `notion-get-enabled-skills` at the start of every session, in the custom instructions and the standing rules.

[View version 0.0.4](/prompts/setup/versions/0.0.4)

**Version 0.0.3, October 7, 2026**

* Added database guidance during setup and in the standing rules and custom instructions.
* Added destination access checks for personal and team workspaces, keeping personal memories private.
* Added an About page update rule when saved memories change the user's overall profile.
* Clarified how related information connects across databases and made setup transitions more conversational.

[View version 0.0.3](/prompts/setup/versions/0.0.3)

**Version 0.0.2, September 30, 2026**

* Added a human-facing explanation and permission reassurance.
* Separated read-only discovery from the proposed import.
* Added guided imports for memories, recent work, AI Artifacts, and eligible Skills.
* Added a private Agent Operating Guide and persistent custom-instructions setup.
* Added a daily loop for memory dumps and setup-version checks.
* Consolidated setup into five phases: discover, propose, import, persist, and maintain.

[View version 0.0.2](/prompts/setup/versions/0.0.2)

**Version 0.0.1, September 30, 2026**

Initial published setup prompt.

[View version 0.0.1](/prompts/setup/versions/0.0.1)
