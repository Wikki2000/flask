import unittest
from app import app
from models.user import User
from werkzeug.security import generate_password_hash

class TestLogin(unittest.TestCase):
    """Test case for the login functionality.
    """
    def setUp(self):
        """Set up the test environment."""
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        # Create a test user and add it to database
        self.attr = {"name": "test_user", "email": "test@gmail.com",
                "password": generate_password_hash('testpassword')}
        self.test_user = User(**self.attr)
        self.test_user.save()

    def tearDown(self):
        """Clean up the database by deleting the test user after each test."""
        session = self.test_user.get_session() # Get session engine
        user = session.query(User).filter_by(email=self.attr["email"]).first()
        if user:
            session.delete(user)
        session.commit()

    def test_login(self):
        """
        Test login with valid credentials and ensure that the session 
        variables are set correctly and the user redirected to the home page.
        """

        rv = self.app.post('/login', data={"email": "test@gmail.com", "password": "testpassword"})
        
        # Check if session variable was set after successful login
        with self.app.session_transaction() as sess:
            self.assertEqual(sess["name"], self.attr["name"])
            self.assertEqual(sess["user_id"], self.test_user.id)
        self.assertEqual(b'Welcome test_user!', rv.data)
        
if __name__ ==  "__main__":
    unittest.main()
