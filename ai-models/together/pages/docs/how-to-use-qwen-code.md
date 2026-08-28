---
title: "Configure Qwen Code with Together AI models"
source: https://docs.together.ai/docs/how-to-use-qwen-code
path: docs/how-to-use-qwen-code
---

Learn how to power Qwen Code with Together AI models.

Qwen Code is a powerful command-line AI workflow tool specifically optimized for code understanding, automated tasks, and intelligent development assistance. While it comes with built-in Qwen OAuth support, you can also configure it to use Together AI's extensive model selection for even more flexibility and control over your AI coding experience.

This guide shows you how to set up Qwen Code with Together AI's powerful models like Kimi K2.7 Code, GLM 5.2, and specialized coding models to enhance your development workflow beyond traditional context window limits.

## Why use Qwen Code with Together AI?

* **Model Choice**: Access to a wide variety of models beyond Qwen models
* **Transparent Pricing**: Clear token-based pricing with no surprises
* **Enterprise Control**: Use your own API keys and have full control over usage
* **Specialized Models**: Access to coding-specific models like Kimi K2.7 Code and Qwen3 Coder Next

## 1. Install Qwen Code

Install Qwen Code globally via npm:

```bash theme={null}
npm install -g @qwen-code/qwen-code@latest
```

Verify the installation:

```bash theme={null}
qwen --version
```

**Requirements:** Ensure you have Node.js version 20 or higher installed.

## 2. Configure Together AI

Instead of using the default Qwen OAuth, you'll configure Qwen Code to use Together AI's OpenAI-compatible API.

### Method 1: Environment variables (recommended)

Set up your environment variables:

```bash theme={null}
export OPENAI_API_KEY="your_together_api_key_here"
export OPENAI_BASE_URL="https://api.together.ai/v1"
export OPENAI_MODEL="your_chosen_model"
```

### Method 2: Project .env file

Create a `.env` file in your project root:

```env theme={null}
OPENAI_API_KEY=your_together_api_key_here
OPENAI_BASE_URL=https://api.together.ai/v1
OPENAI_MODEL=your_chosen_model
```

### Get your Together AI credentials

1. **API Key**: Get your [Together AI API key](https://api.together.ai/settings/projects/~current/api-keys)
2. **Base URL**: Use `https://api.together.ai/v1` for Together AI
3. **Model**: Choose from [Together AI's model catalog](https://www.together.ai/models)

## 3. Choose your model

Select from Together AI's powerful model selection:

### Recommended models for coding

**For General Development:**

* `moonshotai/Kimi-K3` - Top pick for coding agents.
* `Qwen/Qwen3-Coder-Next-FP8` - Fast, cost-effective coding model.

**For Advanced Coding Tasks:**

* `zai-org/GLM-5.2` - Strong all-rounder with a large context window.
* `deepseek-ai/DeepSeek-V4-Pro-0813` - Advanced reasoning capabilities.

See the [pricing page](https://www.together.ai/pricing) for current per-token rates.

### Example configuration

```bash theme={null}
export OPENAI_API_KEY="your_together_api_key"
export OPENAI_BASE_URL="https://api.together.ai/v1"
export OPENAI_MODEL="moonshotai/Kimi-K3"
```

## 4. Launch and use Qwen Code

Navigate to your project and start Qwen Code:

```bash theme={null}
cd your-project/
qwen
```

You're now ready to use Qwen Code with Together AI models!

## Advanced tips

### Token optimization

* Use `/compress` to maintain context while reducing token usage
* Set appropriate session limits based on your Together AI plan
* Monitor usage with `/stats` command

### Model selection strategy

* Use **Kimi K2.7 Code** for general coding tasks.
* Switch to **GLM 5.2** or **DeepSeek V4 Pro** for complex reasoning.
* Use **Qwen3 Coder Next** for faster, cost-effective operations.

### Context window management

Qwen Code is designed to handle large codebases beyond traditional context limits:

* Automatically chunks and processes large files
* Maintains conversation context across multiple API calls
* Optimizes token usage through intelligent compression

## Troubleshooting

### Common issues

**Authentication Errors:**

* Verify your Together AI API key is correct
* Ensure `OPENAI_BASE_URL` is set to `https://api.together.ai/v1`
* Check that your API key has sufficient credits

**Model Not Found:**

* Verify the model name exists in [Together AI's catalog](https://www.together.ai/models)
* Ensure the model name is exactly as listed (case-sensitive)

## Getting started checklist

1. ✅ Install Node.js 20+ and Qwen Code
2. ✅ Get your Together AI API key
3. ✅ Set environment variables or create `.env` file
4. ✅ Choose your preferred model from Together AI
5. ✅ Launch Qwen Code in your project directory
6. ✅ Start coding with AI assistance!

That's it! You now have Qwen Code powered by Together AI's advanced models, giving you unprecedented control over your AI-assisted development workflow with transparent pricing and model flexibility.
