---
title: "Pinecone Assistant: SDK quickstart"
source: https://docs.pinecone.io/guides/assistant/quickstart/sdk-quickstart
path: guides/assistant/quickstart/sdk-quickstart
---

Create a Pinecone Assistant with the Python or Node.js SDK, upload a document, and chat with it to get answers cited from your file.

Pinecone Assistant answers questions about documents you upload, and cites the parts of each document it used. This is known as retrieval-augmented generation (RAG). In this quickstart, you use a Pinecone SDK to create an assistant, upload a sample financial filing, and ask the assistant a question about it.

<Tip>
  To get started in your browser, use the [Assistant Quickstart colab notebook](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/assistant-quickstart.ipynb).
</Tip>

<Steps>
  <Step title="Install an SDK">
    The Pinecone [Python SDK](/reference/sdks/python/overview) and [Node.js SDK](/reference/sdks/node/overview) provide programmatic access to the [Assistant API](/reference/api/assistant/introduction). The Python SDK requires Python 3.10 or later, and the Node.js SDK requires Node.js 22 or later.

    <CodeGroup>
      ```bash Python theme={null}
      pip install "pinecone"
      ```

      ```bash JavaScript theme={null}
      npm install @pinecone-database/pinecone
      ```
    </CodeGroup>
  </Step>

  <Step title="Get an API key">
    You need an API key to make calls to your assistant. Create a new API key in the [Pinecone console](https://app.pinecone.io/organizations/-/keys), or use the widget below to generate one. If you don't have a Pinecone account, the widget signs you up for the free [Starter plan](https://www.pinecone.io/pricing/).

    <div>
      <div>
        <div>
          <div />
        </div>
      </div>
    </div>

    Your generated API key:

    ```text theme={null}
    {{YOUR_API_KEY}}
    ```

    If you generate a key with the widget, the code samples on this page include it. Otherwise, replace `YOUR_API_KEY` in the samples with your key.
  </Step>

  <Step title="Create an assistant">
    [Create an assistant](/reference/api/latest/assistant/create_assistant) named `example-assistant`. The `instructions` apply to every response the assistant gives, and `region` sets where the assistant is deployed (`us` or `eu`).

    The Python SDK waits until the assistant is ready before it returns. The Node.js SDK returns right away, so the example checks the assistant's status until it's no longer `Initializing`.

    <CodeGroup>
      ```python Python theme={null}
      from pinecone import Pinecone

      pc = Pinecone(api_key="{{YOUR_API_KEY}}")

      pc.assistants.create(
          name="example-assistant",
          instructions="Use American English for spelling and grammar.",
          region="us",
      )
      ```

      ```javascript JavaScript theme={null}
      import { Pinecone } from '@pinecone-database/pinecone';

      const pc = new Pinecone({ apiKey: '{{YOUR_API_KEY}}' });

      await pc.assistants.create({
        name: 'example-assistant',
        instructions: 'Use American English for spelling and grammar.',
        region: 'us',
      });

      let { status } = await pc.assistants.describe('example-assistant');
      while (status === 'Initializing') {
        await new Promise((resolve) => setTimeout(resolve, 2000));
        ({ status } = await pc.assistants.describe('example-assistant'));
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Upload a file">
    [Download the sample file](https://s22.q4cdn.com/959853165/files/doc_financials/2023/ar/Netflix-10-K-01262024.pdf), a Netflix 10-K filing, to your local device. Then [upload it](/reference/api/latest/assistant/upload_file) to your assistant, replacing `/path/to/` with the folder you saved it in. The `metadata` is optional. It's returned with each citation, and you can use it to [filter which files the assistant uses](/guides/assistant/chat-with-assistant#filter-chat-with-metadata).

    The assistant has to process the file before it can answer questions about it, which can take a few minutes. The Python SDK waits until processing finishes. The Node.js SDK returns an operation, so the example checks the operation's status until it's `Completed`.

    <CodeGroup>
      ```python Python theme={null}
      pc.assistants.upload_file(
          assistant_name="example-assistant",
          file_path="/path/to/Netflix-10-K-01262024.pdf",
          metadata={"company": "netflix", "document_type": "form 10k"},
      )
      ```

      ```javascript JavaScript theme={null}
      const assistant = pc.assistant({ name: 'example-assistant' });

      const operation = await assistant.uploadFile({
        path: '/path/to/Netflix-10-K-01262024.pdf',
        metadata: { company: 'netflix', document_type: 'form 10k' },
      });

      let { status: uploadStatus } = await assistant.describeOperation(operation.id);
      while (uploadStatus === 'Processing') {
        await new Promise((resolve) => setTimeout(resolve, 5000));
        ({ status: uploadStatus } = await assistant.describeOperation(operation.id));
      }
      console.log(uploadStatus);
      ```
    </CodeGroup>
  </Step>

  <Step title="Chat with the assistant">
    [Chat with the assistant](/reference/api/latest/assistant/chat_assistant) by asking it a question about the file:

    <CodeGroup>
      ```python Python theme={null}
      response = pc.assistants.chat(
          assistant_name="example-assistant",
          messages=[{"role": "user", "content": "Who is the CFO of Netflix?"}],
      )

      print(response.message.content)
      ```

      ```javascript JavaScript theme={null}
      const response = await assistant.chat({
        messages: [{ role: 'user', content: 'Who is the CFO of Netflix?' }],
      });

      console.log(response.message.content);
      ```
    </CodeGroup>

    The assistant answers from the uploaded file:

    ```text Output theme={null}
    The Chief Financial Officer (CFO) of Netflix is Spencer Neumann.
    ```

    The response also includes `citations`. Each citation marks a `position` in the answer and lists the file and pages that support it. The full API response looks like the following:

    ```json Response expandable theme={null}
    {
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "The Chief Financial Officer (CFO) of Netflix is Spencer Neumann."
      },
      "id": "00000000...",
      "model": "gpt-4o-2024-11-20",
      "usage": {
        "prompt_tokens": 23633,
        "completion_tokens": 24,
        "total_tokens": 23657
      },
      "citations": [
        {
          "position": 63,
          "references": [
            {
              "file": {
                "status": "Available",
                "id": "76a11dd1...",
                "name": "Netflix-10-K-01262024.pdf",
                "size": 1073470,
                "metadata": {
                  "company": "netflix",
                  "document_type": "form 10k"
                },
                "updated_on": "2025-07-16T16:46:40.787204651Z",
                "created_on": "2025-07-16T16:45:59.414273474Z",
                "signed_url": "https://storage.googleapis.com/...",
                "multimodal": false
              },
              "pages": [78, 79, 80],
              "highlight": null
            }
          ]
        }
      ],
      "context_snippet_count": 16
    }
    ```

    <Warning>
      [`signed_url`](https://cloud.google.com/storage/docs/access-control/signed-urls) provides temporary, read-only access to the relevant file. Anyone with the link can access the file, so treat it as sensitive data. Expires in one hour.
    </Warning>
  </Step>

  <Step title="Clean up">
    When you no longer need `example-assistant`, [delete it](/reference/api/latest/assistant/delete_assistant):

    <Warning>
      Deleting an assistant also deletes all files uploaded to the assistant.
    </Warning>

    <CodeGroup>
      ```python Python theme={null}
      pc.assistants.delete(name="example-assistant")
      ```

      ```javascript JavaScript theme={null}
      await pc.assistants.delete('example-assistant');
      ```
    </CodeGroup>
  </Step>
</Steps>

## Next steps

* [Evaluate the assistant's answers](/guides/assistant/evaluate-answers) against a ground truth answer (Standard and Enterprise plans).
* [Choose a model, stream responses, and filter by metadata](/guides/assistant/chat-with-assistant) when you chat with an assistant.
* [Retrieve context snippets](/guides/assistant/retrieve-context-snippets) to use with your own LLM.
* Explore a [sample app](/examples/sample-apps/pinecone-assistant) built on Pinecone Assistant.
