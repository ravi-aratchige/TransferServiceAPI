from settings import TEST_MODE
from database import db, test_db


class BaseDataManager:
    def __init__(self, name, model, test_mode=TEST_MODE):
        self.name = name
        self.model = model
        self.database = test_db if test_mode else db

    def read_all(self):
        """Retrieve all records from the in-memory database.

        Returns:
            list: list of items retrieved from the database
        """

        # Get all records for this data category
        all_data = [self.model(**item) for item in self.database.get(self.name, [])]

        # Return a list of model instances
        return all_data


# Make module safely exportable
if __name__ == "__main__":
    pass
