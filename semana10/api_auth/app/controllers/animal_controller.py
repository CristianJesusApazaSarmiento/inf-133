from flask import Blueprint, request, jsonify
from models.animal_model import Animal
from views.animal_view import render_animal_list, render_animal_detail
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps

animal_bp = Blueprint("animal", __name__)


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return fn(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 401

    return wrapper

@animal_bp.route("/animals", methods=["GET"])
@jwt_required
def get_animals():
    animals = Animal.get_all()
    return jsonify(render_animal_list(animals))

@animal_bp.route("/animals/<int:id>", methods=["GET"])
@jwt_required
def get_animal(id):
    animal = Animal.get_by_id(id)
    if animal:
        return jsonify(render_animal_detail(animal))
    return jsonify({"error": "Animal no encontrado"}), 404

@animal_bp.route("/animals", methods=["POST"])
@jwt_required
def create_animal():
    data = request.json
    name = data.get("name")
    species = data.get("species")
    age = data.get("age")

    if not name or not species or age is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    animal = Animal(name=name, species=species, age=age)
    animal.save()

    return jsonify(render_animal_detail(animal)), 201

@animal_bp.route("/animals/<int:id>", methods=["PUT"])
@jwt_required
def update_animal(id):
    animal = Animal.get_by_id(id)

    if not animal:
        return jsonify({"error": "Animal no encontrado"}), 404

    data = request.json
    name = data.get("name")
    species = data.get("species")
    age = data.get("age")
    
    animal.update(name=name, species=species, age=age)
    return jsonify(render_animal_detail(animal))


@animal_bp.route("/animals/<int:id>", methods=["DELETE"])
@jwt_required
def delete_animal(id):
    animal = Animal.get_by_id(id)
    if not animal:
        return jsonify({"error": "Animal no encontrado"}), 404

    animal.delete()
    return "", 204