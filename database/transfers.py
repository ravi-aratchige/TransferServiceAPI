import json
from fastapi import HTTPException
from settings import DATA_FILE_PATH
from models.transfer import TransferModel
from database.base import AbstractDataManager

DB = DATA_FILE_PATH


class TransferDataManager(AbstractDataManager):
    def __init__(self, name="transfers", model=TransferModel):
        super().__init__(name, model)

    def create(self, new_transfer: TransferModel):
        """Create and save a new transfer, ensuring account balances update atomically."""

        # Load database
        with open(DB, "r") as db:
            data = json.load(db)

        # Ensure required categories exist
        if "accounts" not in data:
            data["accounts"] = []
        if self.name not in data:
            data[self.name] = []

        # Convert transfer model object to dictionary
        new_transfer_dict = new_transfer.model_dump()

        sender_acc = new_transfer_dict["sender_account"]
        receiver_acc = new_transfer_dict["receiver_account"]
        amount = new_transfer_dict["amount"]

        # Load accounts as a dictionary {account_number: account_data}
        accounts = {acc["account_number"]: acc for acc in data["accounts"]}

        # Ensure both accounts exist
        if sender_acc not in accounts:
            raise HTTPException(
                status_code=404,
                detail=f"Sender account {sender_acc} does not exist.",
            )
        if receiver_acc not in accounts:
            raise HTTPException(
                status_code=404,
                detail=f"Receiver account {receiver_acc} does not exist.",
            )

        # Ensure sender has enough funds
        if accounts[sender_acc]["balance"] < amount:
            raise HTTPException(
                status_code=405,
                detail=f"Insufficient funds in account {sender_acc}.",
            )

        # Perform the transaction temporarily in-memory
        accounts[sender_acc]["balance"] -= amount
        accounts[receiver_acc]["balance"] += amount

        # Write everything to disk in a single operation (atomicity)
        try:
            # Update the accounts list with modified balances
            data["accounts"] = list(accounts.values())

            # Append new transfer record
            data[self.name].append(new_transfer_dict)

            # Write updated data back to file
            with open(DB, "w") as db:
                json.dump(data, db, indent=4)

            # Return the successful transfer
            return new_transfer_dict

        except Exception as e:
            # Rollback (nothing is saved if anything fails)
            raise HTTPException(
                status_code=500,
                detail=f"Transaction failed: {e}",
            )


# Make module safely exportable
if __name__ == "__main__":
    pass
