from models import UserCrud

db = UserCrud()

rv = db.create_user("Wisdom Okposin", "wisdomokposin@gmalcom", 50)
if rv:
    print(f"User successfully created with value")
else:
    print("Oops! Error inserting a user")

