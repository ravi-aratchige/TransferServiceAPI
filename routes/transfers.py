from fastapi import APIRouter, status
from models.transfer import TransferModel
from data.transfers import TransferDataManager

# Initialize transfers router
router = APIRouter(
    prefix="/transfers",
    tags=["Transfers"],
)

# --------------------------------
#             ROUTES
# --------------------------------


# Test router health
@router.get("/ping", status_code=status.HTTP_200_OK)
def test_transfers_router():
    return {
        "message": "TransferServiceAPI Transfers router is up and running.",
    }


# Get all transfers
@router.get("/", status_code=status.HTTP_200_OK)
def get_all_transfers():
    # Initialize transfer data manager
    data_manager = TransferDataManager()

    # Retrieve transfers from data source
    transfers = data_manager.read_all()

    return {
        "message": "Transfers retrieved successfully",
        "data": transfers,
    }


# Create new transfer
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_transfer(new_transfer: TransferModel):
    # Initialize transfer data manager
    data_manager = TransferDataManager()

    # Create new transfer through data manager
    created_transfer = data_manager.create(new_transfer)

    return {
        "message": "Transfer created successfully",
        "data": created_transfer,
    }


# Make module safely exportable
if __name__ == "__main__":
    pass
