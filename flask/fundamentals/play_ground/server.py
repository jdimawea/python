import re
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def blue_box():
    return render_template('index.html')


@app.route('/play/<int:num>')
def num_box(num):
    return render_template('index2.html', num = num)


@app.route('/play/<int:num>/<color>')
def color_num_box(num, color):
    return render_template('index3.html', num = num, color = color)


if __name__=="__main__":
    app.run(debug=True)