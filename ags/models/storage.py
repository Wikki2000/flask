#!/usr/bin/python3
"""Defines storage system using mysql."""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import environ


class Storage:
    """This models the database system using SQLAlchemy."""

    __engine = None
    __session = None

    def __init__(self):
        from models.base_model import BaseModel, Base

        """Create session engine for interacting with database."""
        username = environ["APP_USER"]
        password = environ["APP_PASSWORD"]
        database = environ["APP_DATABASE"]
        host = environ["APP_HOST"]

        self.__engine = create_engine(f"mysql+mysqldb://{username}:{password}@{host}/{database}", pool_pre_ping=True)

        # Drop all tables each time a set environ is set
        """
        if environ["APP_ENV"] == "test":
            Base.metadata.drop_all(self.__engine)
        """
        Base.metadata.create_all(self.__engine) # Create tables if they do not exist
        Session =  sessionmaker(bind=self.__engine) # Bind Session to engine
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)        
        self.__session = scoped_session(session_factory)

    def new(self, obj):
        """Add object to session.new"""
        self.__session.add(obj)

    def save(self):
        """Persist save change to database and add object to session."""
        self.__session.commit()


    def close(self):
        """Close the session after transaction"""
        self.__session.close()

    def get_session(self):
        """Return the current session."""
        return self.__session
