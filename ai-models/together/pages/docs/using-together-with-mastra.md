---
title: "Mastra quickstart"
source: https://docs.together.ai/docs/using-together-with-mastra
path: docs/using-together-with-mastra
---

Use Together models with Mastra.

[Mastra](https://mastra.ai) is a framework for building and deploying AI-powered features using a modern JavaScript stack powered by the [Vercel AI SDK](/docs/using-together-with-vercels-ai-sdk). Integrating with Together AI provides access to a wide range of models for building intelligent agents.

## Getting started

1. ### Create a new Mastra project

   First, create a new Mastra project using the CLI:

   ```bash theme={null}
   pnpm dlx create-mastra@latest
   ```

   During the setup, the system prompts you to name your project, choose a default provider, and more. Feel free to use the default settings.

2. ### Install dependencies

   To use Together AI with Mastra, install the required packages:

   <CodeGroup>
     ```bash npm theme={null}
     npm i @ai-sdk/togetherai
     ```

     ```bash yarn theme={null}
     yarn add @ai-sdk/togetherai
     ```

     ```bash pnpm theme={null}
     pnpm add @ai-sdk/togetherai
     ```
   </CodeGroup>

3. ### Configure environment variables

   Create or update your `.env` file with your Together AI API key:

   ```bash theme={null}
   TOGETHER_API_KEY=your-api-key-here
   ```

4. ### Configure your agent to use Together AI

   Now, update your agent configuration file, typically `src/mastra/agents/weather-agent.ts`, to use Together AI models:

   ```typescript src/mastra/agents/weather-agent.ts theme={null}
   import 'dotenv/config';
   import { Agent } from '@mastra/core/agent';
   import { createTogetherAI } from '@ai-sdk/togetherai';

   const together = createTogetherAI({
     apiKey: process.env.TOGETHER_API_KEY ?? "",
   });

   export const weatherAgent = new Agent({
     name: 'Weather Agent',
     instructions: `
         You are a helpful weather assistant that provides accurate weather information and can help planning activities based on the weather.
         Use the weatherTool to fetch current weather data.
   `,
      model: together("zai-org/GLM-5"),
     tools: { weatherTool },
    // ... other configuration
   });

   (async () => {
     try {
       const response = await weatherAgent.generate(
         "What's the weather in San Francisco today?",
       );
       console.log('Weather Agent Response:', response.text);
     } catch (error) {
       console.error('Error invoking weather agent:', error);
     }
   })();
   ```

5. ### Running the application

   Since your agent is now configured to use Together AI, run the Mastra development server:

   <CodeGroup>
     ```bash npm theme={null}
     npm run dev
     ```

     ```bash yarn theme={null}
     yarn dev
     ```

     ```bash pnpm theme={null}
     pnpm dev
     ```
   </CodeGroup>

   Open the [Mastra Playground and Mastra API](https://mastra.ai/docs) to test your agents, workflows, and tools.

## Next Steps

* Explore the [Mastra documentation](https://mastra.ai) for more advanced features
* Check out [Together AI's model documentation](https://docs.together.ai/docs/serverless/models) for the latest available models
* Learn about building workflows and tools in Mastra
