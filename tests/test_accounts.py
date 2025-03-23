from fastapi.testclient import TestClient


def test_create_account(client: TestClient):
    """Test creating a new account via API."""

    # Create a new account in the test database
    response = client.post(
        url="/accounts/",
        json={"account_number": "999999", "balance": 100.0},
    )

    # Check status code (must be 201)
    assert response.status_code == 201

    # Check response returned
    assert response.json() == {
        "data": {"account_number": "999999", "balance": 100.0},
        "message": "Account created successfully",
    }


def test_get_account(client: TestClient):
    """Test retrieving an existing account via API."""

    # Create an account first
    client.post(
        url="/accounts/",
        json={"account_number": "123456", "balance": 250.0},
    )

    # Retrieve the account
    response = client.get("/accounts/123456")

    # Check status code (must be 200)
    assert response.status_code == 200

    # Check that the retrieved account matches the created one
    assert response.json() == {
        "data": {"account_number": "123456", "balance": 250.0},
        "message": "Account retrieved successfully",
    }


def test_duplicate_account(client: TestClient):
    """Test creating a duplicate account should return an error."""

    # First creation
    client.post(
        url="/accounts/",
        json={"account_number": "999999", "balance": 100.0},
    )
    # Duplicate
    response = client.post(
        url="/accounts/",
        json={"account_number": "999999", "balance": 200.0},
    )

    # Check status code (must be 400)
    assert response.status_code == 400

    # Check response returned (must contain the words "already exists")
    assert "already exists" in response.json()["detail"]
