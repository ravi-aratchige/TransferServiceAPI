# TransferServiceAPI

This is my submission for the **Internship Programming Assignment** - Network Analytics and Automation Team, Group Technology at Dialog.

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

```shell
.
├── data/                 # Data managers module
│   ├── accounts.py       # Manages account-related operations  
│   ├── base.py           # Abstract base class for data managers  
│   ├── __init__.py       # Package initializer
│   └── transfers.py      # Manages transfer-related operations  
├── models/               # Data models for API requests & responses  
│   ├── account.py        # Account model definition  
│   ├── __init__.py       # Package initializer  
│   └── transfer.py       # Transfer model definition  
├── routes/               # API route definitions  
│   ├── accounts.py       # Account-related API endpoints  
│   ├── __init__.py       # Package initializer  
│   └── transfers.py      # Transfer-related API endpoints  
├── tests/                # Unit tests for the API  
│   ├── conftest.py       # Shared test fixtures (e.g. test client, DB reset)  
│   ├── __init__.py       # Package initializer  
│   ├── test_accounts.py  # Tests for account-related functionality  
│   └── test_transfers.py # Tests for transfer-related functionality  
├── Assignment.pdf        # Assignment document for the project  
├── database.py           # In-memory database simulation file  
├── Dockerfile            # Docker configuration file
├── LICENSE               # License file
├── main.py               # Entry point of the FastAPI application  
├── README.md             # Project documentation  
├── requirements.txt      # Dependencies required to run the project  
├── settings.py           # Configuration settings for the API  
├── SETUP.md              # Setup instructions for the project  
├── swagger.png           # Screenshot of the API documentation
└── tests.png             # Screenshot of test results   
```

## Setup ⚙️

Refer to [SETUP.MD](https://github.com/ravi-aratchige/TransferServiceAPI/blob/main/SETUP.md) for instructions on how to setup this project locally.

---

Made with ❤️ by Ravindu Aratchige
