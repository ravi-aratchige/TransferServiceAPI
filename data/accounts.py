from settings import TEST_MODE
from database import db, test_db
from fastapi import HTTPException
from models.account import AccountModel
from data.base import AbstractDataManager


class AccountDataManager(AbstractDataManager):

    def __init__(self, name="accounts", model=AccountModel, test_mode=TEST_MODE):
        super().__init__(name, model, test_mode)
        self.database = test_db if test_mode else db

    def create(self, new_account: AccountModel):
        """Create and save a new account, ensuring account_number is unique."""

        # Ensure the 'accounts' category exists
        if self.name not in self.database:
            self.database[self.name] = []

        # Convert model object to dictionary
        new_account_dict = (
            new_account.model_dump()
            if hasattr(new_account, "dict")
            else vars(new_account)
        )

        # Check if the account already exists
        for item in self.database[self.name]:
            if item["account_number"] == new_account_dict["account_number"]:
                raise HTTPException(
                    status_code=400,
                    detail=f"Account with account_number {new_account_dict['account_number']} already exists.",
                )

        # Append new account to in-memory database
        self.database[self.name].append(new_account_dict)

        # Return the created account
        return new_account_dict


# Make module safely exportable
if __name__ == "__main__":
    pass
