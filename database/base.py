import json
from settings import DATA_FILE_PATH

DB = DATA_FILE_PATH


class AbstractDataManager:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def read_all(self):
        """Retrieve all records from the JSON database."""

        # Load data from the data file
        with open(DB, "r") as db:
            data = json.load(db)

        # Convert each record in the category (self.name) into a model instance
        all_data = [self.model(**item) for item in data.get(self.name, [])]

        print(all_data)

        return all_data  # Return a list of model instances


# Make module safely exportable
if __name__ == "__main__":
    pass
