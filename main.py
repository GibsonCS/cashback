from fastapi import FastAPI
from app.controllers.cashback_controller import router as cashbackController
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from config.database import engine, Base
from app.models.cashback import Cashback

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)

    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cashbackController, prefix="/api")


