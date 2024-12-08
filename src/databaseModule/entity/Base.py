from sqlalchemy.orm import DeclarativeBase, declarative_base, as_declarative
from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData

@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, autoincrement=True)


