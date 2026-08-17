# Database Specification

## Database

SQLite is the initial database.

Use SQLAlchemy for database access and Alembic for migrations.

Do not put raw SQL throughout the application.

## Tables

### organizations

```text
organization_id UUID PRIMARY KEY
name TEXT NOT NULL
slug TEXT UNIQUE NOT NULL
is_active BOOLEAN NOT NULL
created_at DATETIME NOT NULL
updated_at DATETIME NOT NULL
```

### users

```text
user_id UUID PRIMARY KEY
organization_id UUID NOT NULL
email TEXT UNIQUE NOT NULL
password_hash TEXT NOT NULL
display_name TEXT NOT NULL
role TEXT NOT NULL
is_active BOOLEAN NOT NULL
created_at DATETIME NOT NULL
updated_at DATETIME NOT NULL
last_login_at DATETIME NULL
```

### endpoints

```text
endpoint_id UUID PRIMARY KEY
organization_id UUID NOT NULL
hostname TEXT NOT NULL
os_name TEXT
os_version TEXT
architecture TEXT
ip_address TEXT
mac_address TEXT
status TEXT NOT NULL
last_seen_at DATETIME
registered_at DATETIME NOT NULL
created_at DATETIME NOT NULL
updated_at DATETIME NOT NULL
```

### collectors

```text
collector_id UUID PRIMARY KEY
organization_id UUID NOT NULL
endpoint_id UUID NOT NULL
collector_name TEXT
collector_version TEXT
enrollment_token_hash TEXT NULL
status TEXT NOT NULL
credential_hash TEXT NULL
last_seen_at DATETIME
registered_at DATETIME NOT NULL
created_at DATETIME NOT NULL
updated_at DATETIME NOT NULL
```

The implementation may use a separate credential table if this makes credential rotation cleaner.

Never store raw secrets.

### events

```text
event_id UUID PRIMARY KEY
organization_id UUID NOT NULL
collector_id UUID NOT NULL
endpoint_id UUID NOT NULL
timestamp DATETIME NOT NULL
event_source TEXT NOT NULL
event_type TEXT NOT NULL
event_category TEXT NOT NULL
event_id_external TEXT
username TEXT
process_name TEXT
process_id INTEGER
command_line TEXT
source_ip TEXT
source_port INTEGER
destination_ip TEXT
destination_port INTEGER
hostname TEXT
severity TEXT
raw_log TEXT
metadata JSON
created_at DATETIME NOT NULL
```

## Relationships

```text
organizations
    |
    +-- users
    |
    +-- endpoints
    |      |
    |      +-- collectors
    |      |
    |      +-- events
    |
    +-- collectors
           |
           +-- events
```

## Rules

- Every event belongs to exactly one organization.
- Every event belongs to one collector.
- Every event belongs to one endpoint.
- The collector's endpoint and organization must match the authenticated collector.
- Do not trust organization or endpoint identifiers from untrusted requests.
- Add indexes for common event queries.
- Consider indexes on:
  - timestamp
  - organization_id
  - endpoint_id
  - collector_id
  - event_type
  - severity

## Future Compatibility

The schema should remain portable so that a future migration to PostgreSQL is possible without changing the application's logical data model.
