#!/usr/bin/python3
"""
Contains the class definition of a State
and an instance Base = declarative_base():
State class:
- Inherits from Base
- Links to the MySQL table states
- Class attribute id that represents a column of
an auto-generated, unique integer, can’t be null and is a primary key
- Class attribute name that represents a column of a string
with maximum 128 characters and can’t be null
You must use the module SQLAlchemy.
Your script should connect to a MySQL server running on localhost at port 3306.
WARNING: All classes that inherit from Base must be imported
before calling Base.metadata.create_all(engine).
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    Represents a state in the hbtn_0e_6_usa database.

    Attributes:
        id (int): auto-generated, unique integer representing the primary key.
        name (str): A string representing the name of the states.
    """
    __tablename__ = 'states'
    id = Column(Integer,  primary_key=True)
    name = Column(String(128), nullable=False)
