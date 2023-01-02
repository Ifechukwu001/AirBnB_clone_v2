#!/usr/bin/python3
"""Place API views"""

from api.v1.views import app_views
from flask import jsonify
from flask import abort
from flask import request
from models import storage
from models.place import Place
from models.city import City


@app_views.route("/cities/<city_id>/places")
def get_places(city_id):
    city = storage.get(City, city_id)
    if city:
        city_places = []
        for place in city.places:
            city_places.append(place.to_dict())
        return jsonify(city_places)
    else:
        abort(404)

@app_views.route("/places/<place_id>")
def get_place(place_id):
    place = storage.get(Place, place_id)
    if place:
        return jsonify(place.to_dict())
    else:
        abort(404)

@app_views.route("/places/<place_id>", methods=["DELETE"])
def delete_place(place_id):
    place = storage.get(Place, place_id)
    if place:
        storage.delete(place)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)
