from calculator import *

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    result = f(expression)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run()
