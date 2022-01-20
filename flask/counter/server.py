from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)


app.secret_key = 'VictoriaSecret'


@app.route('/')
def index():
    if 'count' in session:
        session['count'] = session.get('count') + 1
    else:
        session['count'] = 1
    return render_template("index.html", count = session['count'])


@app.route('/increment')
def increment():
    if 'count' in session:
        session['count'] = session.get('count') + 1
    else:
        session['count'] = 1
    return redirect('/')


@app.route('/reset')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)