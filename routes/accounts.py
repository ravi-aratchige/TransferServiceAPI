from fastapi import APIRouter
from models.account import AccountModel
from database.accounts import AccountDataManager

# Initialize accounts router
router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"],
)

# --------------------------------
#             ROUTES
# --------------------------------


# Test router health
@router.get("/ping")
def test_accounts_router():
    return {
        "message": "TransferServiceAPI Accounts router is up and running.",
    }


# Get all accounts
@router.get("/")
def get_all_accounts():
    # Initialize account data manager
    data_manager = AccountDataManager()

    # Retrieve accounts from data source
    accounts = data_manager.read_all()

    return {
        "message": "Accounts retrieved successfully",
        "data": accounts,
    }


# Create new account
@router.post("/")
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
