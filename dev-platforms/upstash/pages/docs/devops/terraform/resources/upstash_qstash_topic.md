---
title: "upstash_qstash_topic"
source: https://upstash.com/docs/devops/terraform/resources/upstash_qstash_topic
path: docs/devops/terraform/resources/upstash_qstash_topic
---

<RequestExample>

```hcl example.tf
resource "upstash_qstash_topic" "exampleQStashTopic" {
  name = "exampleQStashTopicName"
}
```

</RequestExample>

## Schema

### Required

<ParamField query="name" type="string" required>
  Name of the QStash topic
</ParamField>

### Read-Only

<ResponseField name="endpoints" type="list(map(string))">
  Endpoints for the QStash topic
</ResponseField>

<ResponseField name="id" type="string">
  The ID of this resource.
</ResponseField>

<ResponseField name="topic_id" type="string">
  Unique QStash topic ID for requested topic
</ResponseField>
