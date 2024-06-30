#!/usr/bin/python3
from flask import Flask, render_template, url_for, session, request, redirect, flash
from datetime import timedelta
from werkzeug.security import check_password_hash, generate_password_hash
from models.user import User
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.secret_key = "my_secret_key"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)

# csrf = CSRFProtect(app)  # Initialize CSRF protection

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.get_user_email(email).first()

        if user and check_password_hash(user.password, password):
            session["name"] = user.name
            session["user_id"] = user.id
            session.permanent = True
            return "Welcome {}!".format(user.name)
        else:
            flash("Invalid email or password")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        user = User.get_user_email(email).first()

        if user:
            flash("User exists already.")
            return redirect(url_for("registration"))
        user = User(name=name, email=email, password=password)
        user.save()
        flash("Registration successfull")
        return redirect(url_for("login"))
    return render_template('registration.html')

if __name__ == "__main__":
    app.run(debug=True)

