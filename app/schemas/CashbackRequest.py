from pydantic import BaseModel
from app.enum.ClienteType import ClienteType

class CashbackRequest(BaseModel):
    client_type: ClienteType
    value: float
