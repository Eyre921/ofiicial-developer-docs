---
title: "Keep context"
source: https://docs.perplexity.ai/docs/agent-api/building-agents/keep-context
path: docs/agent-api/building-agents/keep-context
---

Carry a conversation across turns by replaying it in the input array, so a follow-up understands what came before.

The Agent API keeps no state across requests: each call sees only its own payload, so nothing from a previous response carries over automatically. To make a follow-up build on an earlier turn, replay the prior conversation in the `input` array. This page shows how.

## Chain turns by replaying `input`

Send the next turn as an `input` array that includes the prior turns. Each turn is a message item with a `role` (`user` or `assistant`). Append the new question at the end.

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  first = client.responses.create(
      model="openai/gpt-5.5",
      input="Who won the 2022 FIFA World Cup?",
      tools=[{"type": "web_search"}],
  )
  print(first.output_text)

  # Replay the conversation so far, then add the follow-up.
  second = client.responses.create(
      model="openai/gpt-5.5",
      input=[
          {"role": "user", "content": "Who won the 2022 FIFA World Cup?"},
          {"role": "assistant", "content": first.output_text},
          {"role": "user", "content": "Who did they beat in the final, and what was the score?"},
      ],
  )
  print(second.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const first = await client.responses.create({
    model: 'openai/gpt-5.5',
    input: 'Who won the 2022 FIFA World Cup?',
    tools: [{ type: 'web_search' as const }],
  });
  console.log(first.output_text);

  const second = await client.responses.create({
    model: 'openai/gpt-5.5',
    input: [
      { role: 'user', content: 'Who won the 2022 FIFA World Cup?' },
      { role: 'assistant', content: first.output_text ?? '' },
      { role: 'user', content: 'Who did they beat in the final, and what was the score?' },
    ],
  });
  console.log(second.output_text);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/agent \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.5",
      "input": [
        { "role": "user", "content": "Who won the 2022 FIFA World Cup?" },
        { "role": "assistant", "content": "Argentina won the 2022 FIFA World Cup." },
        { "role": "user", "content": "Who did they beat in the final, and what was the score?" }
      ]
    }' | jq
  ```
</CodeGroup>

## Next steps

<CardGroup>
  <Card title="Image Attachments" icon="eye" href="/docs/agent-api/image-attachments">
    Attach images to a request.
  </Card>

  <Card title="Output Control" icon="sliders" href="/docs/agent-api/output-control">
    Streaming, background runs, error handling, and full structured-output examples.
  </Card>
</CardGroup>
