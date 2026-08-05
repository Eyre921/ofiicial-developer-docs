---
title: "Build an open source NotebookLM"
source: https://docs.together.ai/docs/open-notebooklm-pdf-to-podcast
path: docs/open-notebooklm-pdf-to-podcast
---

Build an open source NotebookLM that turns a PDF into a podcast.

Inspired by [NotebookLM's podcast generation](https://notebooklm.google/) feature and a recent open source implementation of [Open Notebook LM](https://github.com/gabrielchua/open-notebooklm). In this guide we will implement a walkthrough of how you can build a PDF to podcast pipeline.

Given any PDF we will generate a conversation between a host and a guest discussing and explaining the contents of the PDF.

In doing so we will learn the following:

1. How we can use JSON mode and structured generation with open models like Llama 3 70b to extract a script for the Podcast given text from the PDF.
2. How we can use TTS models to bring this script to life as a conversation.

## Define dialogue schema with Pydantic

We need a way of telling the LLM what the structure of the podcast script between the guest and host will look like. We will do this using `pydantic` models.

Below we define the required classes:

* The overall conversation consists of lines said by either the host or the guest. The `DialogueItem` class specifies the structure of these lines.
* The full script is a combination of multiple lines performed by the speakers, here we also include a `scratchpad` field to allow the LLM to ideate and brainstorm the overall flow of the script prior to actually generating the lines. The `Dialogue` class specifies this.

```py Python theme={null}
from pydantic import BaseModel
from typing import List, Literal, Tuple, Optional


class LineItem(BaseModel):
    """A single line in the script."""

    speaker: Literal["Host (Jane)", "Guest"]
    text: str


class Script(BaseModel):
    """The script between the host and guest."""

    scratchpad: str
    name_of_guest: str
    script: List[LineItem]
```

The inclusion of a scratchpad field is very important - it allows the LLM compute and tokens to generate an unstructured overview of the script prior to generating a structured line by line enactment.

## System prompt for script generation

Next we need to define a detailed prompt template engineered to guide the LLM through the generation of the script. Feel free to modify and update the prompt below.

```py Python theme={null}
# Adapted and modified from https://github.com/gabrielchua/open-notebooklm
SYSTEM_PROMPT = """
You are a world-class podcast producer tasked with transforming the provided input text into an engaging and informative podcast script. The input may be unstructured or messy, sourced from PDFs or web pages. Your goal is to extract the most interesting and insightful content for a compelling podcast discussion.

# Steps to Follow:

1. **Analyze the Input:**
   Carefully examine the text, identifying key topics, points, and interesting facts or anecdotes that could drive an engaging podcast conversation. Disregard irrelevant information or formatting issues.

2. **Brainstorm Ideas:**
   In the `<scratchpad>`, creatively brainstorm ways to present the key points engagingly. Consider:
   - Analogies, storytelling techniques, or hypothetical scenarios to make content relatable
   - Ways to make complex topics accessible to a general audience
   - Thought-provoking questions to explore during the podcast
   - Creative approaches to fill any gaps in the information

3. **Craft the Dialogue:**
   Develop a natural, conversational flow between the host (Jane) and the guest speaker (the author or an expert on the topic). Incorporate:
   - The best ideas from your brainstorming session
   - Clear explanations of complex topics
   - An engaging and lively tone to captivate listeners
   - A balance of information and entertainment

   Rules for the dialogue:
   - The host (Jane) always initiates the conversation and interviews the guest
   - Include thoughtful questions from the host to guide the discussion
   - Incorporate natural speech patterns, including occasional verbal fillers (e.g., "Uhh", "Hmmm", "um," "well," "you know")
   - Allow for natural interruptions and back-and-forth between host and guest - this is very important to make the conversation feel authentic
   - Ensure the guest's responses are substantiated by the input text, avoiding unsupported claims
   - Maintain a PG-rated conversation appropriate for all audiences
   - Avoid any marketing or self-promotional content from the guest
   - The host concludes the conversation

4. **Summarize Key Insights:**
   Naturally weave a summary of key points into the closing part of the dialogue. This should feel like a casual conversation rather than a formal recap, reinforcing the main takeaways before signing off.

5. **Maintain Authenticity:**
   Throughout the script, strive for authenticity in the conversation. Include:
   - Moments of genuine curiosity or surprise from the host
   - Instances where the guest might briefly struggle to articulate a complex idea
   - Light-hearted moments or humor when appropriate
   - Brief personal anecdotes or examples that relate to the topic (within the bounds of the input text)

6. **Consider Pacing and Structure:**
   Ensure the dialogue has a natural ebb and flow:
   - Start with a strong hook to grab the listener's attention
   - Gradually build complexity as the conversation progresses
   - Include brief "breather" moments for listeners to absorb complex information
   - For complicated concepts, reasking similar questions framed from a different perspective is recommended
   - End on a high note, perhaps with a thought-provoking question or a call-to-action for listeners

IMPORTANT RULE: Each line of dialogue should be no more than 100 characters (e.g., can finish within 5-8 seconds)

Remember: Always reply in valid JSON format, without code blocks. Begin directly with the JSON output.
"""
```

## Download PDF and extract contents

Here we will load in an academic paper that proposes the use of many open source language models in a collaborative manner together to outperform proprietary models that are much larger!

We will use the text in the PDF as content to generate the podcast with!

<Frame>
  <img alt="" />
</Frame>

Download the PDF file and then extract text contents using the function below.

```bash Shell theme={null}
!wget https://arxiv.org/pdf/2406.04692
!mv 2406.04692 MoA.pdf
```

```py Python theme={null}
from pypdf import PdfReader


def get_PDF_text(file: str):
    text = ""

    # Read the PDF file and extract text
    try:
        with Path(file).open("rb") as f:
            reader = PdfReader(f)
            text = "\n\n".join([page.extract_text() for page in reader.pages])
    except Exception as e:
        raise f"Error reading the PDF file: {str(e)}"

        # Check if the PDF has more than ~400,000 characters
        # The context length limit of the model is 131,072 tokens and thus the text should be less than this limit
        # Assumes that 1 token is approximately 4 characters
    if len(text) > 400000:
        raise "The PDF is too long. Please upload a PDF with fewer than ~131072 tokens."

    return text


text = get_PDF_text("MoA.pdf")
```

## Generate podcast script using JSON mode

Below we call Llama3.1 70B with JSON mode to generate a script for our podcast. JSON mode makes it so that the LLM will only generate responses in the format specified by the `Script` class. We will also be able to read its scratchpad and see how it structured the overall conversation.

```py Python theme={null}
from together import Together
from pydantic import ValidationError

client_together = Together(api_key="TOGETHER_API_KEY")


def call_llm(system_prompt: str, text: str, dialogue_format):
    """Call the LLM with the given prompt and dialogue format."""
    response = client_together.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text},
        ],
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "script",
                "schema": dialogue_format.model_json_schema(),
            },
        },
    )
    return response


def generate_script(system_prompt: str, input_text: str, output_model):
    """Get the script from the LLM."""
    # Load as python object
    try:
        response = call_llm(system_prompt, input_text, output_model)
        dialogue = output_model.model_validate_json(
            response.choices[0].message.content
        )
    except ValidationError as e:
        error_message = f"Failed to parse dialogue JSON: {e}"
        system_prompt_with_error = f"{system_prompt}\n\nPlease return a VALID JSON object. This was the earlier error: {error_message}"
        response = call_llm(system_prompt_with_error, input_text, output_model)
        dialogue = output_model.model_validate_json(
            response.choices[0].message.content
        )
    return dialogue


# Generate the podcast script

script = generate_script(SYSTEM_PROMPT, text, Script)
```

Above we are also handling the erroneous case which will let us know if the script was not generated following the `Script` class.

Now we can have a look at the script that is generated:

```
[DialogueItem(speaker='Host (Jane)', text='Welcome to today’s podcast. I’m your host, Jane. Joining me is Junlin Wang, a researcher from Duke University and Together AI. Junlin, welcome to the show!'),
 DialogueItem(speaker='Guest', text='Thanks for having me, Jane. I’m excited to be here.'),
 DialogueItem(speaker='Host (Jane)', text='Junlin, your recent paper proposes a new approach to enhancing large language models (LLMs) by leveraging the collective strengths of multiple models. Can you tell us more about this?'),
 DialogueItem(speaker='Guest', text='Our approach is called Mixture-of-Agents (MoA). We found that LLMs exhibit a phenomenon we call collaborativeness, where they generate better responses when presented with outputs from other models, even if those outputs are of lower quality.'),
 DialogueItem(speaker='Host (Jane)', text='That’s fascinating. Can you walk us through how MoA works?'),
 DialogueItem(speaker='Guest', text='MoA consists of multiple layers, each comprising multiple LLM agents. Each agent takes all the outputs from agents in the previous layer as auxiliary information in generating its response. This process is repeated for several cycles until a more robust and comprehensive response is obtained.'),
 DialogueItem(speaker='Host (Jane)', text='I see. And what kind of results have you seen with MoA?'),
 DialogueItem(speaker='Guest', text='We evaluated MoA on several benchmarks, including AlpacaEval 2.0, MT-Bench, and FLASK. Our results show substantial improvements in response quality, with MoA achieving state-of-the-art performance on these benchmarks.'),
 DialogueItem(speaker='Host (Jane)', text='Wow, that’s impressive. What about the cost-effectiveness of MoA?'),
 DialogueItem(speaker='Guest', text='We found that MoA can deliver performance comparable to GPT-4 Turbo while being 2x more cost-effective. This is because MoA can leverage the strengths of multiple models, reducing the need for expensive and computationally intensive training.'),
 DialogueItem(speaker='Host (Jane)', text='That’s great to hear. Junlin, what do you think is the potential impact of MoA on the field of natural language processing?'),
 DialogueItem(speaker='Guest', text='I believe MoA has the potential to significantly enhance the effectiveness of LLM-driven chat assistants, making AI more accessible to a wider range of people. Additionally, MoA can improve the interpretability of models, facilitating better alignment with human reasoning.'),
 DialogueItem(speaker='Host (Jane)', text='That’s a great point. Junlin, thank you for sharing your insights with us today.'),
 DialogueItem(speaker='Guest', text='Thanks for having me, Jane. It was a pleasure discussing MoA with you.')]
```

## Generate podcast using TTS

Below we read through the script and choose the TTS voice depending on the speaker. We define a speaker and guest voice id.

```py Python theme={null}
import subprocess
import ffmpeg
from cartesia import Cartesia

client_cartesia = Cartesia(api_key="CARTESIA_API_KEY")

host_id = "694f9389-aac1-45b6-b726-9d9369183238"  # Jane - host voice
guest_id = "a0e99841-438c-4a64-b679-ae501e7d6091"  # Guest voice

model_id = "sonic-english"  # The Sonic Cartesia model for English TTS

output_format = {
    "container": "raw",
    "encoding": "pcm_f32le",
    "sample_rate": 44100,
}

# Set up a WebSocket connection.
ws = client_cartesia.tts.websocket()
```

We can loop through the lines in the script and generate them by a call to the TTS model with specific voice and lines configurations. The lines all appended to the same buffer and once the script finishes we write this out to a wav file, ready to be played.

```py Python theme={null}
# Open a file to write the raw PCM audio bytes to.
f = open("podcast.pcm", "wb")

# Generate and stream audio.
for line in script.dialogue:
    if line.speaker == "Guest":
        voice_id = guest_id
    else:
        voice_id = host_id

    for output in ws.send(
        model_id=model_id,
        transcript="-"
        + line.text,  # the "-"" is to add a pause between speakers
        voice_id=voice_id,
        stream=True,
        output_format=output_format,
    ):
        buffer = output["audio"]  # buffer contains raw PCM audio bytes
        f.write(buffer)

# Close the connection to release resources
ws.close()
f.close()

# Convert the raw PCM bytes to a WAV file.
ffmpeg.input("podcast.pcm", format="f32le").output("podcast.wav").run()

# Play the file
subprocess.run(["ffplay", "-autoexit", "-nodisp", "podcast.wav"])
```

Once this code executes you will have a `podcast.wav` file saved on disk that can be played!

If you're ready to create your own PDF to podcast app like above [sign up for Together AI today](https://www.together.ai/) and make your first query in minutes!
