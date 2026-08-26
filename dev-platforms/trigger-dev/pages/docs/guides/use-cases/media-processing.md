---
title: "Media processing workflows"
source: https://trigger.dev/docs/guides/use-cases/media-processing
path: docs/guides/use-cases/media-processing
---

Learn how to use Trigger.dev for media processing including video transcoding, image optimization, audio transformation, and document conversion.

## Overview

Build media processing pipelines that handle large files and long-running operations. Process videos, images, audio, and documents with automatic retries, progress tracking, and no timeout limits.

## Featured examples

<CardGroup>
  <Card title="FFmpeg video processing" icon="book" href="/docs/guides/examples/ffmpeg-video-processing">
    Process videos and upload results to R2 storage using FFmpeg.
  </Card>

  <Card title="Product image generator" icon="book" href="/docs/guides/example-projects/product-image-generator">
    Transform product photos into professional marketing images using Replicate.
  </Card>

  <Card title="LibreOffice PDF conversion" icon="book" href="/docs/guides/examples/libreoffice-pdf-conversion">
    Convert documents to PDF using LibreOffice.
  </Card>
</CardGroup>

## Benefits of using Trigger.dev for media processing workflows

**Process multi-hour videos without timeouts:** Transcode videos, extract frames, or run CPU-intensive operations for hours. No execution time limits.

**Stream progress to users in real-time:** Show processing status updating live in your UI. Users see exactly where encoding is and how long remains.

**Parallel processing with resource control:** Process hundreds of files simultaneously with configurable concurrency limits. Control resource usage without overwhelming infrastructure.

## Example workflow patterns

<Tabs>
  <Tab title="Video transcode">
    Simple video transcoding pipeline. Downloads video from storage, batch triggers parallel transcoding to multiple formats and thumbnail extraction, uploads all results.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[processVideo] --> B[downloadFromStorage]
          B --> C[batchTriggerAndWait]

          C --> D[transcodeToHD]
          C --> E[transcodeToSD]
          C --> F[extractThumbnail]

          D --> G[uploadToStorage]
          E --> G
          F --> G
      ```
    </div>
  </Tab>

  <Tab title="Adaptive video processing">
    **Router + Coordinator pattern**. Analyzes video metadata to determine source resolution, routes to appropriate transcoding preset, batch triggers parallel post-processing for thumbnails, preview clips, and chapter detection.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[processVideoUpload] --> B[analyzeMetadata]
          B --> C{Source<br/>Resolution?}

          C -->|4K Source| D[transcode4K]
          C -->|HD Source| E[transcodeHD]
          C -->|SD Source| F[transcodeSD]

          D --> G[coordinatePostProcessing]
          E --> G
          F --> G

          G --> H[batchTriggerAndWait]
          H --> I[extractThumbnails]
          H --> J[generatePreview]
          H --> K[detectChapters]

          I --> L[uploadToStorage]
          J --> L
          K --> L

          L --> M[notifyComplete]
      ```
    </div>
  </Tab>

  <Tab title="Smart image optimization">
    **Router + Coordinator pattern**. Analyzes image content to detect type, routes to specialized processing (background removal for products, face detection for portraits, scene analysis for landscapes), upscales with AI, batch triggers parallel variant generation.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[processImageUpload] --> B[analyzeContent]
          B --> C{Content<br/>Type?}

          C -->|Product| D[removeBackground]
          C -->|Portrait| E[detectFaces]
          C -->|Landscape| F[analyzeScene]

          D --> G[upscaleWithAI]
          E --> G
          F --> G

          G --> H[batchTriggerAndWait]
          H --> I[generateWebP]
          H --> J[generateThumbnails]
          H --> K[generateSocialCrops]

          I --> L[uploadToStorage]
          J --> L
          K --> L
      ```
    </div>
  </Tab>

  <Tab title="Podcast production">
    **Coordinator pattern**. Pre-processes raw audio with noise reduction and speaker diarization, batch triggers parallel tasks for transcription (Deepgram), audio enhancement, and chapter detection, aggregates results to generate show notes and publish.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[processAudioUpload] --> B[cleanAudio]
          B --> C[coordinateProcessing]

          C --> D[batchTriggerAndWait]
          D --> E[transcribeWithDeepgram]
          D --> F[enhanceAudio]
          D --> G[detectChapters]

          E --> H[generateShowNotes]
          F --> H
          G --> H

          H --> I[publishToPlatforms]
      ```
    </div>
  </Tab>

  <Tab title="Document extraction with approval">
    **Router pattern with human-in-the-loop**. Detects file type and routes to appropriate processor, classifies document with AI to determine type (invoice/contract/receipt), extracts structured data fields, optionally pauses with wait.forToken for human approval.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[processDocumentUpload] --> B[detectFileType]

          B -->|PDF| C[extractText]
          B -->|Word/Excel| D[convertToPDF]
          B -->|Image| E[runOCR]

          C --> F[classifyDocument]
          D --> F
          E --> F

          F -->|Invoice| G[extractLineItems]
          F -->|Contract| H[extractClauses]
          F -->|Receipt| I[extractExpenses]

          G --> J{Needs<br/>Review?}
          H --> J
          I --> J

          J -->|Yes| K[wait.forToken approval]
          J -->|No| L[processAndIntegrate]
          K --> L
      ```
    </div>
  </Tab>
</Tabs>

## Featured use cases

<CardGroup>
  <Card title="Data processing & ETL workflows" icon="database" href="/docs/guides/use-cases/data-processing-etl">
    Build complex data pipelines that process large datasets without timeouts.
  </Card>

  <Card title="Media processing workflows" icon="film" href="/docs/guides/use-cases/media-processing">
    Batch process videos, images, audio, and documents with no execution time limits.
  </Card>

  <Card title="AI media generation workflows" icon="wand-magic-sparkles" href="/docs/guides/use-cases/media-generation">
    Generate images, videos, audio, documents and other media using AI models.
  </Card>

  <Card title="Marketing workflows" icon="bullhorn" href="/docs/guides/use-cases/marketing">
    Build drip campaigns, create marketing content, and orchestrate multi-channel campaigns.
  </Card>
</CardGroup>
