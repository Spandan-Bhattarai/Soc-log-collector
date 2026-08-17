from collector.src.normalizer import normalize_event
from collector.src.queue import LocalEventQueue
import os


def test_normalize_event_basic():
    event = normalize_event(
        event_source="windows_security",
        event_type="authentication_failure",
        event_category="authentication",
        event_id_external="4625",
        username="administrator",
        source_ip="192.168.1.50",
        severity="medium",
    )
    assert event["event_source"] == "windows_security"
    assert event["event_type"] == "authentication_failure"
    assert event["event_category"] == "authentication"
    assert event["event_id_external"] == "4625"
    assert event["username"] == "administrator"
    assert event["source_ip"] == "192.168.1.50"
    assert event["severity"] == "medium"
    assert "timestamp" in event


def test_local_event_queue(tmp_path):
    queue_file = str(tmp_path / "test_queue.jsonl")
    q = LocalEventQueue(file_path=queue_file, max_items=10)

    assert q.count() == 0

    event1 = {"id": 1, "type": "auth"}
    event2 = {"id": 2, "type": "proc"}

    q.push(event1)
    q.push(event2)

    assert q.count() == 2

    batch = q.peek_batch(batch_size=1)
    assert len(batch) == 1
    assert batch[0]["id"] == 1

    q.pop_batch(1)
    assert q.count() == 1

    batch_remaining = q.peek_batch(batch_size=10)
    assert len(batch_remaining) == 1
    assert batch_remaining[0]["id"] == 2
