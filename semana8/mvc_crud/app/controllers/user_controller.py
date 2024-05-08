from flask import Blueprint, request, redirect, url_for

from views import user_view

from models.user_model import User

user_bp = Blueprint("user", __name__)

@user_bp.route("/")
def index():
    return redirect(url_for("user.list_users"))

@user_bp.route("/users")
def list_users():
    users = User.get_all()
    return user_view.usuarios(users)

@user_bp.route("/users/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        birthdate = request.form["birthdate"]
        
        user = User(first_name, last_name, email, password, birthdate)
        user.save()
        
        return redirect(url_for("user.list_users"))
    return user_view.registro()


@user_bp.route("/users/<int:id>/update", methods=["GET", "POST"])
def update_user(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        birthdate = request.form["birthdate"]
        
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.password = password
        user.birthdate = birthdate
        
        user.update()
        return redirect(url_for("user.list_users"))
    return user_view.actualizar(user)

@user_bp.route("/users/<int:id>/delete")
def delete_user(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    user.delete()
    return redirect(url_for("user.list_users"))