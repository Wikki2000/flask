from pymongo import MongoClient

class UserCrud:
    """Class encapsulating CRUD operations of user in Mongodb"""
    __collection = None

    def __init__(self):
        """Connect to db and create collection"""
        client = MongoClient("mongodb://localhost:27017/")
        db = client["test_db"] # Select database

        # Use db to create collection
        self.__collection = db["test_collection"]

    def create_user(self, name, email, age):
        """Create new user document in the collection

        Args:
            name (string): The name of user.
            email (string): The email address of user.
            age (int): The age of the user.

        Returns:
            str: The ID of newly created user.
            None: If a user with same email already exists.
        """
        # Check if user with existing email exist already
        if self.__collection.find_one({"email": email}):
            return None

        new_user = {"name": name, "email": email, "age": age}
        result = self.__collection.insert_one(new_user)
        return result

    def get_user_email(self, email):
        """Return a dict. rep. if email match else None"""
        query = {"email": email}
        user = self.__collection.find_one(query)
        return user

    def get_user_id(self, email):
        """
        Retrieved user ID by email
        Return ID object of the user, else None
        """
        query = {"email": email}
        user = self.__collection.find_one(query)
        return user["_id"] if user else None
        

    def update_user(self, user_id, name=None, email=None, age=None):
        """Update an existing user document

        Args:
            user_id (int): The ID of the user to be updated.
            name (str, optional): The new name of the user.
            email (str, optional): The new email of user to be updated.
            age (int, optional): The new age of the user.

        Returns:
            bool: True if documented was updated, else false.
        """
        new_user = {}
        query = {"_id": user_id}
        if name:
            new_user["name"] = name
        if email:
            new_user["email"] = email
        if age:
            new_user["age"] = age

        # lf.__collection.insert_one(query, $set: new_user)
        return new_user

