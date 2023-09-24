#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base = declarative_base():

State class:
- Inherits from Base
- Links to the MySQL table states
- Class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
- Class attribute name that represents a column of a string with maximum 128 characters and can’t be null

You must use the module SQLAlchemy.
Your script should connect to a MySQL server running on localhost at port 3306.
WARNING: All classes that inherit from Base must be imported before calling Base.metadata.create_all(engine).
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine(
    'mysql://root:root/root@localhost:3306/hbtn_0e_6_usa', echo=True)
Base = declarative_base()


class State(Base):
     """
    Represents a state in the hbtn_0e_6_usa database.

    Attributes:
        id (int): An auto-generated, unique integer representing the primary key.
        name (str): A string representing the name of the state with a maximum length of 128 characters.
    """
     __tablename__ = 'states'

     id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
     name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
