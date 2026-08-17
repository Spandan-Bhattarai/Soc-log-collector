import json
import os
from typing import Any, Dict, List


class LocalEventQueue:
    """A resilient JSONL-based local queue for offline event buffering."""

    def __init__(self, file_path: str = "./queue.jsonl", max_items: int = 5000):
        self.file_path = file_path
        self.max_items = max_items

    def push(self, event: Dict[str, Any]) -> bool:
        """Appends an event to the local queue."""
        if self.count() >= self.max_items:
            return False

        with open(self.file_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(event) + "\n")
        return True

    def count(self) -> int:
        """Returns the number of buffered items."""
        if not os.path.exists(self.file_path):
            return 0
        with open(self.file_path, "r", encoding="utf-8") as f:
            return sum(1 for line in f if line.strip())

    def peek_batch(self, batch_size: int = 20) -> List[Dict[str, Any]]:
        """Reads up to `batch_size` items from the top of the queue without removing them."""
        if not os.path.exists(self.file_path):
            return []

        items = []
        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    items.append(json.loads(line))
                if len(items) >= batch_size:
                    break
        return items

    def pop_batch(self, count: int) -> None:
        """Removes the first `count` processed items from the queue."""
        if not os.path.exists(self.file_path) or count <= 0:
            return

        with open(self.file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        remaining = lines[count:]
        with open(self.file_path, "w", encoding="utf-8") as f:
            f.writelines(remaining)
