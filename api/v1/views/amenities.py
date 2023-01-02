#!/usr/bin/python3
"""Amenities API view"""

from api.v1.views import app_views
from flask import abort
from flask import request
from flask import jsonify
from models import storage
from models.amenity import Amenity

@app_views.route("/amenities")
def get_amenities():
    amenities = storage.all(Amenity)
    result = []
    for amenity in amenities.values():
        result.append(amenity.to_dict())
    return jsonify(result)

@app_views.route("/amenities/<amenity_id>")
def get_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        return jsonify(amenity.to_dict())
    else:
        abort(404)

@app_views.route("/amenities/<amenity_id>", methods=["DELETE"])
def delete_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        storage.delete(amenity)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)

@app_views.route("/amenities", methods=["POST"])
def create_amenity():
    if request.headers["Content-Type"] != "application/json":
        abort(400, "Not a JSON")
    data = request.get_json()
    if "name" not in data:
        abort(400, "Missing name")
    amenity = Amenity(**data)
    amenity.save()
    return jsonify(amenity.to_dict()), 201

@app_views.route("/amenities/<amenity_id>", methods=["PUT"])
def update_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        if request.headers["Content-Type"] != "application/json":
            abort(400, "Not a JSON")
        data = request.get_json()
        for key, value in data.items():
            if key == "id" or key == "created_at" or key == "updated_at":
                continue
            amenity.__setattr__(key, value)
        amenity.save()
        return jsonify(amenity.to_dict()), 200
    else:
        abort(404)
