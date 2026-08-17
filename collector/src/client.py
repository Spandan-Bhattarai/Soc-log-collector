from typing import Any, Dict, List, Optional
import httpx
from collector.src.config import CollectorConfig


class CollectorAPIClient:
    """HTTP Client for communicating with the central FastAPI server."""

    def __init__(self, config: CollectorConfig):
        self.config = config
        self.base_url = config.server_url.rstrip("/")
        self.headers = {
            "User-Agent": f"SOC-Collector/{config.collector_version}",
            "Content-Type": "application/json",
        }
        if config.collector_credential:
            self.headers["Authorization"] = f"Bearer {config.collector_credential}"

    def enroll(self, token: str) -> Dict[str, Any]:
        """Enroll the collector with an enrollment token."""
        url = f"{self.base_url}/collectors/enroll"
        payload = {
            "enrollment_token": token,
            "collector_name": self.config.collector_name,
            "collector_version": self.config.collector_version,
        }
        with httpx.Client(timeout=10.0) as client:
            response = client.post(url, json=payload, headers={"Content-Type": "application/json"})
            response.raise_for_status()
            return response.json()

    def send_heartbeat(self) -> Dict[str, Any]:
        """Send periodic heartbeat to maintain online status."""
        url = f"{self.base_url}/collectors/heartbeat"
        with httpx.Client(timeout=5.0) as client:
            response = client.post(url, headers=self.headers)
            response.raise_for_status()
            return response.json()

    def send_events(self, events: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Send a batch of normalized events."""
        url = f"{self.base_url}/events"
        with httpx.Client(timeout=10.0) as client:
            response = client.post(url, json=events, headers=self.headers)
            response.raise_for_status()
            return response.json()
