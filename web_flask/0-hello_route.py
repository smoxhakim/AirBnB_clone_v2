#!/usr/bin/python3
from flask import Flask

HBNB_app = Flask(__name__)

@HBNB_app.route("/",  strict_slashes=False)
def home():
    return "<H1>Hello HBNB!</H1>"


if __name__ == "__main__":
    HBNB_app.run(host='0.0.0.0', port=5000, debug=True)