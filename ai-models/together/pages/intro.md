---
title: "Overview"
source: https://docs.together.ai/intro
path: intro
---

Run, train, and serve open-source AI models on Together AI.

<QuickstartWrapper>
  <CodeGroup>
    ```python Python theme={null}
    from together import Together
    client = Together()

    completion = client.chat.completions.create(
      model="MiniMaxAI/MiniMax-M3",
      messages=[{"role": "user", "content": "What are the top 3 things to do in New York?"}],
    )

    print(completion.choices[0].message.content)
    ```

    ```typescript TypeScript theme={null}
    import Together from 'together-ai';
    const together = new Together();

    const completion = await together.chat.completions.create({
      model: 'MiniMaxAI/MiniMax-M3',
      messages: [{ role: 'user', content: 'Top 3 things to do in New York?' }],
    });

    console.log(completion.choices[0].message.content);
    ```

    ```bash cURL theme={null}
    curl -X POST "https://api.together.ai/v1/chat/completions" \
         -H "Authorization: Bearer $TOGETHER_API_KEY" \
         -H "Content-Type: application/json" \
         -d '{
         	"model": "MiniMaxAI/MiniMax-M3",
         	"messages": [
              {"role": "user", "content": "What are the top 3 things to do in New York?"}
         	]
    }'
    ```
  </CodeGroup>
</QuickstartWrapper>

<Columns>
  <Card title="Run an AI model" href="/docs/quickstart">
    Run leading open-source AI models with our OpenAI-compatible API.
  </Card>

  <Card title="Fine-tune a model" href="/docs/fine-tuning/quickstart">
    Fine-tune models on your own data and deploy them for inference.
  </Card>

  <Card title="Launch a GPU cluster" href="/docs/gpu-clusters-overview">
    Spin up H100 and B200 clusters with attached storage for training or large batch jobs.
  </Card>
</Columns>

<SubHeading description="Together AI hosts many popular models, available via serverless or dedicated endpoints. On serverless, you're charged based on the tokens you use and the size of the model. On dedicated, you're charged based on GPU hours." />

<ModelGrid />

<SubHeading description="" />

<div>
  <CtaCard href="/docs/how-to-build-coding-agents" title="Build an agent" description="Build agent workflows for real-world use cases." />

  <CtaCard href="/docs/nextjs-chat-quickstart" title="Build a Next.js chatbot" description="Spin up a production-ready chatbot with Next.js." />

  <CtaCard href="/docs/building-a-rag-workflow" title="Build RAG apps" description="Combine retrieval and generation to build grounded RAG apps." />

  <CtaCard href="https://www.together.ai/blog/how-to-build-a-real-time-image-generator-with-together-ai" title="Build a real-time image app" description="Stream real-time image generations with FLUX Schnell." />

  <CtaCard href="/docs/how-to-build-a-claude-artifacts-clone-with-llama-31-405b" title="Build a text-to-app workflow" description="Turn natural language into interactive apps with CodeSandbox." />

  <CtaCard href="/docs/ai-search-engine" title="Build an AI search engine" description="Ship a simplified Perplexity-style search." />

  <CtaCard href="/docs/json-mode" title="Use structured inputs with LLMs" description="Get reliable JSON by defining schemas and using structured outputs." />

  <CtaCard href="/docs/reasoning-models-guide#reasoning-models-guide" title="Work with reasoning models" description="Use open reasoning models like DeepSeek-R1 for logic-heavy, multi-step tasks." />

  <CtaCard href="/docs/dedicated_containers_image" title="Deploy an image generation container" description="Run a FLUX2 model on dedicated GPUs with autoscaling and job queues." />
</div>

<SubHeading description="" />

<div>
  <CtaCard href="/docs/batch-inference" title="Spin up a batch job" description="Queue async generations and fetch results later." />

  <CtaCard href="/docs/dedicated-endpoints" title="Run a dedicated instance" description="Provision single-tenant GPUs for predictable, isolated latency." />

  <CtaCard href="/docs/ai-evaluations" title="Use the evals API" description="Automate scoring with LLM judges and reports." />

  <CtaCard href="/docs/code-execution" title="Run code in a sandbox" description="Run Python safely alongside model calls." />

  <CtaCard href="/docs/custom-models" title="Bring your own model" description="Upload weights and serve them via the Together AI API." />

  <CtaCard href="/docs/dedicated-container-inference" title="Deploy dedicated containers" description="Run your own Dockerized inference on managed GPUs with autoscaling and observability." />
</div>

<div>
  <WideCtaCard href="https://github.com/togethercomputer/together-cookbook" title="Cookbook" description="Open-source collection of examples and guides." />

  <WideCtaCard href="https://together.ai/demos" title="Example apps" description="Full-stack open-source Next.js apps built on Together AI." />

  <WideCtaCard href="https://api.together.ai/playground" title="Playground" description="Experiment with models and export code." />

  <WideCtaCard href="/docs/serverless-models" title="Models library" description="Browse supported models." />
</div>
