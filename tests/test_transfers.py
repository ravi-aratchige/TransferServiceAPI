from fastapi.testclient import TestClient


def test_successful_transfer(client: TestClient):
    """Test a successful fund transfer between two accounts."""

    # Create sender and receiver accounts
    client.post("/accounts/", json={"account_number": "123456", "balance": 500.0})
    client.post("/accounts/", json={"account_number": "654321", "balance": 200.0})

    # Perform the transfer
    response = client.post(
        url="/transfers/",
        json={
            "sender_account": "123456",
            "receiver_account": "654321",
            "amount": 100.0,
        },
    )

    # Check status code (must be 201)
    assert response.status_code == 201

    # Check transfer response
    assert response.json() == {
        "data": {
            "sender_account": "123456",
            "receiver_account": "654321",
            "amount": 100.0,
        },
        "message": "Transfer created successfully",
    }

    # Verify updated balances
    sender_response = client.get("/accounts/123456")
    receiver_response = client.get("/accounts/654321")

    assert sender_response.status_code == 200
    assert receiver_response.status_code == 200

    assert sender_response.json()["data"]["balance"] == 400.0  # 500 - 100
    assert receiver_response.json()["data"]["balance"] == 300.0  # 200 + 100


def test_insufficient_funds(client: TestClient):
    """Test that a transfer fails when sender has insufficient funds."""

    # Create sender and receiver accounts
    client.post("/accounts/", json={"account_number": "123456", "balance": 50.0})
    client.post("/accounts/", json={"account_number": "654321", "balance": 200.0})

    # Attempt a transfer that exceeds sender's balance
    response = client.post(
        url="/transfers/",
        json={
            "sender_account": "123456",
            "receiver_account": "654321",
            "amount": 100.0,
        },
    )

    # Check status code (must be 403)
    assert response.status_code == 403

    # Ensure the error message mentions insufficient funds
    assert "Insufficient funds" in response.json()["detail"]

    # Verify that balances remain unchanged
    sender_response = client.get("/accounts/123456")
    receiver_response = client.get("/accounts/654321")

    assert sender_response.status_code == 200
    assert receiver_response.status_code == 200

    assert sender_response.json()["data"]["balance"] == 50.0
    assert receiver_response.json()["data"]["balance"] == 200.0


def test_transfer_nonexistent_sender(client: TestClient):
    """Test transfer fails if the sender account does not exist."""

    # Create only the receiver account
    client.post("/accounts/", json={"account_number": "654321", "balance": 200.0})

    # Attempt a transfer from a non-existent sender
    response = client.post(
        url="/transfers/",
        json={
            "sender_account": "999999",  # Does not exist
            "receiver_account": "654321",
            "amount": 100.0,
        },
    )

    # Check status code (must be 404)
    assert response.status_code == 404

    # Ensure the error message mentions the sender does not exist
    assert "Sender account 999999 does not exist" in response.json()["detail"]


def test_transfer_nonexistent_receiver(client: TestClient):
    """Test transfer fails if the receiver account does not exist."""

    # Create only the sender account
    client.post("/accounts/", json={"account_number": "123456", "balance": 500.0})

    # Attempt a transfer to a non-existent receiver
    response = client.post(
        url="/transfers/",
        json={
            "sender_account": "123456",
            "receiver_account": "999999",  # Does not exist
            "amount": 100.0,
        },
    )

    # Check status code (must be 404)
    assert response.status_code == 404

    # Ensure the error message mentions the receiver does not exist
    assert "Receiver account 999999 does not exist" in response.json()["detail"]
