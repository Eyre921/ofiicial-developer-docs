---
title: "Composio"
source: https://docs.together.ai/docs/composio
path: docs/composio
---

Using Composio With Together AI

Composio allows developers to integrate external tools and services into their AI applications. It handles tool calling, web-hooks, authentication, and more.

You need to register on a Composio account - Sign up here if you haven't already to get their API key [https://platform.composio.dev/](https://platform.composio.dev/)

## Install Libraries

<CodeGroup>
  ```shell Python theme={null}
  pip install together composio-togetherai
  ```

  ```shell TypeScript theme={null}
  npm install @composio/core @composio/vercel @ai-sdk/togetherai ai
  ```
</CodeGroup>

Set your `TOGETHER_API_KEY` environment variable.

```sh Shell theme={null}
export TOGETHER_API_KEY=***
export COMPOSIO_API_KEY=***
```

## Example

In this example, we will use Together AI to star a repository on GitHub using Composio Tools.

<CodeGroup>
  ```python Python theme={null}
  from composio_togetherai import ComposioToolSet, App
  from together import Together

  client = Together()
  toolset = ComposioToolSet()
  ```

  ```typescript TypeScript theme={null}
  /*
  We use the Vercel AI SDK with the Together provider to 
  enable type checking to work correctly for tools and 
  to simplify the Composio integration. 
  This flow enables us to directly execute tool calls
  without having to use composio.provider.handleToolCalls.
  */

  import { Composio } from "@composio/core";
  import { VercelProvider } from "@composio/vercel";
  import { createTogetherAI } from "@ai-sdk/togetherai";
  import { generateText } from "ai";

  export const together = createTogetherAI({
    apiKey: process.env.TOGETHER_API_KEY ?? "",
  });

  const composio = new Composio({
    apiKey: process.env.COMPOSIO_API_KEY ?? "",
    provider: new VercelProvider(),
  });
  ```
</CodeGroup>

### Connect your GitHub account

You need to have an active GitHub Integration in Composio. Learn how to do this [here](https://www.youtube.com/watch?v=LmyWy4LiedQ)

<CodeGroup>
  ```py Python theme={null}
  request = toolset.initiate_connection(app=App.GITHUB)
  print(f"Open this URL to authenticate: {request.redirectUrl}")
  ```

  ```sh Shell theme={null}
  composio login
  composio add github
  ```
</CodeGroup>

### Get All Github Tools

You can get all the tools for a given app as shown below, but you can get specific actions and filter actions using usecase & tags.

<CodeGroup>
  ```python Python theme={null}
  tools = toolset.get_tools(apps=[App.GITHUB])
  ```

  ```typescript TypeScript theme={null}
  const userId = "default"; // replace with user id from composio
  const tools = await composio.tools.get(userId, {
    toolkits: ['github'],
  });
  ```
</CodeGroup>

### Create a Chat Completion with Tools

<CodeGroup>
  ```python Python theme={null}
  response = client.chat.completions.create(
      tools=tools,
      model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "Star the repo 'togethercomputer/together-cookbook'",
          }
      ],
  )

  res = toolset.handle_tool_calls(response)
  print(res)
  ```

  ```typescript TypeScript theme={null}
  const responseGithub = await generateText({
      model: together("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
      messages: [
        {
          role: "user",
          content: "Star the repo 'togethercomputer/together-cookbook'",
        },
      ],
      tools,
      toolChoice: "required",
  });

  console.log(responseGithub);
  ```
</CodeGroup>

## Next Steps

<Note>
  ### Composio - Together AI Cookbook

  Explore our in-depth [Composio Cookbook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Composio/Agents_Composio.ipynb) to learn how to automate emails with LLMs.
</Note>
