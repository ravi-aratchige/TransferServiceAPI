from fastapi import APIRouter

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
