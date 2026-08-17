import uuid
from sqlalchemy import Column, DateTime, ForeignKey, Index, String
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.models.base import GUID, utc_now


class Endpoint(Base):
    __tablename__ = "endpoints"

    endpoint_id = Column(GUID, primary_key=True, default=uuid.uuid4)
    organization_id = Column(GUID, ForeignKey("organizations.organization_id", ondelete="CASCADE"), nullable=False, index=True)
    hostname = Column(String(255), nullable=False)
    os_name = Column(String(100), nullable=True)
    os_version = Column(String(100), nullable=True)
    architecture = Column(String(50), nullable=True)
    ip_address = Column(String(100), nullable=True)
    mac_address = Column(String(50), nullable=True)
    status = Column(String(50), default="active", nullable=False)  # pending, active, offline, revoked
    last_seen_at = Column(DateTime, nullable=True)
    registered_at = Column(DateTime, default=utc_now, nullable=False)
    created_at = Column(DateTime, default=utc_now, nullable=False)
    updated_at = Column(DateTime, default=utc_now, onupdate=utc_now, nullable=False)

    # Relationships
    organization = relationship("Organization", back_populates="endpoints")
    collectors = relationship("Collector", back_populates="endpoint", cascade="all, delete-orphan")
    events = relationship("Event", back_populates="endpoint", cascade="all, delete-orphan")

    __table_args__ = (
        Index("ix_endpoints_org_hostname", "organization_id", "hostname"),
        Index("ix_endpoints_org_status", "organization_id", "status"),
    )

    def __repr__(self) -> str:
        return f"<Endpoint(id={self.endpoint_id}, hostname='{self.hostname}', status='{self.status}')>"
