import uuid
from datetime import datetime, timezone
import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from app.models import Base, Organization, User, Endpoint, Collector, Event


@pytest.fixture(scope="function")
def db_session():
    """Provides a fresh, in-memory SQLite test database with foreign keys enabled."""
    engine = create_engine("sqlite:///:memory:", echo=False)

    @event.listens_for(engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)


def test_create_organization_and_user(db_session):
    org = Organization(
        name="Security Operations Corp",
        slug="soc-corp",
        is_active=True,
    )
    db_session.add(org)
    db_session.commit()
    db_session.refresh(org)

    assert isinstance(org.organization_id, uuid.UUID)
    assert org.slug == "soc-corp"
    assert org.is_active is True
    assert org.created_at is not None

    # Add user
    user = User(
        organization_id=org.organization_id,
        email="analyst@soc-corp.com",
        password_hash="$2b$12$securehashvalue",
        display_name="SOC Analyst",
        role="analyst",
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    assert isinstance(user.user_id, uuid.UUID)
    assert user.organization_id == org.organization_id
    assert user.email == "analyst@soc-corp.com"
    assert user.role == "analyst"
    assert user.is_active is True

    # Relationship check
    assert len(org.users) == 1
    assert org.users[0].email == "analyst@soc-corp.com"
    assert user.organization.name == "Security Operations Corp"


def test_unique_constraints(db_session):
    org1 = Organization(name="Org 1", slug="unique-slug")
    db_session.add(org1)
    db_session.commit()

    # Duplicate slug should fail
    org2 = Organization(name="Org 2", slug="unique-slug")
    db_session.add(org2)
    with pytest.raises(IntegrityError):
        db_session.commit()
    db_session.rollback()

    # Duplicate user email should fail
    user1 = User(
        organization_id=org1.organization_id,
        email="duplicate@example.com",
        password_hash="hash1",
        display_name="User 1",
    )
    db_session.add(user1)
    db_session.commit()

    user2 = User(
        organization_id=org1.organization_id,
        email="duplicate@example.com",
        password_hash="hash2",
        display_name="User 2",
    )
    db_session.add(user2)
    with pytest.raises(IntegrityError):
        db_session.commit()
    db_session.rollback()


def test_endpoint_and_collector_relationships(db_session):
    org = Organization(name="Acme SOC", slug="acme-soc")
    db_session.add(org)
    db_session.commit()

    endpoint = Endpoint(
        organization_id=org.organization_id,
        hostname="WIN-SRV-2026",
        os_name="Windows Server 2022",
        os_version="10.0.20348",
        architecture="x86_64",
        ip_address="10.0.1.100",
        status="active",
    )
    db_session.add(endpoint)
    db_session.commit()
    db_session.refresh(endpoint)

    collector = Collector(
        organization_id=org.organization_id,
        endpoint_id=endpoint.endpoint_id,
        collector_name="endpoint-agent-01",
        collector_version="0.1.0",
        enrollment_token_hash="hash_enroll_token",
        credential_hash="hash_cred",
        status="active",
    )
    db_session.add(collector)
    db_session.commit()
    db_session.refresh(collector)

    assert len(org.endpoints) == 1
    assert len(org.collectors) == 1
    assert len(endpoint.collectors) == 1
    assert endpoint.collectors[0].collector_id == collector.collector_id
    assert collector.endpoint.hostname == "WIN-SRV-2026"


def test_event_ingestion_and_querying(db_session):
    org = Organization(name="SOC Lab", slug="soc-lab")
    db_session.add(org)
    db_session.commit()

    endpoint = Endpoint(organization_id=org.organization_id, hostname="DESKTOP-SEC")
    db_session.add(endpoint)
    db_session.commit()

    collector = Collector(
        organization_id=org.organization_id,
        endpoint_id=endpoint.endpoint_id,
        status="active",
    )
    db_session.add(collector)
    db_session.commit()

    # Add Event (Windows 4625 Failed Logon)
    now = datetime.now(timezone.utc)
    event_entry = Event(
        organization_id=org.organization_id,
        collector_id=collector.collector_id,
        endpoint_id=endpoint.endpoint_id,
        timestamp=now,
        event_source="windows_security",
        event_type="authentication_failure",
        event_category="authentication",
        event_id_external="4625",
        username="administrator",
        source_ip="192.168.1.105",
        hostname="DESKTOP-SEC",
        severity="medium",
        raw_log="Event 4625: An account failed to log on.",
        event_metadata={"failure_reason": "unknown_user_name_or_bad_password", "workstation_name": "DESKTOP-SEC"},
    )
    db_session.add(event_entry)
    db_session.commit()
    db_session.refresh(event_entry)

    assert isinstance(event_entry.event_id, uuid.UUID)
    assert event_entry.event_type == "authentication_failure"
    assert event_entry.event_metadata["failure_reason"] == "unknown_user_name_or_bad_password"

    # Query event by organization and category
    results = (
        db_session.query(Event)
        .filter(
            Event.organization_id == org.organization_id,
            Event.event_category == "authentication",
        )
        .all()
    )
    assert len(results) == 1
    assert results[0].event_id_external == "4625"


def test_foreign_key_enforcement(db_session):
    fake_org_id = uuid.uuid4()
    # Inserting user with non-existent org_id must fail foreign key check
    user = User(
        organization_id=fake_org_id,
        email="invalid@example.com",
        password_hash="pass",
        display_name="Invalid",
    )
    db_session.add(user)
    with pytest.raises(IntegrityError):
        db_session.commit()
    db_session.rollback()


def test_cascading_delete(db_session):
    org = Organization(name="Ephemeral Org", slug="ephemeral-org")
    db_session.add(org)
    db_session.commit()

    endpoint = Endpoint(organization_id=org.organization_id, hostname="EPHEMERAL-HOST")
    db_session.add(endpoint)
    db_session.commit()

    collector = Collector(organization_id=org.organization_id, endpoint_id=endpoint.endpoint_id)
    db_session.add(collector)
    db_session.commit()

    event_entry = Event(
        organization_id=org.organization_id,
        collector_id=collector.collector_id,
        endpoint_id=endpoint.endpoint_id,
        timestamp=datetime.now(timezone.utc),
        event_source="windows_security",
        event_type="logon",
        event_category="authentication",
    )
    db_session.add(event_entry)
    db_session.commit()

    # Deleting organization should cascade to endpoints, collectors, and events
    db_session.delete(org)
    db_session.commit()

    assert db_session.query(Organization).count() == 0
    assert db_session.query(Endpoint).count() == 0
    assert db_session.query(Collector).count() == 0
    assert db_session.query(Event).count() == 0
