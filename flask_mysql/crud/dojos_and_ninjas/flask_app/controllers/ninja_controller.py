from flask import Flask, render_template, redirect, request, session


from flask_app import app


from flask_app.models.ninja import Ninja


from flask_app.models.dojo import Dojo


@app.route("/ninjas")
def ninjas():

    return render_template("new_ninja.html", all_ninjas = Dojo.get_all())


@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    dojo=Dojo.get_one({'id':request.form['dojo_id']})
    data={
        'dojo':dojo,
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age']
    }
    Ninja.add_new(data)
    return redirect('/dojos/' + str(dojo.id))