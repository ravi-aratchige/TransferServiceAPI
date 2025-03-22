import json
from typing import List
from settings import DATA_FILE_PATH
from models.account import AccountModel

DB = DATA_FILE_PATH


class AccountDataManager:
    @staticmethod
    def load_accounts() -> List[AccountModel]:
        """Load all accounts from the data source (data file or database).

        Returns:
            List[AccountModel]: List containing all of the accounts.
        """

        # Read all data from data file
        with open(DB, "r") as db:
            data = json.load(db)

        # Initialize empty accounts dict to load data from data file
        accounts = {}

        for account in data["accounts"]:
            # Convert JSON account dict to account model object
            account_obj = AccountModel(**account)

            # Add account model object to accounts dict
            accounts[account["account_number"]] = account_obj

        return accounts
