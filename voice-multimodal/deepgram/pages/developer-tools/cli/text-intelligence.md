---
title: "Text Intelligence Commands"
source: https://developers.deepgram.com/developer-tools/cli/text-intelligence.md
path: developer-tools/cli/text-intelligence
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Text Intelligence Commands

## Basic Analysis

```shell
dg read document.txt
```

## Analyze a URL

```shell
dg read https://example.com/article.txt
```

## Piped Input

```shell
cat transcript.txt | dg read
echo "Your text here" | dg read
```

## Available Features

### Sentiment Analysis

```shell
dg read document.txt --sentiment
```

Output includes sentiment per sentence and overall document sentiment.

### Topic Detection

```shell
dg read document.txt --topics
```

Returns detected topics with confidence scores.

### Summarization

```shell
dg read document.txt --summarize
```

Generates a brief summary of the content.

### Intent Recognition

```shell
dg read document.txt --intents
```

Detects user intents within the text.

### Full Analysis

```shell
dg read document.txt --sentiment --topics --summarize --intents
```

## Output Format

```shell
dg -o json read document.txt    # JSON
dg -o yaml read document.txt    # YAML
dg -o table read document.txt   # ASCII table
dg -o csv read document.txt     # CSV
```

`-o` belongs to `dg` itself, so it goes before the subcommand name. Without it, `dg read` prints human-readable output.

## Use Cases

### Summarize Transcripts

```shell
dg listen meeting.mp3 | dg read --summarize
```

### Analyze Customer Feedback

```shell
dg read feedback.txt --sentiment --topics
```
