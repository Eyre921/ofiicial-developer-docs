---
title: "How do I use tools with ElevenAgents?"
source: https://elevenlabs.io/docs/help-center/product/eleven-agents/how-do-i-use-tools-with-eleven-agents.md
path: docs/help-center/product/eleven-agents/how-do-i-use-tools-with-eleven-agents
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How do I use tools with ElevenAgents?

You can connect <strong>Client Tools</strong>, <strong>Webhooks</strong>, or <strong>System Tools</strong> to your agent to enhance its functionality.

<strong>Tools</strong> allow your agent to interact with external data, systems, and the environment
it's running in. You define which tools your agent can use, and it will automatically choose the
appropriate one during a conversation.

<strong>Webhooks</strong> are tools that connect your assistant to external APIs. They’re ideal for
tasks like:

* Booking meetings
* Accessing or updating databases
* Telling the current time
* And much more

This type of tool enables powerful real-time interactions with your services.

<strong>Client Tools</strong> interact directly with the user's browser or device where the agent is
hosted. They’re typically used to:

* Redirect users within your site
* Send on-screen notifications
* Guide users through website flows

These tools help deliver a more integrated and seamless user experience.

<strong>System Tools</strong> are built-in and ready to use as soon as your agent is created. They
handle essential conversation management tasks like:

* Ending a call
* Transferring a call
* Switching languages

These foundational tools ensure your agent can manage core interactions out of the box.

For more information on tool implementation, please see our [ElevenAgents documentation.](/docs/agents-platform/customization/tools)
