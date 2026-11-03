---
title: "Reuse instructions and delegate work"
source: https://developers.notion.com/guides/mcp/tools-skills-agents
path: guides/mcp/tools-skills-agents
---

Use shared Skills to repeat tasks with your AI assistant, or delegate work to Custom Agents your team can access in Notion.

Help your team repeat work without starting from scratch. Skills and Custom Agents are resources you can share across your Notion workspace: a Skill gives your AI assistant instructions to follow, while a Custom Agent can take on work you delegate.

Use a shared Skill to prepare a project update in your team’s format, or hand the task to a Custom Agent and review its results. Teammates with access can reuse the same instructions and agents in their own work.

## Try a prompt

> [tab] Use a shared Skill
>
> Find our team’s project update Skill in Notion. Follow its instructions to draft this week’s update using our project notes, and show me the draft for review.
>
> Find our team’s project update Skill in Notion. Follow its instructions to draft this week’s update using our project notes, and show me the draft for review.

> [tab] Delegate to a Custom Agent
>
> Find our reporting Custom Agent in Notion and ask it to prepare this week’s project update. Share the project context from our conversation, then bring back the agent’s draft for me to review.
>
> Find our reporting Custom Agent in Notion and ask it to prepare this week’s project update. Share the project context from our conversation, then bring back the agent’s draft for me to review.

## Personal memories

Memories let your AI assistant save preferences, corrections, and decisions in Notion and recall them in later sessions. You can use them across clients connected to the same Notion account and workspace. Ask your assistant to remember the context you want to save; connecting MCP doesn't automatically import another client's chat history.

Notion stores this context in a personal **Memories** database and an **About page** that summarizes it. Both are created when you save your first memory. You can read, edit, or remove this information in Notion. Memories are private to you. They don't grant a client access to content you can't already access, and they don't replace current source information.

Memory via MCP is available on all plans through user-backed connections, with memories enabled for both you and your workspace. It isn't available through workspace-owned connections. See [View your Notion Agent Memories](https://www.notion.com/help/view-your-notion-agent-memories) for user controls and privacy details, or the [memory tool reference](/guides/mcp/tools-skills-agents-reference#search-personal-memories) for reading, saving, and updating memories.

## Available tools

| Action | What it does | Tool name |
| - | - | - |
| Create a Skill from a page | Turn an existing instructions page into a Notion Skill. | [`notion-convert-page-to-skill`](/guides/mcp/tools-skills-agents-reference#convert-a-page-to-a-skill) |
| Download a Skill | Export a Skill and its supporting files. | [`notion-download-skill`](/guides/mcp/tools-skills-agents-reference#download-a-notion-skill) |
| Upload a Skill | Import a Skill into a page in a Skills database. | [`notion-upload-skill`](/guides/mcp/tools-skills-agents-reference#upload-a-notion-skill) |
| Choose your Skills | See enabled Skills and enable or disable them. | [`notion-get-enabled-skills`](/guides/mcp/tools-skills-agents-reference#manage-enabled-skills)  [`notion-update-enabled-skills`](/guides/mcp/tools-skills-agents-reference#manage-enabled-skills) |
| Find saved context | Search your private memories for preferences and decisions saved by your connected agents. | [`notion-memory-search`](/guides/mcp/tools-skills-agents-reference#search-personal-memories) |
| Find Custom Agents | Find an agent shared with you that can take on a task. | [`notion-search-agents`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions) |
| Find agent conversations | Browse or search existing sessions. | [`notion-query-sessions`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions)  [`notion-search-sessions`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions) |
| Delegate or follow up | Hand a task to a Custom Agent or send a follow-up message. | [`notion-spawn-session`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions)  [`notion-send-message-to-session`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions) |
| Check or stop work | Check progress, wait for a response, or stop a run. | [`notion-get-session-status`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions)  [`notion-wait-session`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions)  [`notion-stop-session`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions) |
| Read session activity | List and read events from an agent session. | [`notion-list-session-events`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions)  [`notion-read-session-event`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions) |

## Things to know

Sharing a Skill or Custom Agent does not make it available to everyone automatically; teammates need access to use it. Enabling a Skill changes your own settings, not your teammates’ settings. Converting a page into a Skill keeps its instructions unchanged; uploading a Skill replaces the target page’s content. Working with Custom Agents requires Notion AI access and access to Custom Agents.

## Technical reference

See the [technical reference](/guides/mcp/tools-skills-agents-reference) for parameters, response formats, requirements, and examples for these tools.
