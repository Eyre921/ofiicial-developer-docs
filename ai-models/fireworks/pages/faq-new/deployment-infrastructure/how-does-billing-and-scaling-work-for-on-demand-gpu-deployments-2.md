---
title: "How does billing and scaling work for on-demand GPU deployments?"
source: https://docs.fireworks.ai/faq-new/deployment-infrastructure/how-does-billing-and-scaling-work-for-on-demand-gpu-deployments
path: faq-new/deployment-infrastructure/how-does-billing-and-scaling-work-for-on-demand-gpu-deployments
---

On-demand GPU deployments have unique billing and scaling characteristics compared to serverless deployments:

**Billing**:

* Charges start when the server begins accepting requests
* **Billed by GPU-second** for each active instance
* Costs accumulate even if there are no active API calls

**Scaling options**:

* Supports **autoscaling** from 0 to multiple GPUs
* Each additional GPU **adds to the billing rate**
* Can handle unlimited requests within the GPU’s capacity

**Management requirements**:

* Not fully serverless; requires some manual management
* **Manually delete deployments** when no longer needed
* Or configure autoscaling to **scale down to 0** during inactive periods

**Cost control tips**:

* Regularly **monitor active deployments**
* **Delete unused deployments** to avoid unnecessary costs
* Consider **serverless options** for intermittent usage
* Use **autoscaling to 0** to optimize costs during low-demand times
