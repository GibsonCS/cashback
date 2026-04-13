from app.services.cashback_service import calculate_cashback
from sqlalchemy.orm import Session
from fastapi import APIRouter, Request, Depends
from app.schemas.CashbackRequest import CashbackRequest
from config.database import get_db

router = APIRouter()

@router.post("/cashback")
async def handleCashback(cashback_request: CashbackRequest, request: Request, db: Session = Depends(get_db)):
        return await calculate_cashback(cashback_request, request.client.host, db)