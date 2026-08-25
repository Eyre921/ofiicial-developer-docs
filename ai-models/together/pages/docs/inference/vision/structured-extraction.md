---
title: "Structured extraction with vision"
source: https://docs.together.ai/docs/inference/vision/structured-extraction
path: docs/inference/vision/structured-extraction
---

Combine image input with a JSON schema to extract typed data from screenshots, documents, and photos.

You can combine vision input with structured outputs to extract typed data from an image. Pass an `image_url` content block and a `response_format` with a JSON schema; the model returns JSON that conforms to the schema.

For example, you could extract a project name and a column count from a screenshot of a Trello board:

<CodeGroup>
  ```python Python theme={null}
  import json
  from together import Together
  from pydantic import BaseModel, Field

  client = Together()


  class ImageDescription(BaseModel):
      project_name: str = Field(
          description="The name of the project shown in the image"
      )
      col_num: int = Field(description="The number of columns in the board")


  image_url = "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/d96a3145-472d-423a-8b79-bca3ad7978dd/trello-board.png"

  extract = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Extract a JSON object from the image.",
                  },
                  {"type": "image_url", "image_url": {"url": image_url}},
              ],
          }
      ],
      model="moonshotai/Kimi-K3",
      reasoning={"enabled": False},
      response_format={
          "type": "json_schema",
          "json_schema": {
              "name": "image_description",
              "schema": ImageDescription.model_json_schema(),
          },
      },
  )

  print(json.dumps(json.loads(extract.choices[0].message.content), indent=2))
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  import { z } from "zod";

  const together = new Together();

  const schema = z.object({
    projectName: z.string().describe("The name of the project shown in the image"),
    columnCount: z.number().describe("The number of columns in the board"),
  });

  const imageUrl =
    "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/d96a3145-472d-423a-8b79-bca3ad7978dd/trello-board.png";

  const extract = await together.chat.completions.create({
    messages: [
      {
        role: "user",
        content: [
          { type: "text", text: "Extract a JSON object from the image." },
          { type: "image_url", image_url: { url: imageUrl } },
        ],
      },
    ],
    model: "moonshotai/Kimi-K3",
    reasoning: { enabled: false },
    response_format: {
      type: "json_schema",
      json_schema: {
        name: "image_description",
        schema: z.toJSONSchema(schema),
      },
    },
  });

  console.log(JSON.parse(extract.choices[0].message.content));
  ```
</CodeGroup>

Example output:

```json JSON theme={null}
{
  "projectName": "Project A",
  "columnCount": 4
}
```

For the full structured-outputs reference, see [Structured outputs](/docs/inference/chat/structured-outputs).
