# Contributing

Thank you for your interest in contributing to ReasonFlow.

ReasonFlow follows a simple feature-branch workflow to keep development clean and maintainable.

## Development Setup

Clone the repository:

```bash
git clone https://github.com/uzair-balouch/reasonflow.git
cd reasonflow
```

Install dependencies:

```bash
uv sync
```

Run the test suite:

```bash
uv run pytest
```

Run static analysis:

```bash
uv run ruff check .
uv run ruff format .
```

## Development Workflow

1. Create a feature branch from `develop`.

```bash
git checkout develop
git pull
git checkout -b feature/your-feature
```

2. Implement the feature.

3. Run the complete test suite.

```bash
uv run pytest
```

4. Commit using Conventional Commits.

Examples:

```
feat(agent): add reflection loop
feat(tool): implement dependency scanner
fix(planner): improve tool selection
```

5. Push the branch.

```bash
git push origin feature/your-feature
```

6. Open a Pull Request into `develop`.

## Code Style

ReasonFlow follows:

- Python 3.12+
- Ruff formatting
- Type hints
- Small, focused feature branches
- Dependency Injection where appropriate
- SOLID-inspired architecture

## Project Structure

```
Planner
      ↓
Executor
      ↓
Tools
      ↓
Memory
      ↓
Reflection
```

Every new capability should be implemented as an independent tool without changing the runtime architecture.