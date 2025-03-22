from pydantic import BaseModel, Field


class AccountModel(BaseModel):
    # Account number
    account_number: str

    # Account balance
    balance: float = Field(
        ge=0,
        description="Account balance cannot be negative.",
    )


# Make module safely exportable
if __name__ == "__main__":
    pass
