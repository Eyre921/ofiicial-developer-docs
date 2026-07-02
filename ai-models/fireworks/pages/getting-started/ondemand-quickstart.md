---
title: "Deployments Quickstart"
source: https://docs.fireworks.ai/getting-started/ondemand-quickstart
path: getting-started/ondemand-quickstart
---

Deploy models on dedicated GPUs in minutes

On-demand deployments are dedicated GPUs that give you better performance, no rate limits, fast autoscaling, and a wider selection of models than serverless. This quickstart will help you spin up your first on-demand deployment in minutes.

## Step 1: Create and export an API key

Before you begin, create an API key in the [Fireworks dashboard](https://app.fireworks.ai/settings/users/api-keys). Click **Create API key** and store it in a safe location.

Once you have your API key, export it as an environment variable in your terminal:

<Tabs>
  <Tab title="macOS / Linux">
    ```bash theme={null}
    export FIREWORKS_API_KEY="your_api_key_here"
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell theme={null}
    setx FIREWORKS_API_KEY "your_api_key_here"
    ```
  </Tab>
</Tabs>

## Step 2: Install the CLI

To create and manage on-demand deployments, you'll need the `firectl` CLI tool. Install it using one of the following methods, based on your platform:

<CodeGroup>
  ```bash homebrew theme={null}
  brew tap fw-ai/firectl
  brew install firectl

  # If you encounter a failed SHA256 check, try first running
  brew update
  ```

  ```bash macOS (Apple Silicon) theme={null}
  curl https://storage.googleapis.com/fireworks-public/firectl/stable/darwin-arm64.gz -o firectl.gz
  gzip -d firectl.gz && chmod a+x firectl
  sudo mv firectl /usr/local/bin/firectl
  sudo chown root: /usr/local/bin/firectl
  ```

  ```bash macOS (x86_64) theme={null}
  curl https://storage.googleapis.com/fireworks-public/firectl/stable/darwin-amd64.gz -o firectl.gz
  gzip -d firectl.gz && chmod a+x firectl
  sudo mv firectl /usr/local/bin/firectl
  sudo chown root: /usr/local/bin/firectl
  ```

  ```bash Linux  (x86_64) theme={null}
  wget -O firectl.gz https://storage.googleapis.com/fireworks-public/firectl/stable/linux-amd64.gz
  gunzip firectl.gz
  sudo install -o root -g root -m 0755 firectl /usr/local/bin/firectl
  ```

  ```Text Windows (64 bit) theme={null}
  wget -L https://storage.googleapis.com/fireworks-public/firectl/stable/firectl.exe
  ```
</CodeGroup>

Then, sign in:

```bash theme={null}
firectl signin
```

## Step 3: Create a deployment

This command will create a deployment of GPT OSS 120B optimized for speed. It will take a few minutes to complete. The resulting deployment will scale up to 1 replica.

```bash theme={null}
firectl deployment create accounts/fireworks/models/gpt-oss-120b \
        --deployment-shape fast \
        --scale-down-window 5m \
        --scale-up-window 30s \
        --min-replica-count 0 \
        --max-replica-count 1 \
        --scale-to-zero-window 5m \
        --wait
```

<Tip>
  `fast` is called a [deployment shape](/guides/ondemand-deployments#deployment-shapes), which is a pre-configured deployment template created by the Fireworks team that sets sensible defaults for most deployment options (such as hardware type).

  You can also pass `throughput` or `cost` to `--deployment-shape`:

  * `throughput` creates a deployment that trades off latency for lower cost-per-token at scale
  * `cost` creates a deployment that trades off latency and throughput for lowest cost-per-token at small scale, usually for early experimentation and prototyping

  While we recommend using a deployment shape, you are also free to pass your own configuration to the deployment via our [deployment guide](/guides/ondemand-deployments).
</Tip>

The response will look like this:

```bash theme={null}
Name: accounts/<YOUR ACCOUNT ID>/deployments/<DEPLOYMENT ID>
Create Time: <CREATION_TIME>
Expire Time: <EXPIRATION_TIME>
Created By: <YOUR EMAIL>
State: CREATING
Status: OK
Min Replica Count: 0
Max Replica Count: 1
Desired Replica Count: 0
Replica Count: 0
Autoscaling Policy:
  Scale Up Window: 30s
  Scale Down Window: 5m0s
  Scale To Zero Window: 5m0s
Base Model: accounts/fireworks/models/gpt-oss-120b
...other fields...
```

Take note of the `Name:` field in the response, as it will be used in the next step to query your deployment.

[Learn more about deployment options→](/guides/ondemand-deployments)

[Learn more about autoscaling options→](/guides/ondemand-deployments#autoscaling)

## Step 4: Query your deployment

Now you can query your on-demand deployment using the same API as serverless models, but using your dedicated deployment. Replace `<DEPLOYMENT_NAME>` in the below snippets with the value from the `Name:` field in the previous step:

<Tabs>
  <Tab title="Python (Fireworks SDK)">
    Install the [Fireworks Python SDK](/tools-sdks/python-sdk):

    <Note>
      The SDK is currently in alpha. Use the `--pre` flag when installing to get the latest version.
    </Note>

    <CodeGroup>
      ```bash pip theme={null}
      pip install --pre fireworks-ai
      ```

      ```bash poetry theme={null}
      poetry add --pre fireworks-ai
      ```

      ```bash uv theme={null}
      uv add --pre fireworks-ai
      ```
    </CodeGroup>

    Then make your first on-demand API call:

    ```python theme={null}
    from fireworks import Fireworks

    client = Fireworks()

    response = client.chat.completions.create(
        model="accounts/fireworks/models/gpt-oss-120b#<DEPLOYMENT_NAME>",
        messages=[{
            "role": "user",
            "content": "Explain quantum computing in simple terms",
        }],
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="Python (OpenAI SDK)">
    ```python theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    response = client.chat.completions.create(
        model="<DEPLOYMENT_NAME>",
        messages=[{
            "role": "user",
            "content": "Explain quantum computing in simple terms",
        }],
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "<DEPLOYMENT_NAME>",
      messages: [
        {
          role: "user",
          content: "Explain quantum computing in simple terms",
        },
      ],
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "<DEPLOYMENT_NAME>",
        "messages": [
          {
            "role": "user",
            "content": "Explain quantum computing in simple terms"
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

The examples from the Serverless quickstart will work with this deployment as well, just replace the model string with the deployment-specific model string from above.

[Serverless quickstart→](/getting-started/quickstart)

## Common use cases

### Autoscale based on requests per second

```bash theme={null}
firectl deployment create accounts/fireworks/models/gpt-oss-120b \
        --deployment-shape fast \
        --scale-down-window 5m \
        --scale-up-window 30s \
        --scale-to-zero-window 5m \
        --min-replica-count 0 \
        --max-replica-count 4 \
        --load-targets requests_per_second=5 \
        --wait
```

### Autoscale based on concurrent requests

```bash theme={null}
firectl deployment create accounts/fireworks/models/gpt-oss-120b \
        --deployment-shape fast \
        --scale-down-window 5m \
        --scale-up-window 30s \
        --scale-to-zero-window 5m \
        --min-replica-count 0 \
        --max-replica-count 4 \
        --load-targets concurrent_requests=5 \
        --wait
```

## Next steps

Ready to scale to production, explore other modalities, or customize your models?

<CardGroup>
  <Card title="Upload a custom model" href="/models/uploading-custom-models" icon="server">
    Bring your own model and deploy it on Fireworks
  </Card>

  <Card title="Fine-tune Models" href="/fine-tuning/finetuning-intro" icon="sliders">
    Improve model quality with supervised and reinforcement learning
  </Card>

  <Card title="Embeddings & Reranking" href="/guides/querying-embeddings-models" icon="brackets-curly">
    Use embeddings & reranking in search & context retrieval
  </Card>

  <Card title="Batch Inference" href="/guides/batch-inference" icon="list-check">
    Run async inference jobs at scale, faster and cheaper
  </Card>

  <Card title="Browse 100+ Models" href="https://fireworks.ai/models" icon="books">
    Explore all available models across modalities
  </Card>

  <Card title="API Reference" href="/api-reference/introduction" icon="code">
    Complete API documentation
  </Card>
</CardGroup>
