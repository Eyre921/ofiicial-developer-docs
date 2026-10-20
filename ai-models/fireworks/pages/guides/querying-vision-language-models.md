---
title: "Vision Models"
source: https://docs.fireworks.ai/guides/querying-vision-language-models
path: guides/querying-vision-language-models
---

Query Fireworks vision-language models with image inputs to analyze photos, screenshots, charts, and documents through the chat completions API and OpenAI SDKs.

Vision-language models (VLMs) process both text and images in a single request, enabling image captioning, visual question answering, document analysis, chart interpretation, OCR, and content moderation. Use VLMs via serverless inference or [dedicated deployments](/getting-started/ondemand-quickstart).

[Browse available vision models →](https://app.fireworks.ai/models?filter=Vision)

## Chat Completions API

Provide images via URL or base64 encoding. The request structure is identical to OpenAI's vision API.

**Python**

```python theme={null}
from fireworks import Fireworks

client = Fireworks()

response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k2p5",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Can you describe this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?w=800"
                    }
                }
            ]
        }
    ]
)

print(response.choices[0].message.content)
```

> [!TIP]
>
> You can also use the [OpenAI SDK](/tools-sdks/openai-compatibility) with Fireworks by changing the base URL and API key.

**JavaScript**

```javascript theme={null}
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

const response = await client.chat.completions.create({
  model: "accounts/fireworks/models/kimi-k2p5",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "Can you describe this image?" },
        {
          type: "image_url",
          image_url: {
            url: "https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?w=800"
          }
        }
      ]
    }
  ]
});

console.log(response.choices[0].message.content);
```

**curl**

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/kimi-k2p5",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "Can you describe this image?"},
          {
            "type": "image_url",
            "image_url": {
              "url": "https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?w=800"
            }
          }
        ]
      }
    ]
  }'
```

### Using base64-encoded images

For local files, encode them as base64 with the appropriate MIME type prefix:

**Python**

```python theme={null}
import base64
from fireworks import Fireworks

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

image_base64 = encode_image("your_image.jpg")

client = Fireworks()

response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k2p5",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Can you describe this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_base64}"
                    }
                }
            ]
        }
    ]
)

print(response.choices[0].message.content)
```

**JavaScript**

```javascript theme={null}
import OpenAI from "openai";
import fs from "fs";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

const imageBase64 = fs.readFileSync("your_image.jpg").toString("base64");

const response = await client.chat.completions.create({
  model: "accounts/fireworks/models/kimi-k2p5",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "Can you describe this image?" },
        {
          type: "image_url",
          image_url: {
            url: `data:image/jpeg;base64,${imageBase64}`
          }
        }
      ]
    }
  ]
});

console.log(response.choices[0].message.content);
```

## Working with images

Vision-language models support [prompt caching](/guides/prompt-caching) to improve performance for requests with repeated content. Both text and image portions can benefit from caching to reduce time to first token by up to 80%.

**Tips for optimal performance:**

* **Use URLs for long conversations** – Reduces latency compared to base64 encoding
* **Downsize images** – Smaller images use fewer tokens and process faster
* **Structure prompts for caching** – Place static instructions at the beginning, variable content at the end
* **Include metadata in prompts** – Add context about the image directly in your text prompt

## Working with PDFs and Word documents

VLMs do not natively accept PDF or Word (`.docx`) files as input. Convert them on your side before sending the request:

* **PDF**: render each page to an image and pass the images to the model using base64 encoding.
* **DOCX**: extract the text, and pass any embedded images alongside it.

> [!NOTE]
>
> Remember the [120-image limit per request](#known-limitations). The count includes images in earlier messages of the conversation that you resend with each request. For long documents, process pages in batches or select only the relevant pages.

**Python**

Install [pypdfium2](https://pypi.org/project/pypdfium2/), [Pillow](https://pypi.org/project/pillow/), and [python-docx](https://pypi.org/project/python-docx/):

```bash theme={null}
python3 -m pip install pypdfium2 pillow python-docx fireworks-ai
```

```python theme={null}
import base64
import io
from pathlib import Path

import docx
import pypdfium2 as pdfium
from docx.table import Table
from fireworks import Fireworks


def pdf_to_content(pdf_path, dpi=200):
    doc = pdfium.PdfDocument(pdf_path)
    content = []
    for page in doc:
        buf = io.BytesIO()
        page.render(scale=dpi / 72).to_pil().save(buf, format="PNG")
        img = base64.b64encode(buf.getvalue()).decode("utf-8")
        content.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/png;base64,{img}"}
        })
    doc.close()
    return content


def docx_to_content(docx_path):
    doc = docx.Document(docx_path)
    parts = []
    for block in doc.iter_inner_content():  # paragraphs and tables in document order
        if isinstance(block, Table):
            for row in block.rows:
                parts.append(" | ".join(cell.text.strip() for cell in row.cells))
        elif block.text.strip():
            parts.append(block.text)
    content = [{"type": "text", "text": "\n".join(parts)}]

    for rel in doc.part.rels.values():
        if "image" in rel.reltype:
            mime = rel.target_part.content_type
            if mime not in ("image/png", "image/jpeg", "image/gif"):
                continue
            img = base64.b64encode(rel.target_part.blob).decode("utf-8")
            content.append({
                "type": "image_url",
                "image_url": {"url": f"data:{mime};base64,{img}"}
            })
    return content


def file_to_content(path):
    suffix = Path(path).suffix.lower()
    if suffix == ".pdf":
        return pdf_to_content(path)
    if suffix == ".docx":
        return docx_to_content(path)
    raise ValueError(f"Unsupported file type: {suffix}")


client = Fireworks()

response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k3",
    messages=[{
        "role": "user",
        "content": [{"type": "text", "text": "Summarize this document."}]
        + file_to_content("document.pdf")  # or "document.docx"
    }]
)

print(response.choices[0].message.content)
```

**JavaScript**

Install [pdf-to-img](https://www.npmjs.com/package/pdf-to-img), [mammoth](https://www.npmjs.com/package/mammoth), and [openai](https://www.npmjs.com/package/openai):

```bash theme={null}
npm install pdf-to-img mammoth openai
```

```javascript theme={null}
import path from "node:path";
import mammoth from "mammoth";
import OpenAI from "openai";
import { pdf } from "pdf-to-img";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

async function pdfToContent(pdfPath) {
  const content = [];
  for await (const page of await pdf(pdfPath, { scale: 2.0 })) {
    content.push({
      type: "image_url",
      image_url: { url: `data:image/png;base64,${Buffer.from(page).toString("base64")}` },
    });
  }
  return content;
}

async function docxToContent(docxPath) {
  const { value: text } = await mammoth.extractRawText({ path: docxPath });
  const content = [{ type: "text", text }];

  const supported = ["image/png", "image/jpeg", "image/gif"];
  await mammoth.convertToHtml(
    { path: docxPath },
    {
      convertImage: mammoth.images.imgElement(async (image) => {
        if (supported.includes(image.contentType)) {
          const base64 = await image.readAsBase64String();
          content.push({
            type: "image_url",
            image_url: { url: `data:${image.contentType};base64,${base64}` },
          });
        }
        return { src: "" };
      }),
    },
  );
  return content;
}

async function fileToContent(filePath) {
  const ext = path.extname(filePath).toLowerCase();
  if (ext === ".pdf") return pdfToContent(filePath);
  if (ext === ".docx") return docxToContent(filePath);
  throw new Error(`Unsupported file type: ${ext}`);
}

const response = await client.chat.completions.create({
  model: "accounts/fireworks/models/kimi-k3",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "Summarize this document." },
        ...(await fileToContent("document.pdf")), // or "document.docx"
      ],
    },
  ],
});

console.log(response.choices[0].message.content);
```

## Advanced capabilities

> **[Vision training](/fine-tuning/fine-tuning-models#vision-training)**
>
> Train VLMs for specialized visual tasks

> **[LoRA adapters](/models/uploading-custom-models)**
>
> Deploy custom LoRA adapters for vision models

> **[Dedicated deployments](/getting-started/ondemand-quickstart)**
>
> Deploy VLMs on dedicated GPUs for better performance

> **[Video & audio inputs](/guides/video-audio-inputs)**
>
> Process video and audio content with multimodal models

## Alternative query methods

For the Completions API, manually insert the image token `<image>` in your prompt and supply images as an ordered list:

```python theme={null}
response = client.completions.create(
    model="accounts/fireworks/models/kimi-k2p5",
    prompt="SYSTEM: Hello\n\nUSER:<image>\ntell me about the image\n\nASSISTANT:",
    extra_body={
        "images": ["https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"]
    }
)

print(response.choices[0].text)
```

## Known limitations

1. **Maximum images per request**: 120 images maximum, including images in earlier messages of the conversation, regardless of format (base64 or URL)
2. **Base64 size limit**: Total base64-encoded images must be less than 10MB
3. **URL size and timeout**: Each image URL must be smaller than 5MB and download within 1.5 seconds
4. **Supported formats**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.tiff`, `.ppm`
5. **Llama 3.2 Vision models**: Pass images before text in the content field to avoid refusals (temporary limitation)
