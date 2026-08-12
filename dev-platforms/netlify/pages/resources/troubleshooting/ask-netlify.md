---
title: "Netlify Support"
source: https://docs.netlify.com/resources/troubleshooting/ask-netlify.md
path: resources/troubleshooting/ask-netlify
---

---
title: "Ask Netlify overview"
description: "Leverage the latest Large Language Model (LLM) technologies to find information faster while using Netlify."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Our Ask Netlify AI chatbot assistant can help you find the answers you need to be successful using Netlify.

### Button Component:

Start a conversation

Ask Netlify AI is built-in to docs search and offers answers based on the following sources: 
- product documentation
- Support Forums
- blog
- CLI documentation
- API documentation

![Ask Netlify icon](/images/ask-netlify-in-search-bar.png)

Ask Netlify AI cannot give you specific information about your Netlify account and projects, even if you share your Deploy ID, site ID, or project ID.

You may need to ask a human for specific support. Learn more about common reasons to reach out to the [Netlify Support team](https://www.netlify.com/support).

### Caution - AI-generated content disclaimer

This experimental feature uses artificial intelligence (AI) to provide you with efficient access to information about Netlify. However, it may not always understand the full context of your query or produce a reliable, accurate answer. When in doubt, please refer to our [documentation](/) or other [help resources](/resources/troubleshooting/overview).

### Tip - Sometimes you need to ask a human

If you're having trouble logging in, need a Netlify project transfer or DNS transfer, or are encountering fraud, [contact the support team](https://www.netlify.com/support#contact) instead.

## Access and use the feature

To access the generative AI chatbot: 
- Open the Search icon on the docs site. The Ask Netlify AI assistant is available in the search bar.
    ![Ask Netlify icon](/images/ask-netlify-in-search-bar.png)

- Alternatively, set up the [Netlify App for Slack](/extend/install-and-use/setup-guides/netlify-app-for-slack) and enter `@Netlify` in any public or private Slack channel where the Netlify App is added.

Use Ask Netlify to ask about how to get started, troubleshoot an issue, or find more information about how to use a specific feature.

For example:

- "How do I protect my project behind a password?"
- "How can I rollback my project to a previous version?"
- "What's the difference between Functions and Edge Functions?"
- "How do I install the Netlify CLI?"

You can submit a follow-up query after your initial prompt to gather additional information.

## How it works

We use all of the content from this [docs site](/), our [CLI reference](https://cli.netlify.com/), [tutorials](https://www.netlify.com/blog/tutorials), other recent content from our blog, and selected posts from our [Support Forums](https://answers.netlify.com/). We then make requests to the OpenAI API with this context so the answers are limited to Netlify topics.

### User information

If you log in with your Netlify user ID and submit questions, we log your Netlify user ID and the questions you submit with the Ask Netlify feature. Gathering this data helps us improve our docs and our product overall.

Your user ID is not shared with OpenAI or any third-party as part of this feature. Your questions are sent to the OpenAI API along with additional context from our docs to generate the most relevant response.

### Privacy

Use of Ask Netlify is subject to Netlify's [privacy policy](https://www.netlify.com/privacy/).

### Caution - Don't submit sensitive data

Sensitive personal data should not be submitted to Ask Netlify. This includes text or other data containing or revealing government-issued identification numbers; financial information such as credit or debit card numbers, any related security codes or passwords, and bank account numbers; personal information such as racial or ethnic origin, political opinions, religious or philosophical beliefs, trade-union membership, information concerning health or sex life; information related to an individual's physical or mental health; and information related to the provision or payment of health care.

## Provide feedback

We welcome your feedback or additional questions about this feature. You can share your thoughts in the form at the end of this page or by posting to our [Support Forums](https://answers.netlify.com/).

## Ask a human 

Sometimes you just need to ask a human. You can reach out to our [Netlify Support](https://www.netlify.com/support) team for specific help. 

Common issues that require human assistance include:
- issues with logging in 
- account or DNS transfers
- fraud
- billing issues
