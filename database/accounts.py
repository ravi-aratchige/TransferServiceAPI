import json
from typing import List
from settings import DATA_FILE_PATH
from models.account import AccountModel
from database.base import AbstractDataManager

DB = DATA_FILE_PATH


class AccountDataManager(AbstractDataManager):
    def __init__(self, name="accounts", model=AccountModel):
        super().__init__(name, model)

    def create(self, new_account):
        """Create and save a new account, ensuring account_number is unique."""
        with open(DB, "r") as db:
            data = json.load(db)

        if self.name not in data:
            data[self.name] = []

        # Convert model object to dictionary
        new_account_dict = (
            new_account.dict() if hasattr(new_account, "dict") else vars(new_account)
        )

        # Check if the account already exists
        for item in data[self.name]:
            if item["account_number"] == new_account_dict["account_number"]:
                raise ValueError(
                    f"Account with account_number {new_account_dict['account_number']} already exists."
                )

        # Append and save the new record
        data[self.name].append(new_account_dict)

        with open(DB, "w") as db:
            json.dump(data, db, indent=4)

        return new_account_dict  # Return the created account


# Make module safely exportable
if __name__ == "__main__":
    pass
