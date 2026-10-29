---
title: "Analysis library"
source: https://elevenlabs.io/docs/eleven-agents/customization/agent-analysis/analysis-library.md
path: docs/eleven-agents/customization/agent-analysis/analysis-library
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Analysis library

Evaluation criteria and data collection fields are stored as **analysis items** in your workspace. The analysis library lists every item, and each agent runs the items attached to it after a conversation. One item can be attached to several agents, so a change to it applies everywhere it is used.

## Open the library

In **Agents**, select **Analysis** in the sidebar. Search by name, or filter by kind and creator.

## Create and attach an item

#### Create the item

Click **Add evaluation** or **Add data collection**. Give the item a name, then write the prompt or extraction instructions. See [Success evaluation](/docs/eleven-agents/customization/agent-analysis/success-evaluation) and [Data collection](/docs/eleven-agents/customization/agent-analysis/data-collection) for how to write them.

#### Attach it to agents

Open the item, click **Attach to branches**, and select the agents and branches that should run it.

You can also start from an agent: in its **Analysis** tab, click **Add evaluation** or **Add data collection** to attach an existing item or create a new one.

## Edit an item

Editing an item publishes a new version, and every agent it is attached to runs the new version on its next conversation. Editing a criterion or field from an agent's **Analysis** tab edits the same item.

To change an item for one agent only, click **Duplicate** on the item and attach the copy to that agent instead.

The **Results** tab on an item shows its outcomes across the conversations of the agents it is attached to.

## Delete an item

An item that is attached to an agent cannot be deleted. Detach it first, or use **Force Delete** to remove it from every agent that uses it.

## Agents created before the library

Criteria and data collection fields configured on agents before the library existed were moved into it automatically. Each agent received its own items, so agents that used the same criterion now have separate items with the same name.

## Configure analysis through the API

Agent configurations that set `platform_settings.evaluation.criteria` or `platform_settings.data_collection` keep working. Each entry is stored as an analysis item attached to the agent, and changing an entry publishes a new version of that item. The attached items are listed in `platform_settings.analysis_items`.

## Limits

* Each agent can run up to 30 evaluation criteria.
* Each agent can have up to 50 data collection fields on Trial and Enterprise plans, and up to 25 on other plans.
