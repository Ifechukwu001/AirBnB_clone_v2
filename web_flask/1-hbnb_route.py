#!/usr/bin/python3
""" Flask Application

    Attributes:
        app (:obj:`Flask`): Instance of Flask.

"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Responds to the home route

    Return:
        str: Greeting.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    """ Responds to the hbnb route

    Return:
        str: Greeting.
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
