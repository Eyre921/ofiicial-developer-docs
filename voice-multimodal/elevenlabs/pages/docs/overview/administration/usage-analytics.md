---
title: "Usage analytics"
source: https://elevenlabs.io/docs/overview/administration/usage-analytics.md
path: docs/overview/administration/usage-analytics
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Usage analytics

The Developers page provides comprehensive tools to monitor and analyze your platform activity.

To access these tools, navigate to the **Developers** page (found at the bottom of the sidebar in both ElevenAgents and ElevenCreative).

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3e8ea126ff2f8d646b145c52257c7dfdd3271d05abbfce82999b0a96727f965e/assets/images/product-guides/administration/analytics.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260724%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260724T233104Z&X-Amz-Expires=604800&X-Amz-Signature=bced5e4a60288a29a8cfb10ea120f696d2128011b9f2462212f6d4d5840eabb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Usage analytics interface" />

The Developers page includes several tabs:

* **Usage**: View and filter usage data for your account or workspace
* **Analytics**: Collect, view, and filter workspace activity including API requests, usage metrics, and webhooks
* **Request Log**: View and filter specific API requests for debugging and monitoring

If you're part of a multi-seat workspace, you'll see a toggle to switch between data for your account and your workspace.

## Usage tab

The Usage tab allows you to choose from a range of metrics for analysis, including credits, and filter your usage data in a number of different ways.

You can break your usage down by voice, product, or API key. If you're viewing workspace usage, you have additional options allowing you to break usage down by individual user or workspace group.

You can view the data by day, week, month or cumulatively. If you want to be more specific, you can use filters to show only your usage for specific voices, products or API keys.

This feature is quite powerful, allowing you to gain great insights into your usage or understand your customers' usage if you've implemented us in your product.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/b95d7c8edd7ad5e94cb97b443850e54ef84e9d3bc8e844d65e04d1b3a06f050b/assets/images/product-guides/administration/analytics-credits-voice.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260724%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260724T233104Z&X-Amz-Expires=604800&X-Amz-Signature=f178bf50a93eae82c0f69b760572ad47ee8c9adb3f98f00c8c59b456486512f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Usage metrics broken down by voice" />

In the API Requests section, you’ll find not only the total number of requests made within a specific timeframe but also the number of concurrent requests during that period.

You can view data by different time periods, for example, hour, day, month and year, and at different levels of granularity.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/03c5a1eba19089ce5a094b115619d5ae8e9397b4f4bfebcc17f5c7d62f153e24/assets/images/product-guides/administration/analytics-workspace-api.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260724%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260724T233104Z&X-Amz-Expires=604800&X-Amz-Signature=5574a9149302127b68a23b29317286ac2619865226cf1ee1651b4b368a43f4d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="API requests for specified time period" />

## Analytics tab

The Analytics tab provides detailed insights into workspace API requests and webhooks. You can filter and analyze data by different time periods (hour, day, month, year) and at different levels of granularity. You can also monitor success rate and average latency for your API requests.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/93993cf042c491a549cffc330357f3aaf272802f037e867e69e32ad27d5505f1/assets/images/product-guides/administration/analytics-requests.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260724%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260724T233104Z&X-Amz-Expires=604800&X-Amz-Signature=3a05697c80f8a1f33e2a61838f28d11da9945f56d2f34d6e94133a42c76742da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Workspace API calls broken down by path" />

## Request Log

The Request Log tab allows you to view and filter specific API requests for debugging and monitoring purposes.

## Export data

You also have the option to export your data as a CSV file. To do this, just click the "Export as CSV" button, and the data from your current view will be exported and downloaded.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/6d41a16a9e09de52a0c9406fe8b02d874e773da2b49f1f0f8c635f9ecda1bc6f/assets/images/product-guides/administration/analytics-export.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260724%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260724T233104Z&X-Amz-Expires=604800&X-Amz-Signature=2db6f1baddd505c60d19af8c9621c778ec9284a0a2a87f7497dc782d4e5448b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Export your usage data as CSV" />
