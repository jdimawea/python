from flask import Flask, render_template, redirect, request, session


from flask_app import app


from flask_app.models.dog import Dog


@app.route("/")
def index():
    list_of_dogs = Dog.get_all()
    print(list_of_dogs)

    return render_template("index.html", all_dogs = list_of_dogs)


@app.route("/dogs/new")
def new_dog():
    return render_template("new_dog.html")


@app.route("/dogs/create", methods = ["POST"])
def create_dog():
    # i access form data with request.form WHICH IS A dictionary
    Dog.create(request.form)

    return redirect("/")


@app.route("/dogs/<int:dog_id>/edit")
def edit_dog(dog_id):
    return render_template("edit_dog.html", this_dog = Dog.get_one({"id": dog_id}))


@app.route("/dogs/update", methods = ["POST"])
def update_dog():
    Dog.update(request.form)

    return redirect("/")


@app.route("/dogs/<int:dog_id>/delete")
def delete_dog(dog_id):
    Dog.delete({"id":dog_id})

    return redirect("/")