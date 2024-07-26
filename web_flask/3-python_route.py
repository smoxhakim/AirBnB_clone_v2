#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask

HBNB_app = Flask(__name__)


@HBNB_app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@HBNB_app.route("/hbnb", strict_slashes=False)
def home_HBNB():
    return "HBNB"


@HBNB_app.route("/c/<text>", strict_slashes=False)
def home_args(text):
    text = text.replace('_', ' ')
    return "C {}".format(text)


@HBNB_app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@HBNB_app.route("/python/<text>", strict_slashes=False)
def home_python(text):
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == "__main__":
    HBNB_app.run(host='0.0.0.0', port=500, debug=True)
