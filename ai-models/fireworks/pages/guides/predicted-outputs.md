---
title: "Using predicted outputs"
source: https://docs.fireworks.ai/guides/predicted-outputs
path: guides/predicted-outputs
---

Use Predicted Outputs to boost output generation speeds for editing / rewriting use cases

<Tip>
  This feature is in beta and we are working on improvements. We welcome your feedback on [Discord](https://discord.gg/fireworks-ai)
</Tip>

In cases where large parts of the LLM output are known in advance, e.g. editing or rewriting a document or code snippet, you can improve output generation speeds with predicted outputs. Predicted outputs allows you to provide strong "guesses" of what output may look like.

Predicted Outputs is configured per request and can work alongside the model-based speculative decoding configured on a dedicated deployment. See [Speculative Decoding](/deployments/speculative-decoding) to compare the available methods.

To use Predicted Outputs, set the `prediction` field in the Fireworks API with the predicted output. For example, you may want to edit a survey and add an option to contact users by text message:

```
{
  "questions": [
    {
      "question": "Name",
      "type": "text"
    },
    {
      "question": "Age",
      "type": "number"
    },
    {
      "question": "Feedback",
      "type": "text_area"
    },
    {
      "question": "How to Contact",
      "type": "multiple_choice",
      "options": ["Email", "Phone"],
      "optional": true
    }
  ]
}
```

In this case, we expect most of the code will remain the same. We set the ‘prediction’ field to be the original survey code. The output generation speed increases using predicted outputs.

```python Python (Fireworks) theme={null}
from fireworks.client import Fireworks
 
code = """{
"questions": [
    {
      "question": "Name",
      "type": "text"
    },
    {
      "question": "Age",
      "type": "number"
    },
    {
      "question": "Feedback",
      "type": "text_area"
    },
    {
      "question": "How to Contact",
      "type": "multiple_choice",
      "options": ["Email", "Phone"],
      "optional": true
    }
  ]
}
"""

client = Fireworks(api_key="<FIREWORKS_API_KEY>")

response = client.chat.completions.create(
  model="accounts/fireworks/models/llama-v3p1-70b-instruct",
  messages=[{
      "role": "user",
      "content": "Edit the How to Contact question to add an option called Text Message. Output the full edited code, with no markdown or explanations.",
    },
    {
      "role": "user",
      "content": code
    }
  ],
  temperature=0,
  prediction={"type": "content", "content": code}
)

print(response.choices[0].message.content)
```

### Additional information on Predicted Outputs:

* Using Predicted Outputs is free at this time
* We recommend setting `temperature=0` for best results for most intended use cases of Predicted Outputs. In these cases, using Predicted Outputs does not impact the quality of outputs generated
* If the prediction is substantially different from the generated output, output generation speed may decrease
* The max length of the `prediction` field is set by `max_tokens` and is 2048 by default, and needs to be updated if you have a longer input and prediction.
* If you are using an on-demand deployment, you can set `rewrite_speculation=True` and potentially get even faster output generation. We are working on rolling this out to Serverless soon.
