---
title: "Understanding Word Confidence Scores"
source: https://developers.deepgram.com/docs/confidence.md
path: docs/confidence
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Understanding Word Confidence Scores

Every word in Deepgram's transcription response includes a `confidence` value — a floating point between 0 and 1 representing the model's estimated probability that the word was transcribed correctly. This per-word score appears in the `words` array within each `alternatives` object and is distinct from the transcript-level `confidence` field, which represents overall transcript reliability.

## What Confidence Means

Deepgram's word confidence is a **calibrated probability**. A confidence of 0.93 means the model estimates a 93% chance the word is correct.

"Calibrated" means the scores are statistically honest: if you took all words the model scored at 0.93, approximately 93% of them would actually be correct. The model's probability outputs are naturally well-calibrated.

Confidence score definitions and calibration vary across STT providers. You cannot directly compare raw confidence distributions between providers. A provider whose scores are spread evenly across 0–1 is not necessarily providing "more informative" scores — they may simply be poorly calibrated, meaning their stated confidence does not match actual accuracy.

## Why Most Scores Are High

On typical audio, most words will have confidence scores above 0.90. This is expected and correct behavior — it reflects the model accurately predicting that it got most words right.

For example, if Deepgram achieves 95% word accuracy on your audio, you should expect the average confidence to be around 0.95, with most words clustering near 1.0. The roughly 5% of words the model is less sure about will have lower scores.

A flat or uniform distribution of confidence scores across 0–1 would actually indicate **poor calibration** — it would mean the model is equally uncertain about every word, which does not reflect reality for a high-accuracy model.

The concentration of scores near 1.0 does not mean the scores lack discriminatory power. Words with lower scores are meaningfully more likely to be errors. The signal is in the tail of the distribution, not the center.

## Using Confidence for Error Detection

### Fixed Threshold

The simplest approach: choose a confidence cutoff and flag all words below it as potential errors.

With Deepgram's well-calibrated scores, a threshold around 0.65 works well as an error detector — words below this threshold are very likely to be genuine errors (high precision). The tradeoff: a low threshold catches only the most obvious errors. Raising it catches more errors but also flags some correct words.

Evaluate precision and recall at multiple thresholds on a sample of your own data to find the right balance for your use case.

```python Python
# Flag words below a confidence threshold
threshold = 0.65
low_confidence_words = [
    word for word in response["results"]["channels"][0]["alternatives"][0]["words"]
    if word["confidence"] < threshold
]

for word in low_confidence_words:
    print(f"  '{word['word']}' (confidence: {word['confidence']:.3f}, "
          f"time: {word['start']:.2f}s - {word['end']:.2f}s)")
```

```java Java
// Flag words below a confidence threshold
double threshold = 0.65;
List<Word> words = response.getResults().getChannels().get(0)
    .getAlternatives().get(0).getWords();

for (Word word : words) {
    if (word.getConfidence() < threshold) {
        System.out.printf("  '%s' (confidence: %.3f, time: %.2fs - %.2fs)%n",
            word.getWord(), word.getConfidence(),
            word.getStart(), word.getEnd());
    }
}
```

### Dynamic Threshold

Adapt the threshold automatically based on audio difficulty:

1. Compute the mean confidence across all words in a transcript.
2. Estimate expected error count: `errors ≈ (1 - mean_confidence) × total_words`.
3. Sort words by confidence (ascending) and flag that many words as potential errors.

Noisy audio produces lower mean confidence, which shifts the threshold accordingly.

```python Python
import statistics

words = response["results"]["channels"][0]["alternatives"][0]["words"]
confidences = [w["confidence"] for w in words]

mean_conf = statistics.mean(confidences)
expected_errors = int((1 - mean_conf) * len(words))

# Flag the N lowest-confidence words as potential errors
sorted_words = sorted(words, key=lambda w: w["confidence"])
flagged = sorted_words[:expected_errors]

print(f"Mean confidence: {mean_conf:.3f}")
print(f"Expected errors: {expected_errors} out of {len(words)} words")
for word in flagged:
    print(f"  '{word['word']}' (confidence: {word['confidence']:.3f})")
```

```java Java
import java.util.Comparator;
import java.util.List;

List<Word> words = response.getResults().getChannels().get(0)
    .getAlternatives().get(0).getWords();

double meanConf = words.stream()
    .mapToDouble(Word::getConfidence)
    .average()
    .orElse(0.0);
int expectedErrors = (int) ((1 - meanConf) * words.size());

// Flag the N lowest-confidence words as potential errors
List<Word> flagged = words.stream()
    .sorted(Comparator.comparingDouble(Word::getConfidence))
    .limit(expectedErrors)
    .toList();

System.out.printf("Mean confidence: %.3f%n", meanConf);
System.out.printf("Expected errors: %d out of %d words%n", expectedErrors, words.size());
for (Word word : flagged) {
    System.out.printf("  '%s' (confidence: %.3f)%n",
        word.getWord(), word.getConfidence());
}
```

## Common Use Cases

### QA and Compliance Review

Flag utterances where any word drops below a threshold for human review. Useful for call centers, legal transcription, and medical documentation where accuracy is critical.

### Entity Validation

Cross-check confidence on detected entities (names, numbers, addresses). Low confidence on an entity word is a stronger signal to escalate than low confidence on a filler word like "um" or "the."

### Transcript Quality Scoring

Use mean word confidence across a full transcript as a quality proxy. Automatically escalate low-quality transcripts to human review and accept high-quality ones without intervention.

### Streaming Confidence Monitoring

In real-time applications, track confidence trends across a stream. A sustained drop in confidence may indicate audio quality degradation (background noise, connection issues) that warrants alerting.

## Confidence in Streaming vs. Pre-recorded

In streaming mode with `interim_results=true`, interim transcripts may show lower confidence on words near the audio boundary (the "tip" of the stream). The model has less surrounding context for these words, so its predictions are less certain.

As more audio arrives, interim confidence values typically improve. Final transcripts (`is_final: true`) will have higher and more reliable confidence scores.

Use confidence values from final transcripts for any downstream decision-making. Use interim confidence only for low-latency display purposes where you expect corrections. See [Interim Results](/docs/interim-results) for details on how interim and final transcripts work.

## Limitations

* **No alternatives**: Confidence tells you how sure the model is about its top prediction, but does not surface the model's second-best guess. You cannot use it to get suggested corrections.
* **Not a WER guarantee**: High average confidence does not guarantee low word error rate on any specific transcript. It is a statistical property across many predictions.
* **Model mismatch**: If you use the wrong language model or the audio contains heavy accents not well-represented in training data, the model can be confidently wrong. Confidence reflects the model's internal estimate, which is only as good as the model's fit to the audio domain.
* **Cross-provider comparison**: Do not compare raw confidence score distributions between STT providers. Different providers may use different calibration methods, temperature scaling, or definitions of "confidence." A meaningful comparison requires evaluating precision and recall of error detection at various thresholds on the same evaluation dataset.

## API Reference

Word confidence appears in the `words` array within each `alternatives` object in the API response:

```json JSON
{
  "results": {
    "channels": [
      {
        "alternatives": [
          {
            "transcript": "the quick brown fox",
            "confidence": 0.9876,
            "words": [
              {
                "word": "the",
                "start": 0.08,
                "end": 0.32,
                "confidence": 0.998,
                "punctuated_word": "The"
              },
              {
                "word": "quick",
                "start": 0.32,
                "end": 0.64,
                "confidence": 0.965,
                "punctuated_word": "quick"
              },
              {
                "word": "brown",
                "start": 0.64,
                "end": 0.88,
                "confidence": 0.991,
                "punctuated_word": "brown"
              },
              {
                "word": "fox",
                "start": 0.88,
                "end": 1.12,
                "confidence": 0.943,
                "punctuated_word": "fox"
              }
            ]
          }
        ]
      }
    ]
  }
}
```

There are two distinct confidence fields in the response:

* **Transcript-level `confidence`** (in `alternatives`): Overall reliability of the full transcript.
* **Word-level `confidence`** (in each `words` entry): Per-word probability of correctness.

For Nova-3 streaming results, the transcript-level `confidence` value in `alternatives` is calculated as the **median** of the word-level confidence scores for all words in that chunk's final transcript. This means the transcript-level score is robust to individual outlier words — a single low-confidence word will not significantly affect the overall score, but a pattern of low-confidence words will pull it down.

If you threshold on transcript-level confidence for routing decisions (for example, escalating to human review), be aware that a transcript with one very low-confidence entity word might still pass a high transcript-level threshold because the median is unaffected by a single outlier. Supplement with word-level checks on critical entities.

## Related Resources

* [Interim Results](/docs/interim-results) — How interim and final transcripts work in streaming.
* [Utterances](/docs/utterances) — Segment speech into meaningful semantic units.
* [Pre-recorded Audio Getting Started](/docs/pre-recorded-audio) — Transcribe audio files with Deepgram.
* [Streaming Audio Getting Started](/docs/live-streaming-audio) — Real-time transcription with WebSockets.
