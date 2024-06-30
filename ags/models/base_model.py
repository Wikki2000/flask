#!/usr/bin/python3
"""
<base_module>: Models the bas class for user_authentication application
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from uuid import uuid4
from datetime import datetime
import models

Base = declarative_base()


class BaseModel:
    """Defines common attributes/method for other class."""
    __abstract__ = True
    id = Column(String(60), primary_key=True, nullable=False)
    create_at = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        """Create instance of base model

        Args:
            args: Won't be use.
            kwargs: The attribute that will be instantiated
        """
        self.id = str(uuid4())
        self.create_at = datetime.now()
        self.__dict__.update(**kwargs)

    def save(self):
        """Save an instance to database."""
        models.storage.new(self)
        models.storage.save()

    @classmethod
    def get_user_email(cls, email):
        """fetch a user by id.

        args:
            user_id (string): the id of the user to retrieve.
        returns:
            user object if found, else none.
        """
        session = models.storage.get_session()
        try:
            user = session.query(cls).filter_by(email=email)
            return user
        except noresultfound:
            return none

    def get_session(self):
        """Get the database session engine.

        returns: The session engine.
        """
        session = models.storage.get_session()
        return session

    def __str__(self):
        """Display an object in a human readable form

        Return: The string representation of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
