from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, index=True, unique=True, nullable=True)
    name = Column(String, index=True)
    description = Column(Text)
    category = Column(String)
    price = Column(Float)
    image_url = Column(String)


class Explanation(Base):
    __tablename__ = "explanations"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    query = Column(String)
    explanation = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product")
