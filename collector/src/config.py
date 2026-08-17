import os
from typing import Optional
from pydantic import BaseModel, Field


class CollectorConfig(BaseModel):
    server_url: str = Field(default_factory=lambda: os.getenv("COLLECTOR_SERVER_URL", "http://localhost:8000/api/v1"))
    enrollment_token: Optional[str] = Field(default_factory=lambda: os.getenv("COLLECTOR_ENROLLMENT_TOKEN", None))
    collector_credential: Optional[str] = Field(default_factory=lambda: os.getenv("COLLECTOR_CREDENTIAL", None))
    collector_name: str = Field(default_factory=lambda: os.getenv("COLLECTOR_NAME", "endpoint-collector-01"))
    collector_version: str = "0.1.0"
    heartbeat_interval_seconds: int = Field(default_factory=lambda: int(os.getenv("COLLECTOR_HEARTBEAT_INTERVAL_SECONDS", "60")))
    batch_size: int = Field(default_factory=lambda: int(os.getenv("COLLECTOR_BATCH_SIZE", "20")))
    queue_file_path: str = Field(default_factory=lambda: os.getenv("COLLECTOR_LOCAL_QUEUE_FILE", "./queue.jsonl"))
    max_queue_items: int = 5000
