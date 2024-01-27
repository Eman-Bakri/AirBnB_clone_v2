#!/usr/bin/python3
"""Shows HTML page with a list of all states and related cities"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """shows an HTML page with all states and cities list"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_session(exc):
    """terminate the session."""
    storage.close()


if __name__ == '__main__':
    """Run the server"""
    app.run(host='0.0.0.0')