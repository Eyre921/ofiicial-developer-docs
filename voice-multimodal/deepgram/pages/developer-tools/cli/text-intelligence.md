---
title: "Text Intelligence commands"
source: https://developers.deepgram.com/developer-tools/cli/text-intelligence.md
path: developer-tools/cli/text-intelligence
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Text Intelligence commands

## Basic analysis

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

## Available features

### Sentiment analysis

```shell
dg read --file document.txt --sentiment
```

Output includes overall document sentiment and its score.

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
dg -o json read --file document.txt    # JSON
dg -o yaml read --file document.txt    # YAML
dg -o table read --file document.txt   # Formatted terminal table
dg -o csv read --file document.txt     # CSV
```

`-o` belongs to `dg` itself, so it goes before the subcommand name. Without it, `dg read` prints human-readable output.

## Use cases

### Summarize transcripts

```shell
dg listen meeting.mp3 | dg read --summarize
```

### Analyze customer feedback

```shell
dg read --file feedback.txt --sentiment --topics
```
