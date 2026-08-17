# Security Requirements

## 1. Threat Model

This project receives data from endpoint collectors over a network.

Assume:

- the endpoint can be compromised
- logs can contain malicious strings
- collectors can be stolen or copied
- clients can send forged requests
- users can attempt horizontal privilege escalation
- attackers can send oversized payloads
- secrets can leak if configuration is handled incorrectly

## 2. Authentication

Passwords must be hashed using a modern password hashing algorithm such as Argon2id or bcrypt through a maintained library.

Never store plaintext passwords.

## 3. Collector Credentials

Enrollment tokens must be:

- high entropy
- short-lived or one-time where possible
- stored only as hashes on the server

Long-lived collector credentials should also be protected and preferably stored as hashes server-side.

Implement credential rotation when practical.

## 4. Authorization

Authorization must happen on the server.

Never trust:

- organization_id
- user_id
- endpoint_id
- collector_id

provided by the frontend.

The backend must determine ownership from the authenticated identity.

## 5. Transport

Collector traffic must use HTTPS outside local development.

Do not disable TLS verification in the collector as a permanent solution.

## 6. Log Safety

Logs are data, not commands.

Never execute:

- command_line
- PowerShell content
- process names
- URLs
- file paths

received from events.

Escape or safely render untrusted values in the frontend.

## 7. Secrets

Use environment variables for:

- secret keys
- database configuration
- development credentials
- external service credentials

Use `.env.example` for documentation.

Never commit `.env`.

## 8. Input Validation

Validate:

- string length
- timestamps
- IP addresses where appropriate
- port ranges
- event types
- payload sizes
- JSON metadata size

Reject malformed or excessively large requests.

## 9. Audit Logging

Record important administrative actions such as:

- login
- endpoint creation
- collector enrollment
- collector revocation
- user changes

Do not store passwords or raw credentials in audit logs.

## 10. Collector Hardening

The collector should:

- run with only the privileges it needs
- avoid unnecessary network listeners
- use HTTPS
- keep credentials out of command-line arguments where possible
- limit local queue size
- avoid logging secrets

## 11. Development Security

Do not solve development problems by:

- disabling authentication
- accepting all origins permanently
- disabling TLS verification permanently
- hard-coding credentials
- granting excessive privileges
- trusting client-provided organization IDs
