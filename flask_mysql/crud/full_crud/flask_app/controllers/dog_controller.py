from flask import render_template, redirect, request, session


from flask_app import app


from flask_app.models.dog import Dog


@app.route("/")
def index():
    list_of_dogs = Dog.get_all()
    print(list_of_dogs)

    return render_template("dogs/index.html", all_dogs = list_of_dogs)


@app.route("/dogs/new")
def new_dog():
    return render_template("dogs/new_dog.html")


@app.route("/dogs/create", methods = ["POST"])
def create_dog():
    # i access form data with request.form WHICH IS A dictionary
    Dog.create(request.form)

    return redirect("/")


@app.route("/dogs/<int:dog_id>/edit")
def edit_dog(dog_id):
    return render_template("dogs/edit_dog.html", this_dog = Dog.get_one({"id": dog_id}))


@app.route("/dogs/<int:dog_id>/update", methods = ["POST"])
def update_dog(dog_id):
    updated_data = {
        **request.form,
        "id": dog_id
    }
    Dog.update(updated_data)

    return redirect("/")


@app.route("/dogs/<int:dog_id>/delete")
def delete_dog(dog_id):
    Dog.delete({"id":dog_id})

    return redirect("/")


@app.route("/dogs/<int:dog_id>")
def display_dog(dog_id):
    return render_template("dogs/dog.html", dog = Dog.get_dog_with_collars({"id": dog_id}))