---
title: "Set session instructions"
source: https://docs.pinecone.io/guides/nexus/set-session-instructions
path: guides/nexus/set-session-instructions
---

Set a per-session system prompt on a Pinecone Nexus query to shape how a session answers, layered over the context's default instructions.

A session can carry its own instructions, a system prompt that shapes every answer in the session. It can set the role to take, the tone to use, or the format of the result. Session instructions add to the context's [default instructions](/guides/nexus/context-design#context-default-instructions) instead of replacing them. The context default always applies, and if the session prompt only repeats it, Nexus skips the session prompt.

## Start and continue a session

Pass `system_prompt` on the query that starts the session, and it applies to every turn after that.

### 1. Start a session with a system prompt

Pass `system_prompt` with `scope` and `ask` on the opening query. You can set `scope` and `system_prompt` only when a session starts.

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

### 2. Continue the session

Reference the previous turn with `previous_query_id`. Follow-up turns keep the system prompt and the context default, so you don't resend either.

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
