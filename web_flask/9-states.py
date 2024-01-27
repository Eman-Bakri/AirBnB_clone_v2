#!/usr/bin/python3
"""Shows HTML page with a list of all State objects"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with all States list"""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Include info about <id>, if exists"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def close_session(exc):
    """terminate the session."""
    storage.close()


if __name__ == '__main__':
    """Run the server"""
    app.run(host='0.0.0.0')