#!/usr/bin/python3
"""
Defines a state model
Inherits from MySQLAlchemy Base and links to MySQL table states
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database
    __tablename__(str): The name of the MySQL table to store States
    id(sqlalchemy.Integer): The state's id
    name(sqlalchemy.String): The state's name
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
