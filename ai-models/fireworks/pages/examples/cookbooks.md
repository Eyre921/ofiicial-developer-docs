---
title: "Cookbooks"
source: https://docs.fireworks.ai/examples/cookbooks
path: examples/cookbooks
---

Interactive Jupyter notebooks demonstrating advanced use cases and best practices with Fireworks AI

Explore our collection of notebooks that showcase real-world applications, best practices, and advanced techniques for building with Fireworks AI.

## Fine-Tuning & Training

<CardGroup>
  <Card title="Knowledge Distillation" href="https://colab.research.google.com/github/fw-ai/cookbook/blob/main/archived/learn/finetuning/knowledge_distillation.ipynb" icon="graduation-cap">
    Transfer large model capabilities to efficient models using a two-stage SFT + RFT approach.

    **Techniques:** Supervised Fine-Tuning (SFT) + Reinforcement Fine-Tuning (RFT)

    **Results:** 52% → 70% accuracy on GSM8K mathematical reasoning
  </Card>

  <Card title="VLM Fine-tuning + Evals" href="https://huggingface.co/spaces/fireworks-ai/catalog-extract/blob/main/notebooks/01-eda-and-fine-tuning.ipynb" icon="image">
    Beat frontier closed-source models for product catalog cleansing with vision-language model fine-tuning.

    **Techniques:** Supervised Fine-Tuning (SFT)

    **Results:** 48% increase in quality from base model
  </Card>
</CardGroup>

## Multimodal AI

<CardGroup>
  <Card title="NVIDIA Nemotron VL for Document Intelligence" href="https://colab.research.google.com/github/fw-ai/cookbook/blob/main/archived/multimedia/vlm/nvidia-nemotron-vl/NVIDIA-Nemotron-v2-VL-cookbook.ipynb" icon="file-invoice">
    Extract structured data from invoices, forms, and financial documents using state-of-the-art OCR and document understanding.

    **Use Cases:** Forms, invoices, financial documents, product catalogs

    **Results:** 90.8% accuracy on invoice extraction (100% on invoice numbers and dates)
  </Card>

  <Card title="Audio Streaming Speech-to-Text" href="https://colab.research.google.com/github/fw-ai/cookbook/blob/main/archived/learn/audio/audio_streaming_speech_to_text/audio_streaming_speech_to_text.ipynb" icon="microphone">
    Real-time audio transcription with streaming support and low latency.

    **Features:** Streaming support, low-latency transcription, production-ready
  </Card>

  <Card title="Chat with Video using Qwen3 Omni" href="https://colab.research.google.com/github/fw-ai/cookbook/blob/main/archived/multimedia/video/Qwen3-Omni-Chat-With-Video-Cookbook.ipynb" icon="video">
    Analyze video and audio content with Qwen3 Omni, a multimodal model supporting video, audio, and text inputs.

    **Features:** Video captioning, scene analysis, content understanding, multimodal Q\&A
  </Card>
</CardGroup>

## Embeddings & RAG

<CardGroup>
  <Card title="Two-Stage Retrieval with Voyage Embeddings and Reranking" href="https://colab.research.google.com/github/fw-ai/cookbook/blob/main/partners/voyage-ai/voyage_two_stage_retrieval.ipynb" icon="magnifying-glass">
    Build a retrieval pipeline that recalls candidates with vector search, then reorders them with a reranker for precision.

    **Techniques:** Voyage embeddings, MongoDB `$vectorSearch`, Voyage ReRank 2.5

    **Models:** Voyage AI embedders and rerankers on dedicated deployments
  </Card>
</CardGroup>

## API Features

<CardGroup>
  <Card title="Fireworks MCP Examples" href="https://colab.research.google.com/github/fw-ai/cookbook/blob/main/archived/learn/response-api/fireworks_mcp_examples.ipynb" icon="code">
    Leverage Model Context Protocol (MCP) for GitHub repository analysis, code search, and documentation Q\&A.

    **Features:** Repository analysis, code search, documentation Q\&A, GitMCP integration

    **Models:** Qwen 3 235B with external tool support
  </Card>
</CardGroup>
