from flask import Flask, render_template, redirect, request, session


from dog import Dog


app =  Flask(__name__)
app.secret_key = "shhhhhhh."


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


if __name__ == "__main__":
    app.run(debug = True)