---
title: "Performance Optimization"
source: https://docs.perplexity.ai/docs/sdk/performance
path: docs/sdk/performance
---

Learn how to optimize the Perplexity SDKs for high-throughput applications with async support, connection pooling, and raw response access.

## Overview

The Perplexity SDKs provide several features to optimize performance for high-throughput applications. This guide covers async operations, connection pooling, raw response access, and other performance optimization techniques.

## Async Support

### Basic Async Usage

For applications that need to handle multiple requests concurrently:

<CodeGroup>
  ```bash Python Installation theme={null}
  pip install perplexityai[aiohttp]
  ```

  ```bash TypeScript Installation theme={null}
  npm install @perplexity-ai/perplexity_ai
  # Async support is built-in with TypeScript
  ```
</CodeGroup>

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  async def main():
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          # Single async request
          search = await client.search.create(query="OpenAI o-series reasoning model benchmarks")
          print(search.results)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function main() {
      const client = new Perplexity();
      
      // Async is built-in for TypeScript
      const search = await client.search.create({ query: "OpenAI o-series reasoning model benchmarks" });
      console.log(search.results);
  }

  main();
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "169d5d3b-272a-46ca-a59d-7c218f9d5ce2",
    "results": [
      {
        "snippet": "",
        "title": "Reasoning best practices | OpenAI API",
        "url": "https://developers.openai.com/api/docs/guides/reasoning-best-practices",
        "date": null,
        "last_updated": "2026-05-21"
      },
      {
        "snippet": "",
        "title": "A Comparative Study on Reasoning Patterns of OpenAI's o1 Model",
        "url": "https://arxiv.org/html/2410.13639v1",
        "date": "2024-10-17",
        "last_updated": "2026-03-22"
      },
      {
        "snippet": "**OpenAI o1** is a generative pre-trained transformer (GPT), the first in OpenAI's \"o\" series of reasoning models.\nA preview of o1 was released by OpenAI on September 12, 2024.\no1 spends time \"thinking\" before it answers, making it better at complex reasoning tasks, science and programming than GPT-4o.\nThe full version was released to ChatGPT users on December 5, 2024.\n...\nOpenAI noted that o1 is the first of a series of \"reasoning\" models.\nOpenAI shared in December 2024 benchmark results for its successor, o3 (the name o2 was skipped to avoid trademark conflict with the mobile carrier brand named O2).\n...\no1 spends additional time thinking (generating a chain of thought) before generating an answer, which makes it better for complex reasoning tasks, particularly in science and mathematics.\n...\nOpenAI's test results suggest a correlation between accuracy and the logarithm of the amount of compute spent thinking before answering.\no1-preview performed approximately at a PhD level on benchmark tests related to physics, chemistry, and biology.\nOn the American Invitational Mathematics Examination, it solved 83% (12.5/15) of the problems, compared to 13% (1.8/15) for GPT-4o.\nIt also ranked in the 89th percentile in Codeforces coding competitions.\no1-mini is faster and 80% cheaper than o1-preview.\nIt is particularly suitable for programming and STEM-related tasks, but does not have the same \"broad world knowledge\" as o1-preview.\nOpenAI noted that o1's reasoning capabilities make it better at adhering to safety rules provided in the prompt's context window.\n...\nAccording to OpenAI's assessments, o1-preview and o1-mini crossed into \"medium risk\" in CBRN (biological, chemical, radiological, and nuclear) weapons.\nDan Hendrycks wrote that \"The model already outperforms PhD scientists most of the time on answering questions related to bioweapons.\"\n...\nAccording to OpenAI, o1 may \"fake alignment\", that is, generate a response that is contrary to accuracy and its own chain of thought, in about 0.38% of cases.\n...\nBy changing the numbers and names used in a math problem or simply running the same problem again, LLMs would perform somewhat worse than their best benchmark results.\nAdding extraneous but logically inconsequential information to the problems caused a much greater drop in performance, from −17.5% for o1-preview and −29.1% for o1-mini, to −65.7% for the worst model tested.",
        "title": "OpenAI o1 - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/OpenAI_o1",
        "date": "2024-09-12",
        "last_updated": "2026-03-31"
      },
      {
        "snippet": "",
        "title": "OpenAI O3 & O4 Mini: The First True Reasoning Agents? - YouTube",
        "url": "https://www.youtube.com/watch?v=TGnPcObHdLY",
        "date": "2025-04-16",
        "last_updated": "2026-04-08"
      },
      {
        "snippet": "",
        "title": "Safety",
        "url": "https://openai.com/index/learning-to-reason-with-llms/",
        "date": "2024-09-12",
        "last_updated": "2026-03-29"
      },
      {
        "snippet": "",
        "title": "Introducing OpenAI o3 and o4-mini",
        "url": "https://openai.com/index/introducing-o3-and-o4-mini/",
        "date": "2025-04-16",
        "last_updated": "2026-05-16"
      },
      {
        "snippet": "",
        "title": "OpenAI's o3 model scores 3% on the ARC-AGI-2 benchmark ...",
        "url": "https://forum.effectivealtruism.org/posts/CoPNbwNqDai6orZhv/openai-s-o3-model-scores-3-on-the-arc-agi-2-benchmark",
        "date": "2025-05-01",
        "last_updated": "2026-05-17"
      },
      {
        "snippet": "Built to handle hard problems — they take more time to think before responding, similar to how a person would approach a difficult task.\nThe “ OpenAI o1 preview ” model, specifically, shows incredible results for various hard problems: math, coding, and reasoning.\n...\nToday, OpenAI released the full version of the o1 model, making it production-ready for a wide range of use cases.\nIn this article, we’ll compare its capabilities with GPT-4o and Claude 3.5 Sonnet to see if it lives up to the claim.\n...\nWe compared these models across three key tasks:\nReasoning riddles, Math Problems, and Classifying customer tickets\nAlong the way, we explored the latest benchmarks, evaluated input and output token costs, assessed latency and throughput, and shared guidance on choosing the best model for your needs.\nFor up-to-date rankings, check our leaderboard , or keep reading to see the results of our evaluation.\nFrom this analysis we learn that:\nProduction apps: For apps in productions, we still recommend sing GPT-4o over o1, at least for one-off tasks like the ones we tested here.\nReasoning riddles: OpenAI o1 showed some inconsistency, refusing to answer one question and scoring 60% accuracy, similar to GPT-4o, though the difference isn’t major.\nGPT-4o is a great model for this task.\nClaude 3.5 Sonnet scored a lower accuracy of 56%.\n- Math equations: GPT-4o and the o1 model performed equally well on this task, raising questions about whether the higher cost of o1 is justified.\n- Surprisingly, the latest Claude 3.5 Sonnet lagged significantly behind, achieving only 39% accuracy on these examples.\n- Classification : All models performed similarly: GPT-4o (74%), O1 (73%), and Model 3.5 Sonnet (76%), with GPT-4o improving by 12% since September.\n- GPT-4o had the highest precision (86%) making it ideal for tasks where correct possitive predictions matter most.\nThe o1 model led in recall (82%) making it suitable when you need to capture as many TRUE cases as possible.\nThe Claude 3.5 Sonnet had best F1 score (77%) indicating robust overall classification performance.\n- Speed &amp; Cost: Given that we saw similar results across the three tasks we evaluated, we still can’t justify the cost of o1, and we recommend going with GPT-4o for most use-cases.\n- Complex Problems: Use OpenAI o1 when you need top-tier reasoning and latency isn’t a concern.\nIt’s ideal for agentic workflows with a “planning” stage, where the model creates a detailed plan that smaller, cheaper models can follow\n...\nAs expected, the new o1 models are slower due to their “reasoning” process.\nThis isn’t a drawback necessarily—it just makes them better suited for tasks where thoughtful problem-solving is essential.\nOpenAI o1 is approximately 30 times slower than GPT-4o.\nSimilarly, the o1 mini version is around 16 times slower than GPT-4o mini.\n## Cost comparison\nIt's evident that using OpenAI o1 will cost roughly 6x more than GPT-4o and Claude 3.5 Sonnet for input tokens, and about 5x more for output tokens.\n## Throughput (Output speed)\nOpenAI o1 stands out with the fastest throughput, generating 143 tokens per second.\nHowever, take this throughput data with a grain of salt — while its output speed is significantly higher than the other models, its latency, or time-to-think, is about 30x longer than GPT-4o and Claude 3.5 Sonnet.\n...\nWhen new models are released, we learn about their capabilities from benchmark data reported in the technical reports.\nThe new OpenAI o1 model improves on the most complex reasoning benchmarks:\nExceeds human PhD-level accuracy on challenging benchmark tasks in physics, chemistry, and biology on the GPQA benchmark Coding is easier — It ranks in the 89th percentile on competitive programming questions (Codeforces) It’s also very good at math — In a qualifying exam for the International Mathematics Olympiad (IMO), GPT-4o correctly solved only 13% of problems, while the reasoning model scored 83%.\nNow, this is next level.\nOn the standard ML benchmarks , it has huge improvements across the board:\n...\nThey’ve gathered over 6,000 votes, and the results show that the OpenAI o1 model is consistently ranked #1 across all categories, with Math being the most notable area of impact.\nThe o1-mini model is #1 in technical areas, #2 overall.\nCheck out the full results on this link.\n...\nThe results show that the newest model is great at complex tasks, but not preferred for some natural language tasks — suggesting that maybe the model is not the best for every use-case.\n...\nGPT-4o and the o1 model performed equally well on this task, raising questions about whether the higher cost of o1 is justified.\nSurprisingly, the latest Claude 3.5 Sonnet lagged significantly behind, achieving only 39% accuracy on these examples.\n...\nOpenAI o1 showed some inconsistency, refusing to answer one question and scoring 60% accuracy, similar to GPT-4o, though the difference isn’t major.\nGPT-4o is a great model for this task.\nClaude 3.5 Sonnet scored a lower accuracy of 56%.\n...\nWe ran the evaluation to test if the models' outputs matched our ground truth data for 100 labeled test cases, and we can see that they all got similar accuracies.\nGPT-4o got 74, O1 got 73, Claude 3.5 Sonnet got 76 answers right from total of 100.\nThis reinforces the idea that smarter, more cost-effective models without a \"reasoning module\" like o1 can perform just as well as o1, but without the added expense.\nIn a similar evaluation in September of 2024, we evaluated that GPT-4o had lower accuracy, and classified only 62 of the 100 examples correctly.\nToday, we’re seeing at a 12% improvement on this task!\n...\nToday, O1 has more production-ready properties and is starting to becomemore valuable for production use cases—though it’s best suited for those who can tolerate higher latency and need to tackle the toughest challenges.\nGPT-4O, however, remains the go-to model for many of the production use cases we see in the market.",
        "title": "Analysis: OpenAI o1 vs GPT-4o vs Claude 3.5 Sonnet - Vellum",
        "url": "https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o",
        "date": "2024-12-17",
        "last_updated": "2026-05-21"
      },
      {
        "snippet": "",
        "title": "THE RELATIONSHIP BETWEEN REASONING AND PERFORMANCE",
        "url": "http://arxiv.org/pdf/2502.15631.pdf",
        "date": null,
        "last_updated": "2025-02-25"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

### Concurrent Requests

Process multiple requests simultaneously for better throughput:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  async def concurrent_searches():
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          # Concurrent requests
          queries = ["AI", "machine learning", "deep learning", "neural networks"]
          tasks = [
              client.search.create(query=query)
              for query in queries
          ]
          
          results = await asyncio.gather(*tasks)
          
          for i, result in enumerate(results):
              print(f"Query '{queries[i]}': {len(result.results)} results")

  asyncio.run(concurrent_searches())
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function concurrentSearches() {
      const client = new Perplexity();
      
      // Concurrent requests
      const queries = ["AI", "machine learning", "deep learning", "neural networks"];
      const tasks = queries.map(query => 
          client.search.create({ query })
      );
      
      const results = await Promise.all(tasks);
      
      results.forEach((result, i) => {
          console.log(`Query '${queries[i]}': ${result.results.length} results`);
      });
  }

  concurrentSearches();
  ```
</CodeGroup>

### Batch Processing with Rate Limiting

Process large numbers of requests while respecting rate limits:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  async def batch_process_with_limit(queries, batch_size=5, delay=1.0):
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          results = []
          
          for i in range(0, len(queries), batch_size):
              batch = queries[i:i + batch_size]
              
              # Process batch concurrently
              tasks = [
                  client.search.create(query=query)
                  for query in batch
              ]
              
              batch_results = await asyncio.gather(*tasks, return_exceptions=True)
              results.extend(batch_results)
              
              # Delay between batches to respect rate limits
              if i + batch_size < len(queries):
                  await asyncio.sleep(delay)
          
          return results

  # Usage
  queries = [f"query {i}" for i in range(20)]
  results = asyncio.run(batch_process_with_limit(queries))
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function batchProcessWithLimit(
      queries: string[], 
      batchSize: number = 5, 
      delay: number = 1000
  ) {
      const client = new Perplexity();
      const results = [];
      
      for (let i = 0; i < queries.length; i += batchSize) {
          const batch = queries.slice(i, i + batchSize);
          
          // Process batch concurrently
          const tasks = batch.map(query => 
              client.search.create({ query }).catch(error => error)
          );
          
          const batchResults = await Promise.all(tasks);
          results.push(...batchResults);
          
          // Delay between batches to respect rate limits
          if (i + batchSize < queries.length) {
              await new Promise(resolve => setTimeout(resolve, delay));
          }
      }
      
      return results;
  }

  // Usage
  const queries = Array.from({ length: 20 }, (_, i) => `query ${i}`);
  const results = await batchProcessWithLimit(queries);
  ```
</CodeGroup>

## Raw Response Access

Access headers, status codes, and raw response data for advanced use cases:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Get raw response with headers
  response = client.search.with_raw_response.create(
      query="OpenAI o-series reasoning model benchmarks"
  )

  print(f"Status Code: {response.status_code}")
  print(f"Request ID: {response.headers.get('X-Request-ID')}")
  print(f"Rate Limit Remaining: {response.headers.get('X-RateLimit-Remaining')}")
  print(f"Rate Limit Reset: {response.headers.get('X-RateLimit-Reset')}")

  # Parse the actual search results
  search = response.parse()
  print(f"Found {len(search.results)} results")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Get raw response with headers
  const { data: search, response: rawResponse } = await client.search
      .create({ query: "OpenAI o-series reasoning model benchmarks" })
      .withResponse();

  console.log(`Status Code: ${rawResponse.status}`);
  console.log(`Request ID: ${rawResponse.headers.get('X-Request-ID')}`);
  console.log(`Rate Limit Remaining: ${rawResponse.headers.get('X-RateLimit-Remaining')}`);
  console.log(`Rate Limit Reset: ${rawResponse.headers.get('X-RateLimit-Reset')}`);
  console.log(`Found ${search.results.length} results`);
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "169d5d3b-272a-46ca-a59d-7c218f9d5ce2",
    "results": [
      {
        "snippet": "",
        "title": "Reasoning best practices | OpenAI API",
        "url": "https://developers.openai.com/api/docs/guides/reasoning-best-practices",
        "date": null,
        "last_updated": "2026-05-21"
      },
      {
        "snippet": "",
        "title": "A Comparative Study on Reasoning Patterns of OpenAI's o1 Model",
        "url": "https://arxiv.org/html/2410.13639v1",
        "date": "2024-10-17",
        "last_updated": "2026-03-22"
      },
      {
        "snippet": "**OpenAI o1** is a generative pre-trained transformer (GPT), the first in OpenAI's \"o\" series of reasoning models.\nA preview of o1 was released by OpenAI on September 12, 2024.\no1 spends time \"thinking\" before it answers, making it better at complex reasoning tasks, science and programming than GPT-4o.\nThe full version was released to ChatGPT users on December 5, 2024.\n...\nOpenAI noted that o1 is the first of a series of \"reasoning\" models.\nOpenAI shared in December 2024 benchmark results for its successor, o3 (the name o2 was skipped to avoid trademark conflict with the mobile carrier brand named O2).\n...\no1 spends additional time thinking (generating a chain of thought) before generating an answer, which makes it better for complex reasoning tasks, particularly in science and mathematics.\n...\nOpenAI's test results suggest a correlation between accuracy and the logarithm of the amount of compute spent thinking before answering.\no1-preview performed approximately at a PhD level on benchmark tests related to physics, chemistry, and biology.\nOn the American Invitational Mathematics Examination, it solved 83% (12.5/15) of the problems, compared to 13% (1.8/15) for GPT-4o.\nIt also ranked in the 89th percentile in Codeforces coding competitions.\no1-mini is faster and 80% cheaper than o1-preview.\nIt is particularly suitable for programming and STEM-related tasks, but does not have the same \"broad world knowledge\" as o1-preview.\nOpenAI noted that o1's reasoning capabilities make it better at adhering to safety rules provided in the prompt's context window.\n...\nAccording to OpenAI's assessments, o1-preview and o1-mini crossed into \"medium risk\" in CBRN (biological, chemical, radiological, and nuclear) weapons.\nDan Hendrycks wrote that \"The model already outperforms PhD scientists most of the time on answering questions related to bioweapons.\"\n...\nAccording to OpenAI, o1 may \"fake alignment\", that is, generate a response that is contrary to accuracy and its own chain of thought, in about 0.38% of cases.\n...\nBy changing the numbers and names used in a math problem or simply running the same problem again, LLMs would perform somewhat worse than their best benchmark results.\nAdding extraneous but logically inconsequential information to the problems caused a much greater drop in performance, from −17.5% for o1-preview and −29.1% for o1-mini, to −65.7% for the worst model tested.",
        "title": "OpenAI o1 - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/OpenAI_o1",
        "date": "2024-09-12",
        "last_updated": "2026-03-31"
      },
      {
        "snippet": "",
        "title": "OpenAI O3 & O4 Mini: The First True Reasoning Agents? - YouTube",
        "url": "https://www.youtube.com/watch?v=TGnPcObHdLY",
        "date": "2025-04-16",
        "last_updated": "2026-04-08"
      },
      {
        "snippet": "",
        "title": "Safety",
        "url": "https://openai.com/index/learning-to-reason-with-llms/",
        "date": "2024-09-12",
        "last_updated": "2026-03-29"
      },
      {
        "snippet": "",
        "title": "Introducing OpenAI o3 and o4-mini",
        "url": "https://openai.com/index/introducing-o3-and-o4-mini/",
        "date": "2025-04-16",
        "last_updated": "2026-05-16"
      },
      {
        "snippet": "",
        "title": "OpenAI's o3 model scores 3% on the ARC-AGI-2 benchmark ...",
        "url": "https://forum.effectivealtruism.org/posts/CoPNbwNqDai6orZhv/openai-s-o3-model-scores-3-on-the-arc-agi-2-benchmark",
        "date": "2025-05-01",
        "last_updated": "2026-05-17"
      },
      {
        "snippet": "Built to handle hard problems — they take more time to think before responding, similar to how a person would approach a difficult task.\nThe “ OpenAI o1 preview ” model, specifically, shows incredible results for various hard problems: math, coding, and reasoning.\n...\nToday, OpenAI released the full version of the o1 model, making it production-ready for a wide range of use cases.\nIn this article, we’ll compare its capabilities with GPT-4o and Claude 3.5 Sonnet to see if it lives up to the claim.\n...\nWe compared these models across three key tasks:\nReasoning riddles, Math Problems, and Classifying customer tickets\nAlong the way, we explored the latest benchmarks, evaluated input and output token costs, assessed latency and throughput, and shared guidance on choosing the best model for your needs.\nFor up-to-date rankings, check our leaderboard , or keep reading to see the results of our evaluation.\nFrom this analysis we learn that:\nProduction apps: For apps in productions, we still recommend sing GPT-4o over o1, at least for one-off tasks like the ones we tested here.\nReasoning riddles: OpenAI o1 showed some inconsistency, refusing to answer one question and scoring 60% accuracy, similar to GPT-4o, though the difference isn’t major.\nGPT-4o is a great model for this task.\nClaude 3.5 Sonnet scored a lower accuracy of 56%.\n- Math equations: GPT-4o and the o1 model performed equally well on this task, raising questions about whether the higher cost of o1 is justified.\n- Surprisingly, the latest Claude 3.5 Sonnet lagged significantly behind, achieving only 39% accuracy on these examples.\n- Classification : All models performed similarly: GPT-4o (74%), O1 (73%), and Model 3.5 Sonnet (76%), with GPT-4o improving by 12% since September.\n- GPT-4o had the highest precision (86%) making it ideal for tasks where correct possitive predictions matter most.\nThe o1 model led in recall (82%) making it suitable when you need to capture as many TRUE cases as possible.\nThe Claude 3.5 Sonnet had best F1 score (77%) indicating robust overall classification performance.\n- Speed &amp; Cost: Given that we saw similar results across the three tasks we evaluated, we still can’t justify the cost of o1, and we recommend going with GPT-4o for most use-cases.\n- Complex Problems: Use OpenAI o1 when you need top-tier reasoning and latency isn’t a concern.\nIt’s ideal for agentic workflows with a “planning” stage, where the model creates a detailed plan that smaller, cheaper models can follow\n...\nAs expected, the new o1 models are slower due to their “reasoning” process.\nThis isn’t a drawback necessarily—it just makes them better suited for tasks where thoughtful problem-solving is essential.\nOpenAI o1 is approximately 30 times slower than GPT-4o.\nSimilarly, the o1 mini version is around 16 times slower than GPT-4o mini.\n## Cost comparison\nIt's evident that using OpenAI o1 will cost roughly 6x more than GPT-4o and Claude 3.5 Sonnet for input tokens, and about 5x more for output tokens.\n## Throughput (Output speed)\nOpenAI o1 stands out with the fastest throughput, generating 143 tokens per second.\nHowever, take this throughput data with a grain of salt — while its output speed is significantly higher than the other models, its latency, or time-to-think, is about 30x longer than GPT-4o and Claude 3.5 Sonnet.\n...\nWhen new models are released, we learn about their capabilities from benchmark data reported in the technical reports.\nThe new OpenAI o1 model improves on the most complex reasoning benchmarks:\nExceeds human PhD-level accuracy on challenging benchmark tasks in physics, chemistry, and biology on the GPQA benchmark Coding is easier — It ranks in the 89th percentile on competitive programming questions (Codeforces) It’s also very good at math — In a qualifying exam for the International Mathematics Olympiad (IMO), GPT-4o correctly solved only 13% of problems, while the reasoning model scored 83%.\nNow, this is next level.\nOn the standard ML benchmarks , it has huge improvements across the board:\n...\nThey’ve gathered over 6,000 votes, and the results show that the OpenAI o1 model is consistently ranked #1 across all categories, with Math being the most notable area of impact.\nThe o1-mini model is #1 in technical areas, #2 overall.\nCheck out the full results on this link.\n...\nThe results show that the newest model is great at complex tasks, but not preferred for some natural language tasks — suggesting that maybe the model is not the best for every use-case.\n...\nGPT-4o and the o1 model performed equally well on this task, raising questions about whether the higher cost of o1 is justified.\nSurprisingly, the latest Claude 3.5 Sonnet lagged significantly behind, achieving only 39% accuracy on these examples.\n...\nOpenAI o1 showed some inconsistency, refusing to answer one question and scoring 60% accuracy, similar to GPT-4o, though the difference isn’t major.\nGPT-4o is a great model for this task.\nClaude 3.5 Sonnet scored a lower accuracy of 56%.\n...\nWe ran the evaluation to test if the models' outputs matched our ground truth data for 100 labeled test cases, and we can see that they all got similar accuracies.\nGPT-4o got 74, O1 got 73, Claude 3.5 Sonnet got 76 answers right from total of 100.\nThis reinforces the idea that smarter, more cost-effective models without a \"reasoning module\" like o1 can perform just as well as o1, but without the added expense.\nIn a similar evaluation in September of 2024, we evaluated that GPT-4o had lower accuracy, and classified only 62 of the 100 examples correctly.\nToday, we’re seeing at a 12% improvement on this task!\n...\nToday, O1 has more production-ready properties and is starting to becomemore valuable for production use cases—though it’s best suited for those who can tolerate higher latency and need to tackle the toughest challenges.\nGPT-4O, however, remains the go-to model for many of the production use cases we see in the market.",
        "title": "Analysis: OpenAI o1 vs GPT-4o vs Claude 3.5 Sonnet - Vellum",
        "url": "https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o",
        "date": "2024-12-17",
        "last_updated": "2026-05-21"
      },
      {
        "snippet": "",
        "title": "THE RELATIONSHIP BETWEEN REASONING AND PERFORMANCE",
        "url": "http://arxiv.org/pdf/2502.15631.pdf",
        "date": null,
        "last_updated": "2025-02-25"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

### Response Streaming

For chat completions, use streaming to get partial results as they arrive:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Stream chat completion responses
  stream = client.chat.completions.create(
      model="sonar",
      messages=[{"role": "user", "content": "Explain what factors determine LLM inference throughput on accelerators: memory bandwidth, KV-cache size, batching, and quantization."}],
      stream=True
  )

  for chunk in stream:
      if chunk.choices[0].delta.content:
          print(chunk.choices[0].delta.content, end="", flush=True)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Stream chat completion responses
  const stream = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [{ role: "user", content: "Explain what factors determine LLM inference throughput on accelerators: memory bandwidth, KV-cache size, batching, and quantization." }],
      stream: true as const
  });

  for await (const chunk of stream) {
      if (chunk.choices[0]?.delta?.content) {
          process.stdout.write((chunk.choices[0]?.delta?.content ?? '') as string);
      }
  }
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "a73cb0f7-3b89-4488-84b1-d5f2d7cc0a55",
    "choices": [
      {
        "delta": {
          "content": "",
          "role": "assistant",
          "reasoning_steps": null,
          "tool_call_id": null,
          "tool_calls": null
        },
        "index": 0,
        "message": {
          "content": "LLM inference throughput on accelerators is mainly determined by how efficiently the GPU can move data, reuse cached state, and keep compute units busy. The four factors you mentioned interact closely:\n\n### 1) Memory bandwidth\nFor decoding, LLM inference is often **memory-bound** rather than compute-bound. The accelerator spends a lot of time reading and writing:\n- model weights,\n- activations,\n- and especially the KV cache.\n\nIf memory bandwidth is high, the model can fetch data faster, which increases tokens/sec and requests/sec. If bandwidth is limited, the GPU can’t stay fully utilized, and throughput drops even if the compute units are powerful.\n\n### 2) KV-cache size\nThe **KV cache** stores key/value tensors for previously processed tokens so the model doesn’t recompute attention over the full prompt every step.\n\nIts size affects throughput because:\n- **Longer prompts and longer generations** make the KV cache larger.\n- A larger cache consumes more GPU memory, reducing room for batching.\n- If the cache doesn’t fit well in memory, you may get more memory traffic or even spill/fragmentation effects, both of which hurt throughput.\n\nSo, a larger or less efficient KV cache usually reduces throughput by increasing memory pressure.\n\n### 3) Batching\n**Batching** improves throughput by letting the accelerator process multiple requests or tokens together.\n\nWhy it helps:\n- better hardware utilization,\n- amortizes kernel launch and scheduling overhead,\n- increases parallel work per step.\n\nBut batching has limits:\n- very large batches can increase latency,\n- batching too many requests can stress memory bandwidth and KV-cache capacity,\n- once the accelerator is saturated, adding more batch size stops helping and may even hurt throughput.\n\nSo batching is usually one of the biggest levers for increasing throughput, until memory or compute saturation is reached.\n\n### 4) Quantization\n**Quantization** reduces the precision of weights and/or activations, for example from FP16 to INT8 or FP8.\n\nThis can improve throughput because it:\n- reduces memory footprint,\n- lowers memory bandwidth requirements,\n- can increase cache efficiency,\n- sometimes enables more batching on the same hardware.\n\nIn some cases, quantization also speeds up computation directly if the accelerator has optimized low-precision kernels. But the benefit depends on the hardware and implementation.\n\n### In short\nThroughput is highest when:\n- the accelerator has enough **memory bandwidth**,\n- the **KV cache** is efficient and fits well in memory,\n- batching keeps the GPU busy without causing excessive memory pressure,\n- and **quantization** reduces memory traffic enough to improve efficiency.\n\nA simple summary is:\n\n**Throughput = how much useful token work the accelerator can do per second, and it improves when memory traffic is reduced, cache usage is efficient, and batching keeps the GPU saturated.**\n\nIf you want, I can also turn this into a compact formula-style explanation or a comparison table.",
          "role": "assistant",
          "reasoning_steps": null,
          "tool_call_id": null,
          "tool_calls": null
        },
        "finish_reason": "stop"
      }
    ],
    "created": 1779391755,
    "model": "sonar-pro",
    "citations": [
      "https://odr.chalmers.se/items/3ec33636-0e02-4dd6-9ecc-3bcf4bf25f74",
      "https://bentoml.com/llm/llm-inference-basics/llm-inference-metrics",
      "https://docs.anyscale.com/llm/serving/benchmarking/metrics",
      "https://www.yottalabs.ai/post/throughput-vs-latency-in-llm-inference-what-teams-get-wrong",
      "https://www.baseten.co/blog/understanding-performance-benchmarks-for-llm-inference/",
      "https://www.youtube.com/watch?v=_rEsLo21WvE",
      "https://dl.acm.org/doi/10.1145/3656019.3676949",
      "https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices",
      "https://www.cs.cmu.edu/~csd-phd-blog/2024/low-latency-llm-serving/"
    ],
    "object": "chat.completion",
    "search_results": [
      {
        "title": "Analyzing Factors Influencing Performance in LLM Inference Systems",
        "url": "https://odr.chalmers.se/items/3ec33636-0e02-4dd6-9ecc-3bcf4bf25f74",
        "date": "2025-05-01",
        "last_updated": "2025-09-18",
        "snippet": "Our results show that increasing the batch size significantly improves throughput but can also lead to higher latency, indicating a trade-off between speed and ...",
        "source": "web"
      },
      {
        "title": "Key metrics for LLM inference - BentoML",
        "url": "https://bentoml.com/llm/llm-inference-basics/llm-inference-metrics",
        "date": null,
        "last_updated": "2026-05-21",
        "snippet": "Measure key metrics like latency and throughput to optimize LLM inference performance ... Factors that impact RPS: Prompt complexity and length; Model size ...",
        "source": "web"
      },
      {
        "title": "Understand LLM latency and throughput metrics - Anyscale Docs",
        "url": "https://docs.anyscale.com/llm/serving/benchmarking/metrics",
        "date": null,
        "last_updated": "2026-05-15",
        "snippet": "Understand and optimize key LLM performance metrics including time to first token, inter-token latency, throughput, and requests per second.",
        "source": "web"
      },
      {
        "title": "Throughput vs Latency in LLM Inference: What Teams Get Wrong",
        "url": "https://www.yottalabs.ai/post/throughput-vs-latency-in-llm-inference-what-teams-get-wrong",
        "date": "2026-03-29",
        "last_updated": "2026-05-20",
        "snippet": "They are tightly connected. The same factors that limit throughput also shape latency, including batching, memory constraints, and workload ...",
        "source": "web"
      },
      {
        "title": "Understanding performance benchmarks for LLM inference - Baseten",
        "url": "https://www.baseten.co/blog/understanding-performance-benchmarks-for-llm-inference/",
        "date": "2025-05-18",
        "last_updated": "2026-05-21",
        "snippet": "This guide helps you interpret LLM performance metrics to make direct comparisons on latency, throughput, and cost.",
        "source": "web"
      },
      {
        "title": "Scaling LLM Batch Inference: Ray Data & vLLM for High Throughput",
        "url": "https://www.youtube.com/watch?v=_rEsLo21WvE",
        "date": "2025-03-07",
        "last_updated": "2026-03-29",
        "snippet": "Struggling to scale your Large Language Model (LLM) batch inference? Learn how Ray Data and vLLM can unlock high throughput and ...",
        "source": "web"
      },
      {
        "title": "Improving Throughput-oriented LLM Inference with CPU Computations",
        "url": "https://dl.acm.org/doi/10.1145/3656019.3676949",
        "date": "2024-10-13",
        "last_updated": null,
        "snippet": "This module accounts for various factors including batch sizes, compression settings, and specific decoder implementations. The profiling ...",
        "source": "web"
      },
      {
        "title": "LLM Inference Performance Engineering: Best Practices - Databricks",
        "url": "https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices",
        "date": "2023-10-12",
        "last_updated": "2026-05-21",
        "snippet": "Learn best practices for optimizing LLM inference performance on Databricks, enhancing the efficiency of your machine learning models.",
        "source": "web"
      },
      {
        "title": "Optimizing and Characterizing High-Throughput Low-Latency LLM ...",
        "url": "https://www.cs.cmu.edu/~csd-phd-blog/2024/low-latency-llm-serving/",
        "date": "2024-11-27",
        "last_updated": "2026-04-12",
        "snippet": "There are various factors contributing to the low latency of MLCEngine, and we are happy to share the lessons we've learnt with the community.",
        "source": "web"
      }
    ],
    "status": null,
    "type": null,
    "usage": {
      "completion_tokens": 587,
      "cost": {
        "input_tokens_cost": 8e-05,
        "output_tokens_cost": 0.00881,
        "total_cost": 0.01489,
        "citation_tokens_cost": null,
        "reasoning_tokens_cost": null,
        "request_cost": 0.006,
        "search_queries_cost": null
      },
      "prompt_tokens": 27,
      "total_tokens": 614,
      "citation_tokens": null,
      "num_search_queries": null,
      "reasoning_tokens": null,
      "search_context_size": "low"
    }
  }
  ```
</Accordion>

## Connection Pooling

### Optimized Connection Settings

Configure connection pooling for better performance:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient, AsyncPerplexity, DefaultAioHttpClient

  # Sync client with optimized connection pooling
  limits = httpx.Limits(
      max_keepalive_connections=50,  # Keep connections alive
      max_connections=100,           # Total connection pool size
      keepalive_expiry=30.0         # Keep-alive timeout
  )

  sync_client = Perplexity(
      http_client=DefaultHttpxClient(limits=limits)
  )

  # Async client with optimized connection pooling
  async_limits = httpx.Limits(
      max_keepalive_connections=100,
      max_connections=200,
      keepalive_expiry=60.0
  )

  async def create_async_client():
      return AsyncPerplexity(
          http_client=DefaultAioHttpClient(limits=async_limits)
      )
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import https from 'https';

  // Optimized HTTPS agent for connection pooling
  const optimizedAgent = new https.Agent({
      keepAlive: true,
      keepAliveMsecs: 30000,  // 30 seconds
      maxSockets: 50,         // Max connections per host
      maxFreeSockets: 10,     // Max idle connections per host
      timeout: 60000          // Socket timeout
  });

  const client = new Perplexity({
      httpAgent: optimizedAgent
  } as any);

  // For high-throughput applications
  const highThroughputAgent = new https.Agent({
      keepAlive: true,
      keepAliveMsecs: 60000,
      maxSockets: 200,
      maxFreeSockets: 50,
      timeout: 120000
  });

  const clientHighThroughput = new Perplexity({
      httpAgent: highThroughputAgent
  } as any);
  ```
</CodeGroup>

## Performance Monitoring

### Request Timing and Metrics

Monitor performance metrics to identify bottlenecks:

<CodeGroup>
  ```python Python theme={null}
  import time
  import asyncio
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  class PerformanceMonitor:
      def __init__(self):
          self.request_times = []
          self.error_count = 0
          
      async def timed_request(self, client, query):
          start_time = time.time()
          try:
              result = await client.search.create(query=query)
              duration = time.time() - start_time
              self.request_times.append(duration)
              return result
          except Exception as e:
              self.error_count += 1
              raise e
      
      def get_stats(self):
          if not self.request_times:
              return {"error": "No successful requests"}
          
          return {
              "total_requests": len(self.request_times),
              "error_count": self.error_count,
              "avg_response_time": sum(self.request_times) / len(self.request_times),
              "min_response_time": min(self.request_times),
              "max_response_time": max(self.request_times)
          }

  async def run_performance_test():
      monitor = PerformanceMonitor()
      
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          queries = [f"test query {i}" for i in range(10)]
          
          tasks = [
              monitor.timed_request(client, query)
              for query in queries
          ]
          
          await asyncio.gather(*tasks, return_exceptions=True)
          
      print(monitor.get_stats())

  asyncio.run(run_performance_test())
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class PerformanceMonitor {
      private requestTimes: number[] = [];
      private errorCount: number = 0;
      
      async timedRequest(client: Perplexity, query: string) {
          const startTime = performance.now();
          try {
              const result = await client.search.create({ query });
              const duration = performance.now() - startTime;
              this.requestTimes.push(duration);
              return result;
          } catch (error) {
              this.errorCount++;
              throw error;
          }
      }
      
      getStats() {
          if (this.requestTimes.length === 0) {
              return { error: "No successful requests" };
          }
          
          return {
              totalRequests: this.requestTimes.length,
              errorCount: this.errorCount,
              avgResponseTime: this.requestTimes.reduce((a, b) => a + b, 0) / this.requestTimes.length,
              minResponseTime: Math.min(...this.requestTimes),
              maxResponseTime: Math.max(...this.requestTimes)
          };
      }
  }

  async function runPerformanceTest() {
      const monitor = new PerformanceMonitor();
      const client = new Perplexity();
      
      const queries = Array.from({ length: 10 }, (_, i) => `test query ${i}`);
      
      const tasks = queries.map(query => 
          monitor.timedRequest(client, query).catch(error => error)
      );
      
      await Promise.all(tasks);
      
      console.log(monitor.getStats());
  }

  runPerformanceTest();
  ```
</CodeGroup>

## Memory Optimization

### Efficient Data Processing

Process large datasets efficiently with streaming and pagination:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  async def process_large_dataset(queries, process_fn):
      """Process queries in batches to manage memory usage"""
      
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          
          async def process_single(query):
              try:
                  result = await client.search.create(query=query)
                  # Process immediately to avoid storing in memory
                  processed = process_fn(result)
                  # Clear the original result from memory
                  del result
                  return processed
              except Exception as e:
                  return f"Error processing {query}: {e}"
          
          # Process in small batches
          batch_size = 5
          for i in range(0, len(queries), batch_size):
              batch = queries[i:i + batch_size]
              
              # Process batch
              tasks = [process_single(query) for query in batch]
              batch_results = await asyncio.gather(*tasks)
              
              # Yield results instead of accumulating
              for result in batch_results:
                  yield result
              
              # Optional: Small delay to prevent overwhelming the API
              await asyncio.sleep(0.1)

  # Usage
  async def summarize_result(search_result):
      """Process function that extracts only what we need"""
      return {
          "query": search_result.query,
          "result_count": len(search_result.results),
          "top_title": search_result.results[0].title if search_result.results else None
      }

  async def main():
      queries = [f"query {i}" for i in range(100)]
      
      async for processed_result in process_large_dataset(queries, summarize_result):
          print(processed_result)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function* processLargeDataset<T>(
      queries: string[], 
      processFn: (result: any) => T
  ): AsyncGenerator<T | string> {
      const client = new Perplexity();
      
      async function processSingle(query: string): Promise<T | string> {
          try {
              const result = await client.search.create({ query });
              // Process immediately to avoid storing in memory
              const processed = processFn(result);
              return processed;
          } catch (error) {
              return `Error processing ${query}: ${error}`;
          }
      }
      
      // Process in small batches
      const batchSize = 5;
      for (let i = 0; i < queries.length; i += batchSize) {
          const batch = queries.slice(i, i + batchSize);
          
          // Process batch
          const tasks = batch.map(query => processSingle(query));
          const batchResults = await Promise.all(tasks);
          
          // Yield results instead of accumulating
          for (const result of batchResults) {
              yield result;
          }
          
          // Optional: Small delay to prevent overwhelming the API
          await new Promise(resolve => setTimeout(resolve, 100));
      }
  }

  // Usage
  function summarizeResult(searchResult: any) {
      return {
          query: searchResult.query,
          resultCount: searchResult.results.length,
          topTitle: searchResult.results[0]?.title || null
      };
  }

  async function main() {
      const queries = Array.from({ length: 100 }, (_, i) => `query ${i}`);
      
      for await (const processedResult of processLargeDataset(queries, summarizeResult)) {
          console.log(processedResult);
      }
  }

  main();
  ```
</CodeGroup>

## Best Practices

<Steps>
  <Step title="Use async for concurrent operations">
    Always use async clients when you need to process multiple requests simultaneously.

    <Tip>
      For CPU-bound processing after API calls, consider using worker threads or processes.
    </Tip>
  </Step>

  <Step title="Implement connection pooling">
    Configure appropriate connection limits based on your application's needs.

    <CodeGroup>
      ```python Python theme={null}
      # Good: Optimized for your use case
      limits = httpx.Limits(
          max_keepalive_connections=20,  # Based on expected concurrency
          max_connections=50,
          keepalive_expiry=30.0
      )
      ```

      ```typescript TypeScript theme={null}
      // Good: Optimized for your use case
      const agent = new https.Agent({
          keepAlive: true,
          maxSockets: 20,  // Based on expected concurrency
          keepAliveMsecs: 30000
      });
      ```
    </CodeGroup>
  </Step>

  <Step title="Monitor and tune performance">
    Use metrics to identify bottlenecks and optimize accordingly.

    <Warning>
      Don't optimize prematurely - measure first, then optimize based on actual performance data.
    </Warning>
  </Step>

  <Step title="Handle backpressure">
    Implement proper rate limiting and backpressure handling for high-throughput applications.

    <CodeGroup>
      ```python Python theme={null}
      # Use semaphores to limit concurrent requests
      semaphore = asyncio.Semaphore(10)  # Max 10 concurrent requests

      async def rate_limited_request(client, query):
          async with semaphore:
              return await client.search.create(query=query)
      ```

      ```typescript TypeScript theme={null}
      // Use a queue or throttling library
      import pLimit from 'p-limit';

      const limit = pLimit(10);  // Max 10 concurrent requests

      const rateLimitedRequest = (client: Perplexity, query: string) =>
          limit(() => client.search.create({ query }));
      ```
    </CodeGroup>
  </Step>
</Steps>

## Related Resources

<CardGroup>
  <Card title="Configuration" icon="settings" href="/docs/sdk/configuration">
    Optimize connection pooling and timeouts
  </Card>

  <Card title="Error Handling" icon="alert-triangle" href="/docs/sdk/error-handling">
    Handle errors in async operations
  </Card>
</CardGroup>
