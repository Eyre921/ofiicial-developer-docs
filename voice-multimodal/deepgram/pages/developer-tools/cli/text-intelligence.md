---
title: "Text Intelligence commands"
source: https://developers.deepgram.com/developer-tools/cli/text-intelligence.md
path: developer-tools/cli/text-intelligence
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Text Intelligence commands

> Deepgram CLI Text Intelligence: analyze text for sentiment, topics, summaries, and intents with dg read.

## Basic analysis

With no feature flag, `dg read` runs all four analyses: summary, sentiment, topics, and intents.

```shell
dg read "Customer called about a billing issue."
```

## Analyze a file

```shell
dg read --file document.txt
```

## Piped input

```shell
cat transcript.txt | dg read
echo "Your text here" | dg read
```

## Language

`-l` (`--language`) sets the text's language; it defaults to `en`.

```shell
dg read --file document.txt --language en
```

## Available features

### Sentiment analysis

```shell
dg read --file document.txt --sentiment
```

Returns overall document sentiment and its score.

### Topic detection

```shell
dg read --file document.txt --topics
```

Returns detected topics with confidence scores.

### Summarization

```shell
dg read --file document.txt --summarize
```

Generates a brief summary of the content.

### Intent recognition

```shell
dg read --file document.txt --intents
```

Detects user intents within the text.

### Full analysis

```shell
dg read --file document.txt --sentiment --topics --summarize --intents
```

## Output format

```shell
# JSON
dg -o json read --file document.txt
# YAML
dg -o yaml read --file document.txt
# Formatted terminal table
dg -o table read --file document.txt
# CSV
dg -o csv read --file document.txt
```

Without `-o`, `dg read` prints human-readable output. `-o` works before the subcommand (`dg -o json read ...`) or after it on most commands (`dg read ... -o json`). On `dg speak`, `-o`/`--output` after the subcommand still sets the output file path but is deprecated; use `--out-file` instead. On `dg plugin` and `dg skills` subcommands, put `-o` before the subcommand.

## Use cases

### Summarize transcripts

Pipe the transcript text, extracted from the JSON payload, into `dg read`:

```shell
dg -o json listen meeting.mp3 2>/dev/null | jq -r '.results.channels[0].alternatives[0].transcript' | dg read --summarize
```

### Analyze customer feedback

```shell
dg read --file feedback.txt --sentiment --topics
```
