---
title: "Search Date and Time Filters"
source: https://docs.perplexity.ai/docs/search/filters/date-time-filters
path: docs/search/filters/date-time-filters
---

<Note>
  The `search_after_date_filter` and `search_before_date_filter` parameters allow you to restrict search results to a specific publication date range. Only results with publication dates falling between these dates will be returned.

  The `last_updated_after_filter` and `last_updated_before_filter` parameters allow you to filter by when content was last modified or updated, rather than when it was originally published.

  The `search_recency_filter` parameter provides a convenient way to filter results by predefined time periods (e.g., "hour", "day", "week", "month", "year") relative to the current date.
</Note>

<Info>
  Specific date filters must be provided in the "%m/%d/%Y" format (e.g., "3/1/2025"). Recency filters use predefined values like "hour", "day", "week", "month", or "year". All filters are optional—you may supply either specific dates or recency filters as needed.
</Info>

## Overview

Date and time filters for the Search API allow you to control which search results are returned by limiting them to specific time periods. There are three types of date and time filters available:

### Publication Date Filters

The `search_after_date_filter` and `search_before_date_filter` parameters filter results based on when content was **originally created or published**. This is useful when you need to:

* Find content published within a specific timeframe
* Exclude outdated or overly recent publications
* Focus on content from a particular publication period

### Last Updated Date Filters

The `last_updated_after_filter` and `last_updated_before_filter` parameters filter results based on when content was **last modified or updated**. This is useful when you need to:

* Find recently updated or maintained content
* Exclude stale content that hasn't been updated recently
* Focus on content that has been refreshed within a specific period

### Search Recency Filter

The `search_recency_filter` parameter provides a simple way to filter results by predefined time periods relative to the current date. This is useful when you need to:

* Find content from the past hour, day, week, month, or year
* Get recent results without specifying exact dates
* Quickly filter for timely information

**Available values:**

* `"hour"` - Content from the past hour. Use for real-time data such as breaking news or live events.
* `"day"` - Content from the past 24 hours
* `"week"` - Content from the past 7 days
* `"month"` - Content from the past 30 days
* `"year"` - Content from the past 365 days

**Important:** Publication filters use the original creation/publication date, last updated filters use the modification date, while recency filters use a relative time period from the current date.

To constrain search results by publication date:

```bash theme={null}
"search_after_date_filter": "3/1/2025",
"search_before_date_filter": "3/5/2025"
```

To constrain search results by last updated date:

```bash theme={null}
"last_updated_after_filter": "07/01/2025",
"last_updated_before_filter": "12/30/2025"
```

To constrain search results by recency:

```bash theme={null}
"search_recency_filter": "week"
```

These filters will be applied in addition to any other search parameters.

## Examples

**1. Limiting Results by Publication Date Range**

This example limits search results to content published between March 1, 2025, and March 5, 2025.

**Request Example**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search.create(
      query="transformer architecture attention mechanism",
      max_results=10,
      search_after_date_filter="3/1/2025",
      search_before_date_filter="3/5/2025"
  )

  print(response)
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search.create({
    query: "transformer architecture attention mechanism",
    max_results: 10,
    search_after_date_filter: "3/1/2025",
    search_before_date_filter: "3/5/2025"
  });

  console.log(response);
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "transformer architecture attention mechanism",
      "max_results": 10,
      "search_after_date_filter": "3/1/2025",
      "search_before_date_filter": "3/5/2025"
    }' | jq
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "5cdd76b9-da5a-4f9f-8c75-61c90a2399a2",
    "results": [
      {
        "snippet": "",
        "title": "What is an attention mechanism?",
        "url": "https://www.ibm.com/think/topics/attention-mechanism",
        "date": "2024-12-05",
        "last_updated": "2026-03-31"
      },
      {
        "snippet": "",
        "title": "Introduction to Transformers and Attention Mechanisms",
        "url": "https://medium.com/@kalra.rakshit/introduction-to-transformers-and-attention-mechanisms-c29d252ea2c5",
        "date": "2024-02-07",
        "last_updated": "2025-10-29"
      },
      {
        "snippet": "",
        "title": "Transformer (deep learning) - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Transformer_(deep_learning)",
        "date": "2019-08-25",
        "last_updated": "2026-05-15"
      },
      {
        "snippet": "",
        "title": "Transformer (deep learning) - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)",
        "date": "2019-08-25",
        "last_updated": "2026-05-19"
      },
      {
        "snippet": "The famous paper “Attention is all you need” by Vaswani et al. presents the transformer architecture.\nThis neural network architecture builds on the attention mechanism and is at the core of current large language models (LLMs) such as ChatGPT, GPT-4, BERT, etc.\n...\nTransformers process sequences of tokens such as (sub-)words in a sentence.\nThe transformer architecture consists of two parts:\n1. The encoder, which processes the tokens of the input sequence and\n2. the decoder, which produces new tokens as output based on the input tokens and the previously produced output tokens.\nThe overall architecture is shown in the figure below with the encoder on the left and the decoder on the right side.\n...\nThe encoder (left side of the figure above), processes the tokens of the input sequence.\nEach token is initially embedded into a *d- * dimensional vector, e.g., using word2vec.\nIt is then processed individually and compared to other tokens in the input.\nThe process works with variable-length sequences.\nAfter embedding the words as vectors, a **positional encoding** is added, which indicates the absolute and relative position of the tokens in the sequence.\nThis is necessary for many tasks, particularly in natural language, since the later parts of the encoder are permutation invariant.\nThis means they do not distinguish the position of the tokens in the sequence.\n...\nAfter positional encoding, follows a **self-attention** block.\nDuring self-attention, the tokens *within the input sequence* are compared to each other, computing *attention weights.\n* A high attention weight for a pair of two tokens indicates that they are syntactically or semantically related.\nThus high weights indicate important tokens that the model should “attend” to.\n...\nFinally, a normal feed-forward neural network follows the attention block and outputs the encoded tokens one by one.\n...\nIn contrast to the encoder, the decoder contains a **cross-attention** block, which compares to the encoded tokens of the input sequence using cross-attention (explained in more detail below).\nThis cross-attention is at the heart of the decoder and helps producing the next output token, taking both the full input and the output produced so far into account.\n...\n## The Attention Mechanism\nThe attention mechanism is at the core of the transformer architecture — thus the paper title “Attention is all you need”.\nIn a transformer, the attention mechanism enables the model to assign different *attention weights/scores* to different tokens in a sequence.\nThis way, the model can give more importance to relevant information, ignore irrelevant information, and effectively capture long-range dependencies in the data.\nThe attention mechanism distinguishes three inputs: The **query Q, the key K, and the value V**.\nEach token in a sequence is a separate input for Q, K, or V.\nThe mechanism compares queries Q with keys K to determine their importance/compatibility to each other, computing attention weights.\nIt then selects corresponding values V with high attention weights.\nThis is an analogy to data bases, hash tables, or Python dictionaries, where we select the values whose keys match a given query best.\n...\n*Self- and cross-attention only differ in which tokens are given as inputs Q, K, and V.* In **self-attention**, the same tokens are used for all three inputs, i.e., each token is used for Q, K, and V.\nIn **cross-attention**, the same tokens are given to K and V, but different tokens are used for Q.\nSelf-attention is applied to the input sequence in the encoder and to the output sequence in the decoder.\nThe decoder’s cross-attention module then uses the encoded input tokens as K and V and the produced output tokens as Q.\nIn either case, attention weights between tokens in Q and in K are calculated using scaled dot-product attention.\nWhile there are other forms of attention such as learned attention weights, scaled dot-product attention is faster and more space efficient.\nIn scaled dot-product attention, attention weights are computed without extra parameters as illustrated in the figure below: Tokens in Q and K are multiplied, scaled, and passed through a softmax function to obtain attention weights.\nThe attention weights are then multiplied with the tokens in V to select values with high corresponding weights.\n...\nMulti-head attention repeats the attention mechanism explained above multiple times (*h * times) in parallel.\nBefore passing the input tokens of dimension *d * into these *h * attention blocks, they projected into smaller embeddings of size* d/h * by using small linear neural networks*.\n* Each of the *h * linear networks has different weights and leads to different projections.\nConsequently, each attention “head” can learn to focus on different aspects, e.g., subject and object of a sentence.\nThe outputs of the *h* heads are then concatenated and passed through another linear neural network.\n...\nOverall, attention is a surprisingly simple yet effective mechanism to emphasize meaningful tokens and ignore less meaningful tokens.\nBased on this mechanism, transformers can take capture the context even in long sequences and produce coherent outputs.",
        "title": "Understanding Transformers and Attention | by Stefan",
        "url": "https://medium.com/@stefanbschneider/understanding-attention-and-transformers-d84b016cd352",
        "date": "2023-11-28",
        "last_updated": "2025-10-27"
      },
      {
        "snippet": "",
        "title": "Attention in transformers, step-by-step | Deep Learning Chapter 6",
        "url": "https://www.youtube.com/watch?v=eMlx5fFNoYc&vl=en",
        "date": "2024-04-07",
        "last_updated": "2026-05-26"
      },
      {
        "snippet": "At the present moment, the dominant models for nearly all natural\nlanguage processing tasks are based on the Transformer architecture.\n...\nThe core idea behind the Transformer model is the *attention mechanism*, an innovation that was originally envisioned as an enhancement for encoder–decoder RNNs applied to sequence-to-sequence applications, such as machine translations ().\nYou might recall that in the first sequence-to-sequence models for machine translation (), the entire input was compressed by the encoder into a single fixed-length vector to be fed into the decoder.\nThe intuition behind attention is that rather than compressing the input, it might be better for the decoder to revisit the input sequence at every step.\nMoreover, rather than always seeing the same representation of the input, one might imagine that the decoder should selectively focus on particular parts of the input sequence at particular decoding steps.\nBahdanau’s attention mechanism provided a simple means by which the decoder could dynamically *attend* to different parts of the input at each decoding step.\nThe high-level idea is that the encoder could produce a representation of length equal to the original input sequence.\nThen, at decoding time, the decoder can (via some control mechanism) receive as input a context vector consisting of a weighted sum of the representations on the input at each time step.\nIntuitively, the weights determine the extent to which each step’s context “focuses” on each input token, and the key is to make this process for assigning the weights differentiable so that it can be learned along with all of the other neural network parameters.\nInitially, the idea was a remarkably successful enhancement to the\n...\nHowever, attention mechanisms soon emerged as more significant concerns,\nbeyond their usefulness as an enhancement for encoder–decoder recurrent\nneural networks and their putative usefulness for picking out salient\ninputs.\nVaswani *et al.* () proposed the Transformer architecture for machine translation, dispensing with recurrent connections altogether, and instead relying on cleverly arranged attention mechanisms to capture all relationships among input and output tokens.",
        "title": "11. Attention Mechanisms and Transformers - Dive into Deep Learning",
        "url": "http://www.d2l.ai/chapter_attention-mechanisms-and-transformers/index.html",
        "date": null,
        "last_updated": "2026-03-12"
      },
      {
        "snippet": "",
        "title": "The self-attention mechanism",
        "url": "https://www.codecademy.com/article/transformer-architecture-self-attention-mechanism",
        "date": "2025-09-19",
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "",
        "title": "How Attention Mechanism Works in Transformer Architecture",
        "url": "https://www.youtube.com/watch?v=KMHkbXzHn7s",
        "date": "2025-03-08",
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "",
        "title": "Transformer (deep learning architecture) - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Grouped-query_attention",
        "date": "2025-03-14",
        "last_updated": "2025-03-15"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

**2. Filtering with a Single Publication Date Parameter**

If you only wish to restrict the results to those published on or after a specific date, include just the `search_after_date_filter`:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search.create(
      query="tech industry layoffs at major technology companies",
      max_results=10,
      search_after_date_filter="3/1/2025"
  )

  print(response)
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search.create({
    query: "tech industry layoffs at major technology companies",
    max_results: 10,
    search_after_date_filter: "3/1/2025"
  });

  console.log(response);
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "tech industry layoffs at major technology companies",
      "max_results": 10,
      "search_after_date_filter": "3/1/2025"
    }' | jq
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "de495208-dca3-4c87-b69a-6f2eecea26dc",
    "results": [
      {
        "snippet": "114,173 tech employees laid off ∙ 148 tech companies w/ layoffs ∙",
        "title": "Layoffs.fyi - Tech and Startup Layoff Tracker",
        "url": "https://layoffs.fyi",
        "date": "2026-02-03",
        "last_updated": "2026-05-20"
      },
      {
        "snippet": "",
        "title": "Tech Layoffs: US Companies With Job Cuts In 2024, 2025 and 2026",
        "url": "https://news.crunchbase.com/startups/tech-layoffs/",
        "date": "2026-05-14",
        "last_updated": "2026-05-15"
      },
      {
        "snippet": "Meta to Cut 10% of Workforce in Latest AI-Driven Tech Layoffs - NerdWallet\n...\nIn 2026, tech layoffs are surging, with major companies citing AI development as a key driver.\n...\nUpdated April 23.\nSo far in 2026, roughly 98 tech companies have laid off over 92,000 workers.\nSeveral major companies have explicitly pointed to investments in AI research and development as the driving force behind recent job cuts.\n- Amazon announced on Jan. 28 it would cut about 16,000 more roles across the company, following an October trim of 14,000 jobs.\n- In February, Block — led by Twitter co-founder Jack Dorsey — cut 4,000 jobs, or about 40% of its staff.\n- On March 11, Atlassian laid off 1,600 workers.\n- On March 16, Dell said it reduced its global staff by 10%, or nearly 11,000 workers.\n- On April 6, Oracle laid off 30,000 workers to fund its AI infrastructure initiatives.\n- On April 23, Meta said it would cut 10% of its workforce — about 8,000 jobs — and close 6,000 open roles as it zeroes in on AI development.\n...\nSo far in 2026, roughly 98 tech companies have laid off more than 92,000 workers.\n...\n## What tech layoffs happened in 2025?\nThe total number of tech layoffs in 2025 was 122,549 across 257 companies according to layoffs.fyi., which tracks job cuts in the tech industry.\nThat’s down from 152,922 employees laid off from 551 companies in 2024, according to layoffs.fyi.\nCompanies that announced layoffs in waves of more than 10,000 workers included some of the biggest names in tech: Intel, Amazon, Tesla, Google, Meta and Microsoft.\n...\nThe majority of layoffs at the beginning of 2022 came from startups, according to Lee.\nBut in late 2022 and early 2023 it started to creep into bigger tech, as well.\nLee also said that “Big Tech” layoffs like those seen at Meta and Twitter “present a unique opportunity to recruit a caliber of talent that would've previously been impossible to attract.”",
        "title": "Meta to Cut 10% of Workforce in Latest AI-Driven Tech Layoffs",
        "url": "https://www.nerdwallet.com/finance/learn/tech-layoffs",
        "date": "2022-12-01",
        "last_updated": "2026-05-22"
      },
      {
        "snippet": "",
        "title": "Companies that announced Major Layoffs and Hiring Freezes",
        "url": "https://intellizence.com/insights/layoff-downsizing/major-companies-that-announced-mass-layoffs/",
        "date": "2026-05-11",
        "last_updated": "2026-05-18"
      },
      {
        "snippet": "",
        "title": "Major tech layoffs: An updated tracker - InformationWeek",
        "url": "https://www.informationweek.com/it-leadership/tech-company-layoffs-the-covid-tech-bubble-bursts-sep-14",
        "date": "2026-01-05",
        "last_updated": "2026-05-26"
      },
      {
        "snippet": "Layoffs are making headlines, and most seem to be centered on one job sector -- tech.\nJanuary layoffs were the highest they've been since 2009, according to a report from Challenger, Gray & Christmas, including 22,291 job cuts in the tech sector.\nThe bulk of these came from a round of Amazon layoffs that cut 16,000 jobs, disproportionately affecting tech roles, including AWS.\nGoogle and Pinterest also announced cuts in January.\nIn 2025, 271 tech companies laid off more than 124,201 employees, according to Layoffs.fyi, compared to 152,922 employees in 2024 and 264,320 in 2023.\nUnlike previous layoff surges during and after the COVID-19 crisis, layoffs are now more focused on restructuring driven by AI and slow market growth, rather than emergency cost-cutting.\nTech roles have accounted for a large share of recent layoffs due to AI integration and AI-related job consolidation, but roles affected by layoffs go far beyond tech.\nHowever, in a high-volume sector, tech layoffs tend to have more visibility because a small percentage of layoffs still translates to thousands of people losing their jobs.\nThere are several factors contributing to tech layoffs, including uncertain macroeconomic conditions, market instability and the scaling of AI.\n...\nAI is now the top influence on layoff decisions, cited more frequently by HR leaders than industry or market trends, according to a CareerMinds report.\n...\nAI was cited as the reason for nearly 55,000 layoffs in 2025, according to Challenger, Gray & Christmas.\nIn the coming year, 32% of companies expect a decrease in workforce size due to AI, according to a McKinsey report.\n...\nThis has led to layoffs due to role redesigns that move away from administrative, repetitive tasks and toward high-level oversight of automated processes and technology.\n...\nIn 2025, 55% of companies conducting layoffs cited economic uncertainty, according to a Resume.org survey.\nSix in 10 companies plan to conduct layoffs in 2026.\n...\nPepsiCo announced job cuts and plant closures, as well as slashing 20% of its products, in relation to an agreement with Elliott Investment Management to improve operational efficiency and cut costs.\n...\nTech layoffs may also result from the industry maturing or becoming more stable after rapid growth.\nDuring the pandemic and into the AI boom, tech companies saw rapid expansions both in operations and hiring.\nNow, many companies are conducting layoffs to stabilize and correct unsustainable growth.\nTech companies may not be on pace to acquire as many new customers as they have already adopted their services.\nInstead, tech companies may be looking beyond growth and into diversifying products or expanding globally.\nOrganizations are also prioritizing workforce consolidation and operational discipline to accommodate market shifts and slower revenue growth.\n...\nMany companies are also laying off workers due to shifts in skill demands.\nAI skills are splitting the market, creating a gap between AI-skilled and non-AI-skilled workers.\n...\nIn September 2025, Accenture's CEO announced layoff plans, targeting employees who couldn't reskill on AI, resulting in 11,000 job cuts.\n...\nDepending on the size of the company, large layoffs may range from a few hundred to tens of thousands, which can be a large percentage of its workforce.\nSome big tech companies -- such as Amazon and Meta -- have announced large layoffs in waves.\nIn October 2025, Amazon announced 14,000 job cuts.\nIn January 2026, they cut 16,000 more jobs.\nSalesforce eliminated more than 4,000 customer support roles in June 2025.\nIts CEO Marc Benioff cited AI, saying that it was already doing 30-50% of the work at the company.\nIn April 2025, Intel cut 20% of its workforce, more than 21,000 roles in a restructuring under new executive leadership.\nHP announced plans to cut 6,000 roles by the end of the 2028 fiscal year in an AI-focused restructuring.\nLayoffs are still rampant across the tech sector in 2026.\nAs of this writing, 35,650 tech employees from 50 tech companies have been laid off, according to Layoffs.fyi.",
        "title": "Tech sector layoffs explained: What you need to know - TechTarget",
        "url": "https://www.techtarget.com/whatis/feature/Tech-sector-layoffs-explained-What-you-need-to-know",
        "date": "2026-03-06",
        "last_updated": "2026-05-23"
      },
      {
        "snippet": "",
        "title": "Tech Companies That Have Made Layoffs from 2022 to 2026",
        "url": "https://tech.co/news/tech-companies-layoffs",
        "date": "2023-02-27",
        "last_updated": "2026-05-22"
      },
      {
        "snippet": "",
        "title": "A comprehensive list of 2025 tech layoffs | TechCrunch",
        "url": "https://techcrunch.com/2025/12/22/tech-layoffs-2025-list/",
        "date": "2025-12-22",
        "last_updated": "2026-05-26"
      },
      {
        "snippet": "",
        "title": "2026 Tech Layoffs Tracker - SkillSyncer",
        "url": "https://skillsyncer.com/layoffs-tracker",
        "date": null,
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "Big Tech companies laid off hundreds of employees in recent days, commanding headlines and confronting workers across the economy with a question: Am I next?\nAmazon and Google each imposed cuts, with Apple shutting down a 121-person team in San Diego, Calif., telling workers they must either transfer to Texas or leave the company, Bloomberg reported.\nIn all, the tech sector has laid off nearly 8,000 workers so far this year, according to layoffs.fyi, a site that tracks tech-sector employment.\nThe job cuts stem in large part from an ongoing staff reevaluation specific to the tech industry, since sales have retreated from the blistering pace attained during the pandemic, analysts said, noting comparatively scant layoffs across the wider workforce.\nHowever, the recent cutbacks in tech also are due to the rise of artificial intelligence and the persistence of high interest rates, some analysts said, foretelling similar risks for workers across major swathes of the economy.MORE: Bank overdraft fees may soon plummet.\nHere's what to know.\n...\nEven the job cuts in tech are relatively small compared with tens of thousands of employees laid off at the outset of last year.\n...\nLayoffs at Google, for instance, affected hundreds of workers focused on the company's well-known products, such as Google Assistant, as well as Google-owned YouTube.\nThe cuts came in part from the company's priority shift toward AI, according to an internal memo from CEO Sundar Pichai, confirmed to ABC News by a Google spokesperson.\n...\n\"Tech companies are hiring and firing on a small scale very often because they're still experimenting with how to commercialize and scale AI,\" Daniel Keum, a professor of management at the Columbia University Business School, told ABC News.\n...\nReluctant to overstate the risk, however, Kayes downplayed the recent job cuts in tech.\n\"These are fairly small layoffs,\" he said.",
        "title": "Big Tech layoffs are back. Are other workers at risk?",
        "url": "https://abcnews.go.com/amp/Business/big-tech-layoffs-back-workers-risk/story?id=106476154",
        "date": "2024-01-18",
        "last_updated": "2025-03-07"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

**3. Filtering by Last Updated Date Range**

This example limits search results to content that was last updated between July 1, 2025, and December 30, 2025. This is useful for finding recently maintained or refreshed content.

**Request Example**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search.create(
      query="machine learning interpretability research methods",
      max_results=10,
      last_updated_after_filter="07/01/2025",
      last_updated_before_filter="12/30/2025"
  )

  print(response)
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search.create({
    query: "machine learning interpretability research methods",
    max_results: 10,
    last_updated_after_filter: "07/01/2025",
    last_updated_before_filter: "12/30/2025"
  });

  console.log(response);
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "machine learning interpretability research methods",
      "max_results": 10,
      "last_updated_after_filter": "07/01/2025",
      "last_updated_before_filter": "12/30/2025"
    }' | jq
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "43425e11-87b1-4ba6-82f6-d399c308f4a6",
    "results": [
      {
        "snippet": "### Model-agnostic interpretability methods\n\nSeveral important model-agnostic interpretability methods exist, and while none of them are perfect, they can help researchers interpret the results of even very complex ML models.\n\nFor demonstration purposes, let’s consider a small time-series dataset. A time series is simply a series of data points indexed in time order. It is the most common type of data in the financial industry. A frequent goal of quantitative research is to identify trends, seasonal variations, and correlation in financial time series data using statistical and machine learning methods.\n\n…\n\n#### Method 1: Partial Dependence Plot (PDP)\n\nThe first method we’ll examine is Partial Dependence Plot or PDP, which was invented decades ago, and shows the marginal effect that one or two features have on the predicted outcome of a machine learning model.\n\nIt helps researchers determine what happens to model predictions as various features are adjusted.\n\nHere in this plot, the x-axis represents the value of feature f0, and the y-axis represents the predicted value. The solid line in the shaded area shows how the average prediction varies as the value of f0 changes.\nPDP is very intuitive and easy to implement, but because it only shows the average marginal effects, **heterogeneous effects might be hidden**.^1^ For example, one feature might show a positive relationship with prediction for half of the data, but a negative relationship for the other half. The plot of the PDP will simply be a horizontal line.\n\n…\n\n##### PDP vs. ICE vs. Feature Importance\n\nAll three of the methods above are intuitive and easy to implement.\n\nPDP shows global effects, while hiding heterogeneous effects. ICE can uncover heterogeneous effects, but makes it hard to see the average.\n\nFeature importance provides a concise way to understand the model’s behavior. The use of error ratio (instead of the error) makes the measurements comparable across different problems. And it automatically takes into account all interactions with other features.\nHowever, the interactions are not additive. Adding up feature importance does not result in a total drop in performance. Shuffling the features adds randomness, so the results may be different each time. Also, the shuffling requires access to true outcomes, which is impossible for many scenarios.\n\nBesides, all three methods assume the independence of the features, so if features are correlated, unlikely data points will be created and the interpretation can be biased by these unrealistic data points.\n\n#### Method 4: Global Surrogate\n\nThe global surrogate method takes a different approach. In this case, an interpretable model is trained to approximate the prediction of a black box model.\n\nThe process is simple. First you get predictions on a dataset with the trained black box model, and then train an interpretable model on this dataset and predictions. The trained interpretable model now becomes a surrogate of the original model, and all we need to do is to interpret the surrogate model. Note, the surrogate model could be any interpretable model: linear model, decision tree, human defined rules, etc.\n\n…\n\nFirst the image on the left is divided into interpretable components. LIME then generates a dataset of perturbed instances by turning some of the interpretable components “off” (in this case, making them gray).\n\nFor each perturbed instance, one can use the trained model to get the probability that a tree frog is in the image, and then learn a locally weighted linear model on this dataset.\n\n…\n\n##### Global vs. Local Surrogate Methods\n\nBoth the global and local surrogate methods have advantages and disadvantages.\n\nGlobal surrogate cares about explaining the whole logic of the model, while local surrogate is only interested in understanding specific predictions.\n\nWith the global surrogate method, any interpretable model can be used as surrogate, and the closeness of the surrogate models to the black box models can easily be measured.\nHowever, since the surrogate models are trained only on the predictions of the black box model instead of the real outcome, they can only interpret the model, and not the data. Besides, the surrogate models, which are simpler than the black box model in a lot of cases, may only be able to give good explanations to part of the data, instead of the entire dataset.\nThe local surrogate method, on the other hand, does not share these shortcomings. In addition, the local surrogate method is model-agnostic: If you need to try a different black box model for your problem, you can still use the same surrogate models for interpretations. And compared with interpretations given by global surrogate methods, the interpretations from local surrogate methods are often short, contrastive, and human-friendly.\nHowever, local surrogate has its own issues.\n\nFirst, LIME uses a kernel to define the area within which data points are considered for local explanations, but it is difficult to find the proper kernel setting for a task. The way sampling is done in LIME can lead to unrealistic data points, and the local interpretation can be biased towards those data points.\nAnother concern is the instability of the explanations. Two very close points could lead to two very different explanations.\n\n…\n\n##### Shapley Value vs. LIME\n\nAs data scientist Christoph Molnar points out in* Interpretable Machine Learning*, the Shapley Value might be the only method to deliver a full interpretation, and it is the explanation method with the strongest theoretical basis.\n\nThere are, however, trade-offs. Calculating the Shapley Value is computationally expensive. The recently developed kernel SHAP method does a fast kernel approximation to solve this problem, but for large background data, it still costs a lot of computation.\n\n…\n\n- **Application-grounded** evaluation requires a human to perform experiments within a real-life application.^4^ For example, to evaluate an interpretation on diagnosing a certain disease, the best way is for the doctor to perform diagnoses.\n- **Human-grounded** evaluation is about conducting simpler human-subject experiments. For example, humans are presented with pairs of explanations, and must choose the one that they find to be of higher quality.",
        "title": "Interpretability Methods in Machine Learning: A Brief Survey",
        "url": "https://www.twosigma.com/articles/interpretability-methods-in-machine-learning-a-brief-survey/",
        "date": "2019-06-25",
        "last_updated": "2026-04-01"
      },
      {
        "snippet": "",
        "title": "2 Interpretability – Interpretable Machine Learning",
        "url": "https://christophm.github.io/interpretable-ml-book/interpretability.html",
        "date": null,
        "last_updated": "2026-05-16"
      },
      {
        "snippet": "## Type 3 interpretability: unraveled rules and laws\n\nWith this type of interpretability, we seek to discover “rules” and “laws” learned by the machine model. These can be in the form of decision rules, or even “counterfactual” explanations in the form of “What if?” question-answer pairs that describe the smallest adjustment to the patient’s features that would change the model’s prediction to a predefined output. For example, a clinician could use this type of interpretability to establish the smallest difference in tumor size that would change the model’s prediction for a patient with cancer.\n\n…\n\nUsing five familiar data sets from the UCI repository and two familiar machine learning algorithms, we demonstrate that our algorithm produces global interpretations that are both faithful (highly accurate) and parsimonious (involve a small number of terms). Our interpretations permit easy understanding of the relative importance of features and feature interactions. Our interpretation algorithm represents a leap forward from the previous state of the art.\n\n…\n\nThrough this rigorous formalism, we derive (1) two metrics to measure the robustness of any interpretability method with respect to the model symmetry group; (2) theoretical robustness guarantees for some popular interpretability methods and (3) a systematic approach to increase the invariance of any interpretability method with respect to a symmetry group. By empirically measuring our metrics for explanations of models associated with various modalities and symmetry groups, we derive a set of 5 guidelines that we present in-depth to allow users and developers of interpretability methods to produce robust explanations.\n\n### Evaluating the Robustness of Interpretability Methods through Explanation Invariance and Equivariance\n\nJonathan Crabbé, Mihaela van der Schaar\n\n*NeurIPS 202*3\n\n**Abstract**\n\nInterpretability methods are valuable only if their explanations faithfully describe the explained model. In this work, we consider neural networks whose predictions are invariant under a specific symmetry group. This includes popular architectures, ranging from convolutional to graph neural networks.\nAny explanation that faithfully explains this type of model needs to be in agreement with this invariance property. We formalize this intuition through the notion of explanation invariance and equivariance by leveraging the formalism from geometric deep learning. Through this rigorous formalism, we derive (1) two metrics to measure the robustness of any interpretability method with respect to the model symmetry group; (2) theoretical robustness guarantees for some popular interpretability methods and (3) a systematic approach to increase the invariance of any interpretability method with respect to a symmetry group.\nBy empirically measuring our metrics for explanations of models associated with various modalities and symmetry groups, we derive a set of 5 guidelines to allow users and developers of interpretability methods to produce robust explanations.",
        "title": "Interpretable machine learning - van der Schaar Lab",
        "url": "https://www.vanderschaar-lab.com/interpretable-machine-learning/",
        "date": "2024-05-31",
        "last_updated": "2026-02-02"
      },
      {
        "snippet": "This taxonomy focuses on the purpose that these methods were created to serve and the ways through which they accomplish this purpose. As a result, according to the presented taxonomy, four major categories for interpretability methods are identified: methods for explaining complex black-box models, methods for creating white-box models, methods that promote fairness and restrict the existence of discrimination, and, lastly, methods for analysing the sensitivity of model predictions.\n\n…\n\nIn order to address this issue, after introducing a quality criterion for neuron-wise signal estimators in order to evaluate existing methods and ultimately obtain estimators that optimize towards this criterion, the authors propose two interpretation methods that are are theoretically sound for linear models, PatternNet and PatternAtrribution. The former is used to estimate the correct direction, improving upon the DeConvNet[32] and Guided BackPropagation[31] visualizations, while the latter to identify how much the different signal dimensions contribute to the output through the network layers.\n\n…\n\nIn order to address these issues, they proposed an improved faster, model agnostic technique for finding explainable counterfactual explanations of classifier predictions. This novel method incorporates class prototypes, constructed using either an encoder or class specific k-d trees, in the cost function to enable the perturbations to converge much faster to an interpretable counterfactual, hence removing the computational bottleneck and making the method more suitable for practical applications.\nIn order to illustrate the effectiveness of their approach and the quality of the produced counterfactuals, the authors introduced two new metrics focusing on local interpretability at the instance level. By conducting experiments on both image data (MNIST dataset) and tabular data (Wisconsin Breast Cancer dataset), they showed that prototypes help to produce counterfactuals of superior quality.",
        "title": "Explainable AI: A Review of Machine Learning Interpretability Methods",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7824368/",
        "date": "2020-12-25",
        "last_updated": "2026-03-27"
      },
      {
        "snippet": "In particular, it is unclear how the wide array of proposed interpretation methods are related and what common concepts can be used to evaluate them. We aim to address these concerns by defining interpretability in the context of machine learning and introducing the predictive, descriptive, relevant (PDR) framework for discussing interpretations. The PDR framework provides 3 overarching desiderata for evaluation: predictive accuracy, descriptive accuracy, and relevancy, with relevancy judged relative to a human audience.\n\n…\n\nIn this paper, we attempt to address these concerns. To do so, we first define interpretability in the context of machine learning and place it within a generic data science life cycle. This allows us to distinguish between 2 main classes of interpretation methods: model based* and post hoc. We then introduce the predictive, descriptive, relevant (PDR) framework, consisting of 3 desiderata for evaluating and constructing interpretations: predictive accuracy, descriptive accuracy, and relevancy, where relevancy is judged by a human audience. Using these terms, we categorize a broad range of existing methods, all grounded in real-world examples.\n\n…\n\n### Interpretation Methods within the PDR Framework.\n\nIn the framework described above, our definition of interpretable ML focuses on methods in either the modeling or post hoc analysis stages. We call interpretability in the modeling stage model-based interpretability (\n\n*Section 5*). This part of interpretability is focused upon the construction of models that readily provide insight into the relationships they have learned. To provide this insight, model-based interpretability techniques must generally use simpler models, which can result in lower predictive accuracy. Consequently, model-based interpretability is best used when the underlying relationship is sufficiently simple that model-based techniques can achieve reasonable predictive accuracy or when predictive accuracy is not a concern.\n\n…\n\n## 5. Model-Based Interpretability\n\nWe now discuss how interpretability considerations come into play in the modeling stage of the data–science life cycle (Fig. 1). At this stage, the practitioner constructs an ML model from the collected data. We define model-based interpretability as the construction of models that readily provide insight into the relationships they have learned. Different model-based interpretability methods provide different ways of increasing descriptive accuracy by constructing models which are easier to understand, sometimes resulting in lower predictive accuracy. The main challenge of model-based interpretability is to come up with models that are simple enough to be easily understood by the audience, while maintaining high predictive accuracy.\nIn selecting a model to solve a domain problem, the practitioner must consider the entirety of the PDR framework. The first desideratum to consider is predictive accuracy. If the constructed model does not accurately represent the underlying problem, any subsequent analysis will be suspect (29, 30). Second, the main purpose of model-based interpretation methods is to increase descriptive accuracy. Finally, the relevancy of a model’s output must be considered and is determined by the context of the problem, data, and audience. We now discuss some common types of model-based interpretability methods.\n\n…\n\n### B. Model Based.\n\nNow that we have discussed the general problem of evaluating interpretations, we highlight important challenges for the 2 main subfields of interpretable machine learning: model-based and post hoc interpretability. Whenever model-based interpretability can achieve reasonable predictive accuracy and relevancy, by virtue of its high descriptive accuracy it is preferable to fitting a more complex model and relying upon post hoc interpretability. Thus, the main focus for model-based interpretability is increasing its range of possible use cases by increasing its predictive accuracy through more accurate models and transparent feature engineering. It is worth noting that sometimes a combination of model-based and post hoc interpretations is ideal.",
        "title": "Definitions, methods, and applications in interpretable machine learning | PNAS",
        "url": "https://www.pnas.org/doi/10.1073/pnas.1900654116",
        "date": "2019-10-29",
        "last_updated": "2025-03-08"
      },
      {
        "snippet": "",
        "title": "[PDF] An Overview of Interpretability of Machine Learning - arXiv",
        "url": "https://arxiv.org/pdf/1806.00069.pdf",
        "date": null,
        "last_updated": "2026-05-06"
      },
      {
        "snippet": "In particular, it is unclear how the wide array of proposed interpretation methods are related and what common concepts can be used to evaluate them. We aim to address these concerns by defining interpretability in the context of machine learning and introducing the predictive, descriptive, relevant (PDR) framework for discussing interpretations. The PDR framework provides 3 overarching desiderata for evaluation: predictive accuracy, descriptive accuracy, and relevancy, with relevancy judged relative to a human audience.\n\n…\n\nIn this paper, we attempt to address these concerns. To do so, we first define interpretability in the context of machine learning and place it within a generic data science life cycle. This allows us to distinguish between 2 main classes of interpretation methods: model based and post hoc. We then introduce the predictive, descriptive, relevant (PDR) framework, consisting of 3 desiderata for evaluating and constructing interpretations: predictive accuracy, descriptive accuracy, and relevancy, where relevancy is judged by a human audience.\n\n…\n\n### Interpretation Methods within the PDR Framework.\n\nIn the framework described above, our definition of interpretable ML focuses on methods in either the modeling or post hoc analysis stages. We call interpretability in the modeling stage model-based interpretability (*Section 5*). This part of interpretability is focused upon the construction of models that readily provide insight into the relationships they have learned. To provide this insight, model-based interpretability techniques must generally use simpler models, which can result in lower predictive accuracy. Consequently, model-based interpretability is best used when the underlying relationship is sufficiently simple that model-based techniques can achieve reasonable predictive accuracy or when predictive accuracy is not a concern.\n\n…\n\nIn selecting a model to solve a domain problem, the practitioner must consider the entirety of the PDR framework. The first desideratum to consider is predictive accuracy. If the constructed model does not accurately represent the underlying problem, any subsequent analysis will be suspect (29, 30). Second, the main purpose of model-based interpretation methods is to increase descriptive accuracy. Finally, the relevancy of a model’s output must be considered and is determined by the context of the problem, data, and audience. We now discuss some common types of model-based interpretability methods.",
        "title": "Definitions, methods, and applications in interpretable ...",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6825274/",
        "date": "2019-10-16",
        "last_updated": "2026-02-02"
      },
      {
        "snippet": "Within this framework, methods are organized into two classes: model-based and post-hoc. To provide guidance in selecting and evaluating interpretation methods, we introduce three desiderata: predictive accuracy, descriptive accuracy, and relevancy. Using our framework, we review existing work, grounded in real-world studies which exemplify our desiderata, and suggest directions for future work. \\authorcontributionsW.M., C.S., K.K., R.A., and B.Y. helped identify important concepts and provided feedback on the paper.\n\n…\n\nWe aim to address these concerns by defining interpretability in the context of machine learning and introducing the Predictive, Descriptive, Relevant (PDR) framework for discussing interpretations. The PDR framework provides three overarching desiderata for evaluation: predictive accuracy, descriptive accuracy and relevancy, with relevancy judged relative to a human audience.\n\n…\n\n### 2.1 Interpretation methods within the PDR framework\n\nIn the framework described above, most interpretation methods fall either in the modeling or post hoc analysis stages. We call interpretability in the modeling stage model-based interpretability (Sec 4). This part of interpretability is focused upon constraining the form of ML models so that they readily provide useful information about the uncovered relationships. As a result of these constraints, the space of potential models is smaller, which can result in lower predictive accuracy. Consequently, model-based interpretability is best used when the underlying relationship is relatively simple.\n\n…\n\nIn selecting a model to solve a domain problem, the practitioner must consider the entirety of the PDR  framework. The first desideratum to consider is predictive accuracy. If the constructed model does not accurately represent the underlying problem, any subsequent analysis will be suspect (28, 29). Second, the main purpose of model-based interpretation methods is to increase descriptive accuracy. Finally, the relevancy of a model’s output must be considered, and is determined by the context of the problem, data, and audience. We now discuss some widely useful types of model-based interpretability methods.\n\n…\n\nMost widely useful post hoc interpretation methods fall into two main categories: prediction-level and dataset-level interpretations, which are sometimes referred to as local and global interpretations, respectively. Prediction-level interpretation methods focus on explaining individual predictions made by models, such as what features and/or interactions led to the particular prediction. Dataset-level approaches focus on the global relationships the model has learned, such as what visual patterns are associated with a predicted response. These two categories have much in common (in fact, dataset-level approaches often yield information at the prediction-level), but we discuss them separately, as methods at different levels are meaningfully different.\n\n…\n\n### 6.2 Model-based\n\nNow that we have discussed the general problem of evaluating interpretations, we highlight important challenges for the two main sub-fields of interpretable machine learning: model-based and post hoc interpretability. Whenever model-based interpretability can achieve reasonable predictive accuracy and relevancy, by virtue of its high descriptive accuracy it is preferable to fitting a more complex model, and relying upon post hoc interpretability. Thus, the main focus for model-based interpretability is increasing its range of possible use cases by increasing its predictive accuracy through more accurate models and transparent feature engineering. It is worth noting that sometimes a combination of model-based and post hoc interpretations is ideal.",
        "title": "Interpretable machine learning: definitions, methods, and applications",
        "url": "https://ar5iv.labs.arxiv.org/html/1901.04592",
        "date": "2011-02-07",
        "last_updated": "2026-03-14"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

**4. Using Search Recency Filter**

The `search_recency_filter` provides a convenient way to filter results by predefined time periods without specifying exact dates:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search.create(
      query="transformer architecture attention mechanism",
      max_results=10,
      search_recency_filter="week"
  )

  print(response)
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search.create({
    query: "transformer architecture attention mechanism",
    max_results: 10,
    search_recency_filter: "week"
  });

  console.log(response);
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "transformer architecture attention mechanism",
      "max_results": 10,
      "search_recency_filter": "week"
    }' | jq
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "5cdd76b9-da5a-4f9f-8c75-61c90a2399a2",
    "results": [
      {
        "snippet": "",
        "title": "What is an attention mechanism?",
        "url": "https://www.ibm.com/think/topics/attention-mechanism",
        "date": "2024-12-05",
        "last_updated": "2026-03-31"
      },
      {
        "snippet": "",
        "title": "Introduction to Transformers and Attention Mechanisms",
        "url": "https://medium.com/@kalra.rakshit/introduction-to-transformers-and-attention-mechanisms-c29d252ea2c5",
        "date": "2024-02-07",
        "last_updated": "2025-10-29"
      },
      {
        "snippet": "",
        "title": "Transformer (deep learning) - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Transformer_(deep_learning)",
        "date": "2019-08-25",
        "last_updated": "2026-05-15"
      },
      {
        "snippet": "",
        "title": "Transformer (deep learning) - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)",
        "date": "2019-08-25",
        "last_updated": "2026-05-19"
      },
      {
        "snippet": "The famous paper “Attention is all you need” by Vaswani et al. presents the transformer architecture.\nThis neural network architecture builds on the attention mechanism and is at the core of current large language models (LLMs) such as ChatGPT, GPT-4, BERT, etc.\n...\nTransformers process sequences of tokens such as (sub-)words in a sentence.\nThe transformer architecture consists of two parts:\n1. The encoder, which processes the tokens of the input sequence and\n2. the decoder, which produces new tokens as output based on the input tokens and the previously produced output tokens.\nThe overall architecture is shown in the figure below with the encoder on the left and the decoder on the right side.\n...\nThe encoder (left side of the figure above), processes the tokens of the input sequence.\nEach token is initially embedded into a *d- * dimensional vector, e.g., using word2vec.\nIt is then processed individually and compared to other tokens in the input.\nThe process works with variable-length sequences.\nAfter embedding the words as vectors, a **positional encoding** is added, which indicates the absolute and relative position of the tokens in the sequence.\nThis is necessary for many tasks, particularly in natural language, since the later parts of the encoder are permutation invariant.\nThis means they do not distinguish the position of the tokens in the sequence.\n...\nAfter positional encoding, follows a **self-attention** block.\nDuring self-attention, the tokens *within the input sequence* are compared to each other, computing *attention weights.\n* A high attention weight for a pair of two tokens indicates that they are syntactically or semantically related.\nThus high weights indicate important tokens that the model should “attend” to.\n...\nFinally, a normal feed-forward neural network follows the attention block and outputs the encoded tokens one by one.\n...\nIn contrast to the encoder, the decoder contains a **cross-attention** block, which compares to the encoded tokens of the input sequence using cross-attention (explained in more detail below).\nThis cross-attention is at the heart of the decoder and helps producing the next output token, taking both the full input and the output produced so far into account.\n...\n## The Attention Mechanism\nThe attention mechanism is at the core of the transformer architecture — thus the paper title “Attention is all you need”.\nIn a transformer, the attention mechanism enables the model to assign different *attention weights/scores* to different tokens in a sequence.\nThis way, the model can give more importance to relevant information, ignore irrelevant information, and effectively capture long-range dependencies in the data.\nThe attention mechanism distinguishes three inputs: The **query Q, the key K, and the value V**.\nEach token in a sequence is a separate input for Q, K, or V.\nThe mechanism compares queries Q with keys K to determine their importance/compatibility to each other, computing attention weights.\nIt then selects corresponding values V with high attention weights.\nThis is an analogy to data bases, hash tables, or Python dictionaries, where we select the values whose keys match a given query best.\n...\n*Self- and cross-attention only differ in which tokens are given as inputs Q, K, and V.* In **self-attention**, the same tokens are used for all three inputs, i.e., each token is used for Q, K, and V.\nIn **cross-attention**, the same tokens are given to K and V, but different tokens are used for Q.\nSelf-attention is applied to the input sequence in the encoder and to the output sequence in the decoder.\nThe decoder’s cross-attention module then uses the encoded input tokens as K and V and the produced output tokens as Q.\nIn either case, attention weights between tokens in Q and in K are calculated using scaled dot-product attention.\nWhile there are other forms of attention such as learned attention weights, scaled dot-product attention is faster and more space efficient.\nIn scaled dot-product attention, attention weights are computed without extra parameters as illustrated in the figure below: Tokens in Q and K are multiplied, scaled, and passed through a softmax function to obtain attention weights.\nThe attention weights are then multiplied with the tokens in V to select values with high corresponding weights.\n...\nMulti-head attention repeats the attention mechanism explained above multiple times (*h * times) in parallel.\nBefore passing the input tokens of dimension *d * into these *h * attention blocks, they projected into smaller embeddings of size* d/h * by using small linear neural networks*.\n* Each of the *h * linear networks has different weights and leads to different projections.\nConsequently, each attention “head” can learn to focus on different aspects, e.g., subject and object of a sentence.\nThe outputs of the *h* heads are then concatenated and passed through another linear neural network.\n...\nOverall, attention is a surprisingly simple yet effective mechanism to emphasize meaningful tokens and ignore less meaningful tokens.\nBased on this mechanism, transformers can take capture the context even in long sequences and produce coherent outputs.",
        "title": "Understanding Transformers and Attention | by Stefan",
        "url": "https://medium.com/@stefanbschneider/understanding-attention-and-transformers-d84b016cd352",
        "date": "2023-11-28",
        "last_updated": "2025-10-27"
      },
      {
        "snippet": "",
        "title": "Attention in transformers, step-by-step | Deep Learning Chapter 6",
        "url": "https://www.youtube.com/watch?v=eMlx5fFNoYc&vl=en",
        "date": "2024-04-07",
        "last_updated": "2026-05-26"
      },
      {
        "snippet": "At the present moment, the dominant models for nearly all natural\nlanguage processing tasks are based on the Transformer architecture.\n...\nThe core idea behind the Transformer model is the *attention mechanism*, an innovation that was originally envisioned as an enhancement for encoder–decoder RNNs applied to sequence-to-sequence applications, such as machine translations ().\nYou might recall that in the first sequence-to-sequence models for machine translation (), the entire input was compressed by the encoder into a single fixed-length vector to be fed into the decoder.\nThe intuition behind attention is that rather than compressing the input, it might be better for the decoder to revisit the input sequence at every step.\nMoreover, rather than always seeing the same representation of the input, one might imagine that the decoder should selectively focus on particular parts of the input sequence at particular decoding steps.\nBahdanau’s attention mechanism provided a simple means by which the decoder could dynamically *attend* to different parts of the input at each decoding step.\nThe high-level idea is that the encoder could produce a representation of length equal to the original input sequence.\nThen, at decoding time, the decoder can (via some control mechanism) receive as input a context vector consisting of a weighted sum of the representations on the input at each time step.\nIntuitively, the weights determine the extent to which each step’s context “focuses” on each input token, and the key is to make this process for assigning the weights differentiable so that it can be learned along with all of the other neural network parameters.\nInitially, the idea was a remarkably successful enhancement to the\n...\nHowever, attention mechanisms soon emerged as more significant concerns,\nbeyond their usefulness as an enhancement for encoder–decoder recurrent\nneural networks and their putative usefulness for picking out salient\ninputs.\nVaswani *et al.* () proposed the Transformer architecture for machine translation, dispensing with recurrent connections altogether, and instead relying on cleverly arranged attention mechanisms to capture all relationships among input and output tokens.",
        "title": "11. Attention Mechanisms and Transformers - Dive into Deep Learning",
        "url": "http://www.d2l.ai/chapter_attention-mechanisms-and-transformers/index.html",
        "date": null,
        "last_updated": "2026-03-12"
      },
      {
        "snippet": "",
        "title": "The self-attention mechanism",
        "url": "https://www.codecademy.com/article/transformer-architecture-self-attention-mechanism",
        "date": "2025-09-19",
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "",
        "title": "How Attention Mechanism Works in Transformer Architecture",
        "url": "https://www.youtube.com/watch?v=KMHkbXzHn7s",
        "date": "2025-03-08",
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "",
        "title": "Transformer (deep learning architecture) - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Grouped-query_attention",
        "date": "2025-03-14",
        "last_updated": "2025-03-15"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

This example will return only content from the past 7 days, automatically calculated from the current date.

**5. Different Recency Filter Options**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Get content from the past hour (real-time: breaking news or live events)
  hour_response = client.search.create(
      query="Apollo 11 moon landing mission overview",
      max_results=5,
      search_recency_filter="hour"
  )

  # Get content from the past day
  day_response = client.search.create(
      query="history of the printing press",
      max_results=5,
      search_recency_filter="day"
  )

  # Get content from the past month
  month_response = client.search.create(
      query="AI research developments",
      max_results=10,
      search_recency_filter="month"
  )

  # Get content from the past year
  year_response = client.search.create(
      query="major technology trends",
      max_results=15,
      search_recency_filter="year"
  )
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Get content from the past hour (real-time: breaking news or live events)
  const hourResponse = await client.search.create({
    query: "Apollo 11 moon landing mission overview",
    max_results: 5,
    search_recency_filter: "hour"
  });

  // Get content from the past day
  const dayResponse = await client.search.create({
    query: "history of the printing press",
    max_results: 5,
    search_recency_filter: "day"
  });

  // Get content from the past month
  const monthResponse = await client.search.create({
    query: "AI research developments",
    max_results: 10,
    search_recency_filter: "month"
  });

  // Get content from the past year
  const yearResponse = await client.search.create({
    query: "major technology trends",
    max_results: 15,
    search_recency_filter: "year"
  });
  ```

  ```bash cURL theme={null}
  # Get content from the past hour (real-time: breaking news or live events)
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "Apollo 11 moon landing mission overview",
      "max_results": 5,
      "search_recency_filter": "hour"
    }' | jq

  # Get content from the past day
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "history of the printing press",
      "max_results": 5,
      "search_recency_filter": "day"
    }' | jq

  # Get content from the past month
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "AI research developments",
      "max_results": 10,
      "search_recency_filter": "month"
    }' | jq
  ```
</CodeGroup>

<AccordionGroup>
  <Accordion title="Response — Apollo 11 moon landing mission overview">
    ```json theme={null}
    {
      "id": "1aebf3c7-ed3b-4e2c-9366-ce8ede12cec3",
      "results": [
        {
          "snippet": "",
          "title": "Apollo 11 - Wikipedia",
          "url": "https://en.wikipedia.org/wiki/Apollo_11",
          "date": "2001-09-24",
          "last_updated": "2026-05-22"
        },
        {
          "snippet": "The primary objective of Apollo 11 was to complete a national goal set by President John F. Kennedy on May 25, 1961: perform a crewed lunar landing and return to Earth.\nAdditional flight objectives included scientific exploration by the lunar module, or LM, crew; deployment of a television camera to transmit signals to Earth; and deployment of a solar wind composition experiment, seismic experiment package and a Laser Ranging Retroreflector.\nDuring the exploration, the two astronauts were to gather samples of lunar-surface materials for return to Earth.\nThey also were to extensively photograph the lunar terrain, the deployed scientific equipment, the LM spacecraft, and each other, both with still and motion picture cameras.\nThis was to be the last Apollo mission to fly a “free-return” trajectory, which would enable a return to Earth with no engine firing, providing a ready abort of the mission at any time prior to lunar orbit insertion.\n...\nApollo 11 launched from Cape Kennedy on July 16, 1969, carrying Commander Neil Armstrong, Command Module Pilot Michael Collins and Lunar Module Pilot Edwin “Buzz” Aldrin into an initial Earth-orbit of 114 by 116 miles.\nAn estimated 650 million people watched Armstrong’s televised image and heard his voice describe the event as he took “…one small step for a man, one giant leap for mankind” on July 20, 1969.\nTwo hours, 44 minutes and one-and-a-half revolutions after launch, the S-IVB stage reignited for a second burn of five minutes, 48 seconds, placing Apollo 11 into a translunar orbit.\nThe command and service module, or CSM, Columbia separated from the stage, which included the spacecraft-lunar module adapter, or SLA, containing the lunar module, or LM, Eagle.\n...\nPartially piloted manually by Armstrong, the Eagle landed in the Sea of Tranquility in Site 2 at 0 degrees, 41 minutes, 15 seconds north latitude and 23 degrees, 26 minutes east longitude.\n...\nAfter a flight of 195 hours, 18 minutes, 35 seconds – about 36 minutes longer than planned – Apollo 11 splashed down in the Pacific Ocean, 13 miles from the recovery ship USS Hornet.\nBecause of bad weather in the target area, the landing point was changed by about 250 miles.\nApollo 11 landed 13 degrees, 19 minutes north latitude and 169 degrees, nine minutes west longitude July 24, 1969.\n**Crew**\nNeil Armstrong, Commander\nEdwin E.\n“Buzz” Aldrin Jr., Lunar Module Pilot\nMichael Collins, Command Module Pilot\n**Backup Crew**\nJames A. Lovell, Commander\nFred W. Haise Jr., Lunar Module Pilot\nWilliam A. Anders, Command Module Pilot\n**Payload**",
          "title": "Apollo 11 Mission Overview - NASA",
          "url": "https://www.nasa.gov/history/apollo-11-mission-overview/",
          "date": "2015-04-17",
          "last_updated": "2026-05-13"
        },
        {
          "snippet": "The primary objective of Apollo 11 was to complete a national goal set by President John F. Kennedy on May 25, 1961: perform a crewed lunar landing and return to Earth.\nMission Type\nLunar Landing\nastronauts\nNeil Armstrong, Buzz Aldrin, Michael Collins\nLaunch\nJuly 16, 1969\nSPLASHDOWN\nJuly 24, 1969\n...\n**First human to set foot on the Moon.**\nNeil A. Armstrong is probably best known as the commander for the Apollo 11 mission.\n...\nWatch highlights from the Apollo 11 mission including the launch on July 16, 1969, the landing of the lunar module, Neil Armstrong's first steps on the Moon, splashdown, and more.\n...\n20 July 1969—Astronaut Edwin E. Aldrin Jr., lunar module pilot, walks on the surface of the moon near the leg of the Lunar Module (LM) “Eagle” during the Apollo 11 extravehicular activity (EVA).\n...\nJOHNSON SPACE CENTER, HOUSTON, TEXAS – With a half-Earth in the background, the Lunar Module ascent stage with Moon-walking astronauts Neil Armstrong and Edwin Aldrin Jr. approaches for a rendezvous with the Apollo Command Module manned by Michael Collins.\nThe Apollo 11 liftoff from the Moon came early, ending a 22-hour stay on the Moon by Armstrong and Aldrin.\n...\nNeil Armstrong was the first person to walk on the moon.\nHe was an astronaut.\nHe flew on two space missions.\nOne was Apollo 11.\nThat mission landed on the moon.",
          "title": "Apollo 11 - NASA",
          "url": "https://www.nasa.gov/mission/apollo-11/",
          "date": "2023-03-08",
          "last_updated": "2026-05-15"
        },
        {
          "snippet": "Apollo 11, the first space mission to put people on the Moon, was launched on July 16, 1969.\nAlmost every major aspect of the flight of Apollo 11 was witnessed via television by hundreds of millions of people in nearly every part of the globe, until splashdown in the Pacific Ocean on July 24.\n...\nApollo 11’s mission objective was to land astronauts on the Moon and return them safely back to Earth.\nIt succeeded in its objective by landing Neil Armstrong and Buzz Aldrin on the Moon on July 20, 1969.\n...\nApollo 11’s crew members were commander Neil Armstrong, lunar module pilot Buzz Aldrin, and command module pilot Michael Collins.\n...\nThe lunar module *Eagle* of the Apollo 11 mission landed on the Moon on July 20, 1969.\nNeil Armstrong and Buzz Aldrin became the first people to land on the Moon and walk on the lunar surface.\n...\nThe fastest speed Apollo 11 achieved was 39,715 kilometers (24,678 miles) per hour when the command module reentered Earth’s atmosphere on July 24, 1969.\n**\n**Apollo 11**, U.S. spaceflight during which commander Neil Armstrong and lunar module pilot Edwin (“Buzz”) Aldrin, Jr., on July 20, 1969, became the first people to land on the Moon and walk the lunar surface.\nApollo 11 was the culmination of the Apollo program and a massive national commitment by the United States to beat the Soviet Union in putting people on the Moon.\nAll told, 24 Apollo astronauts visited the Moon and 12 of them walked on its surface.\nAdditional NASA astronauts are scheduled to return to the Moon by 2025 as part of the Artemis space program.\n...\nSplashdown of Apollo 11 occurred in the Pacific Ocean about 1,400 km (900 miles) west of Hawaii on July 24.",
          "title": "Apollo 11 | History, Mission, Landing, Astronauts ... - Britannica",
          "url": "https://www.britannica.com/topic/Apollo-11",
          "date": "2026-05-25",
          "last_updated": "2026-05-26"
        },
        {
          "snippet": "**On July 20, 1969, humans walked on the Moon for the first time.**\n**We look back at the legacy of our first small steps on the Moon and look forward to the next giant leap.**\n...\nThe Soviet Union launched the first human, Yuri Gagarin, into space on April 12, 1961.\nWithin days of the Soviet achievement, President John F. Kennedy asked Vice President Lyndon Johnson to identify a “space program which promises dramatic results in which we could win.”\nA little over a month later, on May 25, 1961, Kennedy stood before a joint session of Congress and called for human exploration to the Moon.\n...\nJuly 16, 1969\n## Liftoff!\nA Saturn V rocket carrying the three Apollo 11 astronauts blasted off from Cape Kennedy.\nOver a million spectators, including Vice President Spiro Agnew and former President Lyndon Johnson, came to watch the lift off.\nJuly 20, 1969\n## \"The Eagle has landed!\"\nAfter four days traveling to the Moon, the Lunar Module *Eagle*, carrying Neil Armstrong and Buzz Aldrin landed on the Moon.\nNeil Armstrong exited the spacecraft and became the first human to walk on the moon.\nAs an estimated 650 million people watched, Armstrong proclaimed \"That's one small step for man, one giant leap for mankind.\"\nMichael Collins stayed aboard the Command Module *Columbia*, serving as a communications link and photographing the lunar surface.\n...\n## The Sea of Tranquility | Mare Tranquillitatis\n**00.67408° N latitude, 23.47297° E longitude**\nFor the first lunar landing, the Sea of Tranquility (Mare Tranquilitatis) was the site chosen because it is a relatively smooth and level area.\nIt does, however, have some craters and in the last minutes before landing, Neil Armstrong had to manually pilot the lunar module to avoid a sharp-rimmed ray crater measuring some 180 meters across and 30 meters deep known as West.\nThe lunar module landed safely some 6 km from the originally intended landing site, approximately 400 meters west of West crater and 20km south-southwest of the crater Sabine D in the southwestern part of Mare Tranquilitatis.\nThe lunar surface at the landing site consisted of fragmental debris ranging in size from fine particles to blocks about 0.8 meter wide.\n...\nAfter approximately two and half hours on the Moon, Armstrong and Aldrin returned to the lunar module to begin the journey home.\nThe three astronauts splashed down in Hawaii on July 24, 1969.\nFrom there they quarantined for three weeks as a precaution against bringing contagion back from the Moon, before the festivities welcoming them home commenced.\n...\n## Buzz Aldrin\nLunar Module Pilot\n## Michael Collins\nCommand Module Pilot\n...\nThree astronauts were selected as backups for the crew: James A. Lovell, commander; William A. Anders, command module pilot; and Fred W. Haise, lunar module pilot.\nAll three backup crew members would eventually fly on Apollo missions.\n...\nOn July 20th, across the world, people gathered in front of televisions to watch the moon landing.\nAn estimated 650 million viewers were watching.\nIn the United States, 93% of televisions tuned in to see Neil Armstrong walk on the Moon.",
          "title": "Technology",
          "url": "https://airandspace.si.edu/explore/stories/apollo-11-moon-landing",
          "date": "2021-07-29",
          "last_updated": "2026-05-26"
        },
        {
          "snippet": "Apollo 11 was launched on July 16, 1969, at 8:32 AM Central Daylight Time (CDT) with the goal of performing the first human landing on the Moon.\nCommander Neil Armstrong, Command Module Pilot Michael Collins, and Lunar Module Pilot Edwin “Buzz” Aldrin entered lunar orbit on the afternoon of July 19.\nThe following day, Armstrong and Aldrin begin their descent to the lunar surface in the Lunar Module, Eagle.\nThe planned landing site in the Sea of Tranquility was selected as a flat, safe location and had been surveyed by Apollo 10 at an elevation of 10 miles above the Moon.\nHowever, a navigation error earlier in the mission caused Eagle to be about 7 kilometers beyond the planned landing location.\nDuring the 12.6-minute-long powered descent, there were a total of five unexpected computer alarms.\nThese alarms all indicated that Eagle’s computer system was overloaded, but in each case, Mission Control concluded that it was safe to continue the landing.\nThe last of these alarms occurred less than three minutes before landing, when the crew was less than 500 meters above the surface.\nBecause of the navigation error, the computer was guiding the spacecraft towards an unsafe touchdown point in the rugged, boulder-filled ejecta field surrounding West Crater.\nArmstrong took manual control and flew to a safe landing spot beyond the crater.\nAt 3:17 PM CDT, he announced their safe landing, “Houston, Tranquility Base.\nThe Eagle has landed.”\nAt the time of landing, Mission Control thought that the spacecraft had just 17 seconds of fuel left in the descent stage.\nHowever, post mission analysis showed that sloshing in the fuel tank during Armstrong’s search for a safe landing site caused the fuel gauge to give an inaccurate reading.\nEagle actually had about 45 seconds of fuel left when it touched down.\nAfter a checkout of Eagle’s systems, Armstrong and Aldrin prepared for their moonwalk.\nAt 9:56 PM CDT, Armstrong set foot on the lunar surface, “That’s one small step for man, one giant leap for mankind.”\nAldrin followed a short while later.\nThe duration of this first ever moonwalk was limited to just 2 hours and 31 minutes and the crew remained within 60 meters of Eagle.\nArmstrong and Aldrin collected 21.6 kilograms of samples and deployed a seismometer to measure moonquakes, a laser retroreflector to enable precise measurements of the distance between Earth and the Moon, and a device to collect a sample of the solar wind.\nThey also performed ceremonial duties, including setting up a United States flag, unveiling a commemorative plaque on the lunar module, and having a brief conversation with President Richard Nixon.\nDuring the moon landing, Collins remained in lunar orbit in the command module, Columbia.\nAfter just 21.6 hours on the Moon, Eagle’s ascent stage returned to lunar orbit and rejoined Columbia.\nAltogether, Apollo 11 spent 2.5 days in lunar orbit, circling the Moon 31 times.\nThe crew returned safely to Earth on July 24, landing in the Pacific Ocean southwest of Hawaii, after a flight of 8 days and 3 hours.\nAlthough scientists considered it unlikely that the Moon had life on it, the crew was kept in a biological quarantine for 21 days.\nPost-mission analysis showed that the Apollo 11 samples consisted of two primary rock types.\nBasalt is formed by the solidification of molten magma.\nThe Apollo 11 basalts formed 3.6 to 3.9 billion years ago and are unusually rich in the element titanium.\nBreccias are composed of fragments of other rocks.\nOn the Moon, breccias formed from rocks that are broken up by impacting objects.\nAnalysis of the lunar samples also confirmed that they were indeed lifeless and showed no evidence of water.",
          "title": "Lunar - Missions - Apollo 11 Mission",
          "url": "https://www.lpi.usra.edu/lunar/missions/apollo/apollo_11/",
          "date": null,
          "last_updated": "2025-07-28"
        },
        {
          "snippet": "Apollo 11 was the first mission to land humans on the Moon.\nIt fulfilled a 1961 goal set by President John F. Kennedy to send American astronauts to the surface and return them safely to Earth before the end of the decade.\nOn 21 July 1969 at 02:56:15 UTC, Neil Armstrong pressed his left foot onto the Moon and said, \"That's one small step for [a] man, one giant leap for mankind,\" as 530 million people watched live on television.\nThe mission returned 20 kilograms of rock and soil to Earth, and paved the way for 5 additional Moon landings that greatly advanced the field of lunar science.\nNeil Armstrong, Buzz Aldrin, and Michael Collins began their journey\nwith a launch aboard a Saturn V rocket on the morning of 16 July 1969.\nThree hours later, their rocket's upper stage blasted them out of Earth\norbit towards the Moon.\nThey arrived 3 days later on 19 July and entered\nan initial lunar orbit of 111 by 306 kilometers.\nA second engine burn\nlowered their orbit to 100 by 113 kilometers.\nOn 20 July, Armstrong and Aldrin boarded their lunar module, nicknamed Eagle, and undocked it from the command module, where Collins remained.\nAlmost the same as in the Apollo 10 rehearsal 2 months earlier, the astronauts fired Eagle’s descent engine, dropping to an orbit with a low point of 14.5 kilometers.\nRoughly an hour later, as the duo approached the Sea of Tranquility, they began a final powered descent to the surface.\n...\nThe official touchdown time was 20:17:39 UTC on 20 July 1969.\n...\nArmstrong and Aldrin's single moonwalk lasted two and a half hours.\nDuring that time, they deployed science and engineering experiments, photographed their surroundings, displayed an American flag, read an inscription plaque, collected rock and soil samples for return to Earth, and spoke with President Richard Nixon.\nThe astronauts verbally described their surroundings and progress for geologists, while cameras mounted inside and outside the lunar module documented some of their activities.\n...\nThe Apollo 11 lunar module landing coordinates are 0.67416 degrees N, 23.47314 E.",
          "title": "Apollo 11 | The Planetary Society",
          "url": "https://www.planetary.org/space-missions/apollo-11",
          "date": "2019-05-31",
          "last_updated": "2026-03-31"
        },
        {
          "snippet": "Apollo 11 (CSM Columbia and LM Eagle)\nSaturn V\nJuly 16-24, 1969\nNeil A. Armstrong\nMichael Collins\nEdwin E.\n\"Buzz\" Aldrin, Jr.\n08 days, 03 hours, 18 minutes\nFirst manned lunar landing mission and lunar\nsurface EVA.\n\"HOUSTON, TRANQUILITY BASE HERE.\nTHE EAGLE HAS LANDED.\"--July 20,\nLanding site: Sea of Tranquility.\nLanding Coordinates: 0.67409 degrees North, 23.47298 degrees East\n(Source: National Space Science Data Center); LROC QuickMap\n1 EVA of 02 hours, 31 minutes.\nFlag and instruments deployed; unveiled plaque on the LM descent stage with inscription: \"Here Men From Planet Earth First Set Foot Upon the Moon.\nJuly 1969 A.D.\nWe Came In Peace For All Mankind.\"\nLunar surface stay time 21.6 hours; 59.5 hours in lunar orbit, with 30 orbits.\nLM ascent stage left in lunar orbit.\n20 kg (44 lbs) of material gathered.",
          "title": "Apollo 11 Lunar Surface Journal : Mission Overview",
          "url": "https://www.nasa.gov/history/alsj/a11/a11ov.html",
          "date": null,
          "last_updated": "2025-10-25"
        },
        {
          "snippet": "",
          "title": "Apollo 11 Mission Overview | NASA+",
          "url": "https://plus.nasa.gov/video/apollo-11-mission-overview/",
          "date": "2024-07-12",
          "last_updated": "2026-05-17"
        },
        {
          "snippet": "Overview of the Apollo 11 spaceflight in which U.S. astronauts became the first people to walk on the Moon.\n...\nThe mission that took U.S. astronauts to the Moon was Apollo 11, NASA’s fifth crewed Apollo mission.\nThe astronauts on board the spacecraft were Neil Armstrong, Edwin (“Buzz”) Aldrin, Jr., and Michael Collins.\nOn the morning of July 20, Armstrong and Aldrin crawled from the command module, Columbia, through a tunnel to the lunar module, Eagle.\nArmstrong and Aldrin piloted Eagle to the lunar surface, touching down in the Sea of Tranquility.\nAt 4:17 PM U.S. Eastern Daylight Time (EDT), Armstrong radioed, “Houston, Tranquility Base here.\nThe Eagle has landed.”\nAt 10:56 PM EDT on July 20, Armstrong stepped out onto the lunar soil with the words, “That’s one small step for [a] man, one giant leap for mankind.”\n(In the excitement of the moment, Armstrong skipped the “a” in the statement that he had prepared.)\nArmstrong and Aldrin set up a device to measure the composition of the solar wind reaching the Moon, a device to receive laser beams from astronomical observatories on Earth to determine the exact distance of the two bodies from one each other, and a passive seismometer to measure moonquakes and meteor impacts.\nThey also took about 23 kg (50 pounds) of rock and soil samples, took many photographs, and maintained constant communication with mission control in Houston, Texas.\nAfter 21 hours 38 minutes on the Moon’s surface, the astronauts used Eagle’s ascent stage to launch it back into lunar orbit.\nSplashdown of Apollo 11 occurred in the Pacific Ocean about 1,400 km (900 miles) southwest of Hawaii on July 24.\nAfter their return, the astronauts were quarantined for 21 days from the time Eagle had left the Moon.\nThey were checked for any diseases they might have brought back from the Moon.",
          "title": "Apollo 11's Incredible Journey to the Moon | Britannica",
          "url": "https://www.britannica.com/video/Just-the-facts-Apollo-11-moon-landing/-246490",
          "date": "2023-12-06",
          "last_updated": "2025-08-25"
        }
      ],
      "server_time": null
    }
    ```
  </Accordion>

  <Accordion title="Response — history of the printing press">
    ```json theme={null}
    {
      "id": "23f6db05-6316-4a0f-af87-55873840f369",
      "results": [
        {
          "snippet": "",
          "title": "Printing press - Wikipedia",
          "url": "https://en.wikipedia.org/wiki/Printing_press",
          "date": "2001-10-14",
          "last_updated": "2026-05-18"
        },
        {
          "snippet": "Printing presses push paper against inked movable type materials to transfer text and images from the type onto the paper.\nMedieval presses used a handle to turn a wooden screw that moved the platen on which the paper was mounted; the platen squeezed the paper against the type, which was locked in place in a frame, or form.\nMetal presses, developed late in the 18th century, used steam to drive a cylinder press.\nFlatbed presses, emerging early in the 19th century, used flat beds to hold the type and either a reciprocating platen or a cylinder to hold paper.\n...\nMovable type and paper were invented in China, and printing with movable type was undertaken in Korea by the 14th century, if not earlier.\nThe printing press first became mechanized in Europe.\nThe earliest mention of a printing press in Europe appears in a lawsuit in Strasbourg in 1439.\nIt reveals construction of a press for Johannes Gutenberg and his associates.\nThe earliest European printing presses owed much to the medieval paper press, which was in turn modeled after the ancient wine-and-olive press of the Mediterranean area.\n**printing press**, machine by which text and images are transferred from movable type to paper or other media by means of ink.\nMovable type and paper were invented in China, and the oldest known extant book printed from movable type was created in Korea in the 14th century.\nPrinting first became mechanized in Europe during the 15th century.\nThe earliest mention of a mechanized printing press in Europe appears in a lawsuit in Strasbourg in 1439; it reveals construction of a press for Johannes Gutenberg and his associates.\nGutenberg’s press and others of its era in Europe owed much to the medieval paper press, which was in turn modeled after the ancient wine-and-olive press of the Mediterranean area.\n...\nGutenberg used his press to print an edition of the Bible in 1455; this Bible is the first complete extant book in the West, and it is one of the earliest books printed from movable type.\n(*Jikji*, a book of the teachings of Buddhist priests, was printed by hand from movable type in Korea in 1377.)\nIn its essentials, the wooden press used by Gutenberg reigned supreme for more than 300 years, with a hardly varying rate of 250 sheets per hour printed on one side.\nMetal presses began to appear late in the 18th century, at about which time the advantages of the cylinder were first perceived and the application of steam power was considered.\nBy the mid-19th century Richard M. Hoe of New York had perfected a power-driven cylinder press in which a large central cylinder carrying the type successively printed on the paper of four impression cylinders, producing 8,000 sheets an hour in 2,000 revolutions.\nThe rotary press came to dominate the high-speed newspaper field, but the flatbed press, having a flat bed to hold the type and either a reciprocating platen or a cylinder to hold the paper, continued to be used for job printing.\nA significant innovation of the late 19th century was the offset press, in which the printing (blanket) cylinder runs continuously in one direction while paper is impressed against it by an impression cylinder.\nOffset printing is especially valuable for colour printing, because an offset press can print multiple colours in one run.\nOffset lithography—used for books, newspapers, magazines, business forms, and direct mail—continued to be the most widely used printing method at the start of the 21st century, though it was challenged by ink-jet, laser, and other printing methods.\n...\nApart from the introduction of electric power, advances in press design between 1900 and the 1950s consisted of a great number of relatively minor mechanical modifications designed to improve the speed of the operation.\nAmong these changes were better paper feed, improvements in plates and paper, automatic paper reels, and photoelectric control of colour register.\nThe introduction of computers in the 1950s revolutionized printing composition, with more and more steps in the print process being replaced by digital data.\nAt the end of the 20th century a new electronic printing method, print-on-demand, began to compete with offset printing, though it—and printing generally—came under increasing pressure in developed countries as publishers, newspapers, and others turned to online means of distributing what they had previously printed on paper.",
          "title": "Printing press | Invention, Definition, History, Gutenberg, & Facts",
          "url": "https://www.britannica.com/technology/printing-press",
          "date": "2026-04-28",
          "last_updated": "2026-05-20"
        },
        {
          "snippet": "The exact date of the first printing press invention is unknown, however, printed materials date as far back as 868 A.D.\nHere is a general timeline of the printing press invention.\nClick on each section to learn more.\n1. Block Printing: Pre 868 A.D.\n2. Moveable Type: Between 970 - 1051 A.D.\n3. Wood Type Updated: 1297\n4. The Gutenberg Press: 1450\n5. The Spread of Printing in Europe: 1465 - 1495\n6. Industrial Printing Press Invention: 1800 - 1843\n7. Modern Printing Processes: Offset and Digital Printing\n...\nEven though many people believe that the first printing press was invented by Johannes Gutenberg, people in China were actually using a process known as block printing to create printed text many centuries before the Gutenberg press.\nBlock printing involves using panels of wooden blocks that have been hand-carved in reverse.\nThe ink was then applied to these blocks and they were pressed onto paper to form the printed text.\nIt is unclear how long ago this process was developed (possibly as long ago as the 6th century), however, the oldest known printed book that used this method is called The Diamond Sutra, a Buddhist book from Dunhuang China dated 868 A.D.\nOther examples of block printing have also survived including:\n...\n- A calendar dating 877 A.D.\nBlock printing was also used during this time period in both Japan and Korea.\n...\nMoveable type replaced block printing around 970 A.D.\nThe first version of this type of printing involved carving individual letters into clay blocks and then baking them until they were hard.\nThese blocks were then arranged onto an iron frame which was pressed against an iron plate.\nThe great advantage of the moveable type was that you could re-use the letters for different texts.\nThis process was created by Bi Sheng who lived in Yingshan, Hubei, China from about 970 to 1051 A.D.\n...\nThe process of using wood type made a comeback in 1297 when a Chinese magistrate called Wang Zhen improved on the technique.\nHe developed a way of making the wood more precise and durable thus giving you a better-finished product.\nHe also created a type of revolving table that the typesetters were able to use to organize the type more efficiently.\nHis process greatly sped up the printing process.\nThe book Nung Shu was printed using this process and is considered to be the world's first mass-produced book.\n...\nJohannes Gutenberg started experimenting with printing while he was exiled from Germany in Strasbourg France in 1440.\nBy 1450, he had developed a printing machine that was ready to be used commercially.\nGutenberg's printing press used metal pieces instead of wood.\nEach letter was made to uniformly fit together so that the resulting print would be in perfectly straight lines and columns.\nHe also created a special ink that would stick to metal.\nIn addition, he figured out a way to flatten the printing paper to give a better finished product by using a winepress that had previously been used to press grapes and olives.\nGutenberg used his printing press invention to print the famous Gutenberg Bible.\nHe made about 180 copies of the Bible each containing 1.300 pages.\n...\nThe invention of the Gutenberg press meant that books could finally be mass-produced and at a fraction of the cost of previous printing methods.\nThe printing press invention is credited with contributing to the growth of literacy, education, and the availability of uniform information for the common person.\n...\nMany workers who had helped Gutenberg perfect his printing process became printers themselves in Germany.\nThe printing press was later brought to Italy in 1465 and in 1470, German printers were asked to set up printing presses in Sorbonne Paris.\nSpain and Portugal invited German printers to set up in their countries in 1473 and 1495 respectively.\nFinally, the printing press was brought to England in 1476 by William Caxton.\nCaxton was an Englishman who had gone to cologne to learn how to print in 1471.\n...\nEven though the essential workings of the Gutenberg press remained intact, the invention of mechanical printing presses made the printing process much more efficient.\nIn 1800, Lord Stanhope built a press that was completely made of cast iron, with double the printed area, and that was able to produce 480 pages per hour thus doubling the production of the previous presses.\nThe steam-powered rotary printing press, which Richard M. Hoe invented in the United States in 1843 made the printing process even faster, producing millions of copies of a page in one day.",
          "title": "Digital Printing",
          "url": "https://jhfrench.com/blog/the-printing-press-invention-history-important-dates-amp-facts",
          "date": "2022-03-02",
          "last_updated": "2026-05-19"
        },
        {
          "snippet": "In 1436 Johaness Gutenberg, a German goldsmith, began designing a machine capable of producing pages of text at an incredible speed—a product that he hoped would offset losses from a failed attempt to sell metal mirrors.\nBy 1440 Gutenberg had established the basics of his printing press including the use of a mobile, reusable set of type, and within ten years he had constructed a working prototype of the press.\nIn 1454 Gutenberg put his press to commercial use, producing thousands of indulgences for the Church.\nThe following year he printed his famous 42-line Bible, the first book printed on a moveable type press in the West.\n1\nGutenberg's press was the combined effort of several discoveries and inventions.\nThe printing press was built around the traditional screw press, a precursor to today's drill press, with an added matrix on which individually-cast letters and symbols could be arranged to form the desired text.\nThis moveable type design allowed pages of text to be quickly assembled from a pre-cast selection of letters and symbols rather than laboriously carved from a block of wood as in the\n*block printing method*.\nGutenberg also created a unique oil-based ink which transferred from his metal type to the printing substrate much more effectively than the water-based inks that other printers of the era used.\nIn order to print a page, Gutenberg would arrange the necessary letters on the matrix and coat them in his ink.\nThe matrix was then mounted on the contact end of the modified screw press and lowered until it struck the paper underneath.\nThe process, while labor intensive, allowed Gutenberg to print pages at a much greater rate than printers using the block printing method or those doing manuscript work.\n...\nJohannes Gutenberg's moveable type press marked the beginning of the Printing Revolution in the western world, a colossal moment in the history of information and learning.\nWith access to printing presses, scientists, philosophers, politicians, and religious officials could replicate their ideas quickly and make them available to large audiences.",
          "title": "The Gutenberg Press",
          "url": "https://scarc.library.oregonstate.edu/omeka/exhibits/show/mcdonald/incunabula/gutenberg/",
          "date": null,
          "last_updated": "2025-05-09"
        },
        {
          "snippet": "",
          "title": "History of printing - Wikipedia",
          "url": "https://en.wikipedia.org/wiki/History_of_printing",
          "date": "2007-05-02",
          "last_updated": "2026-05-13"
        },
        {
          "snippet": "",
          "title": "A Short History of The Printing Press, by Robert Hoe—A Project ...",
          "url": "https://www.gutenberg.org/files/63545/63545-h/63545-h.htm",
          "date": null,
          "last_updated": "2026-03-21"
        },
        {
          "snippet": "",
          "title": "Printing - Wikipedia",
          "url": "https://en.wikipedia.org/wiki/Printing",
          "date": "2002-03-17",
          "last_updated": "2026-03-30"
        },
        {
          "snippet": "",
          "title": "Gutenberg, Printing Press, Revolution | Britannica",
          "url": "https://www.britannica.com/topic/printing-publishing/The-Gutenberg-press",
          "date": "2025-09-05",
          "last_updated": "2025-10-15"
        },
        {
          "snippet": "The 15th century is a particularly interesting period in our history.\nIt is the last century of the Middle Ages and the Dark Ages, and at the same time, the bridge between the Late Middle Ages, the Early Renaissance, and the Modern Age.\nIt is also known as \"The Century of Innovations.\"\nOne of the most important innovations, and one that marked a milestone in human history, was undoubtedly the invention of the printing press.\nAt that time, reading was reserved for a select few, primarily the clergy and nobility.\nIt is estimated that only about 12% of the European population could read.\nThe few books that existed, produced by hand and copied by hand, were kept mainly in monasteries.\nThe church was the main source of information, transmitted orally.\nThe arrival of the printing press would revolutionize the world.\nSuddenly, people had access to a vast amount of information, which also gave rise to critical thinking.\nThis was not welcomed by those who, throughout history, have sought to control information and thought.\nAlthough the first printed book was a Bible, as early as 1559, Pope Paul IV established an Index Librorum Prohibitorum, a list of all books prohibited to Catholics.\nSince then, the Church and various governments have censored, banned, and burned thousands of books.\n...\nThe person responsible for this information revolution in the 15th Century was the son of a patrician from the city of Mainz, Germany.\nHis name was Johann Gensfleisch zur Laden zum Gutenberg, better known as Johannes Gutenberg.\nSome of the elements of his invention were movable type, an oil ink that soaked into metal and then transferred easily to paper, as well as a new printing press, probably adapted from those used for winemaking.\nLike every endeavor, Gutenberg’s was not without financial problems.\nA wealthy financier, Johann Fust, invested in his project, but later won a lawsuit against Gutenberg, which allowed him to use the invention as his own, continuing to produce Bibles and Gutenberg’s second masterpiece, a psalter.\nIn 1465, the Archbishop of Mainz granted Gutenberg a pension, granting him an annual ration of grain, wine, and clothing.\nShortly thereafter, in 1468, Gutenberg died in his native Mainz.\nThe establishment of the printing press in Mexico, the first in the Americas, is also an interesting story.\nJuan Cromberger, a German printer established in Seville and owner of a prestigious publishing house with capital to establish a branch in the New Spain, entrusted Juan Pablos, whom he trusted as a copyist or typesetter, to found a printing press in the New World.\nJuan Pablos, of Italian origin and whose name, Giovanni Paoli, we know now in Spanish, arrived in Mexico City with his wife Gerónima Gutiérrez, between September and October 1539.\nWith the support of his sponsors, Juan Pablos established the “House of Juan Cromberger” workshop in the “Casa de las Campanas”, Bishop Zumárraga’s house, located on the southwest corner of Moneda and Santa Teresa la Antigua streets, now known as Licenciado Verdad, across the street from the former archbishopric.\nThe workshop opened its doors around April 1540.\nThe world has evolved at an immense speed since the 15th and 16th centuries.\nToday, nearly 4 million book titles are produced annually worldwide.",
          "title": "The history of the printing press - International Publishers Association",
          "url": "https://internationalpublishers.org/the-history-of-the-printing-press/",
          "date": "2025-05-12",
          "last_updated": "2026-03-27"
        },
        {
          "snippet": "The printing press has always been a marvel of human invention, and the printing of newspapers occupies a unique course in the history of printing machines.\nAs demands grew for more pages, more news, and faster delivery, newspapers had to achieve greater speeds and higher efficiency.\nNewspapers started on Gutenberg presses – individual type pieces arranged backwards by hand, secured in a flat bed, inked by hand, and a great leverage force applied to create the impression.\nThe machine did one part of the job, and newspapers were often printed once a week as one, large, single-sided page called a broadside.\nThe force required to get a good image was considerable, the wood that made up the printing press would crack or break over time, and the metal type would wear down.\nFrom the 1440s, the mechanics of the printing press were practically unchanged for 300 years!\nThe first improvements to the press were to replace some of the wooden parts with iron and improve the lever used to press the paper to type.\nThe first printing press made entirely out of iron appeared around 1800 in England and is attributed to Charles Mahon, the third Earl of Stanhope.\nThe power and durability of the Stanhope press allowed printers to get 200 pulls per hour – each ‘pull’ being a pressed side of a paper.\n200 pulls would be 100 issues of a double-sided broadsheet.\nThe Columbian press by George Clymer was the first entirely metal press in the United States, emerging in the 1810s.\nWhile other iron presses emerged in a variety of sizes, these two were the first big names in successful manufacturing companies.\nOne of the biggest jumps in newspaper press development at this time was from the flat-bed hand press (like the Columbian) to the rotary press – a machine run by steam, horses, or manpower that incorporated rotating cylinders in the printing process that skyrocketed production speeds.\nWhile methods of printing with cylinders can be found as far back as 1616, it wasn’t until the 1810s that a practical method was manufactured.\nFrederick Koenig and Andreas Bauer, German immigrants in England, patented a machine that obtained an impression not by pressing but by rolling paper attached to a cylinder over the bed of type.\nMade first for the London Times’ November 29, 1814 issue, this steam powered press could produce 1,100 sheets per hour.\nThe more cylinders the press had, the more pages it could print at once.\nIt even had a cylinder to automatically roll ink onto the type, but it still only printed single sided sheets which were fed into and taken off of the machine by hand.\n...\nCarried on by his son Richard in the 1840s, R.\nHoe developed the type-revolving printing presses nicknamed “lightning presses.”\nInstead of paper on a cylinder, the type pieces were wedge-shaped in order to be secured tightly into the surface of a cylinder and rolled onto paper.\n...\nThe 1860s saw American press factories develop two major improvements for printing newspapers: the stereotype plates and the paper web.\nThe stereotype is a thin piece of metal that has been cast from a mold of the composed type.\nThe thin metal is curved to fit around a rotating cylinder in the printing press, thus eliminating type from the actual printing process for the first time.\nThe stereotype process was developed over the course of the 1840s but did not enter the printing scene at-large until the 1860s.\nThe stereos, as they were called, would remain an integral piece in the printing process until the 1970s.\n...\nIn 1865, William Bullock of Philadelphia collaborated with papermakers to design a web – a continuous roll of paper – to run through his rotary presses and be cut to size in the printing process.\nHis rotary press also set the new standard for “perfecting” the paper – printing on both sides of the page.\nBullock’s early rotary press could get 8,000 – 10,000 copies per hour according to the New-York Tribune.\n...\nThe final touch was mechanized folding of the finished newspaper.\nEnglishman George Ashley Wilson is credited with designing the Victory printing and folding machine combined.\nOther companies like R.\nHoe created separate machines that could be hand-fed finished sheets or attached to the end of one of their existing presses.\nFolding would go on to become a standard function of large presses.\nBy the 1880s, newspaper presses achieved their highest speeds yet.\nCountless individual inventions followed by small adjustments, innovations, and tricks fill printing history, but these “headliners” would consistently be the standard for almost one hundred more years of newspaper printing.",
          "title": "Printing Newspapers: 1400-1900",
          "url": "https://blogs.loc.gov/headlinesandheroes/2022/04/printing-newspapers-1400-1900/",
          "date": "2022-04-21",
          "last_updated": "2026-03-11"
        }
      ],
      "server_time": null
    }
    ```
  </Accordion>

  <Accordion title="Response — AI research developments">
    ```json theme={null}
    {
      "id": "4942a8e3-b0e6-40cc-8e86-ab60e6e4567c",
      "results": [
        {
          "snippet": "# Our latest research breakthroughs\n### Gemini for Science: AI experiments and tools for a new era of discovery\nGoogle Labs\nGoogle DeepMind\nGoogle Research\n### Empirical Research Assistance (ERA): From Nature publication to catalyzing Computational Discovery\nGoogle Research\n### Co-Scientist: A multi-agent AI partner to accelerate research\nGoogle DeepMind\nGoogle Cloud\nGoogle Labs\nGoogle Research\n### Gemini Robotics ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning\nGoogle DeepMind\n### From games to biology and beyond: 10 years of AlphaGo’s impact\nGoogle DeepMind\n### How AI can improve breast cancer detection in the UK\nGoogle Research\n### How we’re helping preserve the genetic information of endangered species with AI\nGoogle Research\n### WeatherNext 2: Our most advanced weather forecasting model\nGoogle DeepMind\nGoogle Research\n### SIMA 2: An agent that plays, reasons, and learns with you in virtual 3D worlds\nGoogle DeepMind\n### Quantum Echoes algorithm is a big step toward practical applications for quantum computing\nGoogle Research\n### How a Gemma model helped discover a new potential cancer therapy pathway\nGoogle DeepMind\nGoogle Research\n### DeepSomatic: Using AI to identify genetic variants in tumors\nGoogle Research\n### Teaching Gemini to spot exploding stars with just a few examples\nGoogle Research\n### Coral NPU: A full-stack platform for Edge AI\nGoogle Research\n### Using AI to perceive the universe in greater depth\nGoogle DeepMind\n### Genie 3: A general purpose world model that can generate a diversity of interactive environments\nGoogle DeepMind\n### Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the International Mathematical Olympiad\nGoogle DeepMind\n### FireSat: First images of wildfires detected by the new satellite constellation\nGoogle Research\n### SensorLM: Learning the language of wearable sensors\nGoogle Research\n### Aeneas transforms how historians connect the past\nGoogle DeepMind\n### ZAPBench: One of the most ambitious datasets in brain activity research\nGoogle Research\n### AlphaProteo: Generate novel proteins for health research\nGoogle DeepMind\n### AlphaFold: Accelerating breakthroughs in biology with AI\nGoogle DeepMind\nSee more research from across Google",
          "title": "Breakthrough AI research - Google AI",
          "url": "https://ai.google/research/",
          "date": null,
          "last_updated": "2026-05-20"
        },
        {
          "snippet": "",
          "title": "The future of AI: trends shaping the next 10 years - IBM",
          "url": "https://www.ibm.com/think/insights/artificial-intelligence-future",
          "date": "2024-10-11",
          "last_updated": "2026-05-03"
        },
        {
          "snippet": "",
          "title": "AI Research Trends",
          "url": "https://ai100.stanford.edu/2016-report/section-i-what-artificial-intelligence/ai-research-trends",
          "date": null,
          "last_updated": "2026-04-28"
        },
        {
          "snippet": "",
          "title": "Agentic AI News + AI Breakthroughs + AI Developments | 2026",
          "url": "https://www.crescendo.ai/news/latest-ai-news-and-updates",
          "date": "2026-05-18",
          "last_updated": "2026-05-20"
        },
        {
          "snippet": "# Pioneering research on the path to AGI\nWe believe our research will eventually lead to artificial general intelligence, a system that can solve human-level problems.\nBuilding safe and beneficial AGI is our mission.\n...\n### We use Deep Learning to leverage large amounts of data and advanced reasoning to train AI systems for task completion.\n...\nOpenAI’s GPT series models are fast, versatile, and cost-efficient AI systems designed to understand context, generate content, and reason across text, images, and more.\n...\nOpenAI’s o series models are advanced reasoning AI systems that use chain-of-thought processes to solve complex STEM problems through logical, step-by-step analysis.\n...\nOur text models are advanced language processing tools that can generate, classify, and summarize text with high levels of coherence and accuracy.\n...\nOur research on generative modeling for images has led to representation models like CLIP, which makes a map between text and images that an AI can read, and DALL-E, a tool for creating vivid images from text descriptions.\n...\n### Audio\nOur research on applying AI to audio processing and audio generation has led to developments in automatic speech recognition and original musical compositions.\n...\n> “Safely aligning powerful AI systems is one of the most important unsolved problems for our mission.\nTechniques like learning from human feedback are helping us get closer, and we are actively researching new techniques to help us fill the gaps.”\n...\nView research index",
          "title": "Research - OpenAI",
          "url": "https://openai.com/research/",
          "date": "2025-08-07",
          "last_updated": "2026-03-29"
        },
        {
          "snippet": "",
          "title": "Artificial Intelligence News",
          "url": "https://www.sciencedaily.com/news/computers_math/artificial_intelligence/",
          "date": "2026-05-21",
          "last_updated": "2026-05-21"
        },
        {
          "snippet": "*The Artificial Intelligence R&D (AI R&D) Interagency Working Group (IWG) coordinates Federal AI R&D and supports activities tasked by both the NSTC Select Committee on AI and the Subcommittee on Machine Learning and Artificial Intelligence.\nThis vital work promotes U.S. leadership and global competitiveness in AI R&D and its applications.\nThe AI IWG reports investments to the AI R&D Program Component Area.*\n...\nThe Artificial Intelligence R&D Interagency Working Group (AI R&D IWG) was formed in 2018 to coordinate Federal AI R&D across 32 participating agencies and to support activities tasked by both the NSTC Select Committee on AI and the Subcommittee on Machine Learning and Artificial Intelligence (MLAI).\nThrough the NITRD Subcommittee, the AI IWG will coordinate AI activities to advance the mission of the National AI Initiative Office (NAIIO).\n...\nThis dashboard illustrates the Federal budget for nondefense AI R&D investments across several fiscal years.\nIt provides both an overall budget rollup, as well as breakdowns of investments by agency and by NITRD Program Component Areas (PCAs), major subject areas for Federal IT R&D.\n*Learn more about Federal Agencies investments in AI R&D which shows sustained investments in key priority R&D areas*: AI R&D Federal Investments Dashboard.\n...\nThe National AI Initiative Office was established in January 2021 to oversee and implement the National AI Initiative Act (NAIIA).\nThe NAIIO along with the NITRD Subcommittee directs the NITRD AI R&D IWG to coordinate Federal R&D investment in AI.",
          "title": "Artificial Intelligence Research and Development - NITRD",
          "url": "https://www.nitrd.gov/coordination-areas/ai/",
          "date": "2025-12-08",
          "last_updated": "2026-05-17"
        },
        {
          "snippet": "Artificial Intelligence has leapt to the forefront of global discourse, garnering increased attention from practitioners, industry leaders, policymakers, and the general public.\nThe diversity of opinions and debates gathered from news articles this year illustrates just how broadly AI is being investigated, studied, and applied.\nHowever, the field of AI is still evolving rapidly and even experts have a hard time understanding and tracking progress across the field.\n...\nThis chapter explores trends in AI research and development, beginning with an analysis of AI publications, patents, and notable AI systems.\nThe Technical Performance section of this year’s AI Index provides a comprehensive overview of AI advancements in 2024.\nArtificial intelligence is now deeply integrated into nearly every aspect of our lives.\nIt is reshaping sectors like education, finance, and healthcare, where algorithm-driven insights guide critical decisions.\n...\nAI’s advancing capabilities have captured policymakers’ attention, leading to an increase in AI-related policies worldwide.\nAI has entered the public consciousness through generative AI’s impact on work...\nAs AI continues to permeate broad swaths of society, it is becoming increasingly important to understand public sentiment around the technology.\n...\nIn 2023, researchers introduced new benchmarks—MMMU, GPQA, and SWE-bench—to test the limits of advanced AI systems.\nJust a year later, performance sharply increased: scores rose by 18.8, 48.9, and 67.3 percentage points on MMMU, GPQA, and SWE-bench, respectively.\nBeyond benchmarks, AI systems made major strides in generating high-quality video, and in some settings, language model agents even outperformed humans in programming tasks with limited time budgets.\nFrom healthcare to transportation, AI is rapidly moving from the lab to daily life.\nIn 2023, the FDA approved 223 AI-enabled medical devices, up from just six in 2015.\nOn the roads, self-driving cars are no longer experimental: Waymo, one of the largest U.S. operators, provides over 150,000 autonomous rides each week, while Baidu’s affordable Apollo Go robotaxi fleet now serves numerous cities across China.\nIn 2024, U.S. private AI investment grew to $109.1 billion—nearly 12 times China’s $9.3 billion and 24 times the U.K.’s $4.5 billion.\nGenerative AI saw particularly strong momentum, attracting $33.9 billion globally in private investment—an 18.7% increase from 2023.\nAI business usage is also accelerating: 78% of organizations reported using AI in 2024, up from 55% the year before.\nMeanwhile, a growing body of research confirms that AI boosts productivity and, in most cases, helps narrow skill gaps across the workforce.\nIn 2024, U.S.-based institutions produced 40 notable AI models, significantly outpacing China’s 15 and Europe’s three.\nWhile the U.S. maintains its lead in quantity, Chinese models have rapidly closed the quality gap: performance differences on major benchmarks such as MMLU and HumanEval shrank from double digits in 2023 to near parity in 2024.\nMeanwhile, China continues to lead in AI publications and patents.\nAt the same time, model development is increasingly global, with notable launches from regions such as the Middle East, Latin America, and Southeast Asia.\nAI-related incidents are rising sharply, yet standardized RAI evaluations remain rare among major industrial model developers.\nHowever, new benchmarks like HELM Safety, AIR-Bench, and FACTS offer promising tools for assessing factuality and safety.\nAmong companies, a gap persists between recognizing RAI risks and taking meaningful action.\nIn contrast, governments are showing increased urgency: In 2024, global cooperation on AI governance intensified, with organizations including the OECD, EU, U.N., and African Union releasing frameworks focused on transparency, trustworthiness, and other core responsible AI principles.\nIn countries like China (83%), Indonesia (80%), and Thailand (77%), strong majorities see AI products and services as more beneficial than harmful.\nIn contrast, optimism remains far lower in places like Canada (40%), the United States (39%), and the Netherlands (36%).\nStill, sentiment is shifting: since 2022, optimism has grown significantly in several previously skeptical countries—including Germany (+10%), France (+10%), Canada (+8%), Great Britain (+8%), and the United States (+4%).\nDriven by increasingly capable small models, the inference cost for a system performing at the level of GPT-3.5 dropped over 280-fold between November 2022 and October 2024.\nAt the hardware level, costs have declined by 30% annually, while energy efficiency has improved by 40% each year.\nOpen-weight models are also closing the gap with closed models, reducing the performance difference from 8% to just 1.7% on some benchmarks in a single year.\nTogether, these trends are rapidly lowering the barriers to advanced AI.\nIn 2024, U.S. federal agencies introduced 59 AI-related regulations—more than double the number in 2023—and issued by twice as many agencies.\nGlobally, legislative mentions of AI rose 21.3% across 75 countries since 2023, marking a ninefold increase since 2016.\nAlongside growing attention, governments are investing at scale: Canada pledged $2.4 billion, China launched a $47.5 billion semiconductor fund, France committed €109 billion, India pledged $1.25 billion, and Saudi Arabia’s Project Transcendence represents a $100 billion initiative.\nTwo-thirds of countries now offer or plan to offer K–12 CS education—twice as many as in 2019—with Africa and Latin America making the most progress.\nIn the U.S., the number of graduates with bachelor’s degrees in computing has increased 22% over the last 10 years.\nYet access remains limited in many African countries due to basic infrastructure gaps like electricity.\nIn the U.S., 81% of K–12 CS teachers say AI should be part of foundational CS education, but less than half feel equipped to teach it.\nNearly 90% of notable AI models in 2024 came from industry, up from 60% in 2023, while academia remains the top source of highly cited research.\nModel scale continues to grow rapidly—training compute doubles every five months, datasets every eight, and power use annually.\nYet performance gaps are shrinking: the score difference between the top and 10th-ranked models fell from 11.9% to 5.4% in a year, and the top two are now separated by just 0.7%.\nThe frontier is increasingly competitive—and increasingly crowded.\nAI’s growing importance is reflected in major scientific awards: two Nobel Prizes recognized work that led to deep learning (physics), and to its application to protein folding (chemistry), while the Turing Award honored groundbreaking contributions to reinforcement learning.\nAI models excel at tasks like International Mathematical Olympiad problems but still struggle with complex reasoning benchmarks like PlanBench.\nThey often fail to reliably solve logic tasks even when provably correct solutions exist, limiting their effectiveness in high-stakes settings where precision is critical.",
          "title": "The 2025 AI Index Report | Stanford HAI",
          "url": "https://hai.stanford.edu/ai-index/2025-ai-index-report",
          "date": "2024-09-10",
          "last_updated": "2026-05-21"
        },
        {
          "snippet": "### Building AI models that understand chemical principles\nConnor Coley works at the interface of chemistry and machine learning, to discover and design new drug compounds.\n...\n### Justin Solomon appointed associate dean of engineering education\nMIT faculty member in electrical engineering and computer science to focus on innovation in engineering education and new pedagogical approaches.\n...\n### Two from MIT named 2026 Knight-Hennessy Scholars\nThe prestigious fellowship funds graduate studies at Stanford University.\n...\n### Q&A: Expanding MIT’s global reach through Universal Learning\nDimitris Bertsimas and Megan Mitchell discuss the motivation behind Universal Learning, and what sets the new MIT Open Learning educational initiative apart.\n...\n### Universal AI is “a pathway to AI fluency that’s accessible and approachable to anyone, anywhere”\nNew AI education program from MIT Open Learning debuts with AI-powered personalization and a free introductory course for learners everywhere.\n...\n### Study: Firms often use automation to control certain workers’ wages\nMIT economists found US companies tend to target employees earning a “wage premium,” which increases inequality but not necessarily productivity.\n...\n### Games people — and machines — play: Untangling strategic reasoning to advance AI\nAssistant Professor Gabriele Farina mines the foundations of decision-making in complex multi-agent scenarios.\n...\n### Beacon Biosignals is mapping the brain during sleep\nFounded by Jake Donoghue PhD ’19 and former MIT researcher Jarrett Revels, the company is creating an AI-driven platform to help diagnose and treat disease.\n...\nMIT senior Olivia Honeycutt investigates how the ways we communicate can shape our views of the world.\n...\nPresident Sally Kornbluth spoke in front of a packed crowd about growing challenges to the U.S. research ecosystem as funding for America’s top research universities becomes increasingly strained.\n...\n### Solving the “Whac-a-mole dilemma”: A smarter way to debias AI vision models\nA new debiasing technique called WRING avoids creating or amplifying biases that can occur with existing debiasing approaches.\n...\n### The MIT-IBM Computing Research Lab launches to shape the future of AI and quantum computing\nBuilding on a long-standing MIT–IBM collaboration, the new lab will chart the convergence of AI, algorithms, and quantum computing.\n...\n### Enabling privacy-preserving AI training on everyday devices\nA new method could bring more accurate and efficient AI models to high-stakes applications like health care and finance, even in under-resourced settings.\n...\n### A faster way to estimate AI power consumption\nThe “EnergAIzer” method generates reliable results in seconds, enabling data center operators to efficiently allocate resources and reduce wasted energy.\n...\n### MIT scientists build the world’s largest collection of Olympiad-level math problems, and open it to everyone\nNew dataset of 30,000-plus competition math problems from 47 countries gives AI researchers a harder test — and students worldwide a better training ground.",
          "title": "Artificial intelligence | MIT News | Massachusetts Institute of ...",
          "url": "https://news.mit.edu/topic/artificial-intelligence2",
          "date": "2026-05-20",
          "last_updated": "2026-05-21"
        },
        {
          "snippet": "The rise of artificial intelligence has already transformed every facet of our lives at a remarkable speed.\nAt UC San Diego, AI is empowering bold advances in science, education, public safety, health and the arts.\n...\nFrom uncovering hidden disease mechanisms to guiding new therapies and medical technologies, UC San Diego researchers are harnessing AI to propel humanity toward a future in which diseases are mitigated or eradicated.\nWhat was once science fiction is now possible.\nAs a tool, AI speeds diagnoses, offers a better understanding of the human body and enables more innovative treatments.\n...\nA gene once thought to be just a biomarker for Alzheimer’s disease is actually one of its causes, according to the work of UC San Diego bioengineers.\nUsing AI to model the 3D structures of proteins, the team discovered that the gene PHGDH has a hidden “moonlighting” role: It disrupts how brain cells switch genes on and off, a disturbance that can fuel the disease.\n...\nJoe Pogliano, professor, and Kit Pogliano, dean and distinguished professor, both in the School of Biological Sciences, worked with Linnaeus Bioscience and Seattle Children’s Research Institute to develop MycoBCP, a new AI-powered tool that could accelerate the search for TB treatments.\n...\nBy pairing that method with deep learning, researchers could detect subtle changes in TB cells that would otherwise escape the human eye — revealing how potential drugs act on the pathogen.\n...\nBy recording signals from outside of heart muscle cells and using AI to reconstruct what’s happening inside these cells, engineers were able to monitor heart activity with remarkable accuracy — without invasive methods or physically penetrating the cells.\nThe breakthrough offers safer, faster insights into how heart cells function, communicate and respond to new drugs.\n...\nResearchers have developed advanced deep-learning techniques that could revolutionize treatment planning for breast cancer radiotherapy — making it faster and improving its quality.\nThe approach reduced errors in radiation doses to critical organs, such as the heart and lungs.\n...\nUC San Diego engineers have created a flexible patch — a wireless, skin-mounted ultrasound device — that monitors muscle activity in real time to control a robotic arm, among other uses.\nTo extract additional insights from these muscle signals, the researchers developed an AI algorithm that maps the signals to their corresponding muscle distributions.\nCompact, battery-powered and designed for long-term wear, the technology could open new possibilities in health care monitoring and human-machine interaction.\n...\nIn a unique and long-standing collaboration, UC San Diego electrical engineering graduate students have been embedded with the Jacobs Retina Center at Shiley Eye Institute to develop better computer vision, AI and image-processing tools.\nThese will help physicians diagnose patients with greater speed and accuracy, predict the most effective treatments, and aid in the development of new treatments.\n...\nUC San Diego researchers are using AI to better understand Earth’s changing environment.\nThese innovations provide faster forecasts, actionable insights and tools that help protect communities and the planet.\n...\nResearchers at UC San Diego and the Allen Institute for AI have developed a new model, Spherical DYffusion, that projects 100 years of climate patterns in just 25 hours.\nBy combining generative AI techniques with physics-based data, the model delivers results 25 times faster than current methods without the need for massive supercomputers.\nThe breakthrough could provide scientists and policymakers with faster and more flexible tools for anticipating the long-term effects of climate change.\n...\nWith a growing network of more than 1,200 natural-hazard monitoring cameras spanning remote mountaintops to wildland-urban interfaces, ALERTCalifornia collects real-time data and utilizes AI that helps emergency managers spot smoke, monitor fires and plan evacuations.\nUC San Diego’s WIFIRE team at the San Diego Supercomputer Center utilizes those camera and sensor feeds to pinpoint wildfire ignition locations and create predictive models that map how a fire will spread.\n...\nThese models are further refined by AI-powered aerial sensing — including infrared imaging — to track fire perimeters through thick smoke and give responders a strategic advantage as wildfires progress.",
          "title": "Nine Breakthroughs Made Possible by AI - UC San Diego Today",
          "url": "https://today.ucsd.edu/story/nine-breakthroughs-made-possible-by-ai",
          "date": "2025-11-21",
          "last_updated": "2026-05-20"
        }
      ],
      "server_time": null
    }
    ```
  </Accordion>

  <Accordion title="Response — major technology trends">
    ```json theme={null}
    {
      "id": "b21a4380-b32c-418a-ba52-960c9fc3f15b",
      "results": [
        {
          "snippet": "## As technology innovation and adoption accelerate, five trends reveal how successful organizations are moving from experimentation to impact\nArticle\n...\nThe question used to be “What can we do with AI?”\nNow it’s “How do we move from experimentation to impact?”\n...\nFor 17 years, Tech Trends has explored emerging technologies poised to reshape business in the next 18 to 24 months.\nOur research is based on trend sensing from conversations with Deloitte subject matter experts and external technology leaders, as well as Deloitte’s proprietary research on emerging technologies.\nThis year, the data reveals five interconnected forces.\n## AI goes physical: Navigating the convergence of AI and roboticstiAmazon deployed its millionth robot, and its DeepFleet AI coordinates the entire robot fleet, improving travel efficiency within warehouses by 10%.^5^ BMW’s factories have cars driving themselves through kilometer-long production routes.^6^ Intelligence isn’t confined to screens anymore; it’s embodied, autonomous, and solving real problems in the physical world.\n## The agentic reality check: Preparing for a silicon-based workforceorOnly 11% of organizations have agents in production, despite 38% piloting them.\nThe gap between pilot to production tells you everything.\nForty-two percent are still developing their strategy, while 35% have no strategy at all.^7^ Gartner predicts that 40% of agentic projects will fail by 2027^8^—not because the technology doesn’t work, but because organizations are automating broken processes instead of redesigning operations.\nHPE’s chief financial officer captured what works: “We wanted to select an end-to-end process where we could truly transform, not just solve for a single pain point.”^9^ Redesign, don’t automate.\nThat’s the pattern separating success from failure.\n## The AI infrastructure reckoning: Optimizing compute strategy in the age of inference economicsmiToken costs have dropped 280-fold in two years;^10^ yet some enterprises are seeing monthly bills in the tens of millions.\nUsage exploded faster than costs declined.\nOrganizations are discovering their existing infrastructure strategies aren't designed to scale AI to production-scale deployment.\nThey're shifting from cloud-first to strategic hybrid: cloud for elasticity, on-premises for consistency, and edge for immediacy.\n## The great rebuild: Architecting an AI-native tech organizationtiAI is restructuring tech organizations, making them leaner, faster, and more strategic.\nOnly 1% of IT leaders surveyed by Deloitte reported that no major operating model changes were underway.^11^ Leaders are shifting from incremental IT management to orchestrating human-agent teams, with CIOs becoming AI evangelists.\nSuccess requires bold reimagination: modular architectures, embedded governance, and perpetual evolution as core capabilities.\n## The AI dilemma: Securing and leveraging AI for cyber defenseenThe technology meant to give businesses an advantage is becoming the target used against them.\nAT&T’s chief information security officer captured the challenge: “What we’re experiencing today is no different than what we’ve experienced in the past.\nThe only difference with AI is speed and impact.”^12^ Organizations must secure AI across four domains—data, models, applications, and infrastructure—but they also have the opportunity to use AI-powered defenses to fight threats operating at machine speed.",
          "title": "Tech Trends 2026 | Deloitte Insights",
          "url": "https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends.html",
          "date": "2025-12-10",
          "last_updated": "2026-05-24"
        },
        {
          "snippet": "",
          "title": "McKinsey Technology Trends Outlook 2025",
          "url": "https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-top-trends-in-tech",
          "date": "2025-07-22",
          "last_updated": "2026-05-27"
        },
        {
          "snippet": "",
          "title": "The new Essential Eight technology trends: PwC",
          "url": "https://www.pwc.com/us/en/tech-effect/emerging-tech/essential-eight-technologies.html",
          "date": "2023-11-15",
          "last_updated": "2026-05-21"
        },
        {
          "snippet": "### The year of truth for AI\nAI becomes the backbone of the digital economy, shifting from isolated proofs of concept to coherent, adaptive, and trusted value systems.\nThis transformation demands not just technology, but governance and cultural readiness to embed AI into the very fabric of enterprise decision-making.\n### AI is eating software\nThe paradigm moves from “writing code” to “expressing intent.”\nDevelopers articulate desired outcomes, and AI autonomously delivers, integrating and maintaining systems behind the scenes.\nAs software becomes self-assembling and self-healing, the competitive edge will hinge on mastering orchestration and governance rather than manual coding.\n### Cloud 3.0: all flavors of cloud\nCloud is entering its next evolution.\nAfter a decade focused on migration and cost efficiency, cloud is now becoming the operational backbone for AI and AI assisted apps.\nAI cannot scale only on the classical public cloud architectures.\nThe need to fine-tune models on proprietary data, manage data sensitivity, and deploy low-latency inference is pushing organizations toward hybrid, private, multi and sovereign cloud models, and not by exception.\nCloud ceases to be a passive infrastructure layer and becomes an active enabler of AI-driven architectures, ensuring portability, sovereignty.\n### The rise of intelligent ops\nMonolithic enterprise backbones evolve into living ecosystems of intelligent, modular, and continuously learning applications, blending human oversight with autonomous AI agents and putting the process back at the core.\nThis shift turns operations into adaptive engines of value creation, where resilience and agility become structural rather than aspirational.\nIntelligent operations position enterprises not just to run better, but to reinvent themselves continuously.\n### The borderless paradox of tech sovereignty\nTech sovereignty returns to at the top of the agenda, but the race is now for resilient interdependence—balancing open collaboration with strategic self-reliance.\nSuccess will depend on designing systems that remain globally connected yet controllable, embedding sovereignty principles into architecture rather than isolationist strategies.\n...\n### What are the Top Tech Trends to watch in 2026?\n*TechnoVision 2026* highlights **five transformative trends that will shape the technology landscape**.\nFirst, **the Year of Truth for AI** signals a shift from hype to measurable impact, as organizations focus on trust and enterprise-wide adoption.\nSecond, **AI is Eating Software**, meaning artificial intelligence is redefining the software lifecycle by moving from traditional coding to intent-driven development and autonomous maintenance.\nThird, **Cloud 3.0: All Flavors of Cloud** introduces a diversified ecosystem of hybrid, multi-cloud, and sovereign architectures to support AI scalability and resilience.\nFourth, **the Rise of Intelligent Ops** marks the evolution of enterprise systems into adaptive engines powered by AI agents for smarter operations.\nFinally, **the Borderless Paradox of Tech Sovereignty** reflects the challenge of balancing global interdependence with strategic control over critical technology stacks.\n...\nIn 2025, we highlighted five major trends—generative AI agents, AI-driven cybersecurity, autonomous robotics, the resurgence of nuclear energy to power computing, and supply chain reinvention—that reached a pivotal moment last year and continue to shape the landscape in 2026.\nWhile artificial Intelligence (AI) and generative AI (Gen AI) remain central, their influence now extends across software development, cloud architectures, and enterprise operations.\n...\nAfter years of fragmented pilots and inflated expectations, 2026 marks the shift from proof-of-concept to **proof-of-impact**.\n...\nThe upcoming year will see AI become the backbone of enterprise architecture, reshape software lifecycle development, and redefine cloud consumption.",
          "title": "Top Tech Trends 2026: AI Backbone, Intelligent Apps ... - Capgemini",
          "url": "https://www.capgemini.com/insights/research-library/top-tech-trends-of-2026/",
          "date": "2026-01-12",
          "last_updated": "2026-05-27"
        },
        {
          "snippet": "",
          "title": "Here are the top 10 trends in tech - The World Economic Forum",
          "url": "https://www.weforum.org/stories/2022/07/top-10-trends-in-tech/",
          "date": "2022-07-27",
          "last_updated": "2026-04-16"
        },
        {
          "snippet": "",
          "title": "Top 25 New Technology Trends in 2025 - GeeksforGeeks",
          "url": "https://www.geeksforgeeks.org/blogs/top-new-technology-trends/",
          "date": "2022-04-12",
          "last_updated": "2026-05-21"
        },
        {
          "snippet": "",
          "title": "25 New Technology Trends for 2025",
          "url": "https://www.simplilearn.com/top-technology-trends-and-jobs-article",
          "date": "2018-08-08",
          "last_updated": "2026-03-28"
        },
        {
          "snippet": "The question used to be “What can we do with AI?”\nNow it’s “How do we move from experimentation to impact?”\nThe focus has moved from endless pilots to real business value, and there’s a sense of urgency behind it all.\nNot because the technology is getting better—though it is—but because the pace of change itself has accelerated.\nThe numbers tell the story (figure 1).\nThe telephone took 50 years to reach 50 million users.\nThe internet took seven years.\nA leading generative AI tool reached about twice that many in two months.\n1 As of this writing, that tool has over 800 million weekly users—roughly 10% of the planet’s population.\n2\nBut rapid adoption is only the surface.\nInnovation is compounding; forces aren’t simply additive, but multiplicative.\nThink of it as a flywheel: Better technology enables more applications.\nMore applications generate more data.\nMore data attracts more investment.\nMore investment builds better infrastructure.\nBetter infrastructure reduces costs.\nLower costs enable more experimentation.\nEach improvement simultaneously accelerates all the others.\nIt’s why AI startups scale from US$1 million to US$30 million in revenue five times faster than SaaS companies did.\n3 It’s why the knowledge half-life in AI has shrunk to months from years.\n4 And it’s why one chief information officer (CIO) told me, “The time it takes us to study a new technology now exceeds that technology’s relevance window.”\n...\nFor 17 years, Tech Trends has explored emerging technologies poised to reshape business in the next 18 to 24 months.\nOur research is based on trend sensing from conversations with Deloitte subject matter experts and external technology leaders, as well as Deloitte’s proprietary research on emerging technologies.\nThis year, the data reveals five interconnected forces.\nAmazon deployed its millionth robot, and its DeepFleet AI coordinates the entire robot fleet, improving travel efficiency within warehouses by 10%.\n5 BMW’s factories have cars driving themselves through kilometer-long production routes.\n6 Intelligence isn’t confined to screens anymore; it’s embodied, autonomous, and solving real problems in the physical world.\nOnly 11% of organizations have agents in production, despite 38% piloting them.\nThe gap between pilot to production tells you everything.\nForty-two percent are still developing their strategy, while 35% have no strategy at all.\n7 Gartner predicts that 40% of agentic projects will fail by 2027 8—not because the technology doesn’t work, but because organizations are automating broken processes instead of redesigning operations.\nHPE’s chief financial officer captured what works: “We wanted to select an end-to-end process where we could truly transform, not just solve for a single pain point.”\n9 Redesign, don’t automate.\nThat’s the pattern separating success from failure.\nToken costs have dropped 280-fold in two years;\n10 yet some enterprises are seeing monthly bills in the tens of millions.\nUsage exploded faster than costs declined.\nOrganizations are discovering their existing infrastructure strategies aren't designed to scale AI to production-scale deployment.\nThey're shifting from cloud-first to strategic hybrid: cloud for elasticity, on-premises for consistency, and edge for immediacy.\nAI is restructuring tech organizations, making them leaner, faster, and more strategic.\nOnly 1% of IT leaders surveyed by Deloitte reported that no major operating model changes were underway.\n11 Leaders are shifting from incremental IT management to orchestrating human-agent teams, with CIOs becoming AI evangelists.\nSuccess requires bold reimagination: modular architectures, embedded governance, and perpetual evolution as core capabilities.\nThe technology meant to give businesses an advantage is becoming the target used against them.\nAT&T’s chief information security officer captured the challenge: “What we’re experiencing today is no different than what we’ve experienced in the past.\nThe only difference with AI is speed and impact.”\n12 Organizations must secure AI across four domains—data, models, applications, and infrastructure—but they also have the opportunity to use AI-powered defenses to fight threats operating at machine speed.\n...\nIt’s not just that AI is powerful.\nIt’s that the S-curves are compressing.\nThe distance between emerging and mainstream is collapsing.\nOrganizations built for sequential improvement can’t compete with those operating in continuous learning loops.\n...\nThat assumption no longer holds.",
          "title": "Tech Trends 2026",
          "url": "https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends.html?icid=disubnav_tech-trends",
          "date": "2025-12-10",
          "last_updated": "2025-12-11"
        },
        {
          "snippet": "Generative AI (gen AI) has rightly seized leaders’ attention in recent years.\nBut is it also eclipsing adjacent or lower-profile digital imperatives?\nQuantumBlack and the McKinsey Technology Council identified 15 most significant technology trends unfolding today, grouped into five broader categories: the AI revolution, building the digital future, compute and connectivity frontiers, cutting-edge engineering, and a sustainable world.",
          "title": "Top 15 technology trends unfolding today - McKinsey & Company",
          "url": "https://www.mckinsey.com/featured-insights/themes/top-15-technology-trends-unfolding-today",
          "date": "2024-08-10",
          "last_updated": "2025-09-20"
        },
        {
          "snippet": "## As technology innovation and adoption accelerate, five trends reveal how successful organizations are moving from experimentation to impact\nArticle\n...\nThe question used to be “What can we do with AI?”\n...\nFor 17 years, Tech Trends has explored emerging technologies poised to reshape business in the next 18 to 24 months.\nOur research is based on trend sensing from conversations with Deloitte subject matter experts and external technology leaders, as well as Deloitte’s proprietary research on emerging technologies.\nThis year, the data reveals five interconnected forces.\n## AI goes physical: Navigating the convergence of AI and robotics\nAmazon deployed its millionth robot, and its DeepFleet AI coordinates the entire robot fleet, improving travel efficiency within warehouses by 10%.^5^ BMW’s factories have cars driving themselves through kilometer-long production routes.^6^ Intelligence isn’t confined to screens anymore; it’s embodied, autonomous, and solving real problems in the physical world.\n## The agentic reality check: Preparing for a silicon-based workforce\nOnly 11% of organizations have agents in production, despite 38% piloting them.\nThe gap between pilot to production tells you everything.\nForty-two percent are still developing their strategy, while 35% have no strategy at all.^7^ Gartner predicts that 40% of agentic projects will fail by 2027^8^—not because the technology doesn’t work, but because organizations are automating broken processes instead of redesigning operations.\n...\nThat’s the pattern separating success from failure.\n## The AI infrastructure reckoning: Optimizing compute strategy in the age of inference economics\nToken costs have dropped 280-fold in two years;^10^ yet some enterprises are seeing monthly bills in the tens of millions.\nUsage exploded faster than costs declined.\nOrganizations are discovering their existing infrastructure strategies aren't designed to scale AI to production-scale deployment.\nThey're shifting from cloud-first to strategic hybrid: cloud for elasticity, on-premises for consistency, and edge for immediacy.\n## The great rebuild: Architecting an AI-native tech organization\nAI is restructuring tech organizations, making them leaner, faster, and more strategic.\nOnly 1% of IT leaders surveyed by Deloitte reported that no major operating model changes were underway.^11^ Leaders are shifting from incremental IT management to orchestrating human-agent teams, with CIOs becoming AI evangelists.\nSuccess requires bold reimagination: modular architectures, embedded governance, and perpetual evolution as core capabilities.\n## The AI dilemma: Securing and leveraging AI for cyber defense\nThe technology meant to give businesses an advantage is becoming the target used against them.\nAT&T’s chief information security officer captured the challenge: “What we’re experiencing today is no different than what we’ve experienced in the past.\nThe only difference with AI is speed and impact.”^12^ Organizations must secure AI across four domains—data, models, applications, and infrastructure—but they also have the opportunity to use AI-powered defenses to fight threats operating at machine speed.",
          "title": "Tech Trends 2025 | Deloitte Insights",
          "url": "https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends.html?icid=disidenav_tech-trends",
          "date": "2025-12-10",
          "last_updated": "2026-03-05"
        }
      ],
      "server_time": null
    }
    ```
  </Accordion>
</AccordionGroup>

## Parameter Reference

### `search_after_date_filter`

* **Type**: String
* **Format**: "%m/%d/%Y" (e.g., "3/1/2025")
* **Description**: Filters search results to only include content published after this date
* **Optional**: Yes
* **Example**: `"search_after_date_filter": "1/1/2025"`

### `search_before_date_filter`

* **Type**: String
* **Format**: "%m/%d/%Y" (e.g., "3/1/2025")
* **Description**: Filters search results to only include content published before this date
* **Optional**: Yes
* **Example**: `"search_before_date_filter": "12/31/2025"`

### `last_updated_after_filter`

* **Type**: String
* **Format**: "%m/%d/%Y" (e.g., "07/01/2025")
* **Description**: Filters search results to only include content last updated after this date
* **Optional**: Yes
* **Example**: `"last_updated_after_filter": "07/01/2025"`

### `last_updated_before_filter`

* **Type**: String
* **Format**: "%m/%d/%Y" (e.g., "12/30/2025")
* **Description**: Filters search results to only include content last updated before this date
* **Optional**: Yes
* **Example**: `"last_updated_before_filter": "12/30/2025"`

### `search_recency_filter`

* **Type**: String
* **Allowed Values**: "hour", "day", "week", "month", "year"
* **Description**: Filters search results to content from the specified time period relative to the current date
* **Optional**: Yes
* **Example**: `"search_recency_filter": "week"`

## Best Practices

**Date Format**

* Strict Format: Dates must match the "%m/%d/%Y" format exactly. For example, "3/1/2025" or "03/01/2025" is acceptable.
* Consistency: Use one or both date filters consistently based on your search needs. Combining both provides a clear range.

**Filter Selection**

* Choose the Right Filter Type: Use publication date filters (`search_after_date_filter`/`search_before_date_filter`) when you care about when content was originally created. Use last updated filters (`last_updated_after_filter`/`last_updated_before_filter`) when you need recently maintained content. Use recency filters (`search_recency_filter`) for quick, relative time filtering.
* Recency vs. Exact Dates: Use `search_recency_filter` for convenience when you want recent content (e.g., "past week"). Use specific date filters when you need precise control over the time range.
* Combining Filters: You can use both publication and last updated filters together to find content that meets both criteria (e.g., published in 2024 but updated recently). Note that `search_recency_filter` cannot be combined with specific date filters (`search_after_date_filter`/`search_before_date_filter` or `last_updated_after_filter`/`last_updated_before_filter`).

**Client-Side Validation**

* Regex Check: Validate date strings on the client side using a regex such as:

<CodeGroup>
  ```bash theme={null}
  date_regex='^(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/[0-9]{4}$'
  ```

  ```python theme={null}
  date_regex = r'^(0?[1-9]|1[0-2])/(0?[1-9]|[12]\d|3[01])/\d{4}$'
  ```
</CodeGroup>

This ensures that dates conform to the required format before sending the request.

**Performance Considerations**

* Narrowing the Search: Applying date range filters typically reduces the number of results, which may improve response times and result relevance.
* Avoid Over-Restriction: Ensure that the date range is neither too narrow (limiting useful results) nor too broad (defeating the purpose of the filter).

## Advanced Usage Patterns

**Finding Breaking News**

Use the `search_recency_filter` with `"hour"` for live events, or `"day"` for the most recent breaking news:

```python theme={null}
# Live events and real-time data
response = client.search(
    query="Apollo 11 moon landing mission overview",
    max_results=5,
    search_recency_filter="hour"
)

# Breaking news from the past 24 hours
response = client.search(
    query="breaking news technology",
    max_results=5,
    search_recency_filter="day"
)
```

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "1d212bdd-e54b-44de-8b21-b902c7dbf82b",
    "results": [
      {
        "snippet": "The primary objective of Apollo 11 was to complete a national goal set by President John F. Kennedy on May 25, 1961: perform a crewed lunar landing and return to Earth.\nAdditional flight objectives included scientific exploration by the lunar module, or LM, crew; deployment of a television camera to transmit signals to Earth; and deployment of a solar wind composition experiment, seismic experiment package and a Laser Ranging Retroreflector.\nDuring the exploration, the two astronauts were to gather samples of lunar-surface materials for return to Earth.\nThey also were to extensively photograph the lunar terrain, the deployed scientific equipment, the LM spacecraft, and each other, both with still and motion picture cameras.\nThis was to be the last Apollo mission to fly a “free-return” trajectory, which would enable a return to Earth with no engine firing, providing a ready abort of the mission at any time prior to lunar orbit insertion.\n...\nApollo 11 launched from Cape Kennedy on July 16, 1969, carrying Commander Neil Armstrong, Command Module Pilot Michael Collins and Lunar Module Pilot Edwin “Buzz” Aldrin into an initial Earth-orbit of 114 by 116 miles.\nAn estimated 650 million people watched Armstrong’s televised image and heard his voice describe the event as he took “…one small step for a man, one giant leap for mankind” on July 20, 1969.\nTwo hours, 44 minutes and one-and-a-half revolutions after launch, the S-IVB stage reignited for a second burn of five minutes, 48 seconds, placing Apollo 11 into a translunar orbit.\nThe command and service module, or CSM, Columbia separated from the stage, which included the spacecraft-lunar module adapter, or SLA, containing the lunar module, or LM, Eagle.\n...\nPartially piloted manually by Armstrong, the Eagle landed in the Sea of Tranquility in Site 2 at 0 degrees, 41 minutes, 15 seconds north latitude and 23 degrees, 26 minutes east longitude.\n...\nAfter a flight of 195 hours, 18 minutes, 35 seconds – about 36 minutes longer than planned – Apollo 11 splashed down in the Pacific Ocean, 13 miles from the recovery ship USS Hornet.\nBecause of bad weather in the target area, the landing point was changed by about 250 miles.\nApollo 11 landed 13 degrees, 19 minutes north latitude and 169 degrees, nine minutes west longitude July 24, 1969.\n**Crew**\nNeil Armstrong, Commander\nEdwin E.\n“Buzz” Aldrin Jr., Lunar Module Pilot\nMichael Collins, Command Module Pilot\n**Backup Crew**\nJames A. Lovell, Commander\nFred W. Haise Jr., Lunar Module Pilot\nWilliam A. Anders, Command Module Pilot\n**Payload**",
        "title": "Apollo 11 Mission Overview - NASA",
        "url": "https://www.nasa.gov/history/apollo-11-mission-overview/",
        "date": "2015-04-17",
        "last_updated": "2026-05-13"
      },
      {
        "snippet": "The primary objective of Apollo 11 was to complete a national goal set by President John F. Kennedy on May 25, 1961: perform a crewed lunar landing and return to Earth.\nMission Type\nLunar Landing\nastronauts\nNeil Armstrong, Buzz Aldrin, Michael Collins\nLaunch\nJuly 16, 1969\nSPLASHDOWN\nJuly 24, 1969\n...\n**First human to set foot on the Moon.**\nNeil A. Armstrong is probably best known as the commander for the Apollo 11 mission.\n...\nWatch highlights from the Apollo 11 mission including the launch on July 16, 1969, the landing of the lunar module, Neil Armstrong's first steps on the Moon, splashdown, and more.\n...\n20 July 1969—Astronaut Edwin E. Aldrin Jr., lunar module pilot, walks on the surface of the moon near the leg of the Lunar Module (LM) “Eagle” during the Apollo 11 extravehicular activity (EVA).\n...\nJOHNSON SPACE CENTER, HOUSTON, TEXAS – With a half-Earth in the background, the Lunar Module ascent stage with Moon-walking astronauts Neil Armstrong and Edwin Aldrin Jr. approaches for a rendezvous with the Apollo Command Module manned by Michael Collins.\nThe Apollo 11 liftoff from the Moon came early, ending a 22-hour stay on the Moon by Armstrong and Aldrin.\n...\nNeil Armstrong was the first person to walk on the moon.\nHe was an astronaut.\nHe flew on two space missions.\nOne was Apollo 11.",
        "title": "Apollo 11 - NASA",
        "url": "https://www.nasa.gov/mission/apollo-11/",
        "date": "2023-03-08",
        "last_updated": "2026-05-15"
      },
      {
        "snippet": "",
        "title": "Apollo 11 - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Apollo_11",
        "date": "2001-09-24",
        "last_updated": "2026-05-18"
      },
      {
        "snippet": "Apollo 11 was launched on July 16, 1969, at 8:32 AM Central Daylight Time (CDT) with the goal of performing the first human landing on the Moon.\nCommander Neil Armstrong, Command Module Pilot Michael Collins, and Lunar Module Pilot Edwin “Buzz” Aldrin entered lunar orbit on the afternoon of July 19.\nThe following day, Armstrong and Aldrin begin their descent to the lunar surface in the Lunar Module, Eagle.\nThe planned landing site in the Sea of Tranquility was selected as a flat, safe location and had been surveyed by Apollo 10 at an elevation of 10 miles above the Moon.\nHowever, a navigation error earlier in the mission caused Eagle to be about 7 kilometers beyond the planned landing location.\nDuring the 12.6-minute-long powered descent, there were a total of five unexpected computer alarms.\nThese alarms all indicated that Eagle’s computer system was overloaded, but in each case, Mission Control concluded that it was safe to continue the landing.\n...\nBecause of the navigation error, the computer was guiding the spacecraft towards an unsafe touchdown point in the rugged, boulder-filled ejecta field surrounding West Crater.\nArmstrong took manual control and flew to a safe landing spot beyond the crater.\nAt 3:17 PM CDT, he announced their safe landing, “Houston, Tranquility Base.\nThe Eagle has landed.”\nAt the time of landing, Mission Control thought that the spacecraft had just 17 seconds of fuel left in the descent stage.\nHowever, post mission analysis showed that sloshing in the fuel tank during Armstrong’s search for a safe landing site caused the fuel gauge to give an inaccurate reading.\nEagle actually had about 45 seconds of fuel left when it touched down.\nAfter a checkout of Eagle’s systems, Armstrong and Aldrin prepared for their moonwalk.\nAt 9:56 PM CDT, Armstrong set foot on the lunar surface, “That’s one small step for man, one giant leap for mankind.”\nAldrin followed a short while later.\nThe duration of this first ever moonwalk was limited to just 2 hours and 31 minutes and the crew remained within 60 meters of Eagle.\nArmstrong and Aldrin collected 21.6 kilograms of samples and deployed a seismometer to measure moonquakes, a laser retroreflector to enable precise measurements of the distance between Earth and the Moon, and a device to collect a sample of the solar wind.\nThey also performed ceremonial duties, including setting up a United States flag, unveiling a commemorative plaque on the lunar module, and having a brief conversation with President Richard Nixon.\nDuring the moon landing, Collins remained in lunar orbit in the command module, Columbia.\nAfter just 21.6 hours on the Moon, Eagle’s ascent stage returned to lunar orbit and rejoined Columbia.\nAltogether, Apollo 11 spent 2.5 days in lunar orbit, circling the Moon 31 times.\nThe crew returned safely to Earth on July 24, landing in the Pacific Ocean southwest of Hawaii, after a flight of 8 days and 3 hours.\nAlthough scientists considered it unlikely that the Moon had life on it, the crew was kept in a biological quarantine for 21 days.\nPost-mission analysis showed that the Apollo 11 samples consisted of two primary rock types.\nBasalt is formed by the solidification of molten magma.\nThe Apollo 11 basalts formed 3.6 to 3.9 billion years ago and are unusually rich in the element titanium.\nBreccias are composed of fragments of other rocks.\nOn the Moon, breccias formed from rocks that are broken up by impacting objects.\nAnalysis of the lunar samples also confirmed that they were indeed lifeless and showed no evidence of water.",
        "title": "Lunar - Missions - Apollo 11 Mission",
        "url": "https://www.lpi.usra.edu/lunar/missions/apollo/apollo_11/",
        "date": null,
        "last_updated": "2025-07-28"
      },
      {
        "snippet": "Apollo 11, the first space mission to put people on the Moon, was launched on July 16, 1969.\nAlmost every major aspect of the flight of Apollo 11 was witnessed via television by hundreds of millions of people in nearly every part of the globe, until splashdown in the Pacific Ocean on July 24.\n...\nApollo 11’s mission objective was to land astronauts on the Moon and return them safely back to Earth.\nIt succeeded in its objective by landing Neil Armstrong and Buzz Aldrin on the Moon on July 20, 1969.\n...\nApollo 11’s crew members were commander Neil Armstrong, lunar module pilot Buzz Aldrin, and command module pilot Michael Collins.\n...\nThe lunar module *Eagle* of the Apollo 11 mission landed on the Moon on July 20, 1969.\nNeil Armstrong and Buzz Aldrin became the first people to land on the Moon and walk on the lunar surface.\n...\nThe fastest speed Apollo 11 achieved was 39,715 kilometers (24,678 miles) per hour when the command module reentered Earth’s atmosphere on July 24, 1969.\n**\n**Apollo 11**, U.S. spaceflight during which commander Neil Armstrong and lunar module pilot Edwin (“Buzz”) Aldrin, Jr., on July 20, 1969, became the first people to land on the Moon and walk the lunar surface.\nApollo 11 was the culmination of the Apollo program and a massive national commitment by the United States to beat the Soviet Union in putting people on the Moon.\nAll told, 24 Apollo astronauts visited the Moon and 12 of them walked on its surface.\n...\nAt 10:56 pm EDT on July 20, Armstrong stepped out onto the lunar soil with the words, “That’s one small step for [a] man, one giant leap for mankind.”\n...\nAfter 21 hours 38 minutes on the Moon’s surface, the astronauts used *Eagle*’s ascent stage to launch it back into lunar orbit.\n...\nSplashdown of Apollo 11 occurred in the Pacific Ocean about 1,400 km (900 miles) west of Hawaii on July 24.",
        "title": "अपोलो 11 | इतिहास, मिशन, लैंडिंग, अंतरिक्ष यात्री, चित्र ...",
        "url": "https://www.britannica.com/topic/Apollo-11",
        "date": "2026-04-04",
        "last_updated": "2026-04-06"
      },
      {
        "snippet": "**On July 20, 1969, humans walked on the Moon for the first time.**\n**We look back at the legacy of our first small steps on the Moon and look forward to the next giant leap.**\n...\nThe Soviet Union launched the first human, Yuri Gagarin, into space on April 12, 1961.\nWithin days of the Soviet achievement, President John F. Kennedy asked Vice President Lyndon Johnson to identify a “space program which promises dramatic results in which we could win.”\nA little over a month later, on May 25, 1961, Kennedy stood before a joint session of Congress and called for human exploration to the Moon.\n...\nJuly 16, 1969\n## Liftoff!\nA Saturn V rocket carrying the three Apollo 11 astronauts blasted off from Cape Kennedy.\nOver a million spectators, including Vice President Spiro Agnew and former President Lyndon Johnson, came to watch the lift off.\nJuly 20, 1969\n## \"The Eagle has landed!\"\nAfter four days traveling to the Moon, the Lunar Module *Eagle*, carrying Neil Armstrong and Buzz Aldrin landed on the Moon.\nNeil Armstrong exited the spacecraft and became the first human to walk on the moon.\nAs an estimated 650 million people watched, Armstrong proclaimed \"That's one small step for man, one giant leap for mankind.\"\nMichael Collins stayed aboard the Command Module *Columbia*, serving as a communications link and photographing the lunar surface.\n...\n## The Sea of Tranquility | Mare Tranquillitatis\n**00.67408° N latitude, 23.47297° E longitude**\nFor the first lunar landing, the Sea of Tranquility (Mare Tranquilitatis) was the site chosen because it is a relatively smooth and level area.\nIt does, however, have some craters and in the last minutes before landing, Neil Armstrong had to manually pilot the lunar module to avoid a sharp-rimmed ray crater measuring some 180 meters across and 30 meters deep known as West.\nThe lunar module landed safely some 6 km from the originally intended landing site, approximately 400 meters west of West crater and 20km south-southwest of the crater Sabine D in the southwestern part of Mare Tranquilitatis.\nThe lunar surface at the landing site consisted of fragmental debris ranging in size from fine particles to blocks about 0.8 meter wide.\n...\nAfter approximately two and half hours on the Moon, Armstrong and Aldrin returned to the lunar module to begin the journey home.\nThe three astronauts splashed down in Hawaii on July 24, 1969.\nFrom there they quarantined for three weeks as a precaution against bringing contagion back from the Moon, before the festivities welcoming them home commenced.\n...\n## Michael Collins\n...\nThree astronauts were selected as backups for the crew: James A. Lovell, commander; William A. Anders, command module pilot; and Fred W. Haise, lunar module pilot.\nAll three backup crew members would eventually fly on Apollo missions.\n...\nOn July 20th, across the world, people gathered in front of televisions to watch the moon landing.\nAn estimated 650 million viewers were watching.\nIn the United States, 93% of televisions tuned in to see Neil Armstrong walk on the Moon.",
        "title": "Technology",
        "url": "https://airandspace.si.edu/explore/stories/apollo-11-moon-landing",
        "date": "2021-07-29",
        "last_updated": "2026-05-20"
      },
      {
        "snippet": "Apollo 11 (CSM Columbia and LM Eagle)\nSaturn V\nJuly 16-24, 1969\nNeil A. Armstrong\nMichael Collins\nEdwin E.\n\"Buzz\" Aldrin, Jr.\n08 days, 03 hours, 18 minutes\nFirst manned lunar landing mission and lunar\nsurface EVA.\n\"HOUSTON, TRANQUILITY BASE HERE.\nTHE EAGLE HAS LANDED.\"--July 20,\nLanding site: Sea of Tranquility.\nLanding Coordinates: 0.67409 degrees North, 23.47298 degrees East\n(Source: National Space Science Data Center); LROC QuickMap\n1 EVA of 02 hours, 31 minutes.\nFlag and instruments deployed; unveiled plaque on the LM descent stage with inscription: \"Here Men From Planet Earth First Set Foot Upon the Moon.\nJuly 1969 A.D.\nWe Came In Peace For All Mankind.\"\nLunar surface stay time 21.6 hours; 59.5 hours in lunar orbit, with 30 orbits.\nLM ascent stage left in lunar orbit.\n20 kg (44 lbs) of material gathered.",
        "title": "Apollo 11 Lunar Surface Journal : Mission Overview",
        "url": "https://www.nasa.gov/history/alsj/a11/a11ov.html",
        "date": null,
        "last_updated": "2025-10-25"
      },
      {
        "snippet": "Apollo 11 was the first mission to land humans on the Moon.\nIt fulfilled a 1961 goal set by President John F. Kennedy to send American astronauts to the surface and return them safely to Earth before the end of the decade.\nOn 21 July 1969 at 02:56:15 UTC, Neil Armstrong pressed his left foot onto the Moon and said, \"That's one small step for [a] man, one giant leap for mankind,\" as 530 million people watched live on television.\nThe mission returned 20 kilograms of rock and soil to Earth, and paved the way for 5 additional Moon landings that greatly advanced the field of lunar science.\nNeil Armstrong, Buzz Aldrin, and Michael Collins began their journey\nwith a launch aboard a Saturn V rocket on the morning of 16 July 1969.\nThree hours later, their rocket's upper stage blasted them out of Earth\norbit towards the Moon.\nThey arrived 3 days later on 19 July and entered\nan initial lunar orbit of 111 by 306 kilometers.\nA second engine burn\nlowered their orbit to 100 by 113 kilometers.\nOn 20 July, Armstrong and Aldrin boarded their lunar module, nicknamed Eagle, and undocked it from the command module, where Collins remained.\nAlmost the same as in the Apollo 10 rehearsal 2 months earlier, the astronauts fired Eagle’s descent engine, dropping to an orbit with a low point of 14.5 kilometers.\nRoughly an hour later, as the duo approached the Sea of Tranquility, they began a final powered descent to the surface.\n...\nThe official touchdown time was 20:17:39 UTC on 20 July 1969.\n...\nArmstrong and Aldrin's single moonwalk lasted two and a half hours.\nDuring that time, they deployed science and engineering experiments, photographed their surroundings, displayed an American flag, read an inscription plaque, collected rock and soil samples for return to Earth, and spoke with President Richard Nixon.\nThe astronauts verbally described their surroundings and progress for geologists, while cameras mounted inside and outside the lunar module documented some of their activities.\n...\nThe Apollo 11 lunar module landing coordinates are 0.67416 degrees N, 23.47314 E.",
        "title": "Apollo 11 | The Planetary Society",
        "url": "https://www.planetary.org/space-missions/apollo-11",
        "date": "2019-05-31",
        "last_updated": "2026-03-31"
      },
      {
        "snippet": "",
        "title": "Apollo 11 Mission Overview | NASA+",
        "url": "https://plus.nasa.gov/video/apollo-11-mission-overview/",
        "date": "2024-07-12",
        "last_updated": "2026-05-17"
      },
      {
        "snippet": "Overview of the Apollo 11 spaceflight in which U.S. astronauts became the first people to walk on the Moon.\n...\nThe mission that took U.S. astronauts to the Moon was Apollo 11, NASA’s fifth crewed Apollo mission.\nThe astronauts on board the spacecraft were Neil Armstrong, Edwin (“Buzz”) Aldrin, Jr., and Michael Collins.\nOn the morning of July 20, Armstrong and Aldrin crawled from the command module, Columbia, through a tunnel to the lunar module, Eagle.\nArmstrong and Aldrin piloted Eagle to the lunar surface, touching down in the Sea of Tranquility.\nAt 4:17 PM U.S. Eastern Daylight Time (EDT), Armstrong radioed, “Houston, Tranquility Base here.\nThe Eagle has landed.”\nAt 10:56 PM EDT on July 20, Armstrong stepped out onto the lunar soil with the words, “That’s one small step for [a] man, one giant leap for mankind.”\n(In the excitement of the moment, Armstrong skipped the “a” in the statement that he had prepared.)\nArmstrong and Aldrin set up a device to measure the composition of the solar wind reaching the Moon, a device to receive laser beams from astronomical observatories on Earth to determine the exact distance of the two bodies from one each other, and a passive seismometer to measure moonquakes and meteor impacts.\nThey also took about 23 kg (50 pounds) of rock and soil samples, took many photographs, and maintained constant communication with mission control in Houston, Texas.\nAfter 21 hours 38 minutes on the Moon’s surface, the astronauts used Eagle’s ascent stage to launch it back into lunar orbit.\nSplashdown of Apollo 11 occurred in the Pacific Ocean about 1,400 km (900 miles) southwest of Hawaii on July 24.\nAfter their return, the astronauts were quarantined for 21 days from the time Eagle had left the Moon.\nThey were checked for any diseases they might have brought back from the Moon.",
        "title": "Apollo 11's Incredible Journey to the Moon | Britannica",
        "url": "https://www.britannica.com/video/Just-the-facts-Apollo-11-moon-landing/-246490",
        "date": "2023-12-06",
        "last_updated": "2025-08-25"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

**Historical Research**

Use specific date ranges to research historical events or trends:

```python theme={null}
response = client.search(
    query="AI developments",
    max_results=20,
    search_after_date_filter="1/1/2023",
    search_before_date_filter="12/31/2023"
)
```

**Finding Recently Maintained Content**

Use last updated filters to find content that has been refreshed or maintained recently:

```python theme={null}
response = client.search(
    query="React best practices",
    max_results=10,
    last_updated_after_filter="07/01/2025"
)
```

**Trend Analysis**

Compare different time periods by making multiple searches:

```python theme={null}
# Recent trends
recent = client.search(
    query="machine learning trends",
    search_recency_filter="month"
)

# Older trends for comparison
older = client.search(
    query="machine learning trends",
    search_after_date_filter="1/1/2023",
    search_before_date_filter="1/31/2023"
)
```

## Error Handling

When using date filters, ensure proper error handling for invalid date formats:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity
  import re

  def validate_date_format(date_string):
      pattern = r'^(0?[1-9]|1[0-2])/(0?[1-9]|[12]\d|3[01])/\d{4}$'
      return bool(re.match(pattern, date_string))

  def search_with_date_filter(query, after_date=None, before_date=None):
      client = Perplexity()
      
      # Validate date formats
      if after_date and not validate_date_format(after_date):
          raise ValueError(f"Invalid date format: {after_date}")
      if before_date and not validate_date_format(before_date):
          raise ValueError(f"Invalid date format: {before_date}")
      
      try:
          response = client.search(
              query=query,
              search_after_date_filter=after_date,
              search_before_date_filter=before_date
          )
          return response
      except Exception as e:
          print(f"Search failed: {e}")
          return None
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  function validateDateFormat(dateString: string): boolean {
    const pattern = /^(0?[1-9]|1[0-2])\/(0?[1-9]|[12]\d|3[01])\/\d{4}$/;
    return pattern.test(dateString);
  }

  async function searchWithDateFilter(
    query: string, 
    afterDate?: string, 
    beforeDate?: string
  ) {
    const client = new Perplexity();
    
    // Validate date formats
    if (afterDate && !validateDateFormat(afterDate)) {
      throw new Error(`Invalid date format: ${afterDate}`);
    }
    if (beforeDate && !validateDateFormat(beforeDate)) {
      throw new Error(`Invalid date format: ${beforeDate}`);
    }
    
    try {
      const response = await client.search.create({
        query,
        search_after_date_filter: afterDate,
        search_before_date_filter: beforeDate
      });
      return response;
    } catch (error) {
      console.error('Search failed:', error);
      return null;
    }
  }
  ```
</CodeGroup>
