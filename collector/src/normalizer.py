from datetime import datetime, timezone
from typing import Any, Dict, Optional


def normalize_event(
    event_source: str,
    event_type: str,
    event_category: str,
    timestamp: Optional[datetime] = None,
    event_id_external: Optional[str] = None,
    username: Optional[str] = None,
    process_name: Optional[str] = None,
    process_id: Optional[int] = None,
    command_line: Optional[str] = None,
    source_ip: Optional[str] = None,
    source_port: Optional[int] = None,
    destination_ip: Optional[str] = None,
    destination_port: Optional[int] = None,
    hostname: Optional[str] = None,
    severity: str = "informational",
    raw_log: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Normalizes an event payload into the SOCUaTrace common event schema."""
    if timestamp is None:
        timestamp = datetime.now(timezone.utc)

    return {
        "timestamp": timestamp.isoformat(),
        "event_source": event_source,
        "event_type": event_type,
        "event_category": event_category,
        "event_id_external": str(event_id_external) if event_id_external is not None else None,
        "username": username,
        "process_name": process_name,
        "process_id": process_id,
        "command_line": command_line,
        "source_ip": source_ip,
        "source_port": source_port,
        "destination_ip": destination_ip,
        "destination_port": destination_port,
        "hostname": hostname,
        "severity": severity,
        "raw_log": raw_log,
        "metadata": metadata or {},
    }
