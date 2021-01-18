import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Render Home Page


@app.route("/")
@app.route("/how-till-spake-norn-irish")
def home():
    return render_template('index.html')

# Render Sign Up Page


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":
        # Check if the username already exists in MongoDB user_profile collection
        existing_user = mongo.db.user_profile.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            # If username already exists, display flash message
            flash("Username already exists.", "error")
            return redirect(url_for("sign_up"))

        # Add new user details to collection
        new_user = {
            "first_name": request.form.get("first_name"),
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password"))
        }

        # Add new user details to user_profile collection in MongoDB
        mongo.db.user_profile.insert_one(new_user)

        # Put the new user into a 'session' cookie
        session["user"] = request.form.get("username")

        # If sign up is successful, display flash message
        flash("You've successfully signed up!", "success")

    return render_template("sign-up.html")

# Render Login Page


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        # Check if username exists in MongoDB user_profile collection
        existing_user = mongo.db.user_profile.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            # Check if hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):

                session["name"] = existing_user["first_name"]
                session["user"] = existing_user["username"]
                flash(f"Bout ye {session['name'].capitalize()}?", "welcome")

            # If password doesn't match input, display flash message
            else:
                flash("Incorrect Username and/or Password", "incorrect")
                return redirect(url_for("login"))

        # If username doesn't exist, display flash mesage
        else:
            flash("Incorrect Username and/or Password", "incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")

# Render Dictionary Page


@app.route("/our-wee-guide")
def dictionary():
    dictionary = mongo.db.dictionary.find()
    return render_template("dictionary.html", dictionary=dictionary)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
