#!/usr/bin/python3
"""flask web application that lists states dynamiclly"""
from flask import Flask, render_template
from models import storage

db_app = Flask(__name__)


@db_app.route("/states_list")
def states():
    """ states list"""
    states_li = storage.all(State)
    if states_li:
        render_template("7-states_list.html", states_li=states_li)
    else:
        return "Storage wasn't imported"


@db_app.teardown_appcontext
def close_dataB():
    """ states list"""
    storage.close()


if __name__ == "__main__":
    db_app.run(host="0.0.0.0", port=5000, debug=True)
