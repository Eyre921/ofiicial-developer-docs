---
title: "Set session instructions"
source: https://docs.pinecone.io/guides/nexus/set-session-instructions
path: guides/nexus/set-session-instructions
---

Set a per-session system prompt on a Pinecone Nexus query to shape how a session answers, layered over the context's default instructions.

A session can carry its own answer instructions, a system prompt that shapes how it answers every turn: the role to take, the tone to use, or how to format the result. These layer on top of a context's [default instructions](/guides/nexus/context-design#context-default-instructions) rather than replacing them. The context default always applies, and the session prompt adds to it, except where it only repeats the default, which Nexus skips.

You pass `system_prompt` on the query that starts the session, and it stays pinned for the rest of the session.

<Steps>
  <Step title="Start a session with a system prompt">
    Pass `system_prompt` alongside `scope` and `ask` on the opening query. These fields are set only when a session starts.

    ```bash curl theme={null}
    curl -fsS -X POST "$NEXUS_BASE_URL/query" \
      -H "Authorization: Bearer $NEXUS_TOKEN" \
      -H 'Content-Type: application/json' \
      -H 'X-Pinecone-Api-Version: 2026-07' \
      -d '{
        "scope": ["company-knowledge"],
        "ask": "What changed in the latest contract?",
        "system_prompt": "Answer as a contracts analyst. Be concise, and cite the clause behind every claim."
      }'
    ```

    The response carries a `session_id` and the query's `id`.
  </Step>

  <Step title="Continue the session">
    Reference the previous turn with `previous_query_id`. Follow-up turns keep the system prompt, so you don't resend it, and the context default still applies.

    ```bash curl theme={null}
    curl -fsS -X POST "$NEXUS_BASE_URL/query" \
      -H "Authorization: Bearer $NEXUS_TOKEN" \
      -H 'Content-Type: application/json' \
      -H 'X-Pinecone-Api-Version: 2026-07' \
      -d '{
        "previous_query_id": "qry_...",
        "ask": "Who owns the renewal?"
      }'
    ```
  </Step>
</Steps>

In the console, open **Advanced options** in the new session composer and set the **System prompt**.
