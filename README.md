# TransferServiceAPI

This is my take on the **Internship Programming Assignment** - Network Analytics and Automation Team, Group Technology at Dialog.

## Technologies 🔧

I selected the following technologies for this project:

- Programming Language - **Python**
- Web Framework - **FastAPI**

I selected Python as the programming language for this because Python is the programming language I am most proficient in. I'm passionate about AI and Machine Learning, and thus I spend a lot of my time coding in Python.

I selected FastAPI as the web framework since
- I have experience working with FastAPI,
- FastAPI is intuitive and easy to work with,
- FastAPI has great documentation, and
- FastAPI has a lot of features out-of-the-box which help with API development.

## Project Structure 🌲

```
.
├── data/                 # Data managers for handling accounts and transfers  
│   ├── accounts.py       # Manages account-related operations  
│   ├── base.py           # Abstract base class for data managers  
│   ├── __init__.py       # Package initializer  
│   └── transfers.py      # Manages transfer-related operations  
├── database.py           # In-memory database simulation (live & test modes)   
├── LICENSE               # License file for the project  
├── main.py               # Entry point of the FastAPI application  
├── models/               # Data models for API requests & responses  
│   ├── account.py        # Account model definition  
│   ├── __init__.py       # Package initializer  
│   └── transfer.py       # Transfer model definition  
├── README.md             # Project documentation  
├── requirements.txt      # Dependencies required to run the project  
├── routes/               # API route definitions  
│   ├── accounts.py       # Account-related API endpoints  
│   ├── __init__.py       # Package initializer  
│   └── transfers.py      # Transfer-related API endpoints  
├── settings.py           # Configuration settings (e.g., environment variables)   
└── tests/                # Unit tests for the API  
    ├── conftest.py       # Shared test fixtures (e.g., test client, database reset)  
    ├── __init__.py       # Package initializer  
    ├── test_accounts.py  # Tests for account-related functionality  
    └── test_transfers.py # Tests for transfer-related functionality  
```

## Setup ⚙️

Refer to [SETUP.MD](https://github.com/ravi-aratchige/TransferServiceAPI/blob/main/SETUP.md) for instructions on how to setup this project locally.

---

Made with ❤️ by Ravindu Aratchige
