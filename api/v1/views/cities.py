#!/usr/bin/python3
"""City API views"""

from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State
from flask import abort
from flask import request
from flask import jsonify


@app_views.route("/states/<state_id>/cities")
def get_cities(state_id):
    state = storage.get(State, state_id)
    if state:
        result = []
        for city in state.cities:
            result.append(city.to_dict())
        return jsonify(result)
    else:
        abort(404)

@app_views.route("/cities/<city_id>")
def get_cities2(city_id):
    city = storage.get(City, city_id)
    if city:
        return jsonify(city.to_dict())
    else:
        abort(404)

@app_views.route("/cities/<city_id>", methods=["DELETE"])
def delete_city(city_id):
    city = storage.get(City, city_id)
    if city:
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)

@app_views.route("/states/<state_id>/cities", methods=["POST"])
def create_city(state_id):
    state = storage.get(State, state_id)
    if state:
        if request.headers["Content-Type"] != "application/json":
            abort(400, "Not a JSON")
        data = request.get_json()
        if "name" not in data:
            abort(400, "Missing name")
        city = City(**data)
        city.state_id = state_id
        city.save()
        return jsonify(city.to_dict()), 201
    else:
        abort(404)

@app_views.route("/cities/<city_id>", methods=["PUT"])
def update_city(city_id):
    city = storage.get(City, city_id)
    if city:
        if request.headers["Content-Type"] != "application/json":
            abort(400, "Not a JSON")
        data = request.get_json()
        for key, value in data.items():
            if key == "id" or key == "created_at" or key == "updated_at" or key == "state_id":
                continue
            city.__setattr__(key, value)
        city.save()
        return jsonify(city.to_dict()), 200
    else:
        abort(404)
