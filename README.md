# ReasonFlow

> A production-oriented Agentic AI runtime for building autonomous, observable, and reliable AI systems.

ReasonFlow is a lightweight framework for orchestrating AI agents that can reason about a goal, plan actions, execute tools, maintain execution memory, reflect on progress, and produce meaningful results.

The current implementation demonstrates these capabilities through a GitHub Repository Analysis workflow, where the agent autonomously analyzes an open-source repository, discovers its dependencies, performs a vulnerability assessment, and maintains execution memory throughout the reasoning process.

---

## Features

- Goal-driven planning using Large Language Models (LLMs)
- Autonomous tool selection and execution
- Shared execution memory
- Reflection-based reasoning loop
- Pluggable LLM providers
- GitHub repository metadata analysis
- Dependency discovery
- Python dependency parsing
- Vulnerability scanning
- Modular and extensible architecture
- Dependency Injection based design
- Fully tested using pytest

---

## Architecture

```text
                  User Goal
                      │
                      ▼
             Planning Agent (LLM)
                      │
                      ▼
               Execution Engine
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   GitHub Tool   Dependency Tool   Vulnerability Tool
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                  Shared Memory
                      │
                      ▼
                  Reflection Loop
                      │
                      ▼
                 Final AI Response
```

---

## Project Structure

```text
src/reasonflow

├── agents/
│   ├── planner.py
│   ├── executor.py
│   └── reporter.py
│
├── cli/
│
├── models/
│
├── services/
│   ├── github.py
│   └── llm/
│       ├── base.py
│       ├── fake.py
│       └── gemini.py
│
├── tools/
│   ├── github.py
│   ├── dependency.py
│   ├── vulnerability.py
│   └── registry.py
│
└── workflows/
    └── analysis.py
```

---

## Current Workflow

The current workflow implemented in ReasonFlow performs the following sequence autonomously:

1. Receive a repository URL.
2. Create a goal.
3. Ask the planner to determine the next action.
4. Execute the selected tool.
5. Store observations in shared memory.
6. Reflect on the current state.
7. Repeat until the goal is satisfied.

This iterative planning loop follows the fundamental Agentic AI pattern:

```text
Think
   ↓
Plan
   ↓
Act
   ↓
Observe
   ↓
Reflect
   ↓
Repeat
```

---

## Implemented Tools

### GitHub Tool

Collects repository metadata including:

- Owner
- Repository name
- Language
- Default branch
- License
- Stars

---

### Dependency Tool

Discovers dependency manifests such as:

- `pyproject.toml`
- `requirements.txt`

Extracts project dependencies for further analysis.

---

### Vulnerability Tool

Scans discovered dependencies.

The current implementation provides a pluggable interface that can be connected to vulnerability databases such as OSV.dev in future versions.

---

## Example

```bash
reasonflow analyze https://github.com/psf/requests
```

Example output:

```text
🚀 ReasonFlow

Planning...

✓ Fetch repository metadata

Planning...

✓ Discover dependencies

Planning...

✓ Scan for vulnerabilities

Repository Information
----------------------
Owner: psf
Repository: requests
Language: Python
License: Apache-2.0

Observations
------------
Repository metadata collected
Found manifest: pyproject.toml
Dependency: urllib3
Dependency: certifi
No known vulnerabilities found.

Reflection
----------
Goal satisfied.
```

---

## Technology Stack

- Python 3.12
- Gemini API
- Typer
- HTTPX
- pytest
- Ruff
- uv

---

## Running Locally

Clone the repository:

```bash
git clone https://github.com/uzair-balouch/reasonflow.git
cd reasonflow
```

Install dependencies:

```bash
uv sync
```

Run the CLI:

```bash
uv run reasonflow analyze https://github.com/psf/requests
```

Run tests:

```bash
uv run pytest
```

---

## Roadmap

### Version 1.0

- Goal-driven planning
- Tool execution
- Reflection loop
- Memory
- GitHub analysis workflow
- Dependency discovery
- Vulnerability scanning

### Version 2.0

- Multi-agent collaboration
- Parallel tool execution
- Long-term memory
- Human approval checkpoints
- Browser automation
- Web search tools
- Code execution
- Additional LLM providers

---

## Design Principles

ReasonFlow is built around a few core engineering principles:

- Modular architecture
- Separation of concerns
- Dependency Injection
- Extensible tool ecosystem
- Provider-agnostic LLM integration
- Testable components
- Production-oriented project structure

---

## License

This project is licensed under the MIT License.