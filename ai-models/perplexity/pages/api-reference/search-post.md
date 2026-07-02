---
title: "Search the Web"
source: https://docs.perplexity.ai/api-reference/search-post
path: api-reference/search-post
---

post /search
Search the web and retrieve relevant web page contents.

<Info>
  **Search API vs. Sonar.** These are different APIs with different response shapes.

  * **Search API** — Returns structured JSON `results[]` with `title`, `url`, `snippet`, `date`, and `last_updated`. Call `https://api.perplexity.ai/search` directly — no router required.
  * **[Sonar](/docs/sonar/quickstart)** — Chat completions with built-in web search. Returns a prose answer with citations, not a results array.

  Both are first-party Perplexity APIs. Neither routes through OpenRouter.
</Info>

## Response Shape

The Search API returns a ranked `results[]` array. Each result includes `title`, `url`, `snippet`, and optional `date` and `last_updated` fields:

<Accordion title="Example Response">
  ```json theme={null}
  {
    "results": [
      {
        "title": "Example Article Title",
        "url": "https://example.com/article",
        "snippet": "A short excerpt from the article relevant to the query...",
        "date": "2025-01-23",
        "last_updated": "2025-09-25"
      },
      {
        "title": "Another Relevant Source",
        "url": "https://example.org/source",
        "snippet": "Another excerpt showing the structured result format.",
        "date": "2024-11-15",
        "last_updated": "2025-08-12"
      },
      {
        "title": "Third Result",
        "url": "https://example.net/page",
        "snippet": "A third result demonstrating the ranked array structure.",
        "date": "2024-09-10",
        "last_updated": "2025-07-03"
      }
    ],
    "id": "e38104d5-6bd7-4d82-bc4e-0a21179d1f77"
  }
  ```
</Accordion>

## Direct Call

```bash theme={null}
curl -X POST 'https://api.perplexity.ai/search' \
  -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "latest AI developments",
    "max_results": 3
  }' | jq
```
