#!/usr/bin/python3
"""User API views"""

from api.v1.views import app_views
from flask import jsonify
from flask import abort
from flask import request
from models import storage
from models.user import User


@app_views.route("/users")
def get_users():
    users = storage.all(User)
    result = []
    for user in users.values():
        result.append(user.to_dict())
    return jsonify(result)

@app_views.route("/users/<user_id>")
def get_user(user_id):
    user = storage.get(User, user_id)
    if user:
        return jsonify(user.to_dict())
    else:
        abort(404)

@app_views.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = storage.get(User, user_id)
    if user:
        storage.delete(user)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)

@app_views.route("/users", methods=["POST"])
def create_user():
    if request.headers["Content-Type"] != "application/json":
        abort(400, "Not a JSON")
    data = request.get_json()
    if "email" not in data:
        abort(400, "Missing email")
    if "password" not in data:
        abort(400, "Missing password")
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201

@app_views.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    user = storage.get(User, user_id)
    if user:
        if request.headers["Content-Type"] != "application/json":
            abort(400, "Not a JSON")
        data = request.get_json()
        for key, value in data.items():
            if key == "id" or key == "email" or key == "created_at" or key == "updated_at":
                continue
            user.__setattr__(key, value)
        user.save()
        return jsonify(user.to_dict()), 200
    else:
        abort(404)
