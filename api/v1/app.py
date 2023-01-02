#!/usr/bin/python3
"""API application to serve requests"""

from os import getenv
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def close(response):
    storage.close()


@app.errorhandler(404)
def url_not_found(err):
    return jsonify({"error": "Not Found"}), 404


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST")
    port = getenv("HBNB_API_PORT")
    if host == "":
        host = "0.0.0.0"
    if port == "":
        port = "5000"
    app.run(host=host, port=port, threaded=True)
