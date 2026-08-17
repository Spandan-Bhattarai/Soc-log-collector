# SOC Log Collector

Project 1 of the **SOCUaTrace** project family (**SOC Unified Analysis Trace**).

The SOC Log Collector collects selected Windows security events, normalizes them into the standard SOCUaTrace event schema, transmits them securely to a FastAPI server, stores them in SQLite, and displays them in a Next.js dashboard.

```text
Windows Endpoint
       |
  collector.exe (Python / Winevt reader)
       |
  Normalized Events + Local JSONL Queue
       |
     HTTPS
       |
    FastAPI (Auth, Token Hash, Ownership derivation)
       |
    SQLite (Indexed Common Event Schema)
       |
  Next.js Dashboard (Telemetry, Details, Filters)
```

## Directory Structure

```text
soc-log-collector/
├── backend/            # FastAPI backend (API, SQLAlchemy, Alembic migrations)
│   ├── app/            # Application core, api routers, models, schemas
│   ├── tests/          # Pytest suite for backend APIs and services
│   └── requirements.txt
├── frontend/           # Next.js TypeScript web application with Tailwind CSS
│   ├── src/app/        # App router, pages, and components
│   └── package.json
├── collector/          # Python Windows event collector
│   ├── src/            # Event reader, normalizer, local retry queue, HTTP client
│   ├── tests/          # Tests for collector normalization and queue logic
│   └── requirements.txt
├── docs/               # Architecture and project specifications
│   ├── AGENTS.md       # Guidelines for AI coding agents
│   ├── PROJECT.md      # High-level architecture & definition of done
│   ├── project-spec.md # Detailed technical specification
│   ├── DATABASE.md     # SQLite schema & relations
│   ├── API.md          # REST API contracts
│   ├── SECURITY.md     # Threat model and hardening requirements
│   ├── PROGRESS.md     # Implementation tracking
│   ├── DEVELOPMENT.md  # Local development guidelines
│   └── ENVIRONMENT.md  # Environment and runtime setup
├── .env.example        # Environment variable template
└── .gitignore
```

## Quick Start (Development)

### 1. Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Backend API Swagger docs will be available at `http://localhost:8000/docs`.

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

Dashboard interface will be available at `http://localhost:3000`.

### 3. Collector

```bash
cd collector
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m collector.src.main
```

## Project Family

1. **SOC Log Collector** (Current)
2. Cybersecurity ML Training & Retraining Pipeline
3. AI SOC Alert Analyzer
4. SOCUaTrace

The common event schema is shared across all projects.
