# Project 1 Progress

Update this file after meaningful implementation work.

## Status

Current phase: Phase 3: Authentication (Phase 2 Complete)

Overall completion: 30%

---

## Phase 0: Environment

- [x] WSL2 Ubuntu working
- [x] Git installed
- [x] Python installed
- [x] Node.js installed
- [x] Docker Engine working
- [x] Docker Compose working
- [x] VS Code/Antigravity connected to WSL
- [x] GitHub repository created

## Phase 1: Repository Foundation

- [x] Project structure created
- [x] AGENTS.md added
- [x] Documentation added
- [x] Backend initialized
- [x] Frontend initialized
- [x] Collector initialized
- [x] `.gitignore`
- [x] `.env.example`
- [x] README
- [x] Initial Git commit

## Phase 2: Database

- [x] SQLAlchemy configured
- [x] SQLite configured
- [x] Alembic configured
- [x] organizations model
- [x] users model
- [x] endpoints model
- [x] collectors model
- [x] events model
- [x] indexes
- [x] initial migration
- [x] database tests

## Phase 3: Authentication

- [ ] Registration
- [ ] Login
- [ ] Password hashing
- [ ] Token/session handling
- [ ] User roles
- [ ] Protected routes
- [ ] Organization isolation tests

## Phase 4: Collector Enrollment

- [ ] Endpoint creation
- [ ] Enrollment token generation
- [ ] Enrollment endpoint
- [ ] Token hashing
- [ ] Collector identity
- [ ] Collector credential
- [ ] Collector revocation
- [ ] Enrollment tests

## Phase 5: Event Ingestion

- [ ] Common event Pydantic schema
- [ ] Event API
- [ ] Server-side collector resolution
- [ ] Event validation
- [ ] Event persistence
- [ ] Pagination
- [ ] Filtering
- [ ] Ingestion tests

## Phase 6: Windows Collector

- [ ] Windows event reader
- [ ] Event filtering
- [ ] 4624 parser
- [ ] 4625 parser
- [ ] 4688 parser
- [ ] Normalization
- [ ] Collector configuration
- [ ] HTTPS transport
- [ ] Retry queue
- [ ] Heartbeat
- [ ] Graceful shutdown

## Phase 7: Dashboard

- [ ] Login
- [ ] Registration
- [ ] Dashboard
- [ ] Endpoint list
- [ ] Endpoint details
- [ ] Collector status
- [ ] Event table
- [ ] Event filters
- [ ] Event details
- [ ] Error states

## Phase 8: Packaging

- [ ] PyInstaller configuration
- [ ] collector.exe build
- [ ] Collector configuration documentation
- [ ] Test on Windows
- [ ] Installation instructions

## Phase 9: Testing and Security

- [ ] Backend unit tests
- [ ] Collector tests
- [ ] API integration tests
- [ ] Authentication tests
- [ ] Authorization tests
- [ ] Organization isolation tests
- [ ] Event validation tests
- [ ] Queue tests
- [ ] Basic security review
- [ ] Dependency review

## Phase 10: GitHub Release

- [ ] README completed
- [ ] Architecture diagram
- [ ] Screenshots
- [ ] Example configuration
- [ ] Example event data
- [ ] Setup instructions
- [ ] Troubleshooting
- [ ] License
- [ ] Final GitHub cleanup
- [ ] Release tag

---

## Decision Log

### Decision 001
SQLite is used initially.

Reason:
- simple local development
- easy GitHub setup
- no separate database server
- SQLAlchemy keeps future migration possible

### Decision 002
Elasticsearch/ELK is not included.

Reason:
- not required for Project 1
- adds operational complexity
- can be evaluated later if search volume makes it useful

### Decision 003
The collector is a Windows application, while the server runs in Linux/WSL/Docker.

Reason:
- endpoint telemetry requires Windows access
- server components are easier to develop in Linux

### Decision 004
The server determines organization and endpoint ownership.

Reason:
- prevents clients from choosing another tenant by modifying IDs

---

## Current Notes

Add implementation notes, problems, and decisions below.

### Date: 2026-08-17
### What changed (Phase 1):
- Initialized root `.gitignore` and `.env.example`.
- Created `backend/` scaffolding with FastAPI, Pydantic settings, SQLAlchemy SQLite session, CORS, and health test.
- Created `frontend/` scaffolding with Next.js 14, TypeScript, and Tailwind CSS.
- Created `collector/` scaffolding with configuration, client, common event normalizer, and local queue buffering.
- Created tests and verified passing execution for backend test suite, collector test suite, and Next.js frontend build.

### Date: 2026-08-17
### What changed (Phase 2):
- Configured SQLite with SQLAlchemy engine connection listener enforcing foreign keys (`PRAGMA foreign_keys=ON`).
- Created relational ORM models: `Organization`, `User`, `Endpoint`, `Collector`, `Event` with full schema and indexes.
- Configured Alembic with batch mode for SQLite schema migrations.
- Created initial migration `42f833fa7fd6_initial_schema.py` and executed `alembic upgrade head`.
- Implemented comprehensive database test suite (`backend/tests/test_database.py`) testing CRUD, foreign key enforcement, unique constraints, cascading deletes, and query filters.

### Tests:
- `backend/tests/test_database.py` (6 passed)
- `backend/tests/test_health.py` (2 passed)
- `collector/tests/test_normalizer_basic.py` (2 passed)

### Problems:
- None.

### Next task:
- Phase 3: Authentication (User registration, login, password hashing via bcrypt/passlib, JWT token session management, user roles, and organization isolation tests).


