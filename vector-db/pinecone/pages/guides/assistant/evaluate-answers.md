---
title: "Evaluate answers"
source: https://docs.pinecone.io/guides/assistant/evaluate-answers
path: guides/assistant/evaluate-answers
---

Evaluate RAG system answers with Pinecone Assistant using correctness, completeness, and alignment metrics against a ground truth answer.

This page shows you how to [evaluate responses](/guides/assistant/evaluation-overview) from an assistant or other RAG systems using the `metrics_alignment` operation.

You can [evaluate a response](/reference/api/latest/assistant/metrics_alignment) from an assistant, as in the following example. The `question` is what you asked, the `answer` is the response to evaluate, and `ground_truth_answer` (`groundTruth` in Node.js) is the response you expect.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  result = pc.assistants.evaluate_alignment(
      question="What are the capital cities of France, England and Spain?",
      answer="Paris is the capital city of France and Barcelona of Spain",
      ground_truth_answer="Paris is the capital city of France, London of England and Madrid of Spain.",
  )

  print(result)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const result = await pc.assistants.evaluate({
    question: 'What are the capital cities of France, England and Spain?',
    answer: 'Paris is the capital city of France and Barcelona of Spain',
    groundTruth: 'Paris is the capital city of France, London of England and Madrid of Spain.',
  });

  console.log(result);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://prod-1-data.ke.pinecone.io/assistant/evaluation/metrics/alignment" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
    "question": "What are the capital cities of France, England and Spain?",
    "answer": "Paris is the capital city of France and Barcelona of Spain",
    "ground_truth_answer": "Paris is the capital city of France, London of England and Madrid of Spain"
  }'
  ```
</CodeGroup>

```json Response theme={null}
{
  "metrics": {
    "correctness": 0.5,
    "completeness": 0.3333,
    "alignment": 0.4
  },
  "reasoning": {
    "evaluated_facts": [
      {
        "fact": {
          "content": "Paris is the capital city of France."
        },
        "entailment": "entailed"
      },
      {
        "fact": {
          "content": "London is the capital city of England."
        },
        "entailment": "neutral"
      },
      {
        "fact": {
          "content": "Madrid is the capital city of Spain."
        },
        "entailment": "contradicted"
      }
    ]
  },
  "usage": {
    "prompt_tokens": 1223,
    "completion_tokens": 51,
    "total_tokens": 1274
  }
}
```
