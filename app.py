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


@app.route("/")
@app.route("/how-till-spake-norn-irish")
# Render Home Page
def home():
    return render_template('index.html')


@app.route("/sign-up", methods=["GET", "POST"])
# Render Sign Up Page
def sign_up():
    if request.method == "POST":
        # Check if the username already exists in MongoDB user_profile collection
        existing_user = mongo.db.user_profile.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            # Display flash message if username already exists
            flash("Sorry! That wee username is already being used!", "error")
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

        # Display flash message if sign up is successful
        flash(
            "You've successfully created a wee account with us! Welcome to your profile page!", "success")

        # Redirect user to their profile
        return redirect(url_for("profile", username=session["user"]))

    return render_template("sign-up.html")


@app.route("/login", methods=["GET", "POST"])
# Render Login Page
def login():
    if request.method == "POST":
        # Check if username exists in MongoDB user_profile collection
        existing_user = mongo.db.user_profile.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            # Check if hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):

                # Put existing user into a 'session' cookie using first_name and username
                session["user"] = request.form.get("username")

                # Redirect user to their profile
                return redirect(url_for("profile", username=session["user"]))

            # Display flash message if password doesn't match input
            else:
                flash("That's the wrong username/password ya melter!", "incorrect")
                return redirect(url_for("login"))

        # Display flash message if username doesn't exist
        else:
            flash("That's the wrong username/password ya melter!", "incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
# Render Profile Page
def profile(username):
    # Grab the session users first_name from MongoDB user_profile collection
    username = mongo.db.user_profile.find_one(
        {"username": session["user"]})["first_name"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
# Render Logout Functionality
def logout():
    # Display flash message if user has been logged out
    flash("Ach, you've logged out of your wee account! If you want to, you can log back in below:", "logout")

    # Remove user from session cookies
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/our-wee-guide")
# Render Dictionary Page
def dictionary():
    dictionary = mongo.db.dictionary.find()
    return render_template("dictionary.html", dictionary=dictionary)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
