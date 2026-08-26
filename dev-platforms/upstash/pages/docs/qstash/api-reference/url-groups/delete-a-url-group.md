---
title: "Delete a URL Group"
source: https://upstash.com/docs/qstash/api-reference/url-groups/delete-a-url-group
path: docs/qstash/api-reference/url-groups/delete-a-url-group
---

> Delete a topic and all its endpoints

`DELETE /v2/topics/{urlGroupName}`

The URL Group and all its endpoints are removed.
In flight messages in the URL Group are not removed but you will not be able to send messages to the URL Group anymore.

<Warning>
  If you have a schedule that is publishing to this URL Group, you need to delete the schedule first before deleting the URL Group.
</Warning>
