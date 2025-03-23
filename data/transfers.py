from settings import TEST_MODE
from database import db, test_db
from fastapi import HTTPException
from data.base import BaseDataManager
from models.transfer import TransferModel


class TransferDataManager(BaseDataManager):
    def __init__(self, name="transfers", model=TransferModel, test_mode=TEST_MODE):
        super().__init__(name, model, test_mode)
        self.name = name
        self.model = model
        self.database = test_db if test_mode else db

    def create(self, new_transfer: TransferModel):
        """Create and save a new transfer, ensuring account balances update atomically.

        Args:
            new_transfer (TransferModel): the new transfer's Pydantic object

        Raises:
            HTTPException: 404 if sender account does not exist
            HTTPException: 404 if receiver account does not exist
            HTTPException: 403 if insufficient funds in account

        Returns:
            dict: the newly recorded transfer
        """

        # Ensure required categories exist
        if "accounts" not in self.database:
            self.database["accounts"] = []
        if self.name not in self.database:
            self.database[self.name] = []

        # Convert transfer model object to dictionary
        new_transfer_dict = new_transfer.model_dump()

        sender_acc = new_transfer_dict["sender_account"]
        receiver_acc = new_transfer_dict["receiver_account"]
        amount = new_transfer_dict["amount"]

        # Load accounts as a dictionary {account_number: account_data}
        accounts = {}
        for acc in self.database["accounts"]:
            accounts[acc["account_number"]] = acc

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
                status_code=403,
                detail=f"Insufficient funds in account {sender_acc}.",
            )

        # Perform the transaction in-memory (atomic)
        accounts[sender_acc]["balance"] -= amount
        accounts[receiver_acc]["balance"] += amount

        # Update the accounts list with modified balances
        self.database["accounts"] = list(accounts.values())

        # Append new transfer record
        self.database[self.name].append(new_transfer_dict)

        # Return the successful transfer
        return new_transfer_dict


# Make module safely exportable
if __name__ == "__main__":
    pass
