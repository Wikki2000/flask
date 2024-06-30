#!/usr/bin/python3
"""Tests for the Storage class."""
import unittest
from models.storage import Storage
from models.base_model import BaseModel, Base 
from sqlalchemy.orm import Session
from sqlalchemy import Column, String


class TestUser(BaseModel, Base):
    """This class inherit from Base for testing purposes."""
    __tablename__ = "test"
    test_email = Column(String(128), nullable=False)
    test_password = Column(String(128), nullable=False)
    test_name = Column(String(128), nullable=True)

class TestStorage(unittest.TestCase):
    """This class define test case for Storage module."""

    def setUp(self):
        """Set up value for testing."""
        self.storage = Storage()
        self.attr = {"test_name": "test_user",
                     "test_email": "test@gmail.com",
                     "test_password": "test_pwd"}
        self.test_user = TestUser(**self.attr)
        self.session = self.storage.get_session() # Retrieve the scoop session engine

    
    def tearDown(self):
        """Tear down any setup that ran for the test"""
        session = self.storage.get_session()
        test_user = session.query(TestUser).filter_by(test_email=self.attr["test_email"])

        if test_user:
            test_user.delete()
            session.commit()

        session.close()

    def test_session_initialization(self):
        """Test that session engine was successfully created."""

        # Obtain the actual session object using the scoped session
        actual_session = self.session()

        self.assertIsNotNone(self.session)
        self.assertIsInstance(actual_session, Session)

    def test_new(self):
        """Test to add object to session."""
        self.storage.new(self.test_user) # Add test_user to session

        # Check if test_user was successfully added to session
        #self.assertTrue(self.test_user in self.storage.get_session().new)
        self.assertIn(self.test_user, self.session.new)

    def test_save(self):
        """Test to see if change persist."""
        self.storage.new(self.test_user)
        self.storage.save()

        # Retrieve the session engine and check if save change persist
        session = self.storage.get_session()
        self.assertNotIn(self.test_user, session.new)
        self.assertIn(self.test_user, session)

        # Retrieve user and check if attributes is present
        retrieved_user = session.query(TestUser).filter_by(test_email=self.attr["test_email"])
        self.assertIsNotNone(retrieved_user)

    def test_get_user(self):
        """Test to ascertain, if user is retrieved by his/her ID."""
        pass

if __name__ == "__main__":
    unittest.main()
