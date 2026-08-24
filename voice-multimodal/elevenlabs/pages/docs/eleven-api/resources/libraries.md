---
title: "Libraries & SDKs"
source: https://elevenlabs.io/docs/eleven-api/resources/libraries.md
path: docs/eleven-api/resources/libraries
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Libraries & SDKs

## Official REST API libraries

ElevenLabs provides officially supported libraries that are updated with the latest features available in the [REST API](/docs/api-reference/introduction).

| Language          | GitHub                                                           | Package Manager                                                |
| ----------------- | ---------------------------------------------------------------- | -------------------------------------------------------------- |
| Python            | [GitHub README](https://github.com/elevenlabs/elevenlabs-python) | [PyPI](https://pypi.org/project/elevenlabs/)                   |
| Javascript (Node) | [GitHub README](https://github.com/elevenlabs/elevenlabs-js)     | [npm](https://www.npmjs.com/package/@elevenlabs/elevenlabs-js) |

## Command-line interface

The [ElevenLabs CLI](/docs/eleven-agents/operate/cli) brings the REST API to your terminal. Homebrew (macOS) and Scoop (Windows) are the recommended install methods.

```bash title="Homebrew (macOS)"
brew install elevenlabs/tap/elevenlabs
```

```powershell title="Scoop (Windows)"
scoop bucket add elevenlabs https://github.com/elevenlabs/scoop-bucket
scoop install elevenlabs
```

```bash title="curl"
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/elevenlabs/cli/releases/latest/download/elevenlabs-cli-installer.sh | sh
```

Working with an AI coding assistant? Run `elevenlabs generate-skills` in your project to write a
`SKILL.md` for every command group into `skills/`, so your assistant knows the CLI's full surface
without you pasting docs. Use `--output-dir` to put them elsewhere. This reads the CLI's own
embedded API definition, so it needs no API key and works offline — and it stays in step with
whichever CLI version you have installed.

Then authenticate — this opens your browser to authorize the CLI:

```bash
elevenlabs auth login
```

## Official Agents Platform libraries

These libraries are designed for use with ElevenLabs [Agents Platform](/docs/eleven-agents/overview).

| Language     | Documentation                                            | Package Manager                                                                 |
| ------------ | -------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Javascript   | [Docs](/docs/eleven-agents/libraries/java-script)        | [npm](https://www.npmjs.com/package/@elevenlabs/client)                         |
| React        | [Docs](/docs/eleven-agents/libraries/react)              | [npm](https://www.npmjs.com/package/@elevenlabs/react)                          |
| React Native | [Docs](/docs/eleven-agents/libraries/react-native)       | [npm](https://www.npmjs.com/package/@elevenlabs/react-native)                   |
| Python       | [Docs](/docs/eleven-agents/libraries/python)             | [PyPI](https://pypi.org/project/elevenlabs/)                                    |
| Swift        | [Docs](/docs/eleven-agents/libraries/swift)              | [Github](https://github.com/elevenlabs/ElevenLabsSwift)                         |
| Kotlin       | [Docs](/docs/eleven-agents/libraries/kotlin)             | [Maven](https://central.sonatype.com/artifact/io.elevenlabs/elevenlabs-android) |
| Flutter      | [Docs](https://github.com/elevenlabs/elevenlabs-flutter) | [Pub](https://pub.dev/packages/elevenlabs_agents)                               |

## Third-party libraries

These libraries are not officially supported by ElevenLabs, but are community-maintained.

| Library       | Documentation                                                             | Package Manager                                              |
| ------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Vercel AI SDK | [Docs](/docs/eleven-api/guides/how-to/speech-to-text/batch/vercel-ai-sdk) | [npm](https://www.npmjs.com/package/ai)                      |
| .NET          | [Docs](https://github.com/RageAgainstThePixel/ElevenLabs-DotNet)          | [NuGet](https://www.nuget.org/packages/ElevenLabs-DotNet)    |
| Unity         | [Docs](https://github.com/RageAgainstThePixel/com.rest.elevenlabs)        | [OpenUPM](https://openupm.com/packages/com.rest.elevenlabs/) |
