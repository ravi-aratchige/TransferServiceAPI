from models.account import AccountModel
from data.accounts import AccountDataManager
from fastapi import APIRouter, status, HTTPException

# Initialize accounts router
router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"],
)

# --------------------------------
#             ROUTES
# --------------------------------


# Test router health
@router.get("/ping", status_code=status.HTTP_200_OK)
def test_accounts_router():
    return {
        "message": "TransferServiceAPI Accounts router is up and running.",
    }


# Get all accounts
@router.get("/", status_code=status.HTTP_200_OK)
def get_all_accounts():
    # Initialize account data manager
    data_manager = AccountDataManager()

    # Retrieve accounts from data source
    accounts = data_manager.read_all()

    return {
        "message": "Accounts retrieved successfully",
        "data": accounts,
    }


# Get a single account by account_number
@router.get("/{account_number}", status_code=status.HTTP_200_OK)
def get_account(account_number: str):
    """Retrieve a specific account by its account_number."""

    # Initialize account data manager
    data_manager = AccountDataManager()

    # Retrieve all accounts
    accounts = data_manager.read_all()

    # Search for the specific account
    for account in accounts:
        if account.account_number == account_number:
            return {
                "message": "Account retrieved successfully",
                "data": account,
            }

    # If not found, raise a 404 error
    raise HTTPException(status_code=404, detail=f"Account {account_number} not found.")


# Create new account
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_account(new_account: AccountModel):
    # Initialize account data manager
    data_manager = AccountDataManager()

    # Create new account through data manager
    created_account = data_manager.create(new_account)

    return {
        "message": "Account created successfully",
        "data": created_account,
    }


# Make module safely exportable
if __name__ == "__main__":
    pass
