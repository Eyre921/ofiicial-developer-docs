---
title: "Evaluate an answer"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/metrics_alignment
path: reference/api/2026-07/assistant/metrics_alignment
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_evaluation_2026-07.oas.yaml POST /evaluation/metrics/alignment
Evaluate the correctness and completeness of a response from an assistant or a RAG system. The correctness and completeness are evaluated based on the precision and recall of the generated answer with respect to the ground truth answer facts. Alignment is the harmonic mean of correctness and completeness.

For guidance and examples, see [Evaluate answers](https://docs.pinecone.io/guides/assistant/evaluate-answers).

```python Python theme={null}
# pip install --upgrade pinecone
import os
from pinecone import Pinecone

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

result = pc.assistants.evaluate_alignment(
    question="What are the capital cities of France, England and Spain?",
    answer="Paris is the capital city of France and Barcelona of Spain",
    ground_truth_answer="Paris is the capital city of France, London of England and Madrid of Spain",
)
print(result.scores.correctness, result.scores.completeness, result.scores.alignment)
```

```javascript JavaScript theme={null}
// npm install @pinecone-database/pinecone
import { Pinecone } from '@pinecone-database/pinecone';

// Reads PINECONE_API_KEY from the environment
const pc = new Pinecone();

const result = await pc.assistants.evaluate({
  question: 'What are the capital cities of France, England and Spain?',
  answer: 'Paris is the capital city of France and Barcelona of Spain',
  groundTruth: 'Paris is the capital city of France, London of England and Madrid of Spain',
});
console.log(result.metrics.correctness, result.metrics.completeness, result.metrics.alignment);
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl https://prod-1-data.ke.pinecone.io/assistant/evaluation/metrics/alignment \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "question": "What are the capital cities of France, England and Spain?",
    "answer": "Paris is the capital city of France and Barcelona of Spain",
    "ground_truth_answer": "Paris is the capital city of France, London of England and Madrid of Spain"
}'
```
