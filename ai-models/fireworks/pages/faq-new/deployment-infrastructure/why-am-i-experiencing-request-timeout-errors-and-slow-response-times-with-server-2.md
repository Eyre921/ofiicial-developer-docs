---
title: "Why am I experiencing request timeout errors and slow response times with serverless LLM models?"
source: https://docs.fireworks.ai/faq-new/deployment-infrastructure/why-am-i-experiencing-request-timeout-errors-and-slow-response-times-with-server
path: faq-new/deployment-infrastructure/why-am-i-experiencing-request-timeout-errors-and-slow-response-times-with-server
---

Timeout errors and increased response times can occur due to **server load during high-traffic periods**.

With serverless, users are essentially **sharing a pool of GPUs** with models pre-provisioned.
The goal of serverless is to allow users and teams to **seamlessly power their generative applications** with the **latest generative models** in **less than 5 lines of code**.
Deployment barriers should be **minimal** and **pricing is based on usage**.

However there are trade-offs with this approach, namely that in order to ensure users have **consistent access** to the most in-demand models, users are also subject to **minor latency and performance variability** during **high-volume periods**.
With **on-demand deployments**, users are reserving GPUs (which are **billed by rented time** instead of usage volume) and don't have to worry about traffic spikes.

Which is why our two recommended ways to address timeout and response time issues is:

### Current solution (recommended for production)

* **Use on-demand deployments** for more stable performance
* **Guaranteed response times**
* **Dedicated resources** to ensure availability

We are always investing in ways to improve speed and performance.

### Upcoming improvements

* Enhanced SLAs for uptime
* More consistent generation speeds during peak load times

If you experience persistent issues, please include the following details in your support request:

1. Exact **model name**
2. **Timestamp** of errors (in UTC)
3. **Frequency** of timeouts
4. **Average wait times**

### Performance optimization tips

* Consider **batch processing** for handling bulk requests
* Implement **retry logic with exponential backoff**
* Monitor **usage patterns** to identify peak traffic times
* Set **appropriate timeout settings** based on model complexity
