---
title: "Speed up models with torch.compile"
source: https://replicate.com/docs/guides/build/torch-compile.md
path: docs/guides/build/torch-compile
---

This guide covers how to implement `torch.compile` in your PyTorch models to improve inference performance and what Replicate does to help cache your compiled artifacts between model runs.

[](#what-is-torchcompile)What is torch.compile?
-----------------------------------------------

`torch.compile` is a feature that analyzes your PyTorch code as it runs and compiles it into optimized CUDA kernels. It works by:

1.  **Instrumentation**: When you call `torch.compile(f)`, it decorates your function for analysis but doesn’t trigger computation yet.
2.  **Tracing**: The first call to the decorated function traces the code execution and compiles it into optimized kernels. which are cached on disk.
3.  **Optimization**: Subsequent calls run the compiled code, which can be significantly faster than the original Python code.

Here’s a simple example:

```python
def f(x, y):
    a = torch.sin(x)
    b = torch.cos(y)
    return a + b
# Decorate f for instrumentation
opt_f = torch.compile(f)
# First call traces and compiles (slower)
print(opt_f(torch.randn(10, 10), torch.randn(10, 10)))
# Subsequent calls run optimized code (faster)
for x in range(100):
    print(opt_f(torch.randn(10, 10), torch.randn(10, 10)))
```

[](#how-does-it-work-with-replicate)How does it work with Replicate?
--------------------------------------------------------------------

1.  When a model container starts, it looks for cached `torch.compile` artifacts.
2.  If found, Torch reuses them instead of re-compiling from scratch.
3.  When containers shut down gracefully, the cache is updated if needed.
4.  Cache files are keyed on model version and stored close to GPU nodes.

[](#prerequisites)Prerequisites
-------------------------------

Before you start using `torch.compile` in your model, make sure you have:

*   An existing cog model to work with. If you don’t have one yet, check out our [guide to pushing your own model](/docs/guides/build/push-a-model) first.
*   PyTorch 2.0 or later installed.
*   A modern GPU (A100 or newer) for best results.
*   A model that benefits from compilation (not all models see improvements).

[](#when-to-use-torchcompile)When to use torch.compile
------------------------------------------------------

Models that commonly benefit include models with

*   Complex computational graphs such as LLMs and diffusion models
*   Repeated computational patterns
*   High enough traffic to serve multiple predictions before an instance shuts off to amortize the increased boot up time across multiple predictions.

Warning

`torch.compile` models are typically slower to setup than non-compiled models, even with caching.

Please make sure to measure your overall performance so that you understand the interplay slower setups and faster inferences.

[](#performance-expectations)Performance expectations
-----------------------------------------------------

Performance varies significantly between models. We have on our testing seen examples of

*   Cold boots: 2x faster when using cached artifacts.
*   Inference times: 20% and up faster compared to non-`torch.compiled` models.

Tip

Calling `torch.compile` does not trigger computation, but signals to torch to compile and cache the function when first called.

To have consistent inference speed, we suggest making an inference call from your `setup()` function to trigger compilation before your models starts accepting incoming calls.

[](#additional-information)Additional information
-------------------------------------------------

To learn how to use `torch.compile`, check out the [official PyTorch torch.compile tutorial](https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html).
