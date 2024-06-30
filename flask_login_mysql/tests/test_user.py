#!/usr/bin/python3
"""Test the user module"""
import unittest
from models.user import User
import models


class TestUser(unittest.TestCase):
    """Define the test case of User class"""

    def setUp(self):
        """Set up test environment."""
        self.atrr = {"name": "test_user",
                     "email": "test@email.com",
                     "password": "12345"}
        self.test_user = User(**self.atrr)
        self.session = models.storage.get_session()

    def tearDown(self):
        """Tear down test environment."""
        self.session.query(User).delete()
        self.session.commit()


    def test_initialization(self):
        """Test initialization of User class."""
        
        # Add self.test_user to the session
        self.session.add(self.test_user)
        self.session.commit() 

        # Check if it inherit the base attr (ID and create_at)
        test_user = self.session.query(User).filter_by(email=self.atrr["email"]).first()
        self.assertIsNotNone(test_user)
        self.assertIsNotNone(test_user.id)
        self.assertIsNotNone(test_user.create_at)

    def test_get_user_email(self):
        """Test that user is correctly retrieved using email."""
        self.session.add(self.test_user)
        retrieved_user = User.get_user_mail(self.atrr["email"]).first()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, self.atrr["email"])
        self.assertEqual(retrieved_user.name, self.atrr["name"])

        # Check if it inherit the base attr (ID and create_at)
        self.assertIsNotNone(retrieved_user.id)
        self.assertIsNotNone(retrieved_user.create_at)


if __name__ == "__main__":
    unittest.main()
