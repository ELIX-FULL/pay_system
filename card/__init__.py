from pydantic import BaseModel


class CardAddValidator(BaseModel):
    user_id: int
    card_number: int
    balance: float
    card_name: str
    exp_date: int
