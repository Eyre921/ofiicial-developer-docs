---
title: "Ori Codex"
source: https://openrouter.ai/docs/guides/ori/codex.md
path: docs/guides/ori/codex
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Ori Codex

> Run the Codex CLI and Codex Desktop on OpenRouter with one setup command, and go back with one reset

Ori Codex is the Codex you already use, on OpenRouter. It is part of [Ori Harness](/docs/guides/ori/harness). The Codex CLI and Codex Desktop share one Codex config, so one setup puts both on OpenRouter, and one reset puts both back.

<Frame caption="Ori Codex in 43 seconds: install, set up, pick a model, and reset.">
  <video controls playsInline preload="none" poster="/assets/guides/ori/ori-codex-poster.jpg" className="w-full aspect-video rounded-xl" src="https://mintcdn.com/openrouter-d02e98a0/BsDm6_lzoycx6YRP/assets/guides/ori/ori-codex.mp4?fit=max&auto=format&n=BsDm6_lzoycx6YRP&q=85&s=b395edce16fab54cdd32cfa3517029c9" data-path="assets/guides/ori/ori-codex.mp4" />
</Frame>

<Accordion title="Video transcript">
  You already use Codex. Now meet Ori Codex. It's the same Codex, on OpenRouter.

  Install Ori with one line, and sign in. Then run one command. That's it.

  Ori Codex works in the terminal, and in the desktop app.

  Open the model picker, and every model your team allows is right there. Pick one, and get back to work.

  Your sessions, your projects, and your skills all stay exactly where they are.

  And if you ever want plain Codex back, it's one command.
</Accordion>

## Start Codex in the terminal

To run the Codex CLI on OpenRouter for one session, launch it through Ori:

```sh theme={null}
ori codex
```

Ori uses the Codex CLI on your `PATH`, and asks to install it if it's missing. To choose a model, pass `--model` with any OpenRouter model ID. See [Any agent, any model](/docs/guides/ori/harness#any-agent-any-model).

## Set up Codex Desktop

<Frame caption="Set up Ori Codex step by step, in one minute.">
  <video controls playsInline preload="none" poster="/assets/guides/ori/ori-codex-tutorial-poster.jpg" className="w-full aspect-video rounded-xl" src="https://mintcdn.com/openrouter-d02e98a0/BsDm6_lzoycx6YRP/assets/guides/ori/ori-codex-tutorial.mp4?fit=max&auto=format&n=BsDm6_lzoycx6YRP&q=85&s=abc10d844eeaa5d37630836177dd6066" data-path="assets/guides/ori/ori-codex-tutorial.mp4" />
</Frame>

<Accordion title="Video transcript">
  Here's how to set up Ori Codex. It takes about a minute.

  Step one. Install Ori. Paste this one line in your terminal.

  Step two. Sign in. Run ori login, and choose the browser sign in.

  Step three. Quit Codex Desktop, then run the setup command. Codex now runs on OpenRouter, in the terminal and in the desktop app.

  Step four. Open Codex. Your threads are all still there. Open the model picker, and choose a model your team allows.

  Step five. Send a prompt, like you always do. The answer comes back through OpenRouter.

  Want plain Codex back? Quit the app, and run the reset command. Everything returns to how it was.
</Accordion>

<Note>
  Quit Codex Desktop before you run setup or reset.
</Note>

1. Install Codex Desktop, then [install Ori](/docs/guides/ori/harness#install-ori).

2. Sign in to OpenRouter:

   ```sh theme={null}
   ori login
   ```

3. Route Codex through OpenRouter:

   ```sh theme={null}
   ori harness setup codex
   ```

4. Open Codex Desktop and pick a model from the model picker. The picker lists models from the OpenRouter catalog.

The setup stays in place until you reset it, so your plain `codex` command also runs on OpenRouter. You don't need to launch Codex Desktop through Ori.

## Go back to your own Codex setup

To put Codex back on your own setup, run:

```sh theme={null}
ori harness reset codex
```

Reset removes the OpenRouter provider from your Codex config and restores the settings that setup replaced.

## What works in Codex Desktop

* Setup with `ori harness setup codex`.
* Chat turns on OpenRouter.
* The model picker with the OpenRouter catalog.
* Reset with `ori harness reset codex`.

Verified on Ori 0.15.6 with Codex Desktop 26.930 on macOS. Codex Desktop on Windows and Linux isn't verified.

## Not available yet

* Plugin search in Codex Desktop.
* Image generation in Codex Desktop.

