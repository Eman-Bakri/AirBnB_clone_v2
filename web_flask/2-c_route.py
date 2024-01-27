#!/usr/bin/python3
"""Starting a Flask web app listening on 0.0.0.0, port 5000"""
from flask import Flask

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


if __name__ == '__main__':
    """Run the server"""
    app.run(host='0.0.0.0')
