from datetime import datetime
from typing import Any, Dict, Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field


class HealthResponse(BaseModel):
    status: str = "ok"
    version: str = "0.1.0"
    environment: str
    timestamp: datetime


class EventBaseSchema(BaseModel):
    timestamp: datetime
    event_source: str = Field(..., max_length=100)
    event_type: str = Field(..., max_length=100)
    event_category: str = Field(..., max_length=100)
    event_id_external: Optional[str] = Field(None, max_length=100)
    username: Optional[str] = Field(None, max_length=255)
    process_name: Optional[str] = Field(None, max_length=500)
    process_id: Optional[int] = None
    command_line: Optional[str] = None
    source_ip: Optional[str] = Field(None, max_length=100)
    source_port: Optional[int] = Field(None, ge=0, le=65535)
    destination_ip: Optional[str] = Field(None, max_length=100)
    destination_port: Optional[int] = Field(None, ge=0, le=65535)
    hostname: Optional[str] = Field(None, max_length=255)
    severity: Optional[str] = Field("informational", max_length=50)
    raw_log: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)


class EventIngestPayload(EventBaseSchema):
    """Event submitted by collector - identity IDs are populated/overwritten server-side."""
    event_id: Optional[UUID] = None


class EventResponse(EventBaseSchema):
    event_id: UUID
    organization_id: UUID
    collector_id: UUID
    endpoint_id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
