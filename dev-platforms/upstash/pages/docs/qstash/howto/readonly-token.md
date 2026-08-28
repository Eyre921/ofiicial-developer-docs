---
title: "Read-only Token"
source: https://upstash.com/docs/qstash/howto/readonly-token
path: docs/qstash/howto/readonly-token
---

You can use a read-only version of your token to safely share it with your team or AI agents.
This token has access to your logs, messages, schedules, and other resources, but it cannot be used to publish messages, create new resources such as schedules or URL Groups, or modify existing resources.

You can get your read-only token from the dashboard by clicking "Read-only token" in the Quickstart section:

  <img />

<Info>
Note that a read-only token can still access sensitive data such as logs and messages.

If you want to share your token without exposing sensitive data, you can use the ["Redact Fields"](/docs/qstash/howto/redact-fields) feature to hide sensitive data from the logs and resources.
</Info>
