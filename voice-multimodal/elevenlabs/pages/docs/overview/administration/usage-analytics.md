---
title: "Usage analytics"
source: https://elevenlabs.io/docs/overview/administration/usage-analytics.md
path: docs/overview/administration/usage-analytics
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Usage analytics

The Developers page provides tools to monitor and analyze your platform activity.

To access these tools, navigate to **Developers** at the bottom of the sidebar in both ElevenAgents and ElevenCreative.

If you are part of a multi-seat workspace, you can switch between data for your account and your workspace.

## Analytics

The **Analytics** tab includes **API Requests**, **Usage**, and **Webhooks**. You can filter and analyze data by time period (for example, hour, day, month, or year) and at different levels of granularity.

### API Requests

The API Requests view shows request volume and performance for your account or workspace. Metrics include:

* Total requests, which you can break down and filter
* Success rate
* Average latency
* Top called path

![API Requests metrics](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/85616095f05819be54ba35639423d2175c51ca34aec2d34273a3e8b1a6bd8401/assets/images/product-guides/administration/analytics-requests.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T113146Z&X-Amz-Expires=604800&X-Amz-Signature=afdb5d310ca1ea89e2814d93f9b0b38de575b4db139bb67190495f0fd5e1f3c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Usage

The Usage view shows credit consumption and related performance metrics. Metrics include:

* Credit usage, which you can break down and filter (for example, by voice, product, or API key)
* Average time to first byte
* Average time to completed transcript
* Concurrent requests

When viewing workspace usage, you can also break usage down by individual user or workspace group.

![Usage metrics](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/7f901489e15c1211a1e7e99d75e6033848d5e3f86df55a320046af43b20614f7/assets/images/product-guides/administration/analytics-usage.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T113146Z&X-Amz-Expires=604800&X-Amz-Signature=fb3f2e5e33a3bef0ff56edde960d8f514bf3aacaa691b996aad0e0aa6cacbf1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Webhooks

The Webhooks view shows webhook delivery activity for your account or workspace. Metrics include:

* Total webhook calls
* Recent webhook calls

## Request Log

The **Request Log** tab lists all API requests for your account or workspace. Use search and filters to find specific requests for debugging and monitoring.

![Request Log](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3ff35ca4c4c47dd86731b7bdc2fb71cff39663cf8cef61d355209b9648ffe003/assets/images/product-guides/administration/analytics-request-log.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T113146Z&X-Amz-Expires=604800&X-Amz-Signature=f481a714002b4884f593fcddb4cd9c35bb5d613c9c15b549a56fb577e8d18cf7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Export data

You can export the data from your current view as a CSV file. Click **Export** to download it.

![Export usage data as CSV](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/52d44c4736ed92ccb037fe8ffb7a3292f20a695350d689785e137fb75fac62a4/assets/images/product-guides/administration/analytics-export.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T113146Z&X-Amz-Expires=604800&X-Amz-Signature=3a9aa37d3fb131e552fe1e0fbed2928776062e0c7e57779457f2c66d61bd01e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
