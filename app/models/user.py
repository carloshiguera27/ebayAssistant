from sqlalchemy import Column, String, Boolean, Text, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    scopes = Column(Text, default="")

    # eBay API credentials
    ebay_client_id = Column(String)
    ebay_client_secret = Column(String)
    ebay_refresh_token = Column(String)
