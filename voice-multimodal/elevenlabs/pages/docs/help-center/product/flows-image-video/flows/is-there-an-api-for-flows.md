---
title: "Is there an API for Flows?"
source: https://elevenlabs.io/docs/help-center/product/flows-image-video/flows/is-there-an-api-for-flows.md
path: docs/help-center/product/flows-image-video/flows/is-there-an-api-for-flows
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Is there an API for Flows?

Yes, in two ways:

* **Run a flow you built in the app.** Publish the flow as a template, and you can run it through the API with your own input values, for example to connect a CMS to a flow for automated content generation. See the [Templates quickstart](/docs/eleven-api/guides/cookbooks/templates).
* **Build the chain in code.** The [Image & Video API](/docs/eleven-api/guides/cookbooks/image-and-video) runs one generation per call, the equivalent of one node in a flow, and each generation can take a previous one as a reference. Your code decides which models to call and in what order, so it can assemble a different chain for each request. See [Chain one generation into the next](/docs/eleven-api/guides/how-to/image-and-video/references#chain-one-generation-into-the-next).
