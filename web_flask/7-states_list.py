#!/usr/bin/python3
"""shows HTML page with a list of all State objects"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """shows an HTML page with State objects list"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """terminate the session."""
    storage.close()


if __name__ == '__main__':
    """Run the server"""
    app.run(host='0.0.0.0')
