---
title: "Choosing a deployment option"
source: https://docs.together.ai/learn/choosing-a-deployment-option
path: learn/choosing-a-deployment-option
---

Deploy your model with serverless, dedicated endpoints, or dedicated containers.

**TL;DR:** There are three ways to run a model in production on Together AI.

* **[Serverless](/docs/serverless/models):** Pay per token to use shared infrastructure, with instant startups and no setup.
* **[Dedicated endpoints](/docs/dedicated-endpoints/overview):** Reserve GPUs for yourself, get predictable performance, pay by the GPU-hour whether you're using the GPU or not.
* **[Dedicated containers](/docs/dedicated-container-inference):** Bring your own inference logic on top of reserved GPUs.

The right choice for a workload depends on your volume, your latency budget, and how much control you need over the inference stack.

## Serverless

Serverless is the default starting point for most workloads. Together AI runs a big shared pool of GPUs hosting popular models, and when you make a serverless request, it gets routed to whichever GPU has capacity. You pay per token of input and output, usually quoted in dollars per million tokens.

Pros:

* **No idle cost:** No requests, no charges. A weekend with zero traffic costs you nothing.
* **Instant start:** No cold-starts, no wait time while the model loads. Send a request and get tokens back immediately.
* **No capacity planning:** Togther automatically handles batching, autoscaling, and load balancing. You just call the API.

Cons:

* **Latency variance:** When the shared pool is busy, your TTFT goes up. At peak times you might see two to three times the average TTFT. This rarely matters for batch jobs but it matters a lot for interactive UIs.
* **Limited model selection:** You can only use models the platform currently has provisioned on its shared pool. Custom fine-tunes, prior model generations, or niche model offerings typically do not have enough demand for providers to warrant offering them on the platform.
* **Less control over throughput:** If you suddenly need to send ten times your usual traffic, the platform might apply [rate limits](/docs/serverless/rate-limits) to keep the shared pool stable and fairly share the capacity with all other users.

Serverless is a great starting point for prototypes, demos, internal tools, and any workloads where you can tolerate high performance variability. See [serverless models](/docs/serverless/models) for the list of available models and per-token pricing.

## Dedicated endpoints

A dedicated endpoint is a copy of a model running on GPUs reserved for you. You pay by the GPU-hour regardless of how many tokens you actually use. At high volume, dedicated hardware can be cheaper than serverless. At low volume, you're paying a flat cost for a GPU that's mostly idle.

Pros:

* **Predictable latency:** You'll never be impacted by other users' traffic. Your TTFT is whatever the model plus your prompt size produces, every single time.
* **Higher sustained throughput:** If you are pushing many tokens per second, dedicated capacity often delivers better total throughput than waiting in a shared queue.
* **Custom weights:** If you have fine-tuned a model, this is usually where you'd host it.
* **Pinned model version:** The platform will never swap out your model or deprecate older models.
* **Optimizations you can opt into:** Things like speculative decoding (a small draft model that proposes ahead while the big model verifies), quantization, prompt caching, and aggressive batching are easier to enable when the endpoint is yours.

Cons:

* **Flat cost when idle:** If your traffic drops to zero, you're still paying for the GPU unless your endpoint supports autoscaling to zero.
* **Capacity planning:** You pick the hardware, so if you pick the wrong size/amount, you'll either waste money on idle GPUs, or experience slowdowns when traffic gets too high.
* **Cold start times:** Bringing an endpoint online from zero takes minutes, not milliseconds. Plan your deploy schedules accordingly.

See [Dedicated endpoints](/docs/dedicated-endpoints/overview) for deployment instructions on Together AI, and [Endpoint settings](/docs/dedicated-endpoints/settings) for details on hardware, autoscaling, and prompt caching.

## Dedicated containers

Dedicated containers go one level deeper. You package the inference logic yourself: your own Docker image, your own inference code and APIs, your own pre- and post-processing. The platform runs your container on dedicated GPUs.

Pros:

* **Full control:** You own the inference code, the Docker image, the inference logic, and the API.
* **Customization:** You can add your own pre- and post-processing, custom batching, custom streaming, mixed workloads, or a model that takes inputs the standard API cannot represent.

Cons:

* **Operational complexity:** You're responsible for the entire inference stack, from the code to the hardware. You'll need to manage your own scaling, monitoring, and logging.
* **Cost:** You're responsible for the cost of the hardware, the container, and the inference code. It's more expensive than serverless, but it's also more flexible and gives you the most control over the inference stack.

## The cost crossover

When it comes to cost, serverless generally beats paying for dedicated hardware until you reach a point when you're keeping your dedicated GPUs busy most of the time. The exact crossover depends on your model size, your input-output token mix, cache hit rate, and the GPU you are paying for, but the shape of the curve is always the same:

<CostCrossoverDiagram />

For a back-of-the-envelope calculation, suppose a dedicated H100 at around \$3 per hour costs \$72 per day. With serverless at \$1 per 1M tokens, the crossover sits at roughly 72M tokens per day, or \~3M tokens per hour sustained. Below that volume, serverless is more cost-effective. Above it, dedicated hardware becomes cheaper. On newer hardware (H200, B200) the per-hour rate goes up but so does the per-GPU throughput, so the token-volume crossover stays roughly similar. Your numbers will differ based on the actual rates and the GPU type.

## Rent, lease, or build

It helps to think of this decision the same way you'd think about office space:

You can **co-work**, paying by the desk-hour. You walk in when you need a desk, walk out when you don't, and share the kitchen with strangers. Co-working is cheap when you barely use it, but it's first-come, first-served, and on busy days you compete with everyone else for space. This is the **serverless** model.

You can **rent an office**, paying a flat monthly rent. The space is yours, nobody else uses your desk, and you don't have to share the space with anyone else even on busy days. Renting is more expensive when your utilization is low, but it gives you predictability and reliability that co-working cannot. This is the **dedicated endpoint** model.

You can **build out the floor yourself**: the space is yours, the layout is yours, the wiring is yours. You get the most control of any option and you take on the most operational ownership. This is the **dedicated container** model.

You pick between these based on how much you use the space, how predictable that usage is, and how custom your workflow needs to be. All three are ways to draw on GPU capacity, and you can employ a mixture. For example, you might run a dedicated endpoint that scales up for peak-hour traffic, with an overflow spilling onto serverless when the endpoint runs out of capacity.

## Defaults that work

Some reasonable defaults for common use cases:

* **Prototype, demo, or internal tool:** Use serverless, almost always. The latency variance will not matter for tens or hundreds of calls a day, and you're spared all the provisioning work.
* **Customer-facing chat with a strict TTFT requirement:** Try serverless first and measure the tail latency. If P95 is fine, stick with that. If it's not, switch the latency-sensitive paths to a dedicated endpoint.
* **High-volume batch jobs:** Use dedicated. Above a certain throughput, you're paying for one GPU's worth of tokens anyway, and paying flat is cheaper than paying per token.
* **Fine-tuned model:** Dedicated endpoint, or dedicated container if your platform does not support serverless for custom models.
* **Custom model with a non-standard pipeline:** Dedicated container.

<Info>
  You don't have to pick one option and stick with it across your entire stack. Many teams run serverless for everything they can, and a small dedicated endpoint for the parts that need it. A mixed approach often works out to be cheaper than going all-in on either side.
</Info>

## Next steps

<CardGroup>
  <Card title="Quantization" icon="zoom-in" href="/learn/quantization">
    The other major lever on inference cost.
  </Card>

  <Card title="Inference metrics: TTFT & TPS" icon="dashboard" href="/learn/ttft-and-tps">
    The latency numbers you'll be comparing across options.
  </Card>

  <Card title="Fine-tune vs. prompt" icon="git-branch" href="/learn/finetune-vs-prompt">
    What determines whether you'll need dedicated hardware at all.
  </Card>
</CardGroup>
