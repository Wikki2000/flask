#!/usr/bin/python3
from flask import Flask, render_template, url_for, session, request, redirect, flash, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from models.user import User
from models import Storage
from os import getenv

Storage()

# Set up flask
app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("SECRET_KEY")


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
        name = request.form.get("name")
        email = request.form.get("email")
        password = generate_password_hash(request.form.get("password"))
        user = User.get_user_email(email).first()

        if user:
            return jsonify(status=False, message="User exists already.")
        user = User(name=name, email=email, password=password)
        user.save()
        return jsonify(status=True, message="Registration successful", redirect=url_for("login"))
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)
