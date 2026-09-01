---
title: "How many tokens per image?"
source: https://docs.fireworks.ai/faq-new/billing-pricing/how-many-tokens-per-image
path: faq-new/billing-pricing/how-many-tokens-per-image
---

Learn how to calculate token usage for images in vision models and understand pricing implications

Image token consumption varies by model and resolution, typically ranging from 1,000 to 2,500 tokens per image for most common resolutions.

## Common resolution token counts

The following table shows the token counts for a single image for Qwen2.5 VL at different image resolutions:

| Resolution | Token Count |
| ---------- | ----------- |
| 336×336    | 144         |
| 672×672    | 576         |
| 1024×1024  | 1,369       |
| 1280×720   | 1,196       |
| 1920×1080  | 2,769       |
| 2560×1440  | 4,641       |
| 3840×2160  | 10,549      |

## Calculating exact token count for your images

You can determine exact token usage by processing your images through the model's tokenizer.
For instance, for Qwen2.5 VL, you can use the following code:

<Steps>
  <Step title="Install dependencies">
    ```bash theme={null}
    pip install torch torchvision transformers pillow
    ```
  </Step>

  <Step title="Tokenize your image">
    ```python Tokenizing your image theme={null}
    import requests
    from PIL import Image
    from transformers import AutoProcessor
    import os

    # Your image source - can be URL or local path
    IMAGE_URL_OR_PATH = "https://images.unsplash.com/photo-1519125323398-675f0ddb6308"

    def load_image(source):
        """Load image from URL or local file path"""
        if source.startswith(('http://', 'https://')):
            print(f"Downloading image from URL: {source}")
            response = requests.get(source)
            response.raise_for_status()
            return Image.open(requests.get(source, stream=True).raw)
        else:
            print(f"Loading image from path: {source}")
            if not os.path.exists(source):
                raise FileNotFoundError(f"Image file not found: {source}")
            return Image.open(source)

    def count_image_tokens(image):
        """Count how many tokens an image takes using Qwen 2.5 VL processor"""
        processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-3B-Instruct")
        
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": image},
                    {"type": "text", "text": "What's in this image?"},
                ],
            }
        ]
        
        text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = processor(text=text, images=[image], return_tensors="pt")
        input_ids = inputs["input_ids"][0]
        
        # Count the image pad tokens (151655 is Qwen2.5 VL's image token ID)
        image_tokens = (input_ids == 151655).sum().item()
        
        return image_tokens, input_ids

    def main():
        import sys
        
        image_source = sys.argv[1] if len(sys.argv) > 1 else IMAGE_URL_OR_PATH
        
        print(f"Processing image: {image_source}")
        image = load_image(image_source)
        print(f"Image size: {image.size}")
        print(f"Image mode: {image.mode}")
        
        print("\nCalculating tokens...")
        image_tokens, input_ids = count_image_tokens(image)
        
        print(f"Total tokens: {len(input_ids)}")
        print(f"Image tokens: {image_tokens}")
        print(f"Text tokens: {len(input_ids) - image_tokens}")
        
    if __name__ == "__main__":
        main()
    ```

    ```bash Usage theme={null}
    # Calculate tokens for an image URL
    python token_calculator.py "https://example.com/image.jpg"

    # Calculate tokens for a local image
    python token_calculator.py "path/to/your/image.png"
    ```
  </Step>
</Steps>
