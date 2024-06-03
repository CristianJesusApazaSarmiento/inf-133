from flask import Blueprint, jsonify, request

from app.models.producto_model import Producto
from app.utils.decorators import jwt_required, roles_required
from app.views.producto_view import render_producto_detail, render_producto_list

producto_bp = Blueprint("producto", __name__)


@producto_bp.route("/productos", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_productos():
    productos = Producto.get_all()
    return jsonify(render_producto_list(productos))


@producto_bp.route("/productos/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_producto(id):
    producto = Producto.get_by_id(id)
    if producto:
        return jsonify(render_producto_detail(producto))
    return jsonify({"error": "Producto no encontrado"}), 404


@producto_bp.route("/productos", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_producto():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")

    if not name or not description or price is None or stock is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    producto = Producto(name=name, description=description, price=price, stock=stock)
    producto.save()

    return jsonify(render_producto_detail(producto)), 201

@producto_bp.route("/productos/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_producto(id):
    producto = Producto.get_by_id(id)

    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")

    producto.update(name=name, description=description, price=price, stock=stock)

    return jsonify(render_producto_detail(producto))

@producto_bp.route("/productos/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_producto(id):
    producto = Producto.get_by_id(id)

    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    producto.delete()
    return "", 204