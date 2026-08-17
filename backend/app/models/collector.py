import uuid
from sqlalchemy import Column, DateTime, ForeignKey, Index, String
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.models.base import GUID, utc_now


class Collector(Base):
    __tablename__ = "collectors"

    collector_id = Column(GUID, primary_key=True, default=uuid.uuid4)
    organization_id = Column(GUID, ForeignKey("organizations.organization_id", ondelete="CASCADE"), nullable=False, index=True)
    endpoint_id = Column(GUID, ForeignKey("endpoints.endpoint_id", ondelete="CASCADE"), nullable=False, index=True)
    collector_name = Column(String(255), nullable=True)
    collector_version = Column(String(50), nullable=True)
    enrollment_token_hash = Column(String(255), nullable=True, index=True)
    status = Column(String(50), default="pending", nullable=False)  # pending, active, offline, revoked
    credential_hash = Column(String(255), nullable=True, index=True)
    last_seen_at = Column(DateTime, nullable=True)
    registered_at = Column(DateTime, default=utc_now, nullable=False)
    created_at = Column(DateTime, default=utc_now, nullable=False)
    updated_at = Column(DateTime, default=utc_now, onupdate=utc_now, nullable=False)

    # Relationships
    organization = relationship("Organization", back_populates="collectors")
    endpoint = relationship("Endpoint", back_populates="collectors")
    events = relationship("Event", back_populates="collector", cascade="all, delete-orphan")

    __table_args__ = (
        Index("ix_collectors_org_status", "organization_id", "status"),
        Index("ix_collectors_endpoint_status", "endpoint_id", "status"),
    )

    def __repr__(self) -> str:
        return f"<Collector(id={self.collector_id}, name='{self.collector_name}', status='{self.status}')>"
