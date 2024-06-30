from flask import Flask, request, render_template, flash, url_for, redirect
from pymongo import MongoClient
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = "test"

# Connect to mongodb which is listening on port 
client = MongoClient("mongodb://localhost:27017/")

# Create or select database if exists already
db = client["authentication_db"]

# Create or select collection
collection = db["users"]

@app.route("/")
def index():
    return redirect(url_for("registration"))

@app.route("/login", methods=["POST", "GET"])
def registration():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        pwd1 = request.form.get("pwd1")
        pwd2 = request.form.get("pwd2")

        if collection.find_one({"email": email}):
            flash("User exists already")
            return redirect(url_for("registration"))
        elif pwd1 != pwd2:
            flash("Password must match")
            return redirect(url_for("registration"))

        password = generate_password_hash("pwd1")
        user = {"name": name, "email": email, "password": password}
        collection.insert_one(user)
        flash("Registration successful")
    return render_template("registration.html")

if __name__ == "__main__":
    app.run(debug=True)
