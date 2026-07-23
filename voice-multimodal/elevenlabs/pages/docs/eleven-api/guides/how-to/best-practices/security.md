---
title: "Secure by design"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/best-practices/security.md
path: docs/eleven-api/guides/how-to/best-practices/security
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Secure by design

Whether you're building voicemail apps, interactive characters, or audio-driven games, the ElevenLabs API gives you direct access to powerful voice capabilities.
But with that access comes the responsibility to secure your users’ data and manage voice resources carefully.

This guide outlines three critical security practices for developers:

* Isolating environments using **service accounts**
* Limiting the lifetime of **user API keys**
* Implementing **resource-level permissions**

## Use service accounts to isolate environments

Service accounts provide scoped, API-only access to the ElevenLabs platform. Unlike user accounts, they’re not tied to individuals—they’re designed for backend systems and automation.

If a service account creates a resource, only admins can see it by default but it can be shared with other users. Similarly, you can share any resource with a service account just as you would with a user.
Each service account is created at the workspace level and managed by workspace admins. They can create and access resources through the API.

We recommend provisioning a dedicated service account for each environment:

* `production-service-account`
* `testing-service-account`
* `uat-service-account` (if applicable)

This ensures clean separation between environments, reduces accidental data leaks across environments, and simplifies monitoring.

### Why this matters

**Separation of concerns**\
Avoid mixing test and production data. Environment isolation supports auditability and compliance.

**Principle of least privilege**\
Each service account should only have access to the minimum necessary resources. API keys can be scoped further at the time of creation.

**Better observability**\
Track API usage and performance by environment. Separate service accounts make it easier to debug issues and monitor activity.

## Limit the lifetime of user API keys

[User API keys](/docs/overview/administration/workspaces/api-keys) are tied to an individual and inherit that a subset of that person's access. That makes them convenient for personal development and scripts, but a poor choice for credentials that live indefinitely, particularly if they make their way into shared scripts, notebooks, or CI pipelines.

User API keys can be set to expire. When you create a key set an expiry between 15 minutes and 30 days, after which the key stops authenticating. The expiry can be edited or extended after creation if needed.

## Apply resource-level permissions in your backend

If your app allows users to record messages using cloned voices, it is essential to ensure users only access voices they own or have been granted permission to use.

While the ElevenLabs platform supports in-app sharing, you should enforce **resource-level access control** within your own systems when using the API.

A recommended model:

```
user_id | voice_id | permission_level
```

Possible permission\_level values:

* `viewer`: can use the voice for speech generation
* `editor`: can update voice settings
* `admin`: can manage sharing and permissions

This structure lets you control who can access and modify voices and prevents unauthorized use of sensitive resources.
These permissions are suggestions based on controls natively offered if you are directly using the ElevenLabs platform.

### Build securely. Scale confidently.

Security should be foundational, not an afterthought.
By leveraging service accounts and implementing permission controls, you’ll reduce risk and build trust—while giving your users the full potential of AI voice.
