from flask import Blueprint, request, jsonify
from models.user_model import User
from views.user_view import render_user_detail, render_user_list
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from utils.decorators import jwt_required, roles_required

user_bp = Blueprint("user", __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    roles = data.get("roles")

    if not username or not password:
        return jsonify({"error": "Se requieren nombre de usuario y contraseña"}), 400

    existing_user = User.find_by_username(username)
    if existing_user:
        return jsonify({"error": "El nombre de usuario ya está en uso"}), 400
    new_user = User(username, password, roles)
    new_user.save()
    return jsonify({"message": "Usuario creado exitosamente"}), 201


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.find_by_username(username)
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity={"username": username, "roles": user.roles})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

@user_bp.route("/users", methods=["GET"])
@jwt_required
@roles_required(roles=["admin"])
def get_users():
    users = User.get_all()
    return jsonify(render_user_list(users))

@user_bp.route("/users/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin"])
def get_user(id):
    user = User.get_by_id(id)
    if user:
        return jsonify(render_user_detail(user))
    return jsonify({"error": "Usuario no encontrado"}), 404

@user_bp.route("/users", methods=["POST"])
@jwt_required 
@roles_required(roles=["admin"])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    roles = data.get("roles")

    if not username or not password or not roles:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user = User(username=username, password=password, roles=roles)
    user.save()

    return jsonify(render_user_detail(user)), 201


@user_bp.route("/users/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_user(id):
    user = User.get_by_id(id)

    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    data = request.json
    username = data.get("username")
    roles = data.get("roles")
    password = data.get("password")
    user.update(username=username, password=password, roles=roles)

    return jsonify(render_user_detail(user))
    
@user_bp.route("/users/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_user(id):
    user = User.get_by_id(id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    user.delete()
    return "", 204
