from flask import render_template, redirect, request, session

from flask_app import app
from flask_app.models.dog import Dog
from flask_app.models.collar import Collar


@app.route("/collars/new")
def new_collar_page():
    return render_template("collars/new_collar.html", all_dogs = Dog.get_all())


@app.route("/collars/create", methods = ["POST"])
def create_collar():
    Collar.create(request.form)

    return redirect("/")

