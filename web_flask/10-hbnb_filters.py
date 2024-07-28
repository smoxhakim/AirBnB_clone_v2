#!/usr/bin/python3
"""
Write a script that starts a Flask web application:

"""

from flask import Flask, render_template
from models import *
from models.state import State
from models.amenity import Amenity
from models import storage
my_app = Flask(__name__)


@my_app.route('/hbnb_filters', strict_slashes=False)
def states_amenities():
    """display the states and cities listed in alphabetical order"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    print(states)
    print(amenities)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@my_app.teardown_appcontext
def close_dataB(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port='5000', debug=True)