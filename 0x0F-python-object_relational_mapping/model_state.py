#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine(
    'mysql://root:root/root@localhost:3306/hbtn_0e_6_usa', echo=True)
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
