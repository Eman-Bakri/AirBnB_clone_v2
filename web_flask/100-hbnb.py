#!/usr/bin/python3
"""Shows HBnB home page"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """shows HTML page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def close_session(exc):
    """terminate the session."""
    storage.close()


if __name__ == '__main__':
    """Run the server"""
    app.run(host='0.0.0.0')
