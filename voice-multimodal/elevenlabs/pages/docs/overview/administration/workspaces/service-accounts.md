---
title: "Service Accounts"
source: https://elevenlabs.io/docs/overview/administration/workspaces/service-accounts.md
path: docs/overview/administration/workspaces/service-accounts
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Service Accounts

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/85b1646b900085c39df273c7337c7428e92325cb621da63c2f6c6d76d2119efd/assets/images/product-guides/workspaces/workspace-service-accounts.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260825%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260825T233151Z&X-Amz-Expires=604800&X-Amz-Signature=d65b6704a936387b9d6f8baead1b64f08c9f02535bfde55d9a06ab6577192f07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Service Accounts" />

## Overview

Service Accounts are currently only available for multi-seat customers, and only Workspace admins
can use this feature. To upgrade, [get in touch with our sales
team](https://elevenlabs.io/contact-sales).

Service Accounts and their respective API keys allow access to workspace resources without relying on an individual's access to ElevenLabs.

## Service Accounts

A service account acts as a workspace member. When originally created, they do not have access to any resources.

The service account can be granted access to resources by either adding the service account to a group or directly sharing resources with the service account.
It is recommended to add them to a group so that future users can be added to the same group and have the same permissions.

## API keys

API keys are created within a service account and authenticate your requests to the ElevenLabs API. For creating, rotating, scoping, and securing them, see [API Keys](/docs/overview/administration/workspaces/api-keys).
