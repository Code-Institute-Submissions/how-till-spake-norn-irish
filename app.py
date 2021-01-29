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
@app.route("/how_till_spake_norn_irish")
# Render Home Page
def home():
    return render_template('index.html')


@app.route("/our_wee_guide")
# Render Dictionary Page
def dictionary():
    dictionary = mongo.db.dictionary.find()
    return render_template("dictionary.html", dictionary=dictionary)


@app.route("/search", methods=["GET", "POST"])
# Search Functionality
def search():
    search = request.form.get("search")
    dictionary = mongo.db.dictionary.find({"$text": {"$search": search}})
    return render_template("dictionary.html", dictionary=dictionary)


# MongoDB sort function: https://www.w3schools.com/python/python_mongodb_sort.asp

@app.route("/ascending")
# Ascending Sort Functionality
def ascending():
    dictionary = mongo.db.dictionary.find().sort("word", 1)
    return render_template("dictionary.html", dictionary=dictionary)


@app.route("/descending")
# Descending Sort Functionality
def descending():
    dictionary = mongo.db.dictionary.find().sort("word", -1)
    return render_template("dictionary.html", dictionary=dictionary)


@app.route("/sign_up", methods=["GET", "POST"])
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

    return render_template("sign_up.html")


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


@app.route("/logout")
# Logout Functionality
def logout():
    # Display flash message if user has been logged out
    flash("Ach, you've logged out of your wee account!", "logout")

    # Remove user from session cookies
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile/<username>", methods=["GET", "POST"])
# Render Profile Page
def profile(username):
    # Grab the session users first_name from MongoDB user_profile collection
    username = mongo.db.user_profile.find_one(
        {"username": session["user"]})["first_name"]

    # Get dictionary to display words added by user
    dictionary = mongo.db.dictionary.find(
        {"added_by": session["user"]})

    if session["user"]:
        return render_template("profile.html", dictionary=dictionary, username=username)

    return redirect(url_for("login"))


@app.route("/add_word", methods=["GET", "POST"])
# Render Add Word Page
def add_word():
    if request.method == "POST":
        word = {
            "word": request.form.get("word"),
            "definition": request.form.get("definition"),
            "example": request.form.get("example"),
            "added_by": session["user"]
        }
        # Add word to dictionary
        mongo.db.dictionary.insert_one(word)
        # Display flash message if word has been added successfully
        flash("Your word has been added to Our Wee Guide!", "add")
        return redirect(url_for("dictionary"))

    return render_template("add_word.html")


@app.route("/edit_word/<word_id>", methods=["GET", "POST"])
# Render Edit Word Page
def edit_word(word_id):
    if request.method == "POST":
        submit = {
            "word": request.form.get("word"),
            "definition": request.form.get("definition"),
            "example": request.form.get("example"),
            "added_by": session["user"]
        }
        # Update word in dictionary
        mongo.db.dictionary.update({"_id": ObjectId(word_id)}, submit)
        # Display flash message if word has been successfully updated
        flash("You've update a word in Our Wee Guide", "edit")
        return redirect(url_for("dictionary"))

    word = mongo.db.dictionary.find_one({"_id": ObjectId(word_id)})
    return render_template("edit_word.html", word=word)


@app.route("/delete_word/<word_id>")
# Delete Functionality
def delete_word(word_id):
    mongo.db.dictionary.remove({"_id": ObjectId(word_id)})
    flash("Your word has been deleted from Our Wee Guide!")
    return redirect(url_for("dictionary"))


@app.route("/contact-us")
# Render Contact Us Page
def contact():
    return render_template("contact.html")


# Error Handlers

@app.errorhandler(404)
# 404 Error Handler
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
