---
title: "Design your own manifest"
source: https://docs.pinecone.io/guides/nexus/design-your-own-manifest
path: guides/nexus/design-your-own-manifest
---

Design a Pinecone Nexus context's manifest yourself by defining custom artifact and edge types in the console, then curating.

When a template doesn't fit your corpus, you can design a context's [manifest](/guides/nexus/context-design) yourself. You define the artifact types and edge types that curation builds, and Pinecone Nexus handles the rest.

## Build the manifest

You design a manifest during a context's guided setup, which has three steps: **Add sources**, **Design your context**, and **Review and curate**. See the [quickstart](/guides/nexus/quickstart) for the full setup. The steps below start on **Design your context**.

<Note>
  Add at least one source to a context before you design its manifest. You can update it later from the context's **Manifest** tab with **Update design**, importing a new manifest or applying a different template.
</Note>

<Steps>
  <Step title="Start from scratch">
    On the **Design your context** step, under **Or start from scratch**, choose **Design your own**, then click **Review**. The **Review and curate** step opens with an empty manifest, which you fill in over the next two steps.
  </Step>

  <Step title="Add an artifact type">
    In **Artifact types**, click **+ Add artifact**, then fill in the fields:

    * **Name** is the type's identifier, shown in the console (for example, `department`).
    * **Kind** is the built-in shape it's based on: `summary`, `topic`, `entity`, `event`, `doc`, or `page`. See [artifact kinds](/guides/nexus/context-design#artifact-kinds).
    * **Scope** is `corpus` for one set across all sources, or `document` for one per source file.
    * **Description** tells curation, in plain language, what to extract.

    Click **Add**, then repeat for each type you want.
  </Step>

  <Step title="Add an edge type">
    Edges link your artifact types into a knowledge graph. This step is optional.

    In **Edge types**, click **+ Add edge**, then fill in the fields:

    * **Name** is the relationship (for example, `owns`).
    * **From** and **To** are the artifact types the edge connects.
    * **Description** explains what the relationship means.

    Click **Add edge**, then repeat for each relationship you want.
  </Step>

  <Step title="Check the cost and curate">
    Check the **Model** and the **Estimated cost**. To see the manifest you built, expand **Review manifest JSON**. When it looks right, click **Save and curate**. The curation task opens.

    Curation runs in the background. When it finishes, your artifact types appear on the context's **Knowledge** tab, and queries can traverse the edges you defined.
  </Step>
</Steps>

## Example manifest

A finished manifest looks like this, with your artifact and edge types under `curate.artifacts`:

```json theme={null}
{
  "curate": {
    "artifacts": {
      "enabled": true,
      "artifact_types": [
        {
          "name": "department",
          "kind": "entity",
          "scope": "corpus",
          "description": "A team or department that owns policies."
        },
        {
          "name": "policy",
          "kind": "topic",
          "scope": "corpus",
          "description": "A company policy and the rules it sets."
        }
      ],
      "edge_types": [
        {
          "name": "owns",
          "from": "department",
          "to": "policy",
          "description": "The department responsible for a policy."
        }
      ]
    }
  }
}
```

## Import a manifest instead

If you already have a manifest, skip the builder. On the **Design your context** step, under **Or start from scratch**, choose **Import your own manifest**, paste a complete manifest in the shape shown [above](#example-manifest), then click **Save and curate**. Nexus applies it and starts curation.
