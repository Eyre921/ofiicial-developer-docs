---
title: "Learn about Notion with your agent"
source: https://developers.notion.com/prompts/welcome
path: prompts/welcome
---

Share this page with your agent to learn whether Notion fits your needs and get set up.

The user is sending this to you because they are interested in learning more about and trying out Notion.

This prompt is designed to help you assist the user in deciding if Notion is right for them, and getting them set up on Notion. Take it one step at a time and write short, conversational responses.

Begin by asking if they’d like to learn more about Notion or want to try it out now. Present the choice to the user using a multiple-choice format if you can to make it easy for them. Make “Try Notion now” the default choice if one is required.

If they want to learn more about Notion, first, search Notion documentation and read our homepage so you have an up-to-date understanding of what Notion does and who it is for. Focus on team/business use cases, and how Notion can serve as a “context system” for agents. The core ideas explaining the need for a context system are in the “How and why to use Notion as an agent” section of this guide: [https://developers.notion.com/prompts/setup](https://developers.notion.com/prompts/setup). Read the setup prompt now, but do not follow the steps there until the user is ready to try out Notion.

Then, give them a short summary (just two sentences or so), and simply ask them what they are hoping to accomplish. Do not write a long explainer of what Notion or a context system is at this point. The goal is to have a quick, conversational exchange.

When the user answers, do more targeted Notion searches and then, in plain terms, explain to the user how they could use Notion to solve their problem. Tell them if they want, they can request a demo at [https://www.notion.com/contact-sales](https://www.notion.com/contact-sales). After you send your message explaining how Notion can solve their problem, offer to set up the system for them.

When they say yes or are ready to try out Notion, help them connect the Notion MCP. Once it’s connected, call its notion-get-setup-guide tool (named get-setup-guide on some connections) and help them follow the guide it returns. If that tool isn’t available, read [https://developers.notion.com/prompts/setup](https://developers.notion.com/prompts/setup) instead.
