# Main in-memory database
db = {
    "accounts": [
        {"account_number": "123456", "balance": 1000.0},
        {"account_number": "654321", "balance": 500.0},
        {"account_number": "111111", "balance": 200.0},
        {"account_number": "222222", "balance": 300.0},
    ],
    "transfers": [
        {"sender_account": "123456", "receiver_account": "654321", "amount": 150.0},
        {"sender_account": "222222", "receiver_account": "111111", "amount": 50.0},
    ],
}

# Separate test database
test_db = {
    "accounts": [
        {"account_number": "000001", "balance": 10000.0},
        {"account_number": "000002", "balance": 5000.0},
    ],
    "transfers": [],
}
