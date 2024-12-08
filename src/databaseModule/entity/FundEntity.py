from sqlalchemy.orm import DeclarativeBase, declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData

Base = declarative_base()

class FundEntity(Base):
    __tablename__ = "funds"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fund = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<FundEntity(id={self.id}, fund='{self.fund}', price={self.price}, quantity={self.quantity})>"

