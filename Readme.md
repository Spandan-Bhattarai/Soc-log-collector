# SOC Log Collector

Project 1 of the SOCUaTrace project family.

SOCUaTrace means **SOC Unified Analysis Trace**.

## What this project does

The SOC Log Collector collects selected Windows security events, normalizes them, sends them to a FastAPI server, stores them in SQLite, and displays them in a Next.js dashboard.

```text
Windows
   |
collector.exe
   |
normalized events
   |
HTTPS
   |
FastAPI
   |
SQLite
   |
Next.js
```

## Documentation

- `AGENTS.md` - instructions for coding agents
- `PROJECT.md` - project overview and goals
- `project-spec.md` - detailed technical specification
- `DATABASE.md` - database schema
- `API.md` - API contract
- `SECURITY.md` - security requirements
- `PROGRESS.md` - implementation checklist

## Development Environment

Recommended:

- Windows
- WSL2 Ubuntu
- Git
- Python
- Node.js
- Docker Engine
- Docker Compose
- VS Code or Antigravity

The central server runs in WSL/Linux.

The Windows collector runs on Windows.

## Important

This is a development project. Do not deploy it to production without a proper security review, secure TLS configuration, secret management, monitoring, backup strategy, and additional testing.

## Project Family

1. SOC Log Collector
2. Cybersecurity ML Training & Retraining Pipeline
3. AI SOC Alert Analyzer
4. SOCUaTrace

The common event schema is intentionally shared between all projects.
