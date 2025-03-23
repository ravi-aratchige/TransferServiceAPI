"""# Data Access Layer

This module acts as the bridge between the in-memory datasource (`database.py`)
which stores data as JSON objects, and the application's data models, which store data as Pydantic models.

This module contains the following utility classes:
1. `BaseDataManager` - super class for developing data manager classes for different data models. Includes
    a common constructor and `real_all()` method (to load data from the data source).
2. `AccountDataManager` - data manager for accounts. Extends `BaseDataManager`.
2. `TransferDataManager` - data manager for transfers. Extends `BaseDataManager`.
"""
