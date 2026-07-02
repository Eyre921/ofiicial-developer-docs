---
title: "Optimize models with Pruna"
source: https://replicate.com/docs/guides/build/optimize-models-with-pruna.md
path: docs/guides/build/optimize-models-with-pruna
---

[Pruna AI](https://github.com/PrunaAI/pruna) is an open-source model optimization framework that compresses deep learning models using quantization, pruning, and compilation to make models faster, smaller, and cheaper.

This guide walks you through building a simple Cog model and optimizing it with [Pruna OSS](https://github.com/PrunaAI/pruna). By the end, you’ll have a compressed model deployed on Replicate that runs faster and costs less than the original.

[](#why-optimize-your-models)Why optimize your models?
------------------------------------------------------

Cog makes it easy to build and package machine learning models, but the models you build are not always guaranteed to be fast or efficient. Unoptimized models can rack up costs, slow down inference, and waste resources. By optimizing your models with Pruna, you can achieve the following benefits:

*   Faster Inference Times: Optimized models run quicker, leading to better user experiences and higher user retention as a result.
*   Smaller Models: Optimized models are smaller, which allows you to either use a smaller GPU to run the same model or to run multiple models on the same GPU.
*   Lower Computational Costs: Faster inference times and smaller models allow you to save on costs by using fewer GPUs to handle the same amount of load.
*   Environmental Impact: Smaller and faster models consume less energy, making AI more sustainable.

[](#prerequisites)Prerequisites
-------------------------------

To follow this guide, you’ll need:

*   An account on Replicate and, optionally, a Replicate API Token. If you don’t have a Replicate account, you can [sign in using your GitHub account](https://replicate.com/signin). If you already have an account, you can [create a new API token](https://replicate.com/account/api-tokens) to push the model automatically using GitHub Actions.
*   Docker. Required for building and running Cog environments. If you don’t have Docker installed, check how to [install and start Docker](https://docs.docker.com/get-docker/) before running Cog.
*   Git. Required for version control and repository management. You can download it from the [official website](https://git-scm.com/downloads)

[](#step-1-create-a-model-on-replicate)Step 1: Create a model on Replicate
--------------------------------------------------------------------------

First, you need to [create a model on Replicate](https://replicate.com/create). Be sure to follow the instructions carefully: select the correct owner or organization, set the appropriate visibility (public for everyone or private for your use only), and choose the desired hardware. It’s also a good idea to check [how billing works in Replicate](https://replicate.com/docs/topics/billing) to avoid unexpected costs.

[](#step-2-install-cog)Step 2: Install Cog
------------------------------------------

[Cog](https://cog.run/) is an open-source tool that lets you package your models in a container and easily deploy them to your own infrastructure or Replicate.

Run the following commands to install it:

```bash
sh <(curl -fsSL <https://cog.run/install.sh)
```

For more installation options, check the [Cog documentation](https://cog.run/#install).

[](#step-3-initialize-your-project)Step 3: Initialize your project
------------------------------------------------------------------

First, you need to create a new directory inside your project and initialize it with Cog:

```bash
mkdir my-pruna-model
cd my-pruna-model
cog init
```

The key components of this repo are:

*   `cog.yaml` - Configures the model for reproducible builds on Replicate and runs using Cog.
*   `predict.py` - Implements the Predictor, which handles the loading, optimization, and inference.

[](#step-4-configure-dependencies)Step 4: Configure dependencies
----------------------------------------------------------------

The `cog.yaml` file is used to configure CUDA, Python, and any other dependencies that are needed to run the model. To use Pruna, you’ll need Python ≥3.9 and any NVIDIA GPU from Replicate.

If you are using Pruna Pro, you will need to [install the Pruna Pro package](https://docs.pruna.ai/en/stable/docs_pruna_pro/user_manual/pruna_pro.html).

```yaml
build:
  gpu: true
  cuda: "12.1"
  system_packages:
    - "libgl1-mesa-glx"
    - "libglib2.0-0"
    - "git"
    - "build-essential"
  python_version: "3.11"
  run:
    - command: pip install pruna # or pip install pruna_pro for more advanced compression algorithms
    - command: pip install colorama
    - command: export CC=/usr/bin/gcc
predict: "predict.py:Predictor"
```

[](#step-5-compress-your-model)Step 5: Compress your model
----------------------------------------------------------

The `predict.py` file defines the inputs and outputs for your model. The steps to compress your model are:

1.  Load the model. You can load the model using the original library, e.g. `diffusers` or `transformers`. This will serve as the baseline model before optimization.
2.  Configure Pruna for optimization. This is done by creating a `SmashConfig` object and setting the desired compression algorithms. You can combine multiple, even more than 5, at the same time. For an overview of the available compression algorithms, check the [Pruna documentation](https://docs.pruna.ai/en/stable/compression.html).
3.  Compress the model. With the `smash` function, you provide the model and its configuration, and it gives you back a compressed version. If you are using Pruna Pro, don’t forget to [provide your Pruna token](https://docs.pruna.ai/en/stable/docs_pruna_pro/user_manual/pruna_pro.html).
4.  Use the compressed model. You can now start predicting with the compressed model.

Here is an example of how to compress a Flux model with Pruna:

```python
import tempfile
import torch
from cog import BasePredictor, Input, Path
from diffusers import FluxPipeline
from pruna import SmashConfig, smash
class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load and optimize the model"""
        # Load the model
        self.pipe = FluxPipeline.from_pretrained(
            "black-forest-labs/FLUX.1-dev",
            torch_dtype=torch.bfloat16,
        ).to("cuda")
        # Configure Pruna
        smash_config = SmashConfig()
        # Add the compiler and cacher
        smash_config["compiler"] = "torch_compile"
        smash_config["cacher"] = "fora"
        # Add the tokenizer
        smash_config.add_tokenizer(self.pipe.tokenizer)
        # Optimize the model
        self.pipe = smash(
            model=self.pipe,
            smash_config=smash_config,
        )
    def predict(
        self,
        prompt: str = Input(description="Prompt"),
        num_inference_steps: int = Input(
            description="Number of inference steps", default=28
        ),
        guidance_scale: float = Input(
            description="Guidance scale", default=0.0
        ),
        max_sequence_length: int = Input(
            description="Max sequence length", default=256
        ),
        seed: int = Input(description="Seed", default=42),
        image_height: int = Input(description="Image height", default=1024),
        image_width: int = Input(description="Image width", default=1024),
    ) -> Path:
        """Run a prediction"""
        image = self.pipe(
            prompt,
            height=image_height,
            width=image_width,
            guidance_scale=guidance_scale,
            num_inference_steps=num_inference_steps,
            max_sequence_length=max_sequence_length,
            generator=torch.Generator("cpu").manual_seed(seed)
        ).images[0]
        # Save the image
        output_dir = Path(tempfile.mkdtemp())
        image_path = output_dir / "output.png"
        image.save(image_path)
        return image_path
```

Great! Your model will now be more efficient and faster to run.

[](#step-6-build-and-test-your-model)Step 6: Build and test your model
----------------------------------------------------------------------

Once you’ve defined your model and compression methods, you can build and run your model locally.

First, you need to install the required dependencies and set up the environment according to the `cog.yaml` file.

```bash
cog build
```

When it’s built, you can run a prediction, which will follow the steps mentioned in the previous section.

```bash
cog run --input prompt="a scenic landscape with mountains" --input num_inference_steps=28 --input guidance_scale=7.5
```

[](#step-7-push-your-model)Step 7: Push your model
--------------------------------------------------

Your model is ready! So it’s time to push it to Replicate. For this, you can set up a GitHub Workflow to automate the deployment or use the Cog CLI manually. Here, we will show you how to do both.

### [](#set-up-a-github-actions-workflow)Set up a GitHub Actions workflow

This is the recommended approach if you want to streamline your deployment. Create a `.yaml` file in the `.github/workflows` directory, and add your Replicate API token to GitHub Secrets as `REPLICATE_API_TOKEN`. Once the GitHub Action runs, the model will be pushed to Replicate.

```yaml
name: Push the model to Replicate
on:
  workflow_dispatch:
    inputs:
      model_name:
        default: "<your-username>/<your-model-name>" # e.g. "prunaai/flux-dev"
jobs:
  push_to_replicate:
    name: Push to Replicate
    runs-on: ubuntu-latest
    steps:
      - name: Free disk space
        uses: jlumbroso/free-disk-space@v1.3.1
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Cog
        uses: replicate/setup-cog@v2
        with:
          token: ${{ secrets.REPLICATE_API_TOKEN }}
      - name: Push to Replicate
        run: |
          cog push
```

### [](#use-the-cog-cli)Use the Cog CLI

If you prefer not to use a GitHub Workflow, you can push your model manually with the Cog CLI. Make sure your Replicate API token is set in your local environment or in GitHub Secrets.

```bash
cog login
cog push r8.im/<your-username>/<your-model-name> # e.g. "r8.im/prunaai/flux-dev"
```

[](#step-8-use-your-model)Step 8: Use your model
------------------------------------------------

Congratulations! Your compressed model is now live on Replicate.

You can try it out right away—either from your model page or by clicking the “Run with an API” button to use it through the API.

[](#next-steps)Next steps
-------------------------

When you bring together Pruna’s optimization superpowers and Replicate’s seamless deployment platform, you unlock the best of both worlds—speed, performance, cost savings, and scalability!

Now that you have your own optimized model, the question is: what will you build next?

*   Compress more models and explore different compression methods with Pruna. Check the [Pruna documentation](https://docs.pruna.ai/en/stable/compression.html) for more information.
*   Join us in [Discord](https://discord.com/invite/JFQmtFKCjd) to get support or to share your feedback.
