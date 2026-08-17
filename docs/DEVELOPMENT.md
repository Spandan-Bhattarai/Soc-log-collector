# Development Guide

## 1. Repository Location

Prefer storing repositories inside the WSL Linux filesystem:

```bash
~/projects/
```

Example:

```bash
mkdir -p ~/projects
cd ~/projects
```

Avoid putting active Linux projects under `/mnt/c/...` unless there is a specific reason.

## 2. Git

Git is installed once inside the WSL environment and is available to all repositories in that WSL environment.

You do NOT install Git separately for every project.

Check:

```bash
git --version
```

Configure once:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

## 3. Project Initialization

```bash
mkdir soc-log-collector
cd soc-log-collector
git init
```

Create the documentation files before asking an AI agent to implement features.

## 4. AI Coding Agent

The project can be opened in Antigravity or VS Code through WSL.

The coding agent should read:

```text
AGENTS.md
PROJECT.md
project-spec.md
DATABASE.md
API.md
SECURITY.md
PROGRESS.md
```

before significant implementation.

## 5. Docker

Use Docker for server-side development where useful.

The Windows collector is not containerized because it needs access to Windows event sources.

Initial services:

- FastAPI
- Next.js

SQLite can be stored in a persistent local volume.

Do not add unnecessary infrastructure.

## 6. Environment Variables

Create:

```text
.env
```

from:

```text
.env.example
```

Never commit `.env`.

## 7. Branches

For a solo project, a simple approach is sufficient:

```text
main
feature/collector-enrollment
feature/event-ingestion
feature/dashboard
```

Keep `main` in a working state.

## 8. Commits

Prefer small commits.

Example:

```bash
git add .
git commit -m "feat: add collector enrollment"
```

## 9. Agent Task Pattern

Give the coding agent focused tasks.

Good:

> Read the project documentation and implement the SQLAlchemy organizations, users, endpoints, collectors, and events models. Do not create API routes yet. Add tests and run them.

Bad:

> Build the whole SOC platform.

## 10. Verification

After every meaningful feature:

```text
1. Run tests.
2. Start the service.
3. Test the API.
4. Inspect database changes.
5. Test the frontend.
6. Update PROGRESS.md.
7. Commit.
```

## 11. Troubleshooting Rule

Do not immediately delete working code to fix an error.

First determine:

- what failed
- where it failed
- why it failed
- whether the error is architectural or implementation-specific

Then make the smallest safe change.
