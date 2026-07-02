---
title: "Error Handling"
source: https://docs.perplexity.ai/docs/sdk/error-handling
path: docs/sdk/error-handling
---

Learn how to handle API errors gracefully with the Perplexity SDKs for Python and TypeScript.

## Overview

The Perplexity SDKs provide robust error handling with specific exception types for different error scenarios. This guide covers how to catch and handle common API errors gracefully.

## Common Error Types

The SDKs provide specific exception types for different error scenarios:

* **APIConnectionError** - Network connection issues
* **RateLimitError** - API rate limit exceeded
* **APIStatusError** - HTTP status errors (4xx, 5xx)
* **AuthenticationError** - Invalid API key or authentication issues
* **ValidationError** - Invalid request parameters

## Basic Error Handling

Handle common API errors with try-catch blocks:

<CodeGroup>
  ```python Python theme={null}
  import perplexity
  from perplexity import Perplexity

  client = Perplexity()

  try:
      search = client.search.create(query="OpenAI o-series reasoning model benchmarks")
      print(search.results)
  except perplexity.APIConnectionError as e:
      print("Network connection failed")
      print(e.__cause__)
  except perplexity.RateLimitError as e:
      print("Rate limit exceeded, please retry later")
  except perplexity.APIStatusError as e:
      print(f"API error: {e.status_code}")
      print(e.response)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  try {
      const search = await client.search.create({ query: "OpenAI o-series reasoning model benchmarks" });
      console.log(search.results);
  } catch (error: any) {
      if (error.constructor.name === 'APIConnectionError') {
          console.log("Network connection failed");
          console.log(error.cause);
      } else if (error.constructor.name === 'RateLimitError') {
          console.log("Rate limit exceeded, please retry later");
      } else if (error.constructor.name === 'APIStatusError') {
          console.log(`API error: ${error.status}`);
          console.log(error.response);
      }
  }
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

<Info>
  Common HTTP status codes: 400 (Bad Request), 401 (Authentication), 403 (Permission Denied), 404 (Not Found), 429 (Rate Limit), 500+ (Server Error).
</Info>

## Advanced Error Handling

### Exponential Backoff for Rate Limits

Implement intelligent retry logic for rate limit errors:

<CodeGroup>
  ```python Python theme={null}
  import time
  import random
  import perplexity
  from perplexity import Perplexity

  def search_with_retry(client, query, max_retries=3):
      for attempt in range(max_retries):
          try:
              return client.search.create(query=query)
          except perplexity.RateLimitError:
              if attempt == max_retries - 1:
                  raise  # Re-raise on final attempt
              
              # Exponential backoff with jitter
              delay = (2 ** attempt) + random.uniform(0, 1)
              print(f"Rate limited. Retrying in {delay:.2f} seconds...")
              time.sleep(delay)
          except perplexity.APIConnectionError:
              if attempt == max_retries - 1:
                  raise
              
              # Shorter delay for connection errors
              delay = 1 + random.uniform(0, 1)
              print(f"Connection error. Retrying in {delay:.2f} seconds...")
              time.sleep(delay)

  # Usage
  client = Perplexity()
  result = search_with_retry(client, "artificial intelligence")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function searchWithRetry(
      client: Perplexity, 
      query: string, 
      maxRetries: number = 3
  ) {
      for (let attempt = 0; attempt < maxRetries; attempt++) {
          try {
              return await client.search.create({ query });
          } catch (error: any) {
              if (attempt === maxRetries - 1) {
                  throw error; // Re-throw on final attempt
              }

              if (error.constructor.name === 'RateLimitError') {
                  // Exponential backoff with jitter
                  const delay = (2 ** attempt + Math.random()) * 1000;
                  console.log(`Rate limited. Retrying in ${delay}ms...`);
                  await new Promise(resolve => setTimeout(resolve, delay));
              } else if (error.constructor.name === 'APIConnectionError') {
                  // Shorter delay for connection errors
                  const delay = (1 + Math.random()) * 1000;
                  console.log(`Connection error. Retrying in ${delay}ms...`);
                  await new Promise(resolve => setTimeout(resolve, delay));
              } else {
                  throw error; // Don't retry other errors
              }
          }
      }
  }

  // Usage
  const client = new Perplexity();
  const result = await searchWithRetry(client, "artificial intelligence");
  ```
</CodeGroup>

### Error Context and Debugging

Extract detailed error information for debugging:

<CodeGroup>
  ```python Python theme={null}
  import perplexity
  from perplexity import Perplexity

  client = Perplexity()

  try:
      chat = client.chat.completions.create(
          model="sonar-pro",
          messages=[{"role": "user", "content": "Explain how the 10-year US Treasury yield is determined and how it influences mortgage rates."}]
      )
  except perplexity.APIStatusError as e:
      print(f"Status Code: {e.status_code}")
      print(f"Error Type: {e.type}")
      print(f"Error Message: {e.message}")
      
      # Access raw response for detailed debugging
      if hasattr(e, 'response'):
          print(f"Raw Response: {e.response.text}")
          print(f"Request ID: {e.response.headers.get('X-Request-ID')}")
          
  except perplexity.ValidationError as e:
      print(f"Validation Error: {e}")
      # Handle parameter validation errors
      
  except Exception as e:
      print(f"Unexpected error: {type(e).__name__}: {e}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  try {
      const chat = await client.chat.completions.create({
          model: "sonar-pro",
          messages: [{ role: "user", content: "Explain how the 10-year US Treasury yield is determined and how it influences mortgage rates." }]
      });
  } catch (error: any) {
      if (error.constructor.name === 'APIStatusError') {
          console.log(`Status Code: ${error.status}`);
          console.log(`Error Type: ${error.type}`);
          console.log(`Error Message: ${error.message}`);
          
          // Access raw response for detailed debugging
          if (error.response) {
              console.log(`Raw Response: ${await error.response.text()}`);
              console.log(`Request ID: ${error.response.headers.get('X-Request-ID')}`);
          }
      } else if (error.constructor.name === 'ValidationError') {
          console.log(`Validation Error: ${error.message}`);
          // Handle parameter validation errors
      } else {
          console.log(`Unexpected error: ${error.constructor.name}: ${error.message}`);
      }
  }
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "ad29d443-937e-4a2d-8675-d1659072fa38",
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
          "content": "The **10‑year U.S. Treasury yield** is a *market‑determined interest rate* reflecting the return investors demand to lend to the U.S. government for 10 years, and it strongly **anchors long‑term mortgage rates**, which typically move in the same direction with a fairly stable spread above that yield.[1][2][3]\n\n---\n\n### 1. How the 10‑year Treasury yield is determined\n\n**What it is**\n\n- The 10‑year yield is the **yield to maturity** on a 10‑year Treasury note – the annualized return an investor earns if they buy the note at today’s market price and hold it until it matures in 10 years.[1][2]  \n- The note pays a fixed **coupon** (interest) twice a year on a face value (usually \\$1,000).[1]\n\n**Core mechanics: price vs. yield**\n\n- Treasuries trade in a secondary market after issuance, and their **price and yield move inversely**.[1][2]  \n  - If the note’s price **falls**, the fixed coupon becomes a higher return relative to the price paid, so **yield rises**.[1][2]  \n  - If the price **rises**, the same fixed coupon implies a lower return, so **yield falls**.[1][2]  \n- Example: A 10‑year note with a 3% coupon (\\$30/year on \\$1,000 face value):  \n  - At \\$1,000 price → yield ≈ 3%.  \n  - At \\$950 price → \\$30 interest on \\$950 → yield ≈ 3.16%.[1]  \n  - At \\$1,050 price → yield ≈ 2.86%.[1]  \n\n**Who sets the yield?**\n\n- There is **no fixed, administratively set 10‑year rate**; it is set by **supply and demand in the bond market**:  \n  - **Supply:** How many Treasuries the government issues to fund deficits.[2]  \n  - **Demand:** Domestic and global investors (banks, funds, foreign central banks, etc.) deciding how much they are willing to pay for Treasuries.\n\n**Key economic forces behind the yield**\n\nLong‑term yields embed expectations about future conditions over the life of the bond:\n\n1. **Expected path of short‑term interest rates (Fed policy)**  \n   - The Federal Reserve controls the federal funds rate (overnight interbank rate), which strongly influences other short‑term rates.[2]  \n   - The 10‑year yield is heavily influenced by what investors **expect the funds rate to average over the next decade**.[2]  \n   - If markets expect the Fed to keep rates **higher for longer** (tight policy), 10‑year yields tend to be higher, and vice versa.[2]\n\n2. **Expected inflation over the next 10 years**  \n   - Investors demand a higher nominal yield if they expect higher inflation to **compensate for erosion of purchasing power**.[2][3]  \n   - All else equal, higher expected inflation → higher 10‑year yield.[2][3]\n\n3. **Term premium and risk perception**  \n   - Investors usually require extra yield (a **term premium**) to lock up money for 10 years instead of rolling short‑term instruments, reflecting uncertainty about future rates, inflation, and market risk.[2]  \n   - Concerns about **default risk or political instability** (e.g., debt ceiling fights, rating downgrades) can raise yields by pushing prices down.[2]\n\n4. **Government deficits and bond supply**  \n   - Larger, persistent **budget deficits** mean more Treasury issuance; if demand does not keep up, prices fall and yields rise.[2]  \n\n**Official measurement**\n\n- The U.S. Treasury publishes **daily par yield curve rates** (including a 10‑year point), derived from closing market bid prices of the most recently auctioned securities.[4]  \n- The Federal Reserve’s FRED series **DGS10** is a widely used measure of the **market yield on 10‑year Treasuries at a constant maturity**, interpolated from the yield curve.[5]  \n\n---\n\n### 2. How the 10‑year Treasury yield influences mortgage rates\n\n**Mortgage rates use the 10‑year as a benchmark**\n\n- The 10‑year yield is a **reference point for many long‑term borrowing costs**, especially **30‑year fixed mortgage rates and high‑grade corporate bonds**.[2][3]  \n- Data show a **close correlation** between the 10‑year Treasury yield, the average 30‑year fixed mortgage rate, and top‑rated corporate bond yields.[2][3]  \n- Mortgage lenders typically set rates as:  \n\n  \\[\n  \\text{30‑year mortgage rate} \\approx \\text{10‑year Treasury yield} + \\text{spread}\n  \\]\n\n**Why use the 10‑year as the anchor for a 30‑year mortgage?**\n\n- Even though a standard fixed mortgage is **30 years**, most are **refinanced, paid off, or the home is sold** well before 30 years. The **average life is closer to 7–10 years**, so its risk profile is more comparable to a 10‑year bond than a full 30‑year bond.  \n- Investors who buy **mortgage‑backed securities (MBS)** look at the 10‑year yield as the risk‑free baseline and demand some extra yield above it.\n\n**What determines the mortgage–Treasury spread?**\n\nMortgage rates usually sit **1.5–3 percentage points** above the 10‑year yield, with the exact spread varying over time. That spread compensates lenders and MBS investors for:\n\n- **Credit risk:** Possibility of borrower default (Treasureis are near risk‑free; mortgages are not).  \n- **Prepayment and refinancing risk:** Borrowers can refinance or prepay if rates fall, which caps investors’ upside and complicates cash‑flow timing.  \n- **Servicing and origination costs:** Underwriting, processing, servicing the loan, and profits for lenders/investors.  \n- **Liquidity and market stress:** In times of financial stress, investors may demand much higher spreads over Treasuries for holding mortgages, widening the gap even if the 10‑year yield does not move much.\n\n**Direction of influence**\n\n- When the **10‑year yield rises** (for example, due to higher expected Fed rates or inflation), **mortgage rates almost always rise** as well, because lenders must keep a similar spread over the risk‑free rate to attract investors.[1][2][3]  \n- When the **10‑year yield falls**, mortgage rates tend to **decline**, although the spread can widen or narrow depending on credit conditions and MBS demand.[1][2]\n\n---\n\n### 3. Putting it together: from Fed and inflation to mortgage payments\n\nHere is the chain in simplified form:\n\n1. **Fed policy, inflation expectations, fiscal deficits, and risk sentiment** influence investor demand for Treasuries.  \n2. That demand sets **market prices** for 10‑year notes; from these prices we get the **10‑year yield**.[1][2][4][5]  \n3. The 10‑year yield becomes the **benchmark** for long‑term borrowing costs, including **mortgages**.[1][2][3]  \n4. Mortgage lenders price loans as **10‑year yield + risk/expense spread**, so mortgage rates move broadly in tandem with the 10‑year yield over time.[1][2][3]  \n\nIf you want, I can walk through a numeric example showing how a specific move in the 10‑year yield could translate into an approximate change in a 30‑year fixed mortgage rate and monthly payment.",
          "role": "assistant",
          "reasoning_steps": null,
          "tool_call_id": null,
          "tool_calls": null
        },
        "finish_reason": "stop"
      }
    ],
    "created": 1779896013,
    "model": "sonar-pro",
    "citations": [
      "https://public.com/learn/10-year-treasury-yield-meaning",
      "https://econofact.org/the-10-year-treasury-rate-why-is-it-important-and-what-can-policy-do-about-it",
      "https://www.youtube.com/watch?v=4sCDCcrH9Xs",
      "https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics",
      "https://fred.stlouisfed.org/series/DGS10"
    ],
    "object": "chat.completion",
    "search_results": [
      {
        "title": "What is the 10-year treasury yield?",
        "url": "https://public.com/learn/10-year-treasury-yield-meaning",
        "date": "2026-03-05",
        "last_updated": "2026-05-22",
        "snippet": "How is the 10-year treasury yield calculated? The yield is calculated based on the note's price and coupon payments. Let us understand this in ...",
        "source": "web"
      },
      {
        "title": "The 10-Year Treasury Rate: Why Is It Important and What Can Policy ...",
        "url": "https://econofact.org/the-10-year-treasury-rate-why-is-it-important-and-what-can-policy-do-about-it",
        "date": "2025-03-27",
        "last_updated": "2026-05-24",
        "snippet": "The 10-year Treasury yield (the “yield to maturity”) is what an investor would earn if they purchased a 10-year bond and held it to maturity.",
        "source": "web"
      },
      {
        "title": "The 10-year U.S. Treasury bond yield, explained - YouTube",
        "url": "https://www.youtube.com/watch?v=4sCDCcrH9Xs",
        "date": "2025-08-12",
        "last_updated": "2026-03-31",
        "snippet": "The 10-year U.S. Treasury bond yield may be poised to increase later this year. Fixed Income Strategist Brian Erickson answers the following ...",
        "source": "web"
      },
      {
        "title": "Interest Rate Statistics | U.S. Department of the Treasury",
        "url": "https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics",
        "date": "2025-12-01",
        "last_updated": "2026-05-26",
        "snippet": "Daily Treasury PAR Yield Curve Rates. This par yield curve, which relates the par yield on a security to its time to maturity, is based on the closing market ...",
        "source": "web"
      },
      {
        "title": "Market Yield on U.S. Treasury Securities at 10-Year Constant ...",
        "url": "https://fred.stlouisfed.org/series/DGS10",
        "date": "2026-05-26",
        "last_updated": "2026-05-26",
        "snippet": "View a 10-year yield estimated from the average yields of a variety of Treasury securities with different maturities derived from the Treasury yield curve.",
        "source": "web"
      }
    ],
    "status": null,
    "type": null,
    "usage": {
      "completion_tokens": 1645,
      "cost": {
        "input_tokens_cost": 6e-05,
        "output_tokens_cost": 0.02467,
        "total_cost": 0.03073,
        "citation_tokens_cost": null,
        "reasoning_tokens_cost": null,
        "request_cost": 0.006,
        "search_queries_cost": null
      },
      "prompt_tokens": 20,
      "total_tokens": 1665,
      "citation_tokens": null,
      "num_search_queries": null,
      "reasoning_tokens": null,
      "search_context_size": "low"
    }
  }
  ```
</Accordion>

## Error Recovery Strategies

### Graceful Degradation

Implement fallback mechanisms when API calls fail:

<CodeGroup>
  ```python Python theme={null}
  import perplexity
  from perplexity import Perplexity

  def get_ai_response(query, fallback_response="I'm sorry, I'm temporarily unavailable."):
      client = Perplexity()
      
      try:
          # Primary: Try online model
          response = client.chat.completions.create(
              model="sonar-pro",
              messages=[{"role": "user", "content": query}]
          )
          return response.choices[0].message.content
          
      except perplexity.RateLimitError:
          try:
              # Fallback: Try offline model if rate limited
              response = client.chat.completions.create(
                  model="llama-3.1-8b-instruct",
                  messages=[{"role": "user", "content": query}]
              )
              return response.choices[0].message.content
          except Exception:
              return fallback_response
              
      except perplexity.APIConnectionError:
          # Network issues - return cached response or fallback
          return fallback_response
          
      except Exception as e:
          print(f"Unexpected error: {e}")
          return fallback_response

  # Usage
  response = get_ai_response("What is machine learning?")
  print(response)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function getAIResponse(
      query: string, 
      fallbackResponse: string = "I'm sorry, I'm temporarily unavailable."
  ): Promise<string> {
      const client = new Perplexity();
      
      try {
          // Primary: Try online model
          const response = await client.chat.completions.create({
              model: "sonar-pro",
              messages: [{ role: "user", content: query }]
          });
          return response.choices[0].message.content as string || "";
          
      } catch (error: any) {
          if (error.constructor.name === 'RateLimitError') {
              try {
                  // Fallback: Try offline model if rate limited
                  const response = await client.chat.completions.create({
                      model: "llama-3.1-8b-instruct",
                      messages: [{ role: "user", content: query }]
                  });
                  return response.choices[0].message.content as string || "";
              } catch {
                  return fallbackResponse;
              }
          } else if (error.constructor.name === 'APIConnectionError') {
              // Network issues - return cached response or fallback
              return fallbackResponse;
          } else {
              console.log(`Unexpected error: ${error.message}`);
              return fallbackResponse;
          }
      }
  }

  // Usage
  const response = await getAIResponse("What is machine learning?");
  console.log(response);
  ```
</CodeGroup>

## Best Practices

<Steps>
  <Step title="Always handle rate limits">
    Rate limiting is common with API usage. Always implement retry logic with exponential backoff.

    <Warning>
      Don't implement aggressive retry loops without delays - this can worsen rate limiting.
    </Warning>
  </Step>

  <Step title="Log errors for monitoring">
    Include proper logging to track error patterns and API health.

    <CodeGroup>
      ```python Python theme={null}
      import logging
      import perplexity
      from perplexity import Perplexity

      logging.basicConfig(level=logging.INFO)
      logger = logging.getLogger(__name__)

      client = Perplexity()

      try:
          result = client.search.create(query="discovery of penicillin by Alexander Fleming")
      except perplexity.APIStatusError as e:
          logger.error(f"API Error {e.status_code}: {e.message}", 
                      extra={'request_id': e.response.headers.get('X-Request-ID')})
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      try {
          const result = await client.search.create({ query: "discovery of penicillin by Alexander Fleming" });
      } catch (error: any) {
          console.error(`API Error ${error.status}: ${error.message}`, {
              requestId: error.response?.headers.get('X-Request-ID')
          });
      }
      ```
    </CodeGroup>

    <Accordion title="Response">
      ```json theme={null}
      {
        "id": "cf46c6eb-bf6e-4ee4-97f8-9d4dcfd99dd4",
        "results": [
          {
            "snippet": "",
            "title": "Alexander Fleming Discovery and Development of Penicillin",
            "url": "https://www.acs.org/education/whatischemistry/landmarks/flemingpenicillin.html",
            "date": null,
            "last_updated": "2026-05-21"
          },
          {
            "snippet": "“*I did not invent penicillin.\nNature did that.\nI only discovered it by accident*.”\nAlexander Fleming was a Scottish physician-scientist who was recognised for discovering penicillin.\nThe simple discovery and use of the antibiotic agent has saved millions of lives, and earned Fleming – together with Howard Florey and Ernst Chain, who devised methods for the large-scale isolation and production of penicillin – the 1945 Nobel Prize in Physiology/Medicine.\n...\nIn 1928, Fleming began a series of experiments involving the common staphylococcal bacteria.\nAn uncovered Petri dish sitting next to an open window became contaminated with mould spores.\nFleming observed that the bacteria in proximity to the mould colonies were dying, as evidenced by the dissolving and clearing of the surrounding agar gel.\nHe was able to isolate the mould and identified it as a member of the *Penicillium* genus.\nHe found it to be effective against all Gram-positive pathogens, which are responsible for diseases such as scarlet fever, pneumonia, gonorrhoea, meningitis and diphtheria.\nHe discerned that it was not the mould itself but some ‘juice’ it had produced that had killed the bacteria.\nHe named the ‘mould juice’ penicillin.\nLater, he would say: “*When I woke up just after dawn on September 28, 1928, I certainly didn’t plan to revolutionize all medicine by discovering the world’s first antibiotic, or bacteria killer.\nBut I suppose that was exactly what I did*.”\nAlthough Fleming published the discovery of penicillin in the British Journal of Experimental Pathology in 1929, the scientific community greeted his work with little initial enthusiasm.\nAdditionally, Fleming found it difficult to isolate this precious ‘mould juice’ in large quantities.\nIt was not until 1940, just as he was contemplating retirement, that two scientists, Howard Florey and Ernst Chain, became interested in penicillin.\nIn time, they were able to mass-produce it for use during World War II.",
            "title": "Alexander Fleming (1881–1955): Discoverer of penicillin - PMC - NIH",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4520913/",
            "date": null,
            "last_updated": "2026-04-11"
          },
          {
            "snippet": "",
            "title": "Alexander Fleming - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Alexander_Fleming",
            "date": "2001-09-18",
            "last_updated": "2026-05-18"
          },
          {
            "snippet": "",
            "title": "Discovery of penicillin - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Discovery_of_penicillin",
            "date": "2009-09-13",
            "last_updated": "2026-03-28"
          },
          {
            "snippet": "",
            "title": "The Discovery of Penicillin—New Insights After More Than 75 Years ...",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5403050/",
            "date": null,
            "last_updated": "2026-03-29"
          },
          {
            "snippet": "The accidental discovery of a mouldy petri-dish in 1928 kickstarted a 20-year long journey to develop the world’s first mass produced drug that could clear a bacterial infection; penicillin.\n...\nIn 1928 Dr Alexander Fleming returned from a holiday to find mould growing on a Petri dish of Staphylococcus bacteria.\nHe noticed the mould seemed to be preventing the bacteria around it from growing.\nHe soon identified that the mould produced a self-defence chemical that could kill bacteria.\nHe named the substance penicillin.\nFleming published his findings and presented his discovery to the Medical Research Club.\nTo his surprise, his peers showed little interest in his work.\n...\nNearly ten years later in 1937, while investigating microorganisms and the substances they produced, Howard Florey and Ernst Chain uncovered Fleming’s research and assembled a team of scientists to work solely on the 'Penicillin Project'.\n...\nThe mould produced six times more penicillin than Fleming’s original strain.\n...\nBy 1943, the US had sufficient penicillin stocks to satisfy the demands of the Armed Forces of the United States, as well as their Allies.\n...\nIn 1946 penicillin became available for the first time in the UK for public use, it transformed medicine worldwide and ushered in the age of antibiotics.",
            "title": "How was penicillin developed?",
            "url": "https://www.sciencemuseum.org.uk/objects-and-stories/how-was-penicillin-developed",
            "date": "2021-02-23",
            "last_updated": "2025-11-10"
          },
          {
            "snippet": "Eighty-three years ago today, Sir Alexander Fleming discovered penicillin, one of the most widely used antibiotics.\nInspired by what he saw on the battlefields of World War I, he went back to his laboratory at St. Mary’s Hospital in London to develop a way to fight bacterial infections.\nIn 1928, he accidentally left a petri dish in which he was growing Staphylococcus aureus bacteria uncovered.\nLater, he noticed that there was mold growing on the plate, and around the mold, the staph bacteria were dead.\nFleming isolated it and identified the mold as Penicillium notatum, a type of fungus that is similar to the mold that grows on bread.\nFleming published his findings in the British Journal of Experimental Pathology in 1929, but the report didn’t garner much interest.\nThen in 1938, Ernst Chain, a biochemist working with pathologist Howard Florey at Oxford University, came across Fleming’s paper while he was researching antibacterial compounds.\nScientists in Florey’s lab started working with penicillin, which they eventually injected into mice to test if it could treat bacterial infections.\nTheir experiments were successful and they went on to test it in humans, where they also saw positive results.\nBy 1941, there was an injectable form that could be used to treat patients, which was especially useful for soldiers fighting in World War II.\n...\nIn 1945, Fleming, Chain and Florey were awarded the Nobel Prize in Physiology or Medicine for “the discovery of penicillin and its curative effects in various infectious diseases”.\nFleming died in 1955.",
            "title": "Penicillin: 83 Years Ago Today",
            "url": "https://www.publichealth.columbia.edu/research/center-infection-and-immunity/penicillin-83-years-ago-today",
            "date": "2015-10-16",
            "last_updated": "2026-03-12"
          },
          {
            "snippet": "",
            "title": "History of penicillin - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/History_of_penicillin",
            "date": "2006-03-31",
            "last_updated": "2026-04-08"
          },
          {
            "snippet": "Scottish bacteriologist Alexander Fleming is best known for his discovery of penicillin in 1928, which started the antibiotic revolution.\nFor his discovery of penicillin, he was awarded a share of the 1945 Nobel Prize for Physiology or Medicine.\n### How did Alexander Fleming discover penicillin?\nIn 1928 Alexander Fleming noticed that a culture plate of *Staphylococcus aureus* bacteria had become contaminated by a fungus.\nThe mold, later identified as *Penicillium notatum* (now classified as *P. chrysogenum*), had inhibited the growth of the bacteria.\nHe later established that the mold prevented bacterial growth because it produced an antibiotic, penicillin.\n...\n**Alexander Fleming** (born August 6, 1881, Lochfield Farm, Darvel, Ayrshire, Scotland—died March 11, 1955, London, England) was a Scottish bacteriologist best known for his discovery of penicillin.\n...\nHis work on wound infection and lysozyme, an antibacterial enzyme found in tears and saliva, guaranteed him a place in the history of bacteriology.\nBut it was his discovery of penicillin in 1928, which started the antibiotic revolution, that sealed his lasting reputation.\nFleming was recognized for that achievement in 1945, when he received the Nobel Prize for Physiology or Medicine, along with Australian pathologist Howard Walter Florey and German-born British biochemist Ernst Boris Chain, both of whom isolated and purified penicillin.\n...\nOn September 3, 1928, shortly after his appointment as professor of bacteriology, Fleming noticed that a culture plate of *Staphylococcus aureus* he had been working on had become contaminated by a fungus.\nA mold, later identified as *Penicillium notatum* (now classified as *P. chrysogenum*), had inhibited the growth of the bacteria.\nHe at first called the substance “mould juice” and then “penicillin,” after the mold that produced it.\nFleming decided to investigate further, because he thought that he had found an enzyme more potent than lysozyme.\nIn fact, it was not an enzyme but an antibiotic—one of the first to be discovered.\n...\nPenicillin eventually came into use during World War II as the result of the work of a team of scientists led by Howard Florey at the University of Oxford.",
            "title": "Alexander Fleming | Biography, Education, Discovery, Nobel Prize ...",
            "url": "https://www.britannica.com/biography/Alexander-Fleming",
            "date": "2026-04-24",
            "last_updated": "2026-04-25"
          },
          {
            "snippet": "Fleming’s serendipitous discovery of penicillin changed the course of medicine and earned him a Nobel Prize.\n...\nIn 1928 Alexander Fleming (1881–1955) discovered penicillin, though he did not realize the full significance of his discovery for at least another decade.\nHe eventually received the Nobel Prize in Physiology or Medicine in 1945.\n...\nIn 1928 Alexander Fleming discovered penicillin, made from the *Penicillium notatum* mold, but he did not receive the Nobel Prize in Physiology or Medicine for his discovery until 1945.\nFleming himself did not realize how important his discovery was; for a decade after, he focused instead on penicillin’s potential use as a topical antiseptic for wounds and surface infections and as a means of isolating certain bacteria in laboratory cultures.\n...\nFleming’s legendary discovery of penicillin occurred in 1928, while he was investigating staphylococcus, a common type of bacteria that causes boils and can also cause disastrous infections in patients with weakened immune systems.\nBefore Fleming left for a two-week vacation, a petri dish containing a staphylococcus culture was left on a lab bench and never placed in the incubator as intended.\nSomehow, in preparing the culture, a *Penicillium* mold spore had been accidentally introduced into the medium—perhaps coming in through a window, or more likely floating up a stairwell from the lab below where various molds were being cultured.\nThe temperature conditions that prevailed during Fleming’s absence permitted both the bacteria and the mold spores to grow; had the incubator been used, only the bacteria could have grown.\n...\nHe discovered that the antibacterial substance was not produced by all molds, only by certain strains of *Penicillium*, namely, *Penicillium notatum*.",
            "title": "Alexander Fleming | Science History Institute",
            "url": "https://www.sciencehistory.org/education/scientific-biographies/alexander-fleming/",
            "date": "2026-02-23",
            "last_updated": "2026-05-07"
          }
        ],
        "server_time": null
      }
      ```
    </Accordion>
  </Step>

  <Step title="Set appropriate timeouts">
    Configure timeouts to prevent hanging requests.

    <CodeGroup>
      ```python Python theme={null}
      import httpx
      from perplexity import Perplexity

      client = Perplexity(
          timeout=httpx.Timeout(connect=5.0, read=30.0, write=5.0, pool=10.0)
      )
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity({
          timeout: 30000 // 30 seconds
      });
      ```
    </CodeGroup>
  </Step>

  <Step title="Handle authentication errors">
    Check for invalid API keys and provide helpful error messages.

    <CodeGroup>
      ```python Python theme={null}
      try:
          result = client.search.create(query="Perplexity Search API Python SDK quickstart example")
      except perplexity.AuthenticationError:
          print("Invalid API key. Please check your PERPLEXITY_API_KEY environment variable.")
      ```

      ```typescript TypeScript theme={null}
      try {
          const result = await client.search.create({ query: "Perplexity Search API Python SDK quickstart example" });
      } catch (error: any) {
          if (error.constructor.name === 'AuthenticationError') {
              console.log("Invalid API key. Please check your PERPLEXITY_API_KEY environment variable.");
          }
      }
      ```
    </CodeGroup>

    <Accordion title="Response">
      ````json theme={null}
      {
        "id": "a3284d7c-f02c-45fc-82db-d368ad880edc",
        "results": [
          {
            "snippet": "",
            "title": "Quickstart - Perplexity API",
            "url": "https://docs.perplexity.ai/docs/getting-started/quickstart",
            "date": null,
            "last_updated": "2026-05-26"
          },
          {
            "snippet": "",
            "title": "Perplexity Search API",
            "url": "https://docs.perplexity.ai/docs/search/quickstart",
            "date": null,
            "last_updated": "2026-05-27"
          },
          {
            "snippet": "# Quickstart\n> Learn how to use the official Perplexity SDKs for Python and TypeScript to access the Perplexity APIs with type safety and async support.\n...\nThe official Perplexity SDKs provide convenient access to the Perplexity APIs from Python 3.8+ and Node.js applications.\nBoth SDKs include type definitions for all request parameters and response fields, with both synchronous and asynchronous clients.\nAccess four APIs: **Agent API** for third-party models with web search tools and presets, **Search** for ranked web search results, **Sonar** for web-grounded AI responses, and **Embeddings** for generating text embeddings.\n...\n<Card title=\"Search\" icon=\"search\" href=\"/docs/search/quickstart\">\nRanked web search results with filtering, multi-query support, and domain controls.\n...\n## Installation\nInstall the SDK for your preferred language:\n<CodeGroup>\n```bash Python theme={null}\npip install perplexityai\n```\n```bash TypeScript theme={null}\nnpm install @perplexity-ai/perplexity_ai\n```\n</CodeGroup>\n## Authentication\n<Card title=\"Get your Perplexity API Key\" icon=\"key\" arrow=\"True\" horizontal=\"True\" iconType=\"solid\" cta=\"Click here\" href=\"https://console.perplexity.ai\">\nNavigate to the **API Keys** tab in the API Portal and generate a new key.\n</Card>\nAfter generating the key, set it as an environment variable in your terminal:\n<Tabs>\n<Tab title=\"Windows\">\n```bash theme={null}\nsetx PERPLEXITY_API_KEY \"your_api_key_here\"\n```\n</Tab>\n<Tab title=\"MacOS/Linux\">\n```bash theme={null}\nexport PERPLEXITY_API_KEY=\"your_api_key_here\"\n```\n</Tab>\n</Tabs>\n### Using Environment Variables\nYou can use the environment variable directly:\n<CodeGroup>\n```python Python theme={null}\nimport os\nfrom perplexity import Perplexity\nclient = Perplexity() # Automatically uses PERPLEXITY_API_KEY\n```\n```typescript TypeScript theme={null}\nimport Perplexity from '@perplexity-ai/perplexity_ai';\nconst client = new Perplexity({\napiKey: process.env['PERPLEXITY_API_KEY'], // This is the default and can be omitted\n});\n```\n</CodeGroup>\nOr use [python-dotenv](https://pypi.org/project/python-dotenv/) (Python) or [dotenv](https://www.npmjs.com/package/dotenv) (Node.js) to load the environment variable from a `.env` file:\n<CodeGroup>\n```python Python theme={null}\nimport os\nfrom dotenv import load_dotenv\nfrom perplexity import Perplexity\nload_dotenv()\nclient = Perplexity() # Uses PERPLEXITY_API_KEY from .env file\n```\n```typescript TypeScript theme={null}\nimport Perplexity from '@perplexity-ai/perplexity_ai';\nimport dotenv from 'dotenv';\ndotenv.config();\nconst client = new Perplexity(); // Uses PERPLEXITY_API_KEY from .env file\n```\n</CodeGroup>\n<Tip>\nNow you're ready to start using the Perplexity APIs!\nChoose your API below for step-by-step usage guides.\n</Tip>\n<CardGroup cols={2}>\n<Card title=\"Agent API\" icon=\"code-circle\" href=\"/docs/agent-api/quickstart\">\nGet started with third-party models\n</Card>\n<Card title=\"Search\" icon=\"search\" href=\"/docs/search/quickstart\">\nGet started with web search\n</Card>\n...\nGet started with AI responses\n</Card>\n<Card title=\"Embeddings\" icon=\"cube\" href=\"/docs/embeddings/quickstart\">\nGet started with text embeddings\n...\nInstall from PyPI with pip\n</Card>\n<Card title=\"Node.js and TypeScript Package\" icon=\"brand-npm\" href=\"https://www.npmjs.com/package/@perplexity-ai/perplexity_ai\">\nInstall from npm registry\n</Card>\n</CardGroup>",
            "title": "Quickstart - Perplexity API",
            "url": "https://docs.perplexity.ai/docs/sdk/overview",
            "date": null,
            "last_updated": "2026-05-27"
          },
          {
            "snippet": "",
            "title": "Perplexity API",
            "url": "https://docs.perplexity.ai/docs/getting-started/overview",
            "date": null,
            "last_updated": "2026-05-26"
          },
          {
            "snippet": "The Perplexity Python library provides convenient access to the Perplexity REST API from any Python 3.8+\napplication.\nThe library includes type definitions for all request params and response fields,\nand offers both synchronous and asynchronous clients powered by httpx.\nIt is generated with Stainless.\n...\nThe REST API documentation can be found on docs.perplexity.ai.\nThe full API of this library can be found in api.md.\n## Installation\n```\n# install from PyPI\npip install perplexityai\n```\n## Search API\nGet web search results:\n```\nimport os\nfrom perplexity import Perplexity\nclient = Perplexity(\napi_key=os.environ.get(\"PERPLEXITY_API_KEY\"), # This is the default and can be omitted\n)\nsearch = client.search.create(\nquery=\"latest AI developments 2024\",\nmax_results=5\n)\nfor result in search.results:\nprint(f\"{result.title}: {result.url}\")\n```\n...\n```\n...\nfrom perplexity import Perplexity\nclient = Perplexity(\n...\n)\n...\nmessages=[\n{\n...\n\"content\": \"Tell me about the latest developments in AI\",\n}\n],\nmodel=\"sonar\",\n)\nprint(stream_chunk.id)\n```\n...\nSimply import `AsyncPerplexity` instead of `Perplexity` and use `await` with each API call:\n```\nimport os\nimport asyncio\nfrom perplexity import AsyncPerplexity\nclient = AsyncPerplexity(\napi_key=os.environ.get(\"PERPLEXITY_API_KEY\"), # This is the default and can be omitted\n)\nasync def main() -> None:\nstream_chunk = await client.chat.completions.create(\nmessages=[\n{\n\"role\": \"user\",\n\"content\": \"Tell me about the latest developments in AI\",\n}\n],\nmodel=\"sonar\",\n)\nprint(stream_chunk.id)\nasyncio.run(main())\n```\n...\nYou can enable this by installing `aiohttp`:\n```\n# install from PyPI\npip install perplexityai[aiohttp]\n```\nThen you can enable it by instantiating the client with `http_client=DefaultAioHttpClient()`:\n```\nimport asyncio\nfrom perplexity import DefaultAioHttpClient",
            "title": "perplexityai/perplexity-py - GitHub",
            "url": "https://github.com/perplexityai/perplexity-py",
            "date": "2025-09-25",
            "last_updated": "2025-10-19"
          },
          {
            "snippet": "## Get your Perplexity API Key\nNavigate to the **API Keys** tab in the API Portal and generate a new key.\nSee the API Groups page to set up an API group.\n**OpenAI SDK Compatible:** Perplexity’s API supports the OpenAI Chat Completions format.\nYou can use OpenAI client libraries by pointing to our endpoint.\n...\n## ​ Making Your First API Call\n- Python SDK\n- TypeScript SDK\n- cURL\n**Install the SDK first:** `pip install perplexityai`\n```\nfrom perplexity import Perplexity\n# Initialize the client (uses PERPLEXITY_API_KEY environment variable)\nclient = Perplexity()\n# Make the API call\ncompletion = client.chat.completions.create(\nmodel=\"sonar-pro\",\nmessages=[\n{\"role\": \"user\", \"content\": \"What were the results of the 2025 French Open Finals?\"}\n]\n)\n# Print the AI's response\nprint(completion.choices[0].message.content)\n```\nSet your API key as an environment variable: `export PERPLEXITY_API_KEY=\"your_api_key_here\"` (macOS/Linux) or `setx PERPLEXITY_API_KEY \"your_api_key_here\"` (Windows).",
            "title": "Quickstart",
            "url": "https://docs.perplexity.ai/getting-started/quickstart",
            "date": "2026-01-10",
            "last_updated": "2026-01-27"
          },
          {
            "snippet": "",
            "title": "Perplexity Search APIdocs.perplexity.ai › guides › search-quickstart",
            "url": "https://docs.perplexity.ai/docs/search/quickstart.md",
            "date": null,
            "last_updated": "2026-05-27"
          },
          {
            "snippet": "### 2.\nSearch API Quickstart (Python & TypeScript SDKs)\nThe docs recommend using official SDKs for safety and type-safety; you can also call the HTTP endpoint directly (POST https://api.perplexity.ai/search) with an Authorization header.\nBelow is a minimal Python example that mirrors the documented pattern.\n#### Basic Python example (client.search.create)\n# Example (conceptual) — mirrors docs pattern\nfrom perplexity import Client  # hypothetical SDK import style\nclient = Client(api_key=”YOUR_API_KEY”)\nresp = client.search.create(\nquery=”latest AI model research 2025″,\nmax_results=5\n)\n# Example response shape (simplified):\n# resp.results -> [ { “title”: “…”, “url”: “…”, “snippet”: “…”, “rank”: 1 }, … ]\nprint(resp.results[0][“title”], resp.results[0][“url”])\nThis call returns ranked results you can present to users or feed into an LLM for grounded synthesis.\nIf you prefer raw HTTP the docs provide a curl example for POST /search.\n...\nStart with the quickstart, use multi-query for depth, control content with max_tokens_per_page, and organize keys and billing via API Groups.",
            "title": "Mastering the Perplexity AI API Documentation",
            "url": "https://seabuckdigital.com/perplexity-ai-api-documentation/",
            "date": "2025-11-08",
            "last_updated": "2026-04-08"
          },
          {
            "snippet": "The Perplexity AI Toolkit makes it easy to use Perplexity Labs' `Sonar` language models (built on top of Meta's latest and most advanced model `LLama-3.1`) for creating chatbots, generating text, and searching the web (***in real-time** *).\nIt's designed for everyone, from beginners to experienced developers, allowing quick addition of AI features to projects with simple commands.\n...\n## Prerequisites\n- `Python 3.x`\n- An API key from Perplexity AI\n## Dependencies\nThe following Python packages are required:\n- `requests`: For making HTTP requests to the Perplexity API.\n...\n## Installation\nTo use the Perplexity AI Toolkit, clone the repository to your local machine and install the required Python packages.\nClone the repository:\n```\ngit clone https://github.com/RMNCLDYO/perplexity-ai-toolkit.git\n```\nNavigate to the repositories folder:\n```\ncd perplexity-ai-toolkit\n```\nInstall the required dependencies:\n```\npip install -r requirements.txt\n```\n## Configuration\n1. Obtain an API key from Perplexity.\n2. You have three options for managing your API key:\nClick here to view the API key configuration options - **Setting it as an environment variable on your device (recommended for everyday use)**\n- Navigate to your terminal.\n- Add your API key like so:\n```\nexport PERPLEXITY_API_KEY=your_api_key\n```\nThis method allows the API key to be loaded automatically when using the wrapper or CLI.\n- **Using an .env file (recommended for development):**\n- Install python-dotenv if you haven't already: `pip install python-dotenv`.\n- Create a .env file in the project's root directory.\n- Add your API key to the .env file like so:\n```\nPERPLEXITY_API_KEY=your_api_key\n```\nThis method allows the API key to be loaded automatically when using the wrapper or CLI, assuming you have python-dotenv installed and set up correctly.\n- **Direct Input:**\n- If you prefer not to use a `.env` file, you can directly pass your API key as an argument to the CLI or the wrapper functions.\n***CLI** *\n```\n--api_key \"your_api_key\"\n```\n***Wrapper** *\n```\napi_key=\"your_api_key\"\n```\n...\nThe Perplexity AI Toolkit can be used in two different modes: `Chat`, and `Search`.\n...\nChat mode is intended for chatting with an AI model (similar to a chatbot) or building conversational applications.\n#### Example Usage\n***CLI** *\n```\npython cli.py --chat\n```\n***Wrapper** *\n```\nfrom perplexity import Chat\nChat().run()\n```\n> An executable version of this example can be found here.\n(*You must move this file to the root folder before running the program.*)\n## Search Mode\nSearch mode is intended for searching online (in real-time) for a single query as perplexity does not support multi-turn conversations with their online models.\n#### Example Usage\n***CLI** *\n```\npython cli.py --search --query \"What is today's date?\"\n```\n***Wrapper** *\n```\nfrom perplexity import Search\nSearch().run(query=\"What is today's date?\")\n```\n> An executable version of this example can be found here.\n(*You must move this file to the root folder before running the program.*)\n*Search mode is limited to 'online' models, such as `llama-3.1-sonar-small-128k-online`, `llama-3.1-sonar-large-128k-online` and `llama-3.1-sonar-huge-128k-online`.*\n...\nA lightweight Python API wrapper and CLI for Perplexity’s Sonar language models.",
            "title": "RMNCLDYO/perplexity-ai-toolkit: A lightweight Python API ... - GitHub",
            "url": "https://github.com/RMNCLDYO/perplexity-ai-toolkit",
            "date": "2024-01-10",
            "last_updated": "2025-10-28"
          },
          {
            "snippet": "> Get started with Perplexity's Sonar API for web-grounded AI responses.\nMake your first API call in minutes.\n...\nPerplexity's Sonar API provides web-grounded AI responses with support for streaming, tools, search options, and more.\nYou can use it with OpenAI-compatible client libraries or our native SDKs for type safety and enhanced features.\nUse the Sonar API when you need web search capabilities built-in, streaming responses, or Perplexity's Sonar models.\n...\n## Installation\nInstall the SDK for your preferred language:\n<CodeGroup>\n```bash Python theme={null}\npip install perplexityai\n```\n```bash Typescript theme={null}\nnpm install @perplexity-ai/perplexity_ai\n```\n```bash OpenAI Python (Compatible) theme={null}\npip install openai\n```\n```bash OpenAI Typescript (Compatible) theme={null}\nnpm install openai\n```\n</CodeGroup>\n## Authentication\nSet your API key as an environment variable.\nThe SDK will automatically read it:\n<Tabs>\n<Tab title=\"macOS/Linux\">\n```bash theme={null}\nexport PERPLEXITY_API_KEY=\"your_api_key_here\"\n```\n</Tab>\n<Tab title=\"Windows\">\n```powershell theme={null}\nsetx PERPLEXITY_API_KEY \"your_api_key_here\"\n```\n</Tab>\n...\nAll SDK examples below automatically use the `PERPLEXITY_API_KEY` environment variable.\nYou can also pass the key explicitly if needed.\n...\n## Basic Usage\n### Non-Streaming Request\n<CodeGroup>\n```python Python SDK theme={null}\nfrom perplexity import Perplexity\nclient = Perplexity()\ncompletion = client.chat.completions.create(\nmodel=\"sonar-pro\",\nmessages=[\n{\"role\": \"user\", \"content\": \"What are the latest developments in quantum computing?\"}\n]\n)\nprint(completion.choices[0].message.content)\n```\n```typescript Typescript SDK theme={null}\nimport Perplexity from '@perplexity-ai/perplexity_ai';\nconst client = new Perplexity();\nconst completion = await client.chat.completions.create({\nmodel: \"sonar-pro\",\nmessages: [\n{ role: \"user\", content: \"What are the latest developments in quantum computing?\"\n}\n],\n});\nconsole.log(completion.choices[0].message.content);\n```\n```python OpenAI Python SDK theme={null}\nimport os\nfrom openai import OpenAI\nclient = OpenAI(\napi_key=os.environ.get(\"PERPLEXITY_API_KEY\"),\nbase_url=\"https://api.perplexity.ai\"\n)\nresp = client.chat.completions.create(\nmodel=\"sonar-pro\",\nmessages=[\n{\"role\": \"user\", \"content\": \"What are the latest developments in quantum computing?\"}\n]\n)\nprint(resp.choices[0].message.content)\n```\n```typescript OpenAI Typescript SDK theme={null}\nimport OpenAI from 'openai';\nconst client = new OpenAI({\napiKey: process.env.PERPLEXITY_API_KEY,\nbaseURL: \"https://api.perplexity.ai\"\n});\nconst resp = await client.chat.completions.create({\nmodel: \"sonar-pro\",\nmessages: [\n{ role: \"user\", content: \"What are the latest developments in quantum computing?\"\n}\n],\n});\nconsole.log(resp.choices[0].message.content);\n```\n```bash cURL theme={null}\ncurl https://api.perplexity.ai/v1/sonar \\\n-H \"Authorization: Bearer $PERPLEXITY_API_KEY\" \\\n-H \"Content-Type: application/json\" \\\n-d '{\n\"model\": \"sonar-pro\",\n\"messages\": [\n{\n\"role\": \"user\",\n\"content\": \"What are the latest developments in quantum computing?\"\n}\n]\n}' | jq\n```\n</CodeGroup>\n### Streaming Response\n<CodeGroup>\n```python Python SDK theme={null}\nfrom perplexity import Perplexity\nclient = Perplexity()\nstream = client.chat.completions.create(\nmodel=\"sonar-pro\",\nmessages=[\n{\"role\": \"user\", \"content\": \"What are the most popular open-source alternatives to OpenAI's GPT models?\"}\n],\nstream=True\n)\nfor chunk in stream:\nif chunk.choices[0].delta.content:\nprint(chunk.choices[0].delta.content, end=\"\")\n```\n```typescript Typescript SDK theme={null}\nimport Perplexity from '@perplexity-ai/perplexity_ai';\nconst client = new Perplexity();\nconst stream = await client.chat.completions.create({\nmodel: \"sonar-pro\",\nmessages: [\n{ role: \"user\", content: \"What are the most popular open-source alternatives to OpenAI's GPT models?\"\n}\n],\nstream: true,\n});\nfor await (const chunk of stream) {\nif (chunk.choices[0].delta.content) {\nprocess.stdout.write((chunk.choices[0]?.delta?.content ?? '') as string);\n}\n}\n```\n```bash cURL theme={null}\ncurl https://api.perplexity.ai/v1/sonar \\\n-H \"Authorization: Bearer $PERPLEXITY_API_KEY\" \\\n-H \"Content-Type: application/json\" \\\n-d '{\n\"model\": \"sonar-pro\",\n\"messages\": [\n{\n\"role\": \"user\",\n\"content\": \"What are the most popular open-source alternatives to OpenAI'\\''s GPT models?\"\n}\n],\n\"stream\": true\n}'\n```\n</CodeGroup>\n...\nGet raw search results with the Search API.",
            "title": "Sonar API - Perplexity",
            "url": "https://docs.perplexity.ai/docs/sonar/quickstart",
            "date": null,
            "last_updated": "2026-05-25"
          }
        ],
        "server_time": null
      }
      ````
    </Accordion>
  </Step>
</Steps>

## Related Resources

<CardGroup>
  <Card title="Configuration" icon="settings" href="/docs/sdk/configuration">
    Configure timeouts and retries
  </Card>

  <Card title="Best Practices" icon="star" href="/docs/sdk/best-practices">
    Environment variables and rate limiting
  </Card>
</CardGroup>
