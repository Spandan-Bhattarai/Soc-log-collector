import uuid
from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.models.base import GUID, utc_now


class Organization(Base):
    __tablename__ = "organizations"

    organization_id = Column(GUID, primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=utc_now, nullable=False)
    updated_at = Column(DateTime, default=utc_now, onupdate=utc_now, nullable=False)

    # Relationships
    users = relationship("User", back_populates="organization", cascade="all, delete-orphan")
    endpoints = relationship("Endpoint", back_populates="organization", cascade="all, delete-orphan")
    collectors = relationship("Collector", back_populates="organization", cascade="all, delete-orphan")
    events = relationship("Event", back_populates="organization", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Organization(id={self.organization_id}, slug='{self.slug}')>"
