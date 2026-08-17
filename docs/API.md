# API Specification

Base URL:

`/api/v1`

## Authentication

### POST /auth/register

Create a user and initial organization where appropriate.

### POST /auth/login

Authenticate the user.

### GET /users/me

Return the authenticated user's profile.

## Endpoints

### POST /endpoints

Create an endpoint.

Server assigns:

- endpoint_id
- organization_id
- registration metadata

### GET /endpoints

Return endpoints belonging to the authenticated user's organization.

### GET /endpoints/{endpoint_id}

Return an endpoint only if it belongs to the user's organization.

## Collectors

### POST /collectors/enroll

Used by a new collector.

The enrollment request contains the enrollment credential.

The server validates it and associates the collector with the pre-created endpoint.

### POST /collectors/heartbeat

Authenticated collector heartbeat.

The server derives collector identity from authentication.

### GET /collectors

Return collectors belonging to the authenticated organization.

### POST /collectors/{collector_id}/revoke

Revoke a collector.

Only an authorized user can perform this operation.

## Events

### POST /events

Submit a normalized event or small batch.

Collector authentication is required.

The server must derive organization_id and endpoint_id from the authenticated collector.

### GET /events

Return events belonging to the authenticated organization.

Supported initial filters:

- endpoint_id
- collector_id
- event_type
- event_category
- severity
- username
- source_ip
- start_time
- end_time

### GET /events/{event_id}

Return a single event after organization ownership is verified.

## API Design Rules

- Use `/api/v1`.
- Validate all request bodies with Pydantic.
- Use appropriate HTTP status codes.
- Do not expose secrets.
- Do not return password hashes.
- Do not allow users to select another organization by passing a query parameter.
- Use pagination for event lists.
- Apply reasonable request size limits.
- Log security-relevant actions.
