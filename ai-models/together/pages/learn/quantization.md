---
title: "Quantization"
source: https://docs.together.ai/learn/quantization
path: learn/quantization
---

What quantization is, how lower precision speeds up inference, and the quality tradeoff.

**TL;DR:** Quantization is the process of storing and using a model's weights such that it uses fewer bits per number. Going from fp16 (16 bits) down to fp8 (8 bits) down to int4/fp4 (4 bits) makes inference faster and reduces model's memory requirements, at the cost of a small hit to quality. For most chat workloads, fp8 is nearly free, i.e. the quality drop is so small that it's unmeasurable. Going down to int4/fp4 can save a lot of money, and if done right, the quality drop is barely noticeable (depending on the task). Frontier open-weight models like DeepSeek-V4 are now trained natively in fp8/fp4 rather than being quantized after the fact, which closes the quality gap even further.

## A JPEG quality slider for models

The mental model for quantization is something you already know from photos. A digital camera stores every pixel as three numbers, one each for red, green, and blue. The standard is 8 bits per channel (24 bits per pixel), which gives you \~16.7 million possible colors and smooth gradients without any visible banding. Drop the encoding to 4 bits per channel and most photos still look essentially fine at first glance. Drop again to 2 bits per channel and the image visibly posterizes: smooth skies break into discrete bands, subtle gradients collapse into chunks of solid color. The scene is the same, but the encoding has gotten coarser.

<Frame>
  <img alt="A high-resolution landscape photograph of a fireweed flower spike in sharp focus against a softly blurred background of forested mountains and a partly cloudy sky." />
</Frame>

<Frame>
  <img alt="The same landscape photo of fireweed against a mountain backdrop, rendered at 8-bit/channel (24-bit total), 4-bit/channel (12-bit total), and 2-bit/channel (6-bit total). The 8-bit and 4-bit versions look nearly identical; the 2-bit version is heavily posterized with visible color banding." />
</Frame>

Quantization is the same trick applied to a model. The model's weights are real numbers, and quantization stores each one using fewer bits. 16 bits per weight is the pristine, uncompressed version. 8 bits per weight is the analogue of dropping the photo to 4 bits per channel: a meaningful reduction in storage that, for most workloads, you can't tell apart from the original. 4 bits per weight is closer to the 2-bits-per-channel photo—aggressive enough that artifacts start showing up in subtle places, and you have to actually evaluate the quantized model to know whether they matter for your specific task.

The bigger the model is to start with, the more headroom you have to compress and quantize. A 70B model at 4 bits per weight will generally outperform a 13B model at 16 bits per weight, the same way a 12-megapixel photo at 4 bits per channel still beats a 4-megapixel photo at 8 bits per channel.

## Why precision matters

A model's weights are real numbers, and at inference time the GPU spends most of its work reading those weights from memory and multiplying them with inputs. The more bits per weight, the more memory bandwidth you burn per token of output you generate. The total memory budget for a model and its activations also scales directly with bits per weight, which determines what hardware you can fit it on in the first place.

Quantization is the family of techniques for storing the same weights using fewer bits each. You end up with the same number of weights, but each one is smaller. Less memory used overall, more weights read per second, faster inference, lower hosting cost. The cost you pay is precision: the weights become slightly approximate, and that approximation translates into a small drop in model quality if done naively.

## Quantization formats

These are the formats you'll likely encounter, in approximate order of decreasing precision:

* **fp32:** 32-bit float. The full-precision format from textbook training. Almost never used for inference because it uses too much memory for not enough quality gain.
* **fp16 / bf16:** 16-bit floats. The standard format that models are trained and shipped in. bf16 has more range while fp16 has more precision. Modern GPUs prefer bf16.
* **fp8 (E4M3 / E5M2):** 8-bit float. Supported natively on H100 and later GPUs. Usually near-indistinguishable from bf16 in quality, while requiring half the memory and bandwidth.
* **int8:** 8-bit integer. An older approach to 8-bit quantization, slightly more involved than fp8 because it requires per-channel scaling. Still common on GPUs that do not have native fp8 support.
* **fp4 (MXFP4 / NVFP4):** 4-bit float. The newer 4-bit format supported natively on Blackwell (B100/B200) GPUs. Closer in quality to fp8 than int4, because it preserves the exponent range.
* **int4:** 4-bit integer. Aggressive enough that quality starts to be impacted. Most modern int4 implementations (AWQ, GPTQ, GGUF) include calibration on a sample dataset to choose quantization parameters that minimize the performance hit.

On Together, many models are served in fp8 or fp4 variants (visible in the [model list](/docs/serverless/models)), and quantization is one of the decoding options you can choose from when configuring a [dedicated endpoint](/docs/dedicated-endpoints/settings).

## How quantization actually works

Take the weights in a single layer. They have some distribution: most are small, a few are large. Suppose the range of values is roughly -1.5 to +1.5. To store these weights in int4 (only 16 possible distinct values), you:

1. Pick a scale factor. For example, 0.2.
2. For each weight, round it to the nearest multiple of the scale factor.
3. Store the integer that corresponds to the rounded value. For scale 0.2 and range -1.5 to +1.5, this gives you the integers -7 through +7, plus 0.
4. At inference time, multiply each stored integer by the scale factor to recover the (approximate) original weight.

That's essentially all there is to it conceptually. The integer takes 4 bits instead of 16, which is a 4× memory reduction. The scale factor is one float per group of weights (usually one per channel or per block), which is negligible for the overall storage cost.

<QuantizationSnapDiagram />

The art is in deciding *which* weights to round, and how. Different layers, different channels, and different blocks within a layer can use different scale factors. Calibrated approaches like AWQ and GPTQ run a small sample of real data through the model to find scales that minimize the effect of rounding on the activations that matter most. The naming conventions you'll see:

* **AWQ (Activation-aware Weight Quantization):** Common for int4.
* **GPTQ (Generalized Post-Training Quantization):** Another int4 family.
* **GGUF:** A file format used by llama.cpp that supports multiple quantization schemes.
* **SmoothQuant:** Targets int8 by smoothing activation outliers before quantizing.
* **MXFP4 / NVFP4:** The microscaling 4-bit floating-point formats used on Blackwell GPUs.

## Native quantization

Most quantization is **post-training quantization (PTQ)**, where you take a model trained in bf16 and compress it after the fact. PTQ works well down to fp8, gets noisier at int4.

The newer pattern is **native quantization**, where the model is *trained* in the low-precision format from the start. DeepSeek-V3 was the first major frontier model to train natively in fp8. DeepSeek-V4 trains natively in fp4. The advantage is that the model never has to be approximated. It was trained at the same precision it will be served in, so there's no quality gap to close. Native quantization is rapidly becoming the default for new open-weight models.

## Weights vs. activations

There are two different things that can be quantized in a model. The weights are fixed once training is done, while the intermediate activations are computed at inference time. Most public discussion of quantization focuses on weights because they account for the bulk of the memory footprint.

Quantizing activations is harder. Activations have wider dynamic ranges than weights, with occasional huge outliers, and they cannot be calibrated as easily because they depend on the current input to the model. When you see formats labeled `W8A8` or `W4A16`, that's Weight-bits / Activation-bits. The right combination depends on hardware support: GPUs that natively support fp8 in both weights and activations can run W8A8 fast, while older hardware often runs W4A16 (quantized weights and fp16 activations).

## Next steps

<CardGroup>
  <Card title="Inference metrics: TTFT & TPS" icon="dashboard" href="/learn/ttft-and-tps">
    Quantization mostly buys you TPS.
  </Card>

  <Card title="Choosing a deployment option" icon="server" href="/learn/choosing-a-deployment-option">
    Your choice of deployment determines which quantization options are available to you.
  </Card>

  <Card title="How LLMs work" icon="cpu" href="/learn/how-llms-work">
    Which weights are getting quantized, and why model size matters.
  </Card>
</CardGroup>
