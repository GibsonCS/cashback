from app.services.cashback_service import calculate_cashback, get_queries_cashback
from sqlalchemy.orm import Session
from fastapi import APIRouter, Request, Depends
from app.schemas.CashbackRequest import CashbackRequest
from config.database import get_db

router = APIRouter()

@router.post("/cashback")
async def handleCashback(cashback_request: CashbackRequest, request: Request, db: Session = Depends(get_db)):
        return await calculate_cashback(cashback_request, request.client.host, db)

@router.get("/cashback")
async def handleGetQueriesCashback(request: Request, db: Session = Depends(get_db)):
        
        if(request.client.host == ""):
                raise RuntimeWarning("ip not found")
        
        return await get_queries_cashback(request.client.host, db)
