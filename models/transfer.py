from pydantic import BaseModel, Field


class TransferModel(BaseModel):
    # Sender account
    sender_account: str

    # Receiver account
    receiver_account: str

    # Transfer amount
    amount: float = Field(
        gt=0,
        description="Transfer amount must be greater than zero.",
    )


# Make module safely exportable
if __name__ == "__main__":
    pass
