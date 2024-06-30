#!/usr/bin/python3
"""This module models the test case of base_model"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session


class TestBaseModel(unittest.TestCase):
    """Sets up the test attributes for each test case."""
    def setUp(self):
        self.attr = {"name": "test_user",
                     "email": "test@gmail.com",
                     "pwd": "test_pwd"}
        self.test_user = BaseModel(**self.attr)

    def test_initialization(self):
        """Test to ascertain if an object was correctly created."""

        # Check if object is created without arguement
        obj1 = BaseModel()
        self.assertIsInstance(obj1, BaseModel)
        self.assertIsInstance(obj1.id, str)
        self.assertIsInstance(obj1.create_at, datetime)

        # Check if object is created with arguments
        obj2 = BaseModel(**self.attr)
        self.assertEqual(obj2.__dict__.get('name'), 'test_user')
        self.assertEqual(obj2.__dict__.get('email'), 'test@gmail.com')
        self.assertEqual(obj2.__dict__.get('pwd'), 'test_pwd')

    def test_str_rep(self):
        """Tests the string representation of the BaseModel object."""
        expected_str = f"[{self.test_user.__class__.__name__}] ({self.test_user.id}) {self.test_user.__dict__}"
        self.assertEqual(str(self.test_user), expected_str)

    def test_get_session(self):
        """Ascertain that session engine is retrieved successfully."""
        session = self.test_user.get_session()
        self.assertIsNotNone(session)
        actual_session = session()
        self.assertIsInstance(actual_session, Session)

        

if __name__ == "__main__":
    unittest.main()
