# SOC Log Collector - Detailed Project Specification

## 1. Architecture

```text
Windows Endpoint
      |
      v
collector.exe
      |
      +--> Windows Event Logs
      |
      +--> Filtering
      |
      +--> Parsing
      |
      +--> Normalization
      |
      +--> Local Queue
      |
      v
HTTPS
      |
      v
FastAPI
      |
      +--> Authentication
      +--> Collector Validation
      +--> Organization/Endpoint Resolution
      +--> Event Validation
      |
      v
SQLite
      |
      v
Next.js Dashboard
```

## 2. User Roles

### admin

- Manage organization users.
- Create endpoints.
- Enroll collectors.
- Revoke collectors.
- View all organization events.
- View audit logs.

### analyst

- View events.
- Investigate events.
- Add notes where implemented.

### viewer

- Read-only dashboard access.

The role must be checked by the backend.

## 3. Organization Model

Every user belongs to one organization in the first version.

Every endpoint, collector, event, and audit record must be associated with an organization.

The backend must derive organization ownership from the authenticated user or authenticated collector.

## 4. Collector Enrollment

Flow:

1. Authenticated user opens endpoint management.
2. User creates an endpoint.
3. Server creates a pending collector.
4. Server generates a one-time enrollment token.
5. User configures the collector with the token.
6. Collector contacts `/api/v1/collectors/enroll`.
7. Server validates the token.
8. Server associates the collector with the endpoint and organization.
9. Server issues a long-lived collector credential.
10. The raw enrollment token is not stored.
11. The collector stores its credential locally.
12. Subsequent requests use the collector credential.

The server is authoritative for organization and endpoint ownership.

## 5. Collector Authentication

Do not trust IDs supplied by the collector to establish ownership.

A collector request should authenticate the collector first.

The server then resolves:

collector credential -> collector_id -> endpoint_id -> organization_id

A revoked collector must no longer be allowed to submit events.

## 6. Event Collection

The first implementation should collect selected Windows Security and related events.

The collector should not collect everything by default.

This reduces unnecessary data collection and keeps the first implementation manageable.

## 7. Event Normalization

Every raw Windows event must be transformed into the common event schema.

Example:

```json
{
  "event_id": "uuid",
  "organization_id": "server-assigned",
  "collector_id": "server-associated",
  "endpoint_id": "server-associated",
  "timestamp": "2026-08-18T02:15:00Z",
  "event_source": "windows_security",
  "event_type": "authentication_failure",
  "event_category": "authentication",
  "event_id_external": 4625,
  "username": "administrator",
  "process_name": null,
  "process_id": null,
  "command_line": null,
  "source_ip": "185.10.20.30",
  "source_port": null,
  "destination_ip": null,
  "destination_port": null,
  "hostname": "DESKTOP-001",
  "severity": "medium",
  "raw_log": "...",
  "metadata": {}
}
```

The server may overwrite identity fields with values derived from the authenticated collector.

## 8. Local Queue

If the API is unavailable:

1. Store unsent normalized events locally.
2. Continue collecting events where practical.
3. Retry with backoff.
4. Remove events from the queue only after successful server acknowledgement.

Do not allow an unlimited queue to consume the entire endpoint disk.

A reasonable first version can use a small SQLite queue or JSONL queue.

## 9. Heartbeat

The collector should periodically call:

`POST /api/v1/collectors/heartbeat`

The server updates:

`last_seen_at`

Heartbeat data should not contain unnecessary endpoint telemetry.

## 10. API Event Ingestion

Preferred endpoint:

`POST /api/v1/events`

The API should accept either a single event or a small batch. Start with single-event ingestion if it simplifies development, then add batching.

The server must validate:

- collector authentication
- event structure
- timestamp
- allowed field types
- payload size
- organization ownership
- endpoint ownership

## 11. Dashboard

The dashboard should initially show:

- Total events today
- Events by category
- Events by severity
- Active collectors
- Offline collectors
- Recent events

The event table should support:

- timestamp
- hostname
- event type
- username
- source IP
- severity
- event ID

Selecting an event should show the complete normalized event and raw log.

## 12. Error Handling

API errors should use structured JSON.

Example:

```json
{
  "detail": "Collector credential is invalid"
}
```

The collector should log enough information for troubleshooting but must not log secrets.

## 13. Testing

Minimum tests:

### Authentication

- valid login
- invalid login
- inactive user
- unauthorized route

### Collector

- valid enrollment
- invalid enrollment token
- revoked collector
- valid heartbeat
- invalid credential

### Events

- valid event
- malformed event
- oversized event
- unauthorized organization
- unknown collector
- unknown endpoint

### Normalization

- Windows 4624
- Windows 4625
- Windows 4688

### Queue

- failed transmission
- retry
- successful flush
- queue size limit

## 14. Out of Scope

Do not implement these in Project 1:

- ML classification
- LLM analysis
- threat intelligence
- MITRE ATT&CK enrichment
- automatic response
- Elasticsearch
- Splunk
- ELK
- Kafka
- Redis
- Kubernetes
- PostgreSQL
- cloud deployment
- complex multi-region architecture

These belong to later projects or future versions.
