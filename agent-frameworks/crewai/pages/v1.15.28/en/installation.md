---
title: "Installation"
source: https://docs.crewai.com/v1.15.28/en/installation
path: v1.15.28/en/installation
---

Get started with CrewAI - Install, configure, and build your first AI crew

Coding agent setup

## Set up CrewAI in your coding agent

Copy a ready-to-paste setup prompt for Claude Code, Codex, Cursor, or any coding agent. It installs the official CrewAI skills, checks the CLI, and points the agent at the right docs before it edits code.

Copy agent setup prompt

[View coding-agent guide](/en/guides/coding-tools/build-with-ai)

### Watch: Building CrewAI Agents & Flows with Coding Agent Skills

[https://www.loom.com/embed/befb9f68b81f42ad8112bfdd95a780af](https://www.loom.com/embed/befb9f68b81f42ad8112bfdd95a780af)

## Video Tutorial

Watch this video tutorial for a step-by-step demonstration of the installation process:

[CrewAI Installation Guide](https://www.youtube.com/embed/-kSOTtYzgEw)

## Text Tutorial

> [!NOTE]
>
> **Python Version Requirements**
>
> CrewAI requires `Python >=3.10 and <3.14`. Here's how to check your version:
>
> ```bash theme={null}
> python3 --version
> ```
>
> If you need to update Python, visit [python.org/downloads](https://python.org/downloads)

> [!NOTE]
>
> **OpenAI SDK Requirement**
>
> CrewAI 0.175.0 requires `openai >= 1.13.3`. If you manage dependencies yourself, ensure your environment satisfies this constraint to avoid import/runtime issues.

CrewAI uses the `uv` as its dependency management and package handling tool. It simplifies project setup and execution, offering a seamless experience.

If you haven't installed `uv` yet, follow **step 1** to quickly get it set up on your system, else you can skip to **step 2**.

**1. Install uv**

* **On macOS/Linux:**

  Use `curl` to download the script and execute it with `sh`:

  ```shell theme={null}
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

  If your system doesn't have `curl`, you can use `wget`:

  ```shell theme={null}
  wget -qO- https://astral.sh/uv/install.sh | sh
  ```

* **On Windows:**

  Use `irm` to download the script and `iex` to execute it:

  ```shell theme={null}
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

  If you run into any issues, refer to [UV's installation guide](https://docs.astral.sh/uv/getting-started/installation/) for more information.

**2. Install CrewAI 🚀**

* Run the following command to install `crewai` CLI:

  ```shell theme={null}
  uv tool install crewai
  ```

  > [!WARNING]
  >
  > If you encounter a `PATH` warning, run this command to update your shell:
  >
  > ```shell theme={null}
  > uv tool update-shell
  > ```

  > [!WARNING]
  >
  > If you encounter the `chroma-hnswlib==0.7.6` build error (`fatal error C1083: Cannot open include file: 'float.h'`) on Windows, install [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/) with *Desktop development with C++*.

* To verify that `crewai` is installed, run:
  ```shell theme={null}
  uv tool list
  ```

* You should see something like:
  ```shell theme={null}
  crewai v0.102.0
  - crewai
  ```

* If you need to update `crewai`, run:
  ```shell theme={null}
  uv tool install crewai --upgrade
  ```

> [!NOTE]
>
> This upgrades the **global `crewai` CLI tool** only. To upgrade the `crewai` version inside your project's virtual environment, see [Upgrading CrewAI in a project](/en/guides/migration/upgrading-crewai).

> [!TIP]
>
> Installation successful! You're ready to create your first crew! 🎉

# Creating a CrewAI Project

`crewai create crew` now creates a JSON-first crew project. Agents live in `agents/*.jsonc`, tasks and crew-level settings live in `crew.jsonc`, and `crewai run` loads that JSON definition directly.

**1. Generate Project Scaffolding**

* Run the `crewai` CLI command:
  ```shell theme={null}
  crewai create crew <your_project_name>
  ```

* This creates a new project with the following structure:
  ```
  my_project/
  ├── .gitignore
  ├── .env
  ├── agents/
  │   └── researcher.jsonc
  ├── crew.jsonc
  ├── knowledge/
  ├── pyproject.toml
  ├── README.md
  ├── skills/
  └── tools/
  ```

* If you need the older Python/YAML scaffold with `crew.py`, `config/agents.yaml`, and `config/tasks.yaml`, run:
  ```shell theme={null}
  crewai create crew <your_project_name> --classic
  ```

**2. Customize Your Project**

* Your project will contain these essential files:
  | File | Purpose |
  | - | - |
  | `crew.jsonc` | Configure the crew, task order, process, and input defaults |
  | `agents/*.jsonc` | Define each agent's role, goal, backstory, LLM, tools, and behavior |
  | `.env` | Store API keys and environment variables |
  | `tools/` | Optional Python files for `custom:<name>` tools |
  | `knowledge/` | Optional knowledge files for agents |
  | `skills/` | Optional skill files applied to the crew |

* Start by editing `crew.jsonc` and the files in `agents/` to define your crew's behavior.

* Use `{placeholder}` values in agent and task text, then set defaults in `crew.jsonc` under `inputs`. When you run `crewai run`, the CLI prompts for any missing values.

* Keep sensitive information like API keys in `.env`.

**3. Run your Crew**

* Before you run your crew, make sure to run:
  ```bash theme={null}
  crewai install
  ```
* If you need to install additional packages, use:
  ```shell theme={null}
  uv add <package-name>
  ```
  > [!NOTE]
  >
  > As a supply-chain security measure, CrewAI's internal packages use `exclude-newer = "3 days"` in their `pyproject.toml` files. This means transitive dependencies pulled in by CrewAI won't resolve packages released less than 3 days ago. Your own direct dependencies are not affected by this policy. If you notice a transitive dependency is behind, you can pin the version you want explicitly in your project's dependencies.
* To run your crew, execute the following command in the root of your project:
  ```bash theme={null}
  crewai run
  ```

## Enterprise Installation Options

> [!NOTE]
>
> For teams and organizations, CrewAI offers enterprise deployment options that eliminate setup complexity:
>
> ### CrewAI AMP (SaaS)
>
> * Zero installation required - just sign up for free at [app.crewai.com](https://app.crewai.com)
> * Automatic updates and maintenance
> * Managed infrastructure and scaling
> * Build Crews with no Code
>
> ### CrewAI Factory (Self-hosted)
>
> * Containerized deployment for your infrastructure
>
> * Supports any hyperscaler including on prem deployments
>
> * Integration with your existing security systems
>
> > **[Explore Enterprise Options](https://share.hsforms.com/1Ooo2UViKQ22UOzdr7i77iwr87kg)**
> >
> > Learn about CrewAI's enterprise offerings and schedule a demo

## Next Steps

> **[Quickstart: Flow + agent](/en/quickstart)**
>
> Follow the quickstart to scaffold a Flow, run a one-agent crew, and produce a report.

> **[Join the Community](https://community.crewai.com)**
>
> Connect with other developers, get help, and share your CrewAI experiences.
