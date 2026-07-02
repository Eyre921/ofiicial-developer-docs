---
title: "Quickstart: How to do OCR"
source: https://docs.together.ai/docs/quickstart-how-to-do-ocr
path: docs/quickstart-how-to-do-ocr
---

A step by step guide on how to do OCR with Together AI's vision models with structured outputs

## Understanding OCR and Its Importance

Optical Character Recognition (OCR) has become a crucial tool for many applications as it enables computers to read & understand text within images. With the advent of advanced AI vision models, OCR can now understand context, structure, and relationships within documents, making it particularly valuable for processing receipts, invoices, and other structured documents while reasoning on the content output format.

In this guide, we're going to look at how you can take documents and images and extract text out of them in markdown (unstructured) or JSON (structured) formats.

## How to do standard OCR with Together SDK

Together AI provides powerful vision models that can process images and extract text with high accuracy.

The basic approach involves sending an image to a vision model and receiving extracted text in return.\
A great example of this implementation can be found at [llamaOCR.com](https://llamaocr.com/).

Here's a basic Typescript/Python implementation for standard OCR:

<CodeGroup>
  ```typescript TypeScript theme={null}

  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const billUrl =
      "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/1627e746-7eda-46d3-8d08-8c8eec0d6c9c/nobu.jpg?x-id=PutObject";

    const response = await together.chat.completions.create({
      model: "google/gemma-4-31B-it",
      messages: [
        {
          role: "system",
          content:
            "You are an expert at extracting information from receipts. Extract all the content from the receipt.",
        },
        {
          role: "user",
          content: [
            { type: "text", text: "Extract receipt information" },
            { type: "image_url", image_url: { url: billUrl } },
          ],
        },
      ],
      reasoning: { enabled: false },
    });

    if (response?.choices?.[0]?.message?.content) {
      console.log(response.choices[0].message.content);
      return (response.choices[0].message.content);
    }

    throw new Error("Failed to extract receipt information");
  }

  main();
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()

  prompt = "You are an expert at extracting information from receipts. Extract all the content from the receipt."

  imageUrl = "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/1627e746-7eda-46d3-8d08-8c8eec0d6c9c/nobu.jpg?x-id=PutObject"


  stream = client.chat.completions.create(
      model="google/gemma-4-31B-it",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": prompt},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": imageUrl,
                      },
                  },
              ],
          }
      ],
      reasoning={"enabled": False},
      stream=True,
  )

  for chunk in stream:
      print(
          chunk.choices[0].delta.content or "" if chunk.choices else "",
          end="",
          flush=True,
      )
  ```
</CodeGroup>

Here's the output from the code snippet above – we're simply giving it a receipt and asking it to extract all the information:

```text Text theme={null}
**Restaurant Information:**
- Name: Noby 
- Location: Los Angeles
- Address: 903 North La Cienega 
- Phone Number: 310-657-5111

**Receipt Details:**
- Date: 04/16/2011
- Time: 9:19 PM
- Server: Daniel
- Guest Count: 15
- Reprint #: 2

**Ordered Items:**
1. **Pina Martini** - $14.00
2. **Jasmine Calpurnina** - $14.00
3. **Yamasaki L. Decar** - $14.00
4. **Ma Margarita** - $4.00
5. **Diet Coke** - $27.00
6. **Lychee Martini (2 @ $14.00)** - $28.00
7. **Lynchee Martini** - $48.00
8. **Green Tea Decaf** - $12.00
9. **Glass Icecube R/Eising** - $0.00
10. **Green Tea Donation ($2)** - $2.00
11. **Lychee Martini (2 @ $14.00)** - $28.00
12. **YS50** - $225.00
13. **Green Tea ($40.00)** - $0.00
14. **Tiradito (3 @ $25.00)** - $75.00
15. **Tiradito** - $25
16. **Tiradito #20** - $20.00
17. **New-F-BOTAN (3 @ $30.00)** - $90.00
18. **Coke Refill** - $0.00
19. **Diet Coke Refill** - $0.00
20. **Bamboo** - $0.00
21. **Admin Fee** - $300.00
22. **TESSLER (15 @ $150.00)** - $2250.00
23. **Sparkling Water Large** - $9.00
24. **King Crab Asasu (3 @ $26.00)** - $78.00
25. **Mexican white shirt (15 @ $5.00)** - $75.00
26. **NorkFish Pate Cav** - $22.00

**Billing Information:**
- **Subtotal** - $3830.00
- **Tax** - $766.00
- **Total** - $4477.72
- **Gratuity** - $4277.72 
- **Total** - $5043.72
- **Balance Due** - $5043.72
```

## How to do structured OCR and extract JSON from images

For more complex applications like receipt processing (as seen on [usebillsplit.com](https://www.usebillsplit.com/)), we can leverage Together AI's vision models to extract structured data in JSON format. This approach is particularly powerful as it combines visual understanding with structured output.

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { z } from "zod";
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const billUrl =
      "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/1627e746-7eda-46d3-8d08-8c8eec0d6c9c/nobu.jpg?x-id=PutObject";
    // Define the receipt schema using Zod
    const receiptSchema = z.object({
      businessName: z
        .string()
        .optional()
        .describe("Name of the business on the receipt"),
      date: z.string().optional().describe("Date when the receipt was created"),
      total: z.number().optional().describe("Total amount on the receipt"),
      tax: z.number().optional().describe("Tax amount on the receipt"),
    });

    // Convert Zod schema to JSON schema for Together AI
    const jsonSchema = z.toJSONSchema(receiptSchema);

    const response = await together.chat.completions.create({
      model: "google/gemma-4-31B-it",
      messages: [
        {
          role: "system",
          content:
            "You are an expert at extracting information from receipts. Extract the relevant information and format it as JSON.",
        },
        {
          role: "user",
          content: [
            { type: "text", text: "Extract receipt information" },
            { type: "image_url", image_url: { url: billUrl } },
          ],
        },
      ],
      reasoning: { enabled: false },
      response_format: {
        type: "json_schema",
        json_schema: {
          name: "receipt",
          schema: jsonSchema,
        },
      },
    });

    if (response?.choices?.[0]?.message?.content) {
      const output = JSON.parse(response.choices[0].message.content);
      console.dir(output);
      return output;
    }

    throw new Error("Failed to extract receipt information");
  }

  main();
  ```

  ```python Python theme={null}
  import json
  import together
  from pydantic import BaseModel, Field
  from typing import Optional

  ## Initialize Together AI client
  client = together.Together()


  ## Define the schema for receipt data matching the Next.js example
  class Receipt(BaseModel):
      businessName: Optional[str] = Field(
          None, description="Name of the business on the receipt"
      )
      date: Optional[str] = Field(
          None, description="Date when the receipt was created"
      )
      total: Optional[float] = Field(
          None, description="Total amount on the receipt"
      )
      tax: Optional[float] = Field(None, description="Tax amount on the receipt")


  def extract_receipt_info(image_url: str) -> dict:
      """
      Extract receipt information from an image using Together AI's vision capabilities.

      Args:
          image_url: URL of the receipt image to process

      Returns:
          A dictionary containing the extracted receipt information
      """
      # Call the Together AI API with the image URL and schema
      response = client.chat.completions.create(
          model="google/gemma-4-31B-it",
          messages=[
              {
                  "role": "system",
                  "content": "You are an expert at extracting information from receipts. Extract the relevant information and format it as JSON.",
              },
              {
                  "role": "user",
                  "content": [
                      {"type": "text", "text": "Extract receipt information"},
                      {"type": "image_url", "image_url": {"url": image_url}},
                  ],
              },
          ],
          reasoning={"enabled": False},
          response_format={
              "type": "json_schema",
              "json_schema": {
                  "name": "receipt",
                  "schema": Receipt.model_json_schema(),
              },
          },
      )

      # Parse and return the response
      if response and response.choices and response.choices[0].message.content:
          try:
              return json.loads(response.choices[0].message.content)
          except json.JSONDecodeError:
              return {"error": "Failed to parse response as JSON"}

      return {"error": "Failed to extract receipt information"}


  ## Example usage
  def main():
      receipt_url = "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/1627e746-7eda-46d3-8d08-8c8eec0d6c9c/nobu.jpg?x-id=PutObject"
      result = extract_receipt_info(receipt_url)
      print(json.dumps(result, indent=2))
      return result


  if __name__ == "__main__":
      main()
  ```
</CodeGroup>

In this case, we passed in a schema to the model since we want specific information out of the receipt in JSON format. Here's the response:

```json JSON theme={null}
{
  "businessName": "Noby", 
  "date": "04/16/2011", 
  "total": 5043.72, 
  "tax": 766 
}
```

## Best Practices

1. **Structured Data Definition**: Define clear schemas for your expected output, making it easier to validate and process the extracted data.
2. **Model Selection**: Choose the appropriate model based on your use case. Feel free to experiment with [our vision models](/docs/serverless/models#vision-models) to find the best one for you.
3. **Error Handling**: Always implement robust error handling for cases where the OCR might fail or return unexpected results.
4. **Validation**: Implement validation for the extracted data to ensure accuracy and completeness.

By following these patterns and leveraging Together AI's vision models, you can build powerful OCR applications that go beyond simple text extraction to provide structured, actionable data from images.
