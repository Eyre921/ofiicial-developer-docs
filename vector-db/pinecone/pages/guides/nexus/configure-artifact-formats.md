---
title: "Configure artifact formats"
source: https://docs.pinecone.io/guides/nexus/configure-artifact-formats
path: guides/nexus/configure-artifact-formats
---

Configure Pinecone Nexus artifact types as markdown prose or queryable SQLite tables through the manifest API.

In Pinecone Nexus, curation writes each artifact type in one of two formats, set per type in the [manifest](/guides/nexus/context-design): `markdown` for prose, or `sqlite` for rows in a queryable table. You choose the format in the `manifest` you send when you create or update a context.

## Markdown artifacts

`markdown` is the default. Curation writes one prose file per artifact, embedded for semantic retrieval, so it fits knowledge that reads as text: summaries, concepts, and per-document notes. A markdown artifact type needs a `name`, a `kind`, a `scope`, and a `description` that steers what curation extracts:

```json theme={null}
{
  "name": "Concept",
  "kind": "topic",
  "scope": "corpus",
  "description": "A recurring concept or theme that appears across the corpus."
}
```

Omitting `format` defaults to `markdown`. See [artifact kinds](/guides/nexus/context-design#artifact-kinds) for the kinds a type can take.

## SQLite artifacts

`sqlite` writes rows into the context's structured database instead of prose, so the type becomes a table the query agent reads with SQL for exact counts, filters, and joins. Set `format` to `sqlite` and declare the table's `columns`:

```json theme={null}
{
  "name": "Meeting Log",
  "kind": "entity",
  "scope": "corpus",
  "format": "sqlite",
  "description": "One row per meeting: the body that met, the date, the type, and who chaired.",
  "columns": [
    { "name": "body", "type": "TEXT", "description": "The board, committee, or team that met, as a short canonical name." },
    { "name": "meeting_date", "type": "TEXT", "description": "The meeting date in ISO format, YYYY-MM-DD." },
    { "name": "year", "type": "INTEGER", "description": "The calendar year of the meeting." },
    { "name": "chair", "type": "TEXT", "description": "Full name of whoever chaired the meeting." }
  ],
  "natural_key": ["body", "meeting_date"]
}
```

* Each column has a `name`, a `type` (`TEXT`, `INTEGER`, `REAL`, or `NUMERIC`), and a `description` that steers what curation extracts into it.
* `natural_key` names the columns that identify a row, so re-curating a source upserts its rows instead of duplicating them.

Because the table is queryable, a `sqlite` type answers questions prose can't, like "how many meetings did each chair run this year?" or "who was present at a given meeting?" To answer across tables, define a second table that shares columns, so queries can join the two:

```json theme={null}
{
  "name": "Meeting Attendance",
  "kind": "entity",
  "scope": "corpus",
  "format": "sqlite",
  "description": "One row per person per meeting, taken from the attendance roster.",
  "columns": [
    { "name": "person", "type": "TEXT", "description": "The attendee's full name, spelled the same way wherever it appears, so counts and joins line up." },
    { "name": "body", "type": "TEXT", "description": "The body that met, matching Meeting Log." },
    { "name": "meeting_date", "type": "TEXT", "description": "The meeting date in ISO format, matching Meeting Log." },
    { "name": "status", "type": "TEXT", "description": "Either 'present' or 'absent', from the roster." }
  ],
  "natural_key": ["person", "body", "meeting_date"]
}
```

## Set the formats through the API

Put your artifact types in a context's manifest under `curate.artifacts.artifact_types`, then curate. The walkthrough below seeds the `Concept` and `Meeting Log` types, and you add more the same way. These steps use the data-plane base URL and session token from [Authentication](/reference/api/nexus/authentication).

<Note>
  Add at least one source to the context before you curate. See the [quickstart](/guides/nexus/quickstart) for creating a context and adding sources.
</Note>

<Steps>
  <Step title="Write the manifest to the context">
    Send the manifest when you create the context, or update an existing one with `PUT /contexts/{slug}`. This example seeds both a markdown type and a SQLite table at creation:

    ```bash curl theme={null}
    curl -fsS -X POST "$NEXUS_BASE_URL/contexts" \
      -H "Authorization: Bearer $NEXUS_TOKEN" \
      -H 'Content-Type: application/json' \
      -H 'X-Pinecone-Api-Version: 2026-07' \
      -d '{
        "slug": "board-minutes",
        "name": "Board minutes",
        "manifest": {
          "curate": {
            "artifacts": {
              "enabled": true,
              "artifact_types": [
                { "name": "Concept", "kind": "topic", "scope": "corpus",
                  "description": "A recurring concept or theme across the minutes." },
                { "name": "Meeting Log", "kind": "entity", "scope": "corpus", "format": "sqlite",
                  "description": "One row per meeting: body, date, and chair.",
                  "columns": [
                    { "name": "body", "type": "TEXT", "description": "The body that met." },
                    { "name": "meeting_date", "type": "TEXT", "description": "ISO date, YYYY-MM-DD." },
                    { "name": "chair", "type": "TEXT", "description": "Who chaired the meeting." }
                  ],
                  "natural_key": ["body", "meeting_date"] }
              ]
            }
          }
        }
      }'
    ```
  </Step>

  <Step title="Curate the context">
    Curation reads the sources and builds the artifacts your manifest defines. An empty body runs the first curate:

    ```bash curl theme={null}
    curl -fsS -X POST "$NEXUS_BASE_URL/contexts/board-minutes/curate" \
      -H "Authorization: Bearer $NEXUS_TOKEN" \
      -H 'Content-Type: application/json' \
      -H 'X-Pinecone-Api-Version: 2026-07' \
      -d '{}'
    ```

    After a later manifest change, pass `{"force": true}` to rebuild everything under the new manifest. Curation runs as a background task, so query the context once it finishes. See [How curation works](/guides/nexus/how-curation-works).
  </Step>

  <Step title="Query across both formats">
    A query reads both formats: the prose `Concept` artifacts semantically, and the `Meeting Log` table with SQL for exact answers.

    ```bash curl theme={null}
    curl -fsS -X POST "$NEXUS_BASE_URL/query" \
      -H "Authorization: Bearer $NEXUS_TOKEN" \
      -H 'Content-Type: application/json' \
      -H 'X-Pinecone-Api-Version: 2026-07' \
      -d '{"scope": ["board-minutes"], "ask": "How many meetings did each chair run this year?"}' \
    | jq -r '.output[].content[].text'
    ```

    ```console Output theme={null}
    Jordan Lee chaired 8 meetings, Priya Shah chaired 5, and Marcus Cole chaired 3.
    ```

    The counts come from the `Meeting Log` table, so they're exact rather than estimated from prose.
  </Step>
</Steps>
