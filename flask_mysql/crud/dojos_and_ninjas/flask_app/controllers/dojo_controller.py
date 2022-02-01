from flask import Flask, render_template, redirect, request, session


from flask_app import app


from flask_app.models.dojo import Dojo


from flask_app.models.ninja import Ninja


@app.route('/dojos')
def dojos():
    list_of_dojos = Dojo.get_all()
    return render_template('index.html', all_dojos = list_of_dojos)


@app.route("/dojos/<int:id>")
def display_dojo(id):
    return render_template("dojo_show.html", dojo = Dojo.get_dojo_with_ninjas({"id": id}))


@app.route("/dojos/create", methods = ["POST"])
def create_dojo():

    Dojo.create(request.form)

    return redirect("/dojos")