---
title: "Design your own manifest"
source: https://docs.pinecone.io/guides/nexus/design-your-own-manifest
path: guides/nexus/design-your-own-manifest
---

Author a Pinecone Nexus context's manifest through the API by defining custom artifact and edge types, then curating.

When a template doesn't fit your corpus, you can author a Pinecone Nexus context's [manifest](/guides/nexus/context-design) yourself. You define the artifact types and edge types curation builds, send them in the `manifest` field when you create or update a context, then curate.

## Artifact and edge types

A manifest's `curate.artifacts` section holds your artifact types and edge types:

* An artifact type has a `name`, a `kind` (its built-in shape, see [artifact kinds](/guides/nexus/context-design#artifact-kinds)), a `scope` (`corpus` for one artifact per subject across the corpus, or `document` for one per source), and a `description` that steers extraction. Optionally, `coverage` lists the points the extraction must address. A type defaults to the `markdown` format. See [artifact formats](/guides/nexus/configure-artifact-formats) for the `sqlite` table format.
* An edge type has a `name`, the `from` and `to` artifact types it connects, a `description`, and optional `attributes` recorded on each edge. Edges turn the artifacts into a graph the query agent can traverse.

The `kind` sets what an artifact represents and how it's extracted. The `name` is your label for that type. A corpus can mix kinds: a per-document `summary`, corpus-wide `topic` and `entity` types, and dated `event` types, linked by edges.

## Author it through the API

These steps use the data-plane base URL and session token from [Authentication](/reference/api/nexus/authentication). The manifest here is a general concept-and-entity design: a per-document note, corpus-wide concepts and entities, and an edge linking them.

<Steps>
  <Step title="Create the context with your manifest">
    Send the manifest in the `manifest` field when you create the context. To apply it to an existing context instead, use `PUT /contexts/{slug}` with the same body.

    ```bash curl theme={null}
    curl -fsS -X POST "$NEXUS_BASE_URL/contexts" \
      -H "Authorization: Bearer $NEXUS_TOKEN" \
      -H 'Content-Type: application/json' \
      -H 'X-Pinecone-Api-Version: 2026-07' \
      -d '{
        "slug": "company-knowledge",
        "name": "Company knowledge",
        "manifest": {
          "curate": {
            "artifacts": {
              "enabled": true,
              "artifact_types": [
                { "name": "Note", "kind": "summary", "scope": "document",
                  "description": "A per-document note: key points, decisions, and takeaways." },
                { "name": "Concept", "kind": "topic", "scope": "corpus",
                  "description": "A recurring concept or theme across the corpus." },
                { "name": "Entity", "kind": "entity", "scope": "corpus",
                  "description": "A named person, organization, product, or system across the corpus." }
              ],
              "edge_types": [
                { "name": "relates_to", "from": "Entity", "to": "Concept",
                  "description": "The entity relates to or exemplifies this concept." }
              ]
            }
          }
        }
      }'
    ```
  </Step>

  <Step title="Add sources">
    Curation needs sources. Upload files or import from a connector, then confirm at least one source is staged. See the [quickstart](/guides/nexus/quickstart) for adding sources.
  </Step>

  <Step title="Curate">
    Curation executes the manifest against the sources, building your artifact and edge types:

    ```bash curl theme={null}
    curl -fsS -X POST "$NEXUS_BASE_URL/contexts/company-knowledge/curate" \
      -H "Authorization: Bearer $NEXUS_TOKEN" \
      -H 'Content-Type: application/json' \
      -H 'X-Pinecone-Api-Version: 2026-07' \
      -d '{}'
    ```

    An empty body runs an incremental curate. After a later manifest change, pass `{"force": true}` to rebuild everything under the new manifest. Curation runs as a background task, so query the context once it finishes. See [How curation works](/guides/nexus/how-curation-works).
  </Step>

  <Step title="Query the context">
    Query the context to see the artifacts and edges curation built:

    ```bash curl theme={null}
    curl -fsS -X POST "$NEXUS_BASE_URL/query" \
      -H "Authorization: Bearer $NEXUS_TOKEN" \
      -H 'Content-Type: application/json' \
      -H 'X-Pinecone-Api-Version: 2026-07' \
      -d '{"scope": ["company-knowledge"], "ask": "How do the entities relate to each concept?"}'
    ```
  </Step>
</Steps>

## More example manifests

Each of these is a `curate.artifacts` manifest for a different corpus. Send one in the `manifest` field the same way, and adjust the types to your own documents.

<AccordionGroup>
  <Accordion title="Contracts, obligations, and key dates">
    Shows the `event` kind, a `coverage` list on a type, and edge `attributes`.

    ```json theme={null}
    {
      "curate": {
        "artifacts": {
          "enabled": true,
          "artifact_types": [
            { "name": "Agreement", "kind": "entity", "scope": "corpus",
              "description": "One contract or agreement in the corpus." },
            { "name": "Party", "kind": "entity", "scope": "corpus",
              "description": "A person or organization that is party to an agreement." },
            { "name": "Obligation", "kind": "topic", "scope": "corpus",
              "description": "A duty an agreement imposes on a party.",
              "coverage": ["Who owes the obligation", "What it requires", "Any deadline or condition"] },
            { "name": "Key Date", "kind": "event", "scope": "corpus",
              "description": "A dated milestone in an agreement, such as an effective or renewal date." }
          ],
          "edge_types": [
            { "name": "party_to", "from": "Party", "to": "Agreement",
              "description": "The party is bound by this agreement.", "attributes": ["role"] },
            { "name": "owed_by", "from": "Party", "to": "Obligation",
              "description": "The party owes this obligation." },
            { "name": "effective_on", "from": "Agreement", "to": "Key Date",
              "description": "The agreement takes effect on this date.", "attributes": ["type"] }
          ]
        }
      }
    }
    ```
  </Accordion>

  <Accordion title="Papers and citations">
    Shows a per-document summary and a self-referential edge (a paper cites another paper).

    ```json theme={null}
    {
      "curate": {
        "artifacts": {
          "enabled": true,
          "artifact_types": [
            { "name": "Paper Summary", "kind": "summary", "scope": "document",
              "description": "A per-paper summary: the problem, method, and headline result." },
            { "name": "Paper", "kind": "entity", "scope": "corpus",
              "description": "One research paper in the corpus." },
            { "name": "Method", "kind": "topic", "scope": "corpus",
              "description": "A method or technique a paper uses." }
          ],
          "edge_types": [
            { "name": "uses_method", "from": "Paper", "to": "Method",
              "description": "The paper uses this method." },
            { "name": "cites", "from": "Paper", "to": "Paper",
              "description": "The paper cites another paper.", "attributes": ["context"] }
          ]
        }
      }
    }
    ```
  </Accordion>

  <Accordion title="Code and technical docs">
    Shows a dependency graph: a self-referential `depends_on` edge, plus edge `attributes`.

    ```json theme={null}
    {
      "curate": {
        "artifacts": {
          "enabled": true,
          "artifact_types": [
            { "name": "Component", "kind": "entity", "scope": "corpus",
              "description": "A service, module, or library in the codebase." },
            { "name": "API Endpoint", "kind": "entity", "scope": "corpus",
              "description": "An endpoint a component exposes." },
            { "name": "Pattern", "kind": "topic", "scope": "corpus",
              "description": "A design or architectural pattern used across the codebase." }
          ],
          "edge_types": [
            { "name": "depends_on", "from": "Component", "to": "Component",
              "description": "The component depends on another component.", "attributes": ["type"] },
            { "name": "exposes_endpoint", "from": "Component", "to": "API Endpoint",
              "description": "The component exposes this endpoint.", "attributes": ["method"] },
            { "name": "implements_pattern", "from": "Component", "to": "Pattern",
              "description": "The component implements this pattern." }
          ]
        }
      }
    }
    ```
  </Accordion>
</AccordionGroup>

## Tune the design

Beyond the basics, a few fields shape how thoroughly curation builds each type:

* `coverage` (per type): The points the extraction must address wherever a source speaks to them. Use it to make a type consistent and thorough.
* `scope` (per type): Set `document` for one artifact per source, which suits summaries and notes, or `corpus` to fold mentions from across every source into one artifact per subject, which suits entities and themes.
* `attributes` (per edge): Extra values recorded on each edge, such as a `role` on a `party_to` edge or a `value` on a metric edge.
* `min_doc_count` (on `curate.artifacts`, or overridden per type): How many sources must mention a corpus subject before it earns its own artifact. Raise it to suppress one-off mentions.

For the `sqlite` table format, its `columns`, and its upsert `natural_key`, see [artifact formats](/guides/nexus/configure-artifact-formats).

## Revise a manifest

To change a context's manifest after it's curated:

1. Send the full updated manifest with `PUT /contexts/{slug}`.
2. Run a forced curate, `POST /contexts/{slug}/curate` with `{"force": true}`, so the change reaches the index.

This is the API equivalent of updating a context's design in the console. To read the manifest currently pinned on a context, use `GET /contexts/{slug}/manifest`.
