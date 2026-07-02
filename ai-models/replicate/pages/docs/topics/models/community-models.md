---
title: "Community models"
source: https://replicate.com/docs/topics/models/community-models.md
path: docs/topics/models/community-models
---

Community models are models that people in the Replicate community have created and shared. These range from fine-tuned versions of popular models to completely custom implementations that solve specific problems.

[](#what-are-community-models)What are community models?
--------------------------------------------------------

Community models are models that users have created and published on Replicate. They can be:

*   Fine-tuned models: Custom versions of existing models trained on specific datasets
*   Custom implementations: Models built from scratch using [Cog](https://cog.run/) and packaged as containers
*   Research implementations: Academic or experimental models

Custom-built community models are packaged and published using [Cog](https://cog.run/), an open-source tool that lets you package machine learning models in standard, production-ready containers. This ensures consistency and makes it easier to deploy models across different environments.

Unlike [official models](/docs/topics/models/official-models), community models are maintained by their creators, not by Replicate. This means they may have different levels of stability, documentation, and support.

[](#how-to-run-community-models)How to run community models
-----------------------------------------------------------

Community models work the same way as other models on Replicate. You can run them using the same tools and interfaces.

### [](#using-the-api)Using the API

When running community models, you need to specify the [model version](/docs/topics/models/versions). Here’s an example using the Python client:

```python
import replicate
# Run a community model with a specific version
output = replicate.run(
    "prunaai/flux.1-dev:b0306d92aa025bb747dc74162f3c27d6ed83798e08e5f8977adf3d859d0536a3",
    input={"prompt": "A beautiful sunset over mountains"}
)
```

### [](#using-the-web-interface)Using the web interface

You can also run community models directly in the web playground:

1.  Visit the model page on Replicate, like [replicate.com/prunaai/flux.1-dev](https://replicate.com/prunaai/flux.1-dev)
2.  Fill in the input parameters
3.  Click **Run** to start the prediction

[](#differences-from-official-models)Differences from official models
---------------------------------------------------------------------

Community models differ from official models in several key ways:

### [](#api-stability)API stability

*   Official models: Have stable APIs that don’t change without notice
*   Community models: May have API changes between [versions](/docs/topics/models/versions) as creators improve their models

### [](#pricing)Pricing

*   Official models: Priced by predictable metrics (per image, per token, etc.)
*   Community models: Priced by hardware usage and runtime

### [](#availability)Availability

*   Official models: Always warm and ready to respond
*   Community models: May experience cold boots when not frequently used

### [](#support)Support

*   Official models: Maintained and supported by Replicate
*   Community models: Supported by their creators

[](#using-deployments-for-better-control)Using deployments for better control
-----------------------------------------------------------------------------

For community models that you rely on heavily, you can create [deployments](/docs/topics/deployments) to have more control over performance and scaling behavior.

### [](#benefits-of-deployments)Benefits of deployments

*   Always warm: Deployed models stay warm and ready to respond
*   Predictable performance: No cold boots or scaling delays
*   Custom scaling: Set minimum and maximum instances based on your needs
*   Dedicated resources: Your model runs on dedicated hardware

### [](#creating-a-deployment)Creating a deployment

You can create a deployment from any community model:

```python
import replicate
# Create a deployment
deployment = replicate.deployments.create(
    name="my-flux-deployment",
    model="prunaai/flux.1-dev",
    version="b0306d92aa025bb747dc74162f3c27d6ed83798e08e5f8977adf3d859d0536a3",
    hardware="gpu-t4",
    min_instances=1,
    max_instances=3
)
```

### [](#running-predictions-on-deployments)Running predictions on deployments

Once you have a deployment, you can run predictions using the deployment endpoint:

```python
# Run a prediction on your deployment
output = replicate.deployments.predictions.create(
    deployment_owner="your-username",
    deployment_name="my-flux-deployment",
    input={"prompt": "A beautiful sunset over mountains"}
)
```

[](#finding-community-models)Finding community models
-----------------------------------------------------

You can discover community models in several ways:

*   Explore page: Browse popular and featured models
*   Search: Search for specific models or tasks
*   Collections: Browse curated collections of models
*   Model pages: Follow links from other models or documentation

[](#best-practices)Best practices
---------------------------------

When using community models:

1.  Check the model description: Read the model’s description and examples to understand what it does
2.  Review the version history: Look at recent [versions](/docs/topics/models/versions) to see if there have been breaking changes
3.  Test with small inputs: Start with simple inputs to verify the model works as expected
4.  Consider deployments: For production use, consider creating a deployment for better reliability
5.  Check the creator: Look at the model creator’s profile and other models they’ve published

[](#contributing-to-the-community)Contributing to the community
---------------------------------------------------------------

If you’ve created a useful model, consider publishing it to share with the community:

1.  [Create a model](/docs/topics/models/create-a-model) on Replicate
2.  [Push your model](/docs/guides/push-a-model) using Cog
3.  [Add good examples and documentation](/docs/guides/build/model-best-practices)
4.  [Make it public](/docs/topics/models/private-models) so others can discover and use it

For more information about creating and publishing models, see the [guide to publishing your first model](/docs/topics/models/publish-a-model).
