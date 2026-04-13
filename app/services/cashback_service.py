from app.schemas.CashbackRequest import CashbackRequest
from app.models.cashback import Cashback
from sqlalchemy.orm import Session
from datetime import datetime

async def calculate_cashback(cashbackRequest: CashbackRequest, ip_address: str, db: Session):

    if(cashbackRequest.value < 0):
        raise RuntimeWarning("The value must be more than zero")
    
    base_cashback =  0.05
    
    new_cashback = Cashback()

    if(cashbackRequest.value > 500):
        base_cashback *= 2
    
    if(cashbackRequest.client_type == 'VIP'):

        new_cashback.client_type = cashbackRequest.client_type
        new_cashback.value = cashbackRequest.value
        new_cashback.cashback = calculateVipCashback(cashbackRequest.value, base_cashback)
        new_cashback.ip_address = ip_address
        new_cashback.query_date = datetime.now()

        db.add(new_cashback)
        db.commit()
        db.refresh(new_cashback)
        
        return {"cashback": new_cashback.cashback}

    new_cashback.client_type = cashbackRequest.client_type
    new_cashback.value = cashbackRequest.value
    new_cashback.cashback = cashbackRequest.value * base_cashback
    new_cashback.ip_address = ip_address
    new_cashback.query_date = datetime.now()

    db.add(new_cashback)
    db.commit()
    db.refresh(new_cashback)

    return {"cashback": new_cashback.cashback}

def calculateVipCashback(value: float, base_cashback: float):
    return (value * base_cashback) + (value * base_cashback) * 0.10

