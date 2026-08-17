# Project 1: SOC Log Collector

## Project Identity

**Project name:** SOC Log Collector

**Project family:** SOCUaTrace

**Final platform:** SOC Unified Analysis Trace

## Purpose

Build an independent endpoint telemetry project that demonstrates how a basic SOC platform can collect security events from Windows endpoints.

The project should be small enough to understand, run locally, demonstrate, and publish on GitHub.

## Problem

A SOC needs security telemetry from endpoints. Windows generates useful security events, but raw operating system events are difficult to work with directly.

This project creates a simple pipeline:

Windows endpoint -> collector -> normalization -> secure API -> database -> dashboard

## Main Features

### Collector

- Read selected Windows Event Logs.
- Filter useful security events.
- Normalize events.
- Add endpoint and collector identity.
- Queue events when the server is unavailable.
- Retry failed transmissions.
- Send events over HTTPS.
- Send periodic heartbeats.
- Support enrollment and revocation.
- Run in the background.
- Report collector version.

### Backend

- User registration and login.
- Organization support.
- Endpoint creation.
- Collector enrollment.
- Collector authentication.
- Event ingestion.
- Event querying.
- Collector heartbeat.
- Collector revocation.
- Basic audit logging.

### Frontend

- Login page.
- Registration page.
- SOC dashboard.
- Endpoint list.
- Endpoint details.
- Collector status.
- Event list.
- Event details.
- Basic filtering.

## Initial Windows Events

Start with these event IDs:

- 4624: successful logon
- 4625: failed logon
- 4688: process creation
- 4672: special privileges assigned
- 4720: user account created
- 4728: member added to a security-enabled global group
- 4732: member added to a security-enabled local group
- 7045: service installed
- 4104: PowerShell script block logging

The implementation may begin with only 4624, 4625, and 4688. Add the others incrementally.

## Common Event Schema

The following field names must remain consistent across the SOCUaTrace project family:

- event_id
- organization_id
- collector_id
- endpoint_id
- timestamp
- event_source
- event_type
- event_category
- event_id_external
- username
- process_name
- process_id
- command_line
- source_ip
- source_port
- destination_ip
- destination_port
- hostname
- severity
- raw_log
- metadata
- created_at

`event_id` is the internal UUID.

`event_id_external` is the operating system or external event identifier such as Windows Event ID 4625.

## Technology

### Backend

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- Alembic
- SQLite
- PyJWT or another well-maintained authentication library

### Frontend

- Next.js
- TypeScript
- Tailwind CSS
- Fetch or Axios
- A lightweight chart/table library only when needed

### Collector

- Python
- Windows Event Log APIs
- `pywin32` or an appropriate Windows event library
- HTTP client such as `httpx`
- PyInstaller for executable packaging

### Development

- WSL2 Ubuntu
- Docker Engine
- Docker Compose
- Git
- GitHub
- VS Code or Antigravity

## Deployment Model

During development:

Windows host
    |
    +-- WSL2 Ubuntu
          |
          +-- FastAPI
          +-- Next.js
          +-- SQLite
          +-- Docker

A Windows VM may be used to safely test the collector.

The collector itself runs on Windows, not inside the Linux server container.

## Definition of Done

Project 1 is complete when:

1. A user can register and log in.
2. A user can create/register an endpoint.
3. A collector can enroll.
4. The server can identify which organization and endpoint a collector belongs to.
5. The collector can read selected Windows events.
6. Events are normalized into the common schema.
7. Events are authenticated and transmitted to the API.
8. The API validates and stores them in SQLite.
9. The dashboard displays the events.
10. Collector heartbeat/status works.
11. Collector revocation works.
12. Important security and ingestion tests pass.
13. The collector can be packaged as an `.exe`.
14. A new developer can follow the README and run the project.
