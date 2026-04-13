from fastapi import FastAPI
from app.controllers.cashback_controller import router as cashbackController

app = FastAPI(title="Supreme cashback API")

app.include_router(cashbackController, prefix="/api")


