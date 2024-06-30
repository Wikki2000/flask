#!/usr/bin/python3
"""This models the storage for users data."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """Class models of user data table.

    Attribute:
        name (string): 
    """
    __tablename__ = "users"

    name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    password = Column(String(5000), nullable=False)
