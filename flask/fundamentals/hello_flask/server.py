from flask import Flask, render_template  # Import Flask to allow us to create our app


app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html', phrase = "hello", times = 5)


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/repeat/<int:num>/<string:word>')
def repeat(word, num):
    return f"{word * num}"


@app.route('/success')
def success():
    return 'success'


@app.route('/say/<string:name>')
def hello(name):
    print(name)
    return "Hi " + name


@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id:" + id


if __name__=="__main__":   
    app.run(debug=True)    



