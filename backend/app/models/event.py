import uuid
from sqlalchemy import JSON, Column, DateTime, ForeignKey, Index, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.models.base import GUID, utc_now


class Event(Base):
    __tablename__ = "events"

    event_id = Column(GUID, primary_key=True, default=uuid.uuid4)
    organization_id = Column(GUID, ForeignKey("organizations.organization_id", ondelete="CASCADE"), nullable=False, index=True)
    collector_id = Column(GUID, ForeignKey("collectors.collector_id", ondelete="CASCADE"), nullable=False, index=True)
    endpoint_id = Column(GUID, ForeignKey("endpoints.endpoint_id", ondelete="CASCADE"), nullable=False, index=True)

    timestamp = Column(DateTime, nullable=False, index=True)
    event_source = Column(String(100), nullable=False)
    event_type = Column(String(100), nullable=False, index=True)
    event_category = Column(String(100), nullable=False, index=True)
    event_id_external = Column(String(100), nullable=True)

    username = Column(String(255), nullable=True, index=True)
    process_name = Column(String(500), nullable=True)
    process_id = Column(Integer, nullable=True)
    command_line = Column(Text, nullable=True)
    source_ip = Column(String(100), nullable=True, index=True)
    source_port = Column(Integer, nullable=True)
    destination_ip = Column(String(100), nullable=True)
    destination_port = Column(Integer, nullable=True)
    hostname = Column(String(255), nullable=True, index=True)
    severity = Column(String(50), default="informational", nullable=True, index=True)
    raw_log = Column(Text, nullable=True)
    event_metadata = Column("metadata", JSON, nullable=True)

    created_at = Column(DateTime, default=utc_now, nullable=False)

    # Relationships
    organization = relationship("Organization", back_populates="events")
    endpoint = relationship("Endpoint", back_populates="events")
    collector = relationship("Collector", back_populates="events")

    __table_args__ = (
        Index("ix_events_org_timestamp", "organization_id", "timestamp"),
        Index("ix_events_org_severity", "organization_id", "severity"),
        Index("ix_events_org_category", "organization_id", "event_category"),
        Index("ix_events_org_endpoint", "organization_id", "endpoint_id"),
    )

    def __repr__(self) -> str:
        return f"<Event(id={self.event_id}, type='{self.event_type}', source='{self.event_source}')>"
