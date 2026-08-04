---
title: "Side-by-side demo"
source: https://docs.fireworks.ai/ecosystem/fireconnect/demo
path: ecosystem/fireconnect/demo
---

Race Claude Code on Anthropic against Fireworks on the same prompt with fireconnect demo

Not ready to rewire your whole setup? **`fireconnect demo`** runs the same code-generation prompt through both sides: your current Claude Code provider on Anthropic, and a Fireworks model on the challenger side. It then puts the results next to each other so you can judge speed, cost, and output quality yourself.

The demo is read-only against your environment. It uses throwaway config dirs, so your `~/.claude/settings.json` is never touched.

## What you get

1. **Live terminal race**: both models stream code in a split-pane TUI with real token counts and wall-clock timers.
2. **Browser comparison**: both generated apps run side by side, with measured speed and cost at the bottom.
3. **Shareable artifacts**: outputs land in `./fireconnect-demo/` (`compare.html`, `result.json`, stream logs).

### Browser comparison

Side-by-side runnable apps with measured speed and cost:

<Frame>
  <img alt="FireConnect demo browser comparison page with Tetris apps from Anthropic and Fireworks side by side and speed and cost metrics" />
</Frame>

### Terminal race

Split-pane TUI while both models stream the same prompt:

<Frame>
  <img alt="Animated capture of a real FireConnect demo split-pane terminal race: Anthropic Claude Sonnet vs Fireworks GLM 5.2 Fast on a Tetris prompt" />
</Frame>

## Prerequisites

* FireConnect installed ([overview](/ecosystem/fireconnect/overview#install))
* [Claude Code](https://claude.ai/code) CLI (`claude`) on your `PATH`
* An **Anthropic API key** for the incumbent side (`ANTHROPIC_API_KEY`, or pass `--anthropic-key`)
* A **Fireworks API key** for the challenger side (`fireconnect login` or `FIREWORKS_API_KEY`)

<Tip>
  Run `fireconnect login` first so the Fireworks side resolves your key automatically. The demo only supports **Claude Code** today.
</Tip>

## Run the demo

```bash theme={null}
fireconnect demo
```

That runs the default **Tetris** preset: both sides get the same prompt to build a playable game in a single HTML file.

### Try other presets

```bash theme={null}
fireconnect demo --prompt snake
fireconnect demo --prompt tictactoe
fireconnect demo --prompt clock
```

Presets: `tetris` (default), `snake`, `tictactoe`, `clock`, or `custom` with your own task text.

### Pick the Fireworks model

```bash theme={null}
fireconnect demo --challenger glm-5p2-fast
```

Default challenger is `glm-5p2-fast`. Pass any serverless ID from [Models](/ecosystem/fireconnect/models) (same IDs as `fireconnect claude on --model`).

### Non-interactive / CI-friendly

```bash theme={null}
fireconnect demo --yes --no-open --json
```

| Flag                        | What it does                                              |
| --------------------------- | --------------------------------------------------------- |
| `--yes`                     | Skip the setup form                                       |
| `--no-open`                 | Do not open a browser; write outputs to disk only         |
| `--json`                    | Print a machine-readable result to stdout (skips the TUI) |
| `--out <dir>`               | Output directory (default: `./fireconnect-demo/`)         |
| `--anthropic-model <alias>` | Incumbent model: `opus` (default), `sonnet`, or `haiku`   |
| `--anthropic-key <key>`     | Anthropic API key for the incumbent side                  |
| `--api-key <key>`           | Fireworks API key for the challenger side                 |

## Clean up

```bash theme={null}
fireconnect demo clean          # prompts before deleting ./fireconnect-demo/
fireconnect demo clean --yes    # delete without prompting
fireconnect demo clean --out /path/to/output
```

`demo clean` only removes directories that contain demo markers (`result.json`, `compare.html`, etc.), so it will not delete an unrelated folder you pointed `--out` at by mistake.

## After the demo

Liked what you saw on the Fireworks side? Wire it into your daily driver:

```bash theme={null}
fireconnect claude on --model glm-5p2-fast
```

More IDs and latest vs fast guidance: [Models](/ecosystem/fireconnect/models).

Want automatic cost routing instead of a fixed model? Try [FireRouter](/ecosystem/firerouter/overview):

```bash theme={null}
fireconnect claude on --model firerouter
```

## How it works

* Each side runs real `claude -p` in an isolated temporary config directory.
* Numbers in the comparison strip are **measured from the run**, not list-price estimates.
* If one side fails to finish, the page says so instead of fabricating a winner.
* Open `compare.html` from the output folder anytime. It inlines both apps and works offline.

## Source

The demo ships with FireConnect: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)

## See also

* [FireConnect overview](/ecosystem/fireconnect/overview)
* [Models](/ecosystem/fireconnect/models)
* [CLI reference](/ecosystem/fireconnect/cli-reference)
