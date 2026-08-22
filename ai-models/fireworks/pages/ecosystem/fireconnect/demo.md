---
title: "Side-by-side demo"
source: https://docs.fireworks.ai/ecosystem/fireconnect/demo
path: ecosystem/fireconnect/demo
---

Race two models through Claude Code on the same prompt with fireconnect claude demo

**`fireconnect claude demo`** runs the same code-generation prompt through two models using your current FireConnect Claude profile. It then puts the results next to each other so you can judge speed, cost, and output quality yourself.

The demo reads your active FireConnect Claude profile but does not modify `~/.claude/settings.json`. Each side runs in a separate temporary working directory.

## What you get

1. **Live terminal race**: both models stream code in a split-pane TUI with real token counts and wall-clock timers.
2. **Browser comparison**: both generated apps run side by side, with measured speed and cost at the bottom.
3. **Shareable artifacts**: outputs land in `./fireconnect-demo/` (`compare.html`, `result.json`, stream logs).

### Browser comparison

Side-by-side runnable apps with measured speed and cost:

<Frame>
  <img alt="FireConnect demo browser comparison page with two Tetris apps side by side and speed and cost metrics" />
</Frame>

### Terminal race

Split-pane TUI while both models stream the same prompt:

<Frame>
  <img alt="Animated capture of a FireConnect split-pane terminal race between Claude Sonnet and GLM 5.2 Fast on a Tetris prompt" />
</Frame>

## Prerequisites

* FireConnect installed ([overview](/ecosystem/fireconnect/overview#install))
* [Claude Code](https://claude.ai/code) CLI (`claude`) on your `PATH`
* Claude Code already connected with `fireconnect claude`

<Tip>
  Both sides use the same authentication and routing as your existing FireConnect Claude setup. The demo only supports **Claude Code** today.
</Tip>

## Run the demo

```bash theme={null}
fireconnect claude demo
```

That runs the default **Tetris** preset: both sides get the same prompt to build a playable game in a single HTML file.

<Note>
  The old top-level `fireconnect demo` form is deprecated. Use `fireconnect claude demo`.
</Note>

### Try other presets

```bash theme={null}
fireconnect claude demo --prompt snake
fireconnect claude demo --prompt clock
fireconnect claude demo --prompt "Build a todo app in one HTML file"
fireconnect claude demo --prompt-file ./task.txt
```

Presets: `tetris` (default), `snake`, or `clock`. You can also pass custom task text or use `--prompt-file`.

### Pick the models

```bash theme={null}
fireconnect claude demo --left-model opus --right-model glm-fast-latest
```

The defaults are `opus` on the left and `glm-fast-latest` on the right. Pass any available model or Claude alias from your connected profile.

### Non-interactive / CI-friendly

```bash theme={null}
fireconnect claude demo --yes --no-open --json
```

| Flag                        | What it does                                                           |
| --------------------------- | ---------------------------------------------------------------------- |
| `--yes`                     | Skip the setup form                                                    |
| `--no-open`                 | Do not open a browser; write outputs to disk only                      |
| `--json`                    | Print a machine-readable result to stdout (skips the TUI)              |
| `--out <dir>`               | Output directory (default: `./fireconnect-demo/`)                      |
| `--prompt-file <path>`      | Read a custom task from a file (overrides the preset)                  |
| `--left-model <model>`      | Left model (default: `opus`)                                           |
| `--right-model <model>`     | Right model (default: `glm-fast-latest`)                               |
| `--challenger <model>`      | Alias for `--right-model`                                              |
| `--anthropic-model <alias>` | Alias for `--left-model` (`opus`, `sonnet`, `haiku`, or `fable`)       |
| `--api-key <key>`           | Override the Fireworks key from your environment or FireConnect config |

## Clean up

```bash theme={null}
fireconnect claude demo clean          # prompts before deleting ./fireconnect-demo/
fireconnect claude demo clean --yes    # delete without prompting
fireconnect claude demo clean --out /path/to/output
```

`demo clean` only removes directories that contain demo markers (`result.json`, `compare.html`, etc.), so it will not delete an unrelated folder you pointed `--out` at by mistake.

## After the demo

Liked one of the models? Set it as your daily driver:

```bash theme={null}
fireconnect claude on --model glm-5p2-fast
```

More IDs and latest vs fast guidance: [Models](/ecosystem/fireconnect/models).

Want automatic cost routing instead of a fixed model? Try [FireRouter](/ecosystem/firerouter/overview):

```bash theme={null}
fireconnect claude on --model firerouter
```

## How it works

* Each side runs real `claude -p` in a separate temporary working directory, using your active FireConnect Claude profile with only the model changed.
* Numbers in the comparison strip are **measured from the run**, not list-price estimates.
* If one side fails to finish, the page says so instead of fabricating a winner.
* Open `compare.html` from the output folder anytime. It inlines both apps and works offline.

## Source

The demo ships with FireConnect: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)

## See also

* [FireConnect overview](/ecosystem/fireconnect/overview)
* [Models](/ecosystem/fireconnect/models)
* [CLI reference](/ecosystem/fireconnect/cli-reference)
