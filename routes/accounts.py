from fastapi import APIRouter

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
@router.get("/ping", tags=["Debug"])
def test_router():
    return {
        "message": "TransferServiceAPI Accounts router is up and running.",
    }


# Get all accounts
@router.get("/")
def get_all_accounts():
    # Retrieve accounts from data source
    accounts = AccountDataManager.load_accounts()

    return {
        "message": "Accounts retrieved successfully",
        "data": accounts,
    }
