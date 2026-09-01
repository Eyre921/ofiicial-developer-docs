---
title: "Routers"
source: https://docs.fireworks.ai/deployments/routers
path: deployments/routers
---

Distribute traffic across multiple deployments for A/B testing, traffic migration, and load distribution.

A **Router** is a resource that controls how inference traffic is routed to one or more deployments. Instead of sending all requests to a single deployment, a router lets you split traffic across multiple deployments — useful for A/B testing model variants, gradually migrating traffic to a new deployment, or distributing load.

Traffic is split proportionally based on the number of replicas in each deployment. For example, if a router covers two deployments — one with 3 replicas and another with 2 — the first receives 60% of traffic and the second receives 40%.

<Warning>
  Routers only work with multi-region deployments.
</Warning>

## When to use a router

### Stable alias for deployment replacement

If you plan to replace a deployment later (e.g., changing to a new model later), give your application the **router name** instead of the deployment name. You can then swap the underlying deployment without your application changing anything.

```
Your app calls: accounts/<ACCOUNT_ID>/routers/my-router
  └── Initially routes to: accounts/<ACCOUNT_ID>/deployments/v1
  └── Later updated to:    accounts/<ACCOUNT_ID>/deployments/v2
```

### A/B testing between deployments

Place multiple deployments under a single router. Traffic is automatically split by replica count, so you can control the ratio by adjusting replicas on each deployment.

```bash theme={null}
firectl router create \
    --router-id=ab-test \
    --deployments=model-a,model-b
```

### Gradual traffic migration

Shift traffic from an old deployment to a new one with zero downtime by scaling replicas up on the new deployment and down on the old. See the [worked example](#example-traffic-migration) below.

## How traffic routing works

Traffic is distributed based on **replica count**. Each replica across all deployments in the router receives an equal share of traffic.

| Deployment     | Replicas | Traffic share |
| -------------- | -------- | ------------- |
| `deployment-a` | 3        | 60%           |
| `deployment-b` | 2        | 40%           |
| **Total**      | **5**    | **100%**      |

To shift traffic, scale the replica counts on the underlying deployments. The router automatically adjusts the distribution.

### Sending traffic to a router

Use the router's name in the `model` field of your API request, just like you would use a deployment name:

```bash theme={null}
curl -s -X POST https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "accounts/<ACCOUNT_ID>/routers/<ROUTER_ID>",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

### Routing strategy

Traffic is routed using **weighted replica** selection: each request is randomly assigned to a deployment, weighted by its replica count. A deployment with more replicas receives proportionally more traffic.

## Managing routers

### Creating a router

A router requires at least one deployment.

```bash theme={null}
firectl router create \
    --deployments=<DEPLOYMENT_1>,<DEPLOYMENT_2>
```

Optional flags:

| Flag             | Description                                                    |
| ---------------- | -------------------------------------------------------------- |
| `--router-id`    | Set a specific router ID. If omitted, a random ID is generated |
| `--display-name` | Human-readable name for the router                             |
| `--model`        | The model to route traffic to                                  |
| `--strategy`     | Routing strategy. Default: `weighted-random`                   |
| `--public`       | Make the router accessible to other accounts                   |

### Listing routers

```bash theme={null}
firectl router list
```

### Getting router details

```bash theme={null}
firectl router get <ROUTER_ID>
```

You can also use the full resource name:

```bash theme={null}
firectl router get accounts/<ACCOUNT_ID>/routers/<ROUTER_ID>
```

### Updating a router

Update the deployments, strategy, or other properties of an existing router:

```bash theme={null}
firectl router update <ROUTER_ID> \
    --deployments=<DEPLOYMENT_1>,<DEPLOYMENT_2>,<DEPLOYMENT_3>
```

### Deleting a router

```bash theme={null}
firectl router delete <ROUTER_ID>
```

<Warning>
  Deleting a router takes effect immediately. Any traffic sent to the router's alias will fail. Make sure all clients have switched to a different route before deleting.
</Warning>

## Example: traffic migration

This example walks through migrating traffic from an existing deployment to a new one with zero downtime.

**Step 1** — Create a router for your existing deployment and point your application at the router alias:

```bash theme={null}
firectl router create \
    --router-id=my-router \
    --deployments=current-deployment
```

Your application sends traffic to `accounts/<ACCOUNT_ID>/routers/my-router`. All traffic goes to `current-deployment`.

**Step 2** — Create the new deployment and add it to the router:

```bash theme={null}
firectl deployment create accounts/<ACCOUNT_ID>/models/<MODEL_ID> \
    --deployment-id=new-deployment
```

```bash theme={null}
firectl router update my-router \
    --deployments=current-deployment,new-deployment
```

A new deployment starts with 1 replica by default, so if `current-deployment` has 4 replicas, the split is immediately 80%/20%.

**Step 3** — Shift more traffic by increasing replicas on the new deployment and decreasing the old:

```bash theme={null}
firectl deployment update new-deployment \
    --min-replica-count=4 \
    --max-replica-count=4

firectl deployment update current-deployment \
    --min-replica-count=1 \
    --max-replica-count=1
```

Traffic split is now 20% old / 80% new.

**Step 4** — Complete the migration by scaling the old deployment to zero:

```bash theme={null}
firectl deployment update current-deployment \
    --min-replica-count=0 \
    --max-replica-count=0
```

All traffic now flows to `new-deployment`. Clean up by removing the old deployment from the router:

```bash theme={null}
firectl router update my-router --deployments=new-deployment
```

<Tip>
  Monitor your new deployment's latency and error rates at each step before shifting more traffic. This lets you catch issues early and roll back by increasing replicas on the old deployment.
</Tip>
