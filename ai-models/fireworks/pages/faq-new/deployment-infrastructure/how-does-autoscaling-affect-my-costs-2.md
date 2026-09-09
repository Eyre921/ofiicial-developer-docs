---
title: "How does autoscaling affect my costs?"
source: https://docs.fireworks.ai/faq-new/deployment-infrastructure/how-does-autoscaling-affect-my-costs
path: faq-new/deployment-infrastructure/how-does-autoscaling-affect-my-costs
---

* **Scaling from 0**: No minimum cost when scaled to zero
* **Scaling up**: Each new replica adds to your total cost proportionally. For example:
  * Scaling from 1 to 2 replicas doubles your GPU costs
  * If each replica uses multiple GPUs, costs scale accordingly (e.g., scaling from 1 to 2 replicas with 2 GPUs each means paying for 4 GPUs total)

For current pricing details, please visit our [pricing page](https://fireworks.ai/pricing).
