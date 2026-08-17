from datetime import datetime, timezone
import uuid
from sqlalchemy import Column, DateTime
from sqlalchemy.types import String, TypeDecorator
from app.db.session import Base


class GUID(TypeDecorator):
    """Platform-independent GUID type.
    Uses string(36) for SQLite storage while working with Python UUID objects.
    """
    impl = String(36)
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif isinstance(value, uuid.UUID):
            return str(value)
        return str(uuid.UUID(str(value)))

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        return uuid.UUID(str(value))


def utc_now() -> datetime:
    return datetime.now(timezone.utc)
