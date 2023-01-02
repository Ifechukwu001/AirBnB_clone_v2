#!/usr/bin/python3
"""States Api view"""

from api.v1.views import app_views
from flask import jsonify
from flask import abort
from flask import request
from models.state import State
from models import storage

@app_views.route("/states")
def get_states():
    states = storage.all(State)
    states_info = []
    for key in states:
        states_info.append(states[key].to_dict())
    return jsonify(states_info)

@app_views.route("/states/<state_id>")
def get_state(state_id):
    state = storage.get(State, state_id)
    if state == None:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route("/states/<state_id>", methods=["DELETE"])
def delete_state(state_id):
    state = storage.get(State, state_id)
    if state:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)

@app_views.route("/states", methods=["POST"])
def create_state():
    if request.headers["Content-Type"] != "application/json":
        abort(400, "Not a JSON")
    data = request.get_json()
    if "name" not in data:
        abort(400, "Missing Name")
    obj = State(**data)
    obj.save()
    return jsonify(obj.to_dict()), 201

@app_views.route("/states/<state_id>", methods=["PUT"])
def update_state(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if request.headers["Content-Type"] != "application/json":
        abort(400, "Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key == "id" or key == "created_at" or key == "updated_at":
            continue
        state.__setattr__(key, value)
    state.save()
    return jsonify(state.to_dict()), 200
