---
title: "Video & Audio Inputs"
source: https://docs.fireworks.ai/guides/video-audio-inputs
path: guides/video-audio-inputs
---

Query multimodal models to process video and audio content directly

Some multimodal models can process audio and/or video inputs directly, enabling video captioning, scene analysis, content understanding, and multimodal question answering. Availability depends on the model: GLM 5.3 Flash supports video input on Serverless, while Qwen3 Omni and Molmo2 use [dedicated deployments](/getting-started/ondemand-quickstart).

## Available models

| Model                                                                                            | Input support      | Notes                         |
| ------------------------------------------------------------------------------------------------ | ------------------ | ----------------------------- |
| GLM 5.3 Flash                                                                                    | Image, video, text | Serverless                    |
| [Qwen3 Omni 30B A3B Instruct](https://fireworks.ai/models/fireworks/qwen3-omni-30b-a3b-instruct) | Video, audio, text | Dedicated deployment required |
| [Molmo2-4B](https://fireworks.ai/models/fireworks/molmo2-4b)                                     | Video, text        | Dedicated deployment required |
| [Molmo2-8B](https://fireworks.ai/models/fireworks/molmo2-8b)                                     | Video, text        | Dedicated deployment required |

<Note>
  GLM 5.3 Flash supports image, video, and text inputs. This page does not claim audio input support for GLM 5.3 Flash. Qwen3 Omni supports native video and audio inputs. Molmo2 models are video-only, so use the dedicated request structure below but omit `audio_url`; Molmo2 cannot understand audio from videos.
</Note>

## Choose a serving path

### Serverless

GLM 5.3 Flash is available directly through Serverless. No deployment is required:

```text theme={null}
accounts/fireworks/models/glm-5p3-flash
```

### Dedicated deployment

Qwen3 Omni and Molmo2 require dedicated deployments. For Qwen3 Omni, create one using firectl:

```bash theme={null}
firectl deployment create qwen3-omni-30b-a3b-instruct \
  --account-id <YOUR_ACCOUNT_ID> \
  --min-replica-count 1 \
  --max-replica-count 1 \
  --deployment-shape qwen3-omni-30b-a3b-instruct-minimal
```

<Note>
  Make sure to use the predefined `qwen3-omni-30b-a3b-instruct-minimal` deployment shape for your deployment to work correctly.
</Note>

## Chat Completions API

### Serverless video by URL

GLM 5.3 Flash accepts a reachable video URL in a `video_url` content block.

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    import os
    import requests

    url = "https://api.fireworks.ai/inference/v1/chat/completions"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['FIREWORKS_API_KEY']}",
    }

    payload = {
        "model": "accounts/fireworks/models/glm-5p3-flash",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What happens in this video?"},
                    {
                        "type": "video_url",
                        "video_url": {
                            "url": "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"
                        },
                    },
                ],
            }
        ],
    }

    response = requests.post(url, headers=headers, json=payload, timeout=300)
    response.raise_for_status()
    print(response.json()["choices"][0]["message"]["content"])
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/glm-5p3-flash",
        "messages": [
          {
            "role": "user",
            "content": [
              {"type": "text", "text": "What happens in this video?"},
              {
                "type": "video_url",
                "video_url": {
                  "url": "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"
                }
              }
            ]
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

The URL must return the media file directly and remain reachable while the request is processed. For private media, use a signed HTTPS URL that remains valid until inference finishes.

### Dedicated video and audio with Base64

Qwen3 Omni accepts `video_url`, `audio_url`, and `text` content types. Provide the video and audio as Base64-encoded data URLs.

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    import os
    import base64
    import requests

    # Load and encode your preprocessed video and audio
    with open("processed_video.mp4", "rb") as f:
        video_b64 = base64.b64encode(f.read()).decode("utf-8")

    with open("audio.ogg", "rb") as f:
        audio_b64 = base64.b64encode(f.read()).decode("utf-8")

    # API configuration
    url = "https://api.fireworks.ai/inference/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['FIREWORKS_API_KEY']}",
    }

    # Request payload
    payload = {
        "model": "accounts/<YOUR_ACCOUNT_ID>/models/qwen3-omni-30b-a3b-instruct#accounts/<YOUR_ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
        "max_tokens": 1000,
        "temperature": 0.3,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "video_url", "video_url": {"url": f"data:video/mp4;base64,{video_b64}"}},
                    {"type": "audio_url", "audio_url": {"url": f"data:audio/ogg;base64,{audio_b64}"}},
                    {"type": "text", "text": "Describe what happens in this video."},
                ],
            },
        ],
    }

    # Send request
    response = requests.post(url, headers=headers, json=payload)
    print(response.json()["choices"][0]["message"]["content"])
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    # Encode your files (run these separately)
    VIDEO_B64=$(base64 -i processed_video.mp4)
    AUDIO_B64=$(base64 -i audio.ogg)

    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/<YOUR_ACCOUNT_ID>/models/qwen3-omni-30b-a3b-instruct#accounts/<YOUR_ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
        "max_tokens": 1000,
        "temperature": 0.3,
        "messages": [
          {
            "role": "user",
            "content": [
              {"type": "video_url", "video_url": {"url": "data:video/mp4;base64,'$VIDEO_B64'"}},
              {"type": "audio_url", "audio_url": {"url": "data:audio/ogg;base64,'$AUDIO_B64'"}},
              {"type": "text", "text": "Describe what happens in this video."}
            ]
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

## Working with videos

Video models perform best with inputs that balance quality and token efficiency. When you control the source media, use ffmpeg to optimize video and audio before sending requests. The settings below are starting points for the dedicated Base64 example, not universal hard limits.

### Preprocessing video

Extract frames at 1 FPS and downscale to 360p for efficient processing:

```bash theme={null}
ffmpeg -y -i input_video.mp4 \
  -t 60 \
  -vf "fps=1,scale=-1:360" \
  -c:v libx264 -preset fast \
  -an \
  processed_video.mp4
```

| Parameter      | Description                                     |
| -------------- | ----------------------------------------------- |
| `-t 60`        | Limit to first 60 seconds                       |
| `fps=1`        | Extract 1 frame per second                      |
| `scale=-1:360` | Downscale to 360p height, maintain aspect ratio |
| `-an`          | Remove audio track (extracted separately)       |

### Preprocessing audio

Extract audio as Opus in an Ogg container for optimal compression:

```bash theme={null}
ffmpeg -y -i input_video.mp4 \
  -t 60 \
  -vn \
  -c:a libopus \
  -b:a 24k \
  -ar 16000 \
  -ac 1 \
  audio.ogg
```

| Parameter      | Description               |
| -------------- | ------------------------- |
| `-t 60`        | Limit to first 60 seconds |
| `-vn`          | Remove video track        |
| `-c:a libopus` | Use Opus codec            |
| `-b:a 24k`     | 24 kbps bitrate           |
| `-ar 16000`    | 16 kHz sample rate        |
| `-ac 1`        | Mono audio                |

### Complete preprocessing example

```python theme={null}
import subprocess
import tempfile
import base64
import os

def preprocess_video(video_path: str) -> tuple[str, str]:
    """
    Preprocess video for optimal model input.
    
    Returns:
        Tuple of (video_base64, audio_base64)
    """
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as tmp_video:
        processed_video_path = tmp_video.name
    with tempfile.NamedTemporaryFile(suffix=".ogg", delete=False) as tmp_audio:
        audio_path = tmp_audio.name
    
    try:
        # Process video: 1 FPS, 360p, max 60 seconds
        subprocess.run([
            "ffmpeg", "-y", "-i", video_path,
            "-t", "60",
            "-vf", "fps=1,scale=-1:360",
            "-c:v", "libx264", "-preset", "fast",
            "-an",
            processed_video_path
        ], check=True, capture_output=True)
        
        # Extract audio: Opus/Ogg, mono, 16kHz, 24kbps
        subprocess.run([
            "ffmpeg", "-y", "-i", video_path,
            "-t", "60",
            "-vn",
            "-c:a", "libopus",
            "-b:a", "24k",
            "-ar", "16000",
            "-ac", "1",
            audio_path
        ], check=True, capture_output=True)
        
        with open(processed_video_path, "rb") as f:
            video_b64 = base64.b64encode(f.read()).decode("utf-8")
        
        with open(audio_path, "rb") as f:
            audio_b64 = base64.b64encode(f.read()).decode("utf-8")
        
        return video_b64, audio_b64
    
    finally:
        os.unlink(processed_video_path)
        os.unlink(audio_path)
```

<Tip>
  Preprocessing is highly recommended to reduce latency and ensure consistent performance.
</Tip>

## Performance considerations

**Tips for optimal throughput:**

* **Preprocess all videos** – 1 FPS at 360p provides good quality with minimal tokens
* **Extract audio separately** – Opus/Ogg at 24kbps offers excellent compression
* **Limit video duration** – Start with 60 seconds or less for consistent performance
* **Choose the appropriate serving path** – Use GLM 5.3 Flash on Serverless, or scale replicas for models that require dedicated deployments

## Known limitations

1. **Video duration**: 60 seconds is a performance recommendation for the preprocessing example, not a universal API limit.
2. **Supported formats**: The examples use `.mp4` for video and `.ogg` (Opus) for audio.
3. **Base64 size**: Keep the total encoded payload for the dedicated example under 10MB.
4. **Video URLs**: The URL must be reachable by Fireworks and return the media file directly without custom authorization headers.
5. **Availability**: GLM 5.3 Flash supports Serverless video input. Qwen3 Omni and Molmo2 require dedicated deployments.
6. **Audio support**: Only use `audio_url` with models whose input support explicitly includes audio.

## Related resources

<CardGroup>
  <Card title="Chat with Video using Qwen3 Omni" href="https://colab.research.google.com/github/fw-ai/cookbook/blob/main/archived/multimedia/video/Qwen3-Omni-Chat-With-Video-Cookbook.ipynb" icon="video">
    Interactive notebook for video and audio analysis
  </Card>

  <Card title="Vision models" href="/guides/querying-vision-language-models" icon="image">
    Query models with image inputs
  </Card>

  <Card title="Dedicated deployments" href="/getting-started/ondemand-quickstart" icon="server">
    Deploy models on dedicated GPUs
  </Card>
</CardGroup>
