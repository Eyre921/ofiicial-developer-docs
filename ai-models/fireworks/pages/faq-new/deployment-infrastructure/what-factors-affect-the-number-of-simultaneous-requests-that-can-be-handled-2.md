---
title: "What factors affect the number of simultaneous requests that can be handled?"
source: https://docs.fireworks.ai/faq-new/deployment-infrastructure/what-factors-affect-the-number-of-simultaneous-requests-that-can-be-handled
path: faq-new/deployment-infrastructure/what-factors-affect-the-number-of-simultaneous-requests-that-can-be-handled
---

The request handling capacity is influenced by multiple factors:

* **Model size and type**
* **Number of GPUs** allocated to the deployment
* **GPU type** (e.g., A100 vs. H100)
* **Prompt size** and **generation token length**
* **Deployment type** (serverless vs. on-demand)
