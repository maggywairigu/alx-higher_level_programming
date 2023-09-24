#!/usr/bin/python3
"""
Contains the class definition of a State
and an instance Base = declarative_base():
State class:
inherits from Base Tips
links to the MySQL table states
class attribute id that represents a column of
an auto-generated, unique integer, can’t be null and is a primary key
class attribute name that represents a column of a string with
maximum 128 characters and can’t be null
You must use the module SQLAlchemy
Your script should connect to a MySQL server running on localhost at port 3306
WARNING: all classes who inherit from Base must be
imported before calling Base.metadata.create_all(engine)
"""
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
