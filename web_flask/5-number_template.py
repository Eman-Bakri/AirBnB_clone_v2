#!/usr/bin/python3
"""Starting a Flask web app listening on 0.0.0.0, port 5000"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Prints 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Prints 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Prints 'C' then <text> value"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """Prints 'Python' then <text> value"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def if_number(n):
    """If n is an integer, prints 'n is a number'"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """If the number is an integer, show an HTML page"""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    """Run the server"""
    app.run(host='0.0.0.0')
