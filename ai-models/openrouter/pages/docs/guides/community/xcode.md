---
title: "Xcode"
source: https://openrouter.ai/docs/guides/community/xcode.md
path: docs/guides/community/xcode
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Xcode

> Using OpenRouter with Apple Intelligence in Xcode

## Using Xcode with Apple Intelligence

[Apple Intelligence](https://developer.apple.com/apple-intelligence/) in Xcode 26 provides built-in AI assistance for coding. By integrating OpenRouter, you can access hundreds of AI models directly in your Xcode development environment, going far beyond the default ChatGPT integration.

This integration allows you to use models from Anthropic, Google, Meta, and many other providers without leaving your development environment.

### Prerequisites

> [!WARNING]
>
> Apple Intelligence on Xcode is currently in Beta and requires:
>
> * **macOS Tahoe 26.0 Beta** or later
> * **[Xcode 26 beta 4](https://developer.apple.com/download/applications/)** or later

### Setup Instructions

#### Step 1: Enable Apple Intelligence

Navigate to **macOS Settings > Apple Intelligence & Siri** and make sure **Apple Intelligence** is turned on. This is required before Xcode can use any AI model providers.

![Apple Intelligence & Siri Settings](https://mintcdn.com/openrouter-d02e98a0/PSwwwiCqAD_BNeni/assets/guides/community/xcode/xcode-setup-1.png?fit=max\&auto=format\&n=PSwwwiCqAD_BNeni\&q=85\&s=3f626fa13ad09eb3a56409de15a3306e)

#### Step 2: Open Xcode Intelligence Settings

Open **Xcode > Settings > Intelligence** and click **Add a Chat Provider** at the bottom of the page.

![Xcode Intelligence Settings](https://mintcdn.com/openrouter-d02e98a0/PSwwwiCqAD_BNeni/assets/guides/community/xcode/xcode-setup-1b.png?fit=max\&auto=format\&n=PSwwwiCqAD_BNeni\&q=85\&s=ac7c8256fc028811eaba7e971b8a89a4)

#### Step 3: Configure OpenRouter Provider

In the dialog that appears, enter the following details:

* **URL**: `https://openrouter.ai/api`
  * **Important**: Do not add `/v1` at the end of the endpoint like you typically would for direct API calls
* **API Key Header**: `Authorization`
* **API Key**: `Bearer YOUR_API_KEY_HERE` (replace `YOUR_API_KEY_HERE` with your OpenRouter API key that starts with `sk-or-v1-`)
* **Description**: `OpenRouter` (or any name you prefer)

Click **Add** to save the configuration.

![OpenRouter Configuration](https://mintcdn.com/openrouter-d02e98a0/PSwwwiCqAD_BNeni/assets/guides/community/xcode/xcode-setup-2.png?fit=max\&auto=format\&n=PSwwwiCqAD_BNeni\&q=85\&s=a92d81faf97d7f0f0f9076493e9c66d1)

#### Step 4: Browse Available Models

Once configured, click on **OpenRouter** to see all available models. Since OpenRouter offers hundreds of models, you should bookmark your favorite models for quick access. Bookmarked models will appear at the top of the list, making them easily accessible from within the pane whenever you need them.

![Available Models](https://mintcdn.com/openrouter-d02e98a0/PSwwwiCqAD_BNeni/assets/guides/community/xcode/xcode-setup-3.png?fit=max\&auto=format\&n=PSwwwiCqAD_BNeni\&q=85\&s=56a9c029ef15ef81538a6f6133c1b5dd)

You'll have access to models from various providers including:

* Anthropic Claude models
* Google Gemini models
* Meta Llama models
* OpenAI GPT models
* And hundreds more

![Extended Model List](https://mintcdn.com/openrouter-d02e98a0/PSwwwiCqAD_BNeni/assets/guides/community/xcode/xcode-setup-4.png?fit=max\&auto=format\&n=PSwwwiCqAD_BNeni\&q=85\&s=956122de5ac17b8bf4bc5030fe5eabd1)

#### Step 5: Start Using AI in Xcode

Head back to the chat interface (icon at the top) and start chatting with your selected models directly in Xcode.

![Xcode Chat Interface](https://mintcdn.com/openrouter-d02e98a0/PSwwwiCqAD_BNeni/assets/guides/community/xcode/xcode-setup-5.png?fit=max\&auto=format\&n=PSwwwiCqAD_BNeni\&q=85\&s=b83c25958625d578551ce5812ef79be9)

### Using Apple Intelligence Features

Once configured, you can use Apple Intelligence features in Xcode with OpenRouter models:

* **Code Completion**: Get intelligent code suggestions
* **Code Explanation**: Ask questions about your code
* **Refactoring Assistance**: Get help improving your code structure
* **Documentation Generation**: Generate comments and documentation

![Apple Intelligence Interface](https://mintcdn.com/openrouter-d02e98a0/PSwwwiCqAD_BNeni/assets/guides/community/xcode/xcode-setup-6.png?fit=max\&auto=format\&n=PSwwwiCqAD_BNeni\&q=85\&s=c787766f34817b5220fe389f117234fb)

*Image credit: [Apple Developer Documentation](https://developer.apple.com/documentation/Xcode/writing-code-with-intelligence-in-xcode)*

### Learn More

* **Apple Intelligence Documentation**: [Writing Code with Intelligence in Xcode](https://developer.apple.com/documentation/Xcode/writing-code-with-intelligence-in-xcode)
* **OpenRouter Quick Start**: [Getting Started with OpenRouter](https://openrouter.ai/docs/quickstart.md)
* **Available Models**: [Browse OpenRouter Models](https://openrouter.ai/models)

