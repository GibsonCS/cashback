from config.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Float, text

class Cashback(Base):
    __tablename__ = "cashback"

    id = Column(Integer, primary_key=True, nullable=False)
    client_type = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    cashback = Column(Float, nullable=False)
    ip_address = Column(String, nullable=False)
    query_date = Column(TIMESTAMP(timezone=True), server_default=text('now()'))