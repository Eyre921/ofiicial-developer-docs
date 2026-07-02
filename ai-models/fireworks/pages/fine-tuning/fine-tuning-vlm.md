---
title: "Supervised Fine Tuning - Vision"
source: https://docs.fireworks.ai/fine-tuning/fine-tuning-vlm
path: fine-tuning/fine-tuning-vlm
---

Learn how to fine-tune vision-language models on Fireworks AI with image and text datasets

Vision-language model (VLM) fine-tuning allows you to adapt pre-trained models that can understand both text and images to your specific use cases.
This is particularly valuable for tasks like document analysis, visual question answering, image captioning, and domain-specific visual understanding.

To see all vision models that support fine-tuning, visit the [Model Library for vision models](https://app.fireworks.ai/models?filter=vision\&tunable=true).

## Fine-tuning a VLM using LoRA

<Steps>
  <Step title="Prepare your vision dataset">
    vision datasets must be in JSONL format in OpenAI-compatible chat format.
    Each line represents a complete training example.

    **Dataset Requirements:**

    * **Format**: `.jsonl` file
    * **Minimum examples**: 3
    * **Maximum examples**: 3 million per dataset
    * **Images**: Must be base64 encoded with proper MIME type prefixes
    * **Supported image formats**: PNG, JPG, JPEG

    **Message Schema:**
    Each training example must include a `messages` array where each message has:

    * `role`: one of `system`, `user`, or `assistant`
    * `content`: an array containing text and image objects or just text

    ### Basic VLM Dataset Example

    ```json theme={null}
    {
      "messages": [
        {
          "role": "system",
          "content": "You are a helpful visual assistant that can analyze images and answer questions about them."
        },
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "What objects do you see in this image?"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
              }
            }
          ]
        },
        {
          "role": "assistant",
          "content": "I can see a red car, a tree, and a blue house in this image."
        }
      ]
    }
    ```

    ### If your dataset contains image urls

    Images must be base64 encoded with MIME type prefixes. If your dataset contains image URLs, you'll need to download and encode them to base64.

    <Tabs>
      <Tab title="❌ Incorrect">
        ```json theme={null}
        {
          "type": "image_url",
          "image_url": {
            // ❌ Raw HTTP/HTTPS URLs are NOT supported
            "url": "https://example.com/image.jpg"
          }
        }
        ```
      </Tab>

      <Tab title="✅ Correct">
        ```json theme={null}
        {
          "type": "image_url",
          "image_url": {
            // ✅ Use data URI with base64 encoding
            // Format: data:image/{format};base64,{base64_encoded_data}
            "url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
          }
        }
        ```
      </Tab>
    </Tabs>

    You can use the following script to automatically convert your dataset to the correct format:

    <AccordionGroup>
      <Accordion title="Python script to download and encode images to base64">
        **Usage:**

        ```bash theme={null}
        # Install required dependency
        pip install requests

        # Download the script
        wget https://raw.githubusercontent.com/fw-ai/cookbook/refs/heads/main/learn/vlm-finetuning/utils/download_images_and_encode_to_b64.py

        # Run the script - will output a new dataset <path_to_your_dataset>_base64.jsonl
        python download_images_and_encode_to_b64.py --input_file <path_to_your_dataset.jsonl>
        ```
      </Accordion>
    </AccordionGroup>

    ### Advanced Dataset Examples

    <Tabs>
      <Tab title="Multi-image Conversation">
        ```json expandable theme={null}
        {
          "messages": [
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "Compare these two images and tell me the differences"
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": "data:image/jpeg;base64,/9j/4AAQSkZJRg..."
                  }
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": "data:image/jpeg;base64,/9j/4BBBSkZJRg..."
                  }
                }
              ]
            },
            {
              "role": "assistant",
              "content": "The first image shows a daytime scene while the second shows the same location at night. The lighting and shadows are completely different."
            }
          ]
        }
        ```
      </Tab>

      <Tab title="Multi-turn Conversation">
        ```json expandable theme={null}
        {
          "messages": [
            {
              "role": "system",
              "content": "You are a helpful visual assistant that can analyze images and remember details from previous images in our conversation."
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "Can you describe this kitchen layout for me?"
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQ..."
                  }
                }
              ]
            },
            {
              "role": "assistant",
              "content": "This is a modern open-plan kitchen with white cabinets, granite countertops, and stainless steel appliances. The island is positioned in the center with bar seating for 3-4 people. There's a large window above the sink providing natural light."
            },
            {
              "role": "user",
              "content": "Now look at this living room. Do you think the styles would work well together?"
            },
            {
              "role": "assistant",
              "content": "I'd be happy to help compare the styles! However, I don't see a living room image in your message. Could you please share the living room photo so I can analyze how well it would coordinate with the modern kitchen style we just discussed?"
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "Sorry about that! Here's the living room:"
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": "data:image/jpeg;base64,/9j/4BBBSkZJRgABAQ..."
                  }
                }
              ]
            },
            {
              "role": "assistant",
              "content": "Perfect! This living room has a complementary modern aesthetic that would work beautifully with the kitchen. Both spaces feature clean lines and a neutral color palette. The living room's contemporary furniture and the kitchen's sleek design would create a cohesive flow in an open floor plan. The warm wood accents in the living room would add nice contrast to the kitchen's cooler tones."
            },
          ]
        }
        ```
      </Tab>
    </Tabs>

    ### Try with an Example Dataset

    To get a feel for how VLM fine-tuning works, you can use an example vision dataset. This is a classification dataset that contains images of food with `<think></think>` tags for reasoning.

    <Tabs>
      <Tab title="Download with curl">
        ```bash theme={null}
        # Download the example dataset
        curl -L -o food_reasoning.jsonl https://huggingface.co/datasets/fireworks-ai/vision-food-reasoning-dataset/resolve/main/food_reasoning.jsonl
        ```
      </Tab>

      <Tab title="Download with wget">
        ```bash theme={null}
        # Download the example dataset
        wget https://huggingface.co/datasets/fireworks-ai/vision-food-reasoning-dataset/resolve/main/food_reasoning.jsonl
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Upload your VLM dataset">
    Upload your prepared JSONL dataset to Fireworks for training:

    <Tabs>
      <Tab title="firectl">
        ```bash theme={null}
        firectl dataset create my-vlm-dataset /path/to/vlm_training_data.jsonl
        ```
      </Tab>

      <Tab title="UI">
        Navigate to the Datasets tab in the Fireworks console, click "Create Dataset", and upload your JSONL file through the wizard.

        <Frame>
          <img alt="Dataset creation interface" />
        </Frame>
      </Tab>

      <Tab title="REST API">
        ```javascript theme={null}
        // Create dataset entry
        const createDatasetPayload = {
          datasetId: "my-vlm-dataset",
          dataset: { userUploaded: {} }
        };

        const response = await fetch(`${BASE_URL}/datasets`, {
          method: "POST",
          headers: {
            "Authorization": `Bearer ${API_KEY}`,
            "Content-Type": "application/json"
          },
          body: JSON.stringify(createDatasetPayload)
        });

        // Upload JSONL file
        const formData = new FormData();
        formData.append("file", fileInput.files[0]);

        const uploadResponse = await fetch(`${BASE_URL}/datasets/my-vlm-dataset:upload`, {
          method: "POST",
          headers: { "Authorization": `Bearer ${API_KEY}` },
          body: formData
        });
        ```
      </Tab>
    </Tabs>

    <Tip>
      For larger datasets (>500MB), use `firectl` as it handles large uploads more reliably than the web interface. For enhanced data control and security, we also support bring your own bucket (BYOB) configurations. See our [Secure Fine Tuning](/fine-tuning/secure-fine-tuning#gcs-bucket-integration) guide for setup details.
    </Tip>
  </Step>

  <Step title="Launch VLM fine-tuning job">
    Create a supervised fine-tuning job for your VLM:

    <Tabs>
      <Tab title="firectl">
        ```bash theme={null}
        firectl sftj create \
          --base-model accounts/fireworks/models/qwen2p5-vl-32b-instruct \
          --dataset my-vlm-dataset \
          --output-model my-custom-vlm \
          --epochs 3
        ```

        For additional parameters like learning rates, evaluation datasets, and batch sizes, see [Additional SFT job settings](/fine-tuning/fine-tuning-models#additional-sft-job-settings).
      </Tab>

      <Tab title="UI">
        1. Navigate to the Fine-tuning tab in the Fireworks console
        2. Click "Create Fine-tuning Job"
        3. Select your VLM base model (Qwen 2.5 VL)
        4. Choose your uploaded dataset
        5. Configure training parameters
        6. Launch the job

        <Frame>
          <img alt="Fine-tuning job creation interface" />
        </Frame>
      </Tab>
    </Tabs>

    VLM fine-tuning jobs typically take longer than text-only models due to the additional image processing. Expect training times of several hours depending on dataset size and model complexity.
  </Step>

  <Step title="Monitor training progress">
    Track your VLM fine-tuning job in the [Fireworks console](https://app.fireworks.ai/dashboard/fine-tuning).

    <Frame>
      <img alt="VLM fine-tuning job in the Fireworks console" />
    </Frame>

    Monitor key metrics:

    * **Training loss**: Should generally decrease over time
    * **Evaluation loss**: Monitor for overfitting if using evaluation dataset
    * **Training progress**: Epochs completed and estimated time remaining

    <Check>
      Your VLM fine-tuning job is complete when the status shows `COMPLETED` and your custom model is ready for deployment.
    </Check>
  </Step>

  <Step title="Deploy your fine-tuned VLM">
    Once training is complete, deploy your custom VLM:

    <Tabs>
      <Tab title="firectl">
        ```bash theme={null}
        # Create a deployment for your fine-tuned VLM
        firectl deployment create my-custom-vlm

        # Check deployment status
        firectl deployment get accounts/your-account/deployment/deployment-id
        ```
      </Tab>

      <Tab title="UI">
        Deploy from the UI using the `Deploy` dropdown in the fine-tuning job page.

        <Frame>
          <img alt="Deploy dropdown in the fine-tuning job page" />
        </Frame>
      </Tab>
    </Tabs>
  </Step>
</Steps>

## Advanced Configuration

For additional fine-tuning parameters and advanced settings like custom learning rates, batch sizes, and optimization options, see the [Additional SFT job settings](/fine-tuning/fine-tuning-models#additional-sft-job-settings) section in our comprehensive fine-tuning guide.

<Tip>
  Need custom training loops for VLMs? The **Training API** also supports vision-language model fine-tuning with full control over loss functions, training objectives, and evaluation. See [Training API — Vision Inputs](/fine-tuning/training-api/vision-inputs) for details.
</Tip>

## Interactive Tutorials: Fine-tuning VLMs

For a hands-on, step-by-step walkthrough of VLM fine-tuning, we've created two fine tuning cookbooks that demonstrates the complete process from dataset preparation, model deployment to evaluation.

<CardGroup>
  <Card title="VLM Fine-tuning Quickstart" icon="notebook" href="https://colab.research.google.com/drive/11WpagNa6xKgh1zhr1xh5uIuVtkPPL-qn">
    **Google Colab Notebook: Fine-tune Qwen2.5 VL on Fireworks AI**
  </Card>

  <Card title="VLM Fine-tuning + Evals" icon="notebook" href="https://huggingface.co/spaces/fireworks-ai/catalog-extract/tree/main/notebooks">
    **Finetuning a VLM to beat SOTA closed source model**
  </Card>
</CardGroup>

The cookbooks above cover the following:

* Setting up your environment with Fireworks CLI
* Preparing vision datasets in the correct format
* Launching and monitoring VLM fine-tuning jobs
* Testing your fine-tuned model
* Best practices for VLM fine-tuning
* Running inference on serverless VLMs
* Running evals to show performance gains

## Testing Your Fine-tuned VLM

After deployment, test your fine-tuned VLM using the same API patterns as base VLMs:

```python Python (OpenAI SDK) theme={null}
import openai

client = openai.OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="<FIREWORKS_API_KEY>",
)

response = client.chat.completions.create(
    model="accounts/your-account/models/my-custom-vlm",
    messages=[{
        "role": "user",
        "content": [{
            "type": "image_url",
            "image_url": {
                "url": "https://raw.githubusercontent.com/fw-ai/cookbook/refs/heads/main/learn/vlm-finetuning/images/icecream.jpeg"
            },
        },{
            "type": "text",
            "text": "What's in this image?",
        }],
    }]
)
print(response.choices[0].message.content)
```

<Tip>
  If you fine-tuned using the example dataset, your model should include `<think></think>` tags in its response.
</Tip>
