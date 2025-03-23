import pytest
from main import app
from database import test_db
from fastapi.testclient import TestClient


# Create a shared test client
@pytest.fixture(scope="module")
def client():
    return TestClient(app)


# Ensure a fresh test database for each test
@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Reset test database before and after each test."""
    test_db.clear()
    yield

    test_db.clear()
