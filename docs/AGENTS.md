# AGENTS.md

## Purpose

This repository is Project 1 of the SOCUaTrace project family:

**Project 1: SOC Log Collector**

The goal is to build a small, defensive endpoint telemetry platform that collects selected Windows security events, normalizes them into the SOCUaTrace common event schema, sends them securely to a FastAPI server, stores them in SQLite, and displays them in a Next.js dashboard.

Read these files before making significant changes:

1. `PROJECT.md`
2. `project-spec.md`
3. `DATABASE.md`
4. `API.md`
5. `SECURITY.md`
6. `PROGRESS.md`

## Core Rules

- Do not redesign the architecture without explaining why first.
- Do not change the common event schema casually.
- Do not introduce PostgreSQL, Elasticsearch, Splunk, ELK, Redis, Kafka, Kubernetes, or other infrastructure unless explicitly approved.
- SQLite is the database for this project.
- Use FastAPI for the backend.
- Use SQLAlchemy for database access.
- Use Pydantic for API validation.
- Use Next.js + TypeScript for the frontend.
- Use Tailwind CSS for styling.
- Use Python for the Windows collector.
- The collector may later be packaged as `collector.exe` using PyInstaller.
- Keep the collector independent from the web dashboard.
- Keep organization and endpoint ownership enforced by the server.
- Never trust `organization_id`, `endpoint_id`, or `user_id` supplied by an untrusted client.
- Never store plaintext passwords, collector secrets, enrollment tokens, API keys, or other credentials in source code.
- Never commit `.env` files containing real secrets.
- Treat all logs as untrusted input.
- Never execute commands contained in logs.
- Use HTTPS for collector-to-server communication.
- Validate and authenticate collector requests.
- Write tests for important backend, normalization, authentication, and ingestion behavior.

## Coding Style

- Prefer clear, readable code over clever code.
- Use type hints in Python and TypeScript.
- Keep functions reasonably small.
- Separate API routes, business logic, database models, and schemas.
- Use meaningful names.
- Avoid unnecessary dependencies.
- Do not duplicate business logic between frontend and backend.
- Do not silently change database fields or API contracts.
- Update documentation when an interface changes.

## Agent Workflow

Before implementing a significant feature:

1. Read the relevant documentation.
2. Inspect the existing repository.
3. Check `PROGRESS.md`.
4. Explain the planned files and changes.
5. Implement the smallest useful version.
6. Run relevant tests.
7. Fix failures.
8. Update `PROGRESS.md`.
9. Summarize what changed and what remains.

If requirements are ambiguous, stop and ask rather than inventing a major architectural decision.

## Git Rules

Use small, meaningful commits.

Examples:

- `chore: initialize project structure`
- `feat: add database models`
- `feat: add collector enrollment`
- `feat: add event ingestion`
- `feat: add event dashboard`
- `test: add ingestion tests`
- `fix: validate collector credentials`

Do not rewrite Git history unless explicitly requested.

## Security Rule

This is a cybersecurity project, but it is a defensive telemetry and analysis system. Development must prioritize safe collection, authentication, validation, logging, and isolation.
