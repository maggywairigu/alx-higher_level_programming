#!/usr/bin/python3
"""
Define a city model
Inherits from MySQLAlchemy Base and links to MySQL table cities
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """
    Represents a state for a MYSQL database
    __tablename__(str): The name of the MySQL table to store cities
    id(sqlalchemy.Integer): The cities` id
    name(sqlalchemy.String): The cities` name
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
