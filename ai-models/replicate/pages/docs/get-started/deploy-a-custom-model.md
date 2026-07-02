---
title: "Deploy a custom model"
source: https://replicate.com/docs/get-started/deploy-a-custom-model.md
path: docs/get-started/deploy-a-custom-model
---

Replicate lets you build and scale AI products with your own custom models. You write the code, we handle the infrastructure orchestration and scaling.

With custom models and [deployments](/docs/topics/deployments), you can:

*   Run arbitrary code and weights on high-end GPUs (A100s, H100s, B200s, and more) via API
*   Dedicated deployments with no noisy neighbors
*   Scale from zero to thousands of GPUs automatically based on demand
*   Deploy updates without downtime using rolling deployments
*   Monitor performance, costs, and usage in real-time
*   Pay only for what you use

This guide shows you how to deploy your model on production-grade GPU infrastructure that scales dynamically and can handle millions of requests.

Note

This guide will show you how to build a custom model from scratch using Cog. If you’re looking to create a fine-tuned image generation model using your own training data, check out the [guide to fine-tuning image models](/docs/guides/fine-tune-an-image-model).

[](#what-is-a-custom-model)What is a custom model?
--------------------------------------------------

In the world of machine learning, the word “model” can mean many different things depending on context. It can be the source code, trained weights, architecture, or some combination thereof. At Replicate, when we say “model” we’re referring to a trained, packaged, and published software program that accepts inputs and returns outputs.

Models on Replicate are built with [Cog](https://cog.run/), an open-source tool that packages arbitrary code into a standard, production-ready container. Cog handles generating API servers and cloud deployment automatically. You define your model environment and prediction logic, and Replicate handles the server, scaling, and compute management.

[](#step-1-create-a-model)Step 1: Create a model
------------------------------------------------

Click “Create model” in the account menu or go to [replicate.com/create](https://replicate.com/create) to create your new model.

### [](#choose-a-name)Choose a name

Pick a short and memorable name, like `hotdog-detector`. You can use lower case characters and dashes.

### [](#choose-an-owner)Choose an owner

If you’re working with a team, you should **create your model under an organization** so you and your team can share access and billing. To create an organization, click “Join or create organization” from the account menu or go to [replicate.com/organizations/create](https://replicate.com/organizations/create). Learn more about [organizations](/docs/topics/organizations).

If you’re creating a model for your own individual use, you don’t need an organization. Create it under your user account.

### [](#choose-model-visibility)Choose model visibility

Public models can be discovered and used by anyone. Private models can only be seen by the user or organization that owns them.

Set your model to be private to start, so it’s accessible only to you and your organization. You can make it public later if you want to share it with others.

### [](#choose-hardware)Choose hardware

Choose the type of hardware your model runs on. This affects performance and cost. [The billing docs](/docs/topics/billing) show specifications and pricing for available hardware.

For GPU-accelerated models, start with a **Nvidia T4 GPU** for development. You can upgrade to more powerful GPUs like A100s or H100s later using deployments without changing your code.

Once you’ve created your new model, you should see a page that looks something like this:

![new-model-page](https://github.com/replicate/cog/assets/2289/e36e6405-356f-4158-afdd-a61d22e248e6)

> If you prefer to work from the command line, you can use the [Replicate CLI](https://github.com/replicate/cli) to create models, or [create models programmatically using the API](https://replicate.com/changelog/2023-11-06-api-for-creating-models).

[](#step-2-build-your-model)Step 2: Build your model
----------------------------------------------------

Now that you’ve created your model on Replicate, it’s time to actually write the code for it, build it, and push it to Replicate.

You’ll use [Cog](https://cog.run) to build and push your model. Cog is an open-source tool that packages arbitrary code in production-ready containers with automatic API generation.

Follow this guide to learn how to install Cog, write the code for your model, and push it to Replicate:

⚙️ [Guide: Push your own model with Cog](/docs/guides/push-a-model)

Once you’ve pushed your custom model, return to this guide to learn how to create a deployment and scale it.

[](#step-3-create-a-deployment)Step 3: Create a deployment
----------------------------------------------------------

When you push a model to Replicate, we automatically generate an API server and deploy it on our GPU cluster. For production use, you should create a [deployment](/docs/topics/deployments) to get full control over scaling, hardware, and performance.

Deployments give you production-grade control over your model’s infrastructure and provide a private, dedicated API endpoint.

To create a deployment, go to your model page and click the **Deploy** button.

You’ll see a form where you can configure:

*   Deployment name: Choose a descriptive name for your deployment
*   Hardware type: Select from available GPU architectures
*   Instance scaling: Set minimum and maximum instance counts
*   Cost estimation: Live preview of your deployment costs

The form shows real-time cost estimates as you adjust your configuration, helping you balance performance and budget.

Once you’re satisfied with your choices, click **Create a deployment**.

![deployment-form](https://github.com/replicate/cog/assets/2289/8fd72cc5-0a8b-4e7b-b7f3-3b23aabff96f)

> **Keep your model warm.** If you’re giving a demo or putting your model in the hands of users, you’ll want it to respond quickly, without a [cold boot](/docs/topics/models/run-a-model#warm-models). Set the minimum number of instances to 1 to make sure that at least one instance is always running. You can reduce this to 0 later if you don’t need the model to be instantaneously responsive to new requests.

After creating your deployment, you’ll see updated example code for running your model through the deployment endpoint. This code differs from the earlier API calls—it references your deployment (`you/your-deployment`) rather than the model directly (`you/your-model`):

![deployment-snippet](https://github.com/replicate/cog/assets/2289/d2adde0e-4281-4a0d-914c-73fef5a42ec3)

[](#step-4-monitor-your-deployment)Step 4: Monitor your deployment
------------------------------------------------------------------

Once your deployment receives traffic, go to your deployment page to monitor its performance. The dashboard shows:

*   Request volume and latency: Track how many requests you’re processing and response times
*   Instance utilization: See how many instances are active, idle, or starting up
*   Error rates: Monitor failed requests and troubleshoot issues
*   Cost analysis: View detailed spending broken down by compute time and instance hours

![deployment-metrics](https://github.com/replicate/cog/assets/2289/214e1a90-62f5-4577-a556-3736c340a4c1)

[](#step-5-iterate-on-your-deployment)Step 5: Iterate on your deployment
------------------------------------------------------------------------

Machine learning models improve over time as you retrain with new data, fix bugs, or update dependencies. With deployments, you can update your model without disrupting service.

When you make changes to your model, run `cog push` to publish updates. Your deployment can then use rolling updates to deploy the new model without downtime. [You can integrate this into your existing development workflow using GitHub Actions.](https://github.com/replicate/setup-cog)

Deployments handle the complexity of managing multiple model iterations, allowing you to test changes, rollback if needed, and ensure consistent performance for your users.

[](#next-steps)Next steps
-------------------------

You’ve successfully created a custom model on Replicate, built it with Cog, deployed it with production-grade infrastructure control, and set up monitoring to track its performance. Your model now has a private API endpoint that can scale automatically based on demand.

Now it’s time to integrate your deployed model into your app or product:

*   Learn how to [continuously deploy your model using GitHub Actions](https://github.com/replicate/setup-cog).
*   Check out the [client libraries](/docs/reference/client-libraries) you can use to run your model.
*   Check out the [deployments guide](/docs/topics/deployments) to learn more about model performance and scaling.
