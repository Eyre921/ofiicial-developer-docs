---
title: "Resume"
source: https://upstash.com/docs/vector/api/endpoints/resumable-query/resume
path: docs/vector/api/endpoints/resumable-query/resume
---

> Resumes a previously started query to fetch additional results.

`POST https://{endpoint}/resumable-query-next`

## Request

<ParamField body="uuid" type="string" required>
  The unique identifier returned from the start resumable query request.
</ParamField>

<ParamField body="additionalK" type="number" required>
  The number of additional results to fetch.
</ParamField>

## Response

<ResponseField name="Scores" type="Object[]">
  <Expandable defaultOpen="true">
    <ResponseField name="id" type="string" required>
      The id of the vector.
    </ResponseField>
    <ResponseField name="score" type="number" required>
      The similarity score of the vector, calculated based on the distance
      metric of your index.
    </ResponseField>
    <ResponseField name="vector" type="number[]">
      The dense vector value for dense and hybrid indexes.
    </ResponseField>
    <ResponseField name="sparseVector" type="Object[]">
      The sparse vector value for sparse and hybrid indexes.
      <Expandable defaultOpen="true">
        <ResponseField name="indices" type="number[]">
          Indices of the non-zero valued dimensions.
        </ResponseField>
        <ResponseField name="values" type="number[]">
          Values of the non-zero valued dimensions.
        </ResponseField>
      </Expandable>
    </ResponseField>
    <ResponseField name="metadata" type="Object">
      The metadata of the vector, if any.
    </ResponseField>
    <ResponseField name="data" type="string">
      The unstructured data of the vector, if any.
    </ResponseField>
  </Expandable>
</ResponseField>
