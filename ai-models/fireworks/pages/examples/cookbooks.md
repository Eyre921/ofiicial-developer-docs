---
title: "Cookbooks"
source: https://docs.fireworks.ai/examples/cookbooks
path: examples/cookbooks
---

Interactive Jupyter notebook cookbooks for Fireworks AI showing RAG, function calling, fine-tuning, structured outputs, and other advanced inference patterns.

Explore our collection of notebooks that showcase real-world applications, best practices, and advanced techniques for building with Fireworks AI.

## Training

> **[Knowledge Distillation](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/archived/learn/finetuning/knowledge_distillation.ipynb)**
>
> Transfer large model capabilities to efficient models using a two-stage SFT + RFT approach.
>
> **Techniques:** Supervised Fine-Tuning (SFT) + Reinforcement Fine-Tuning (RFT)
>
> **Results:** 52% → 70% accuracy on GSM8K mathematical reasoning

> **[VLM Training + Evals](https://huggingface.co/spaces/fireworks-ai/catalog-extract/blob/main/notebooks/01-eda-and-fine-tuning.ipynb)**
>
> Beat frontier closed-source models for product catalog cleansing with vision-language model training.
>
> **Techniques:** Supervised Fine-Tuning (SFT)
>
> **Results:** 48% increase in quality from base model

## Multimodal AI

> **[NVIDIA Nemotron VL for Document Intelligence](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/archived/multimedia/vlm/nvidia-nemotron-vl/NVIDIA-Nemotron-v2-VL-cookbook.ipynb)**
>
> Extract structured data from invoices, forms, and financial documents using state-of-the-art OCR and document understanding.
>
> **Use Cases:** Forms, invoices, financial documents, product catalogs
>
> **Results:** 90.8% accuracy on invoice extraction (100% on invoice numbers and dates)

> **[Chat with Video using Qwen3 Omni](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/archived/multimedia/video/Qwen3-Omni-Chat-With-Video-Cookbook.ipynb)**
>
> Analyze video and audio content with Qwen3 Omni, a multimodal model supporting video, audio, and text inputs.
>
> **Features:** Video captioning, scene analysis, content understanding, multimodal Q\&A

## Embeddings & RAG

> **[Two-Stage Retrieval with Voyage Embeddings and Reranking](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/partners/voyage-ai/voyage_two_stage_retrieval.ipynb)**
>
> Build a retrieval pipeline that recalls candidates with vector search, then reorders them with a reranker for precision.
>
> **Techniques:** Voyage embeddings, MongoDB `$vectorSearch`, Voyage ReRank 2.5
>
> **Models:** Voyage AI embedders and rerankers on dedicated deployments

## API Features

> **[Fireworks MCP Examples](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/archived/learn/response-api/fireworks_mcp_examples.ipynb)**
>
> Leverage Model Context Protocol (MCP) for GitHub repository analysis, code search, and documentation Q\&A.
>
> **Features:** Repository analysis, code search, documentation Q\&A, GitMCP integration
>
> **Models:** Qwen 3 235B with external tool support
