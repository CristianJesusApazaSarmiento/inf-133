from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

from views import user_view

from models.user_model import User

user_bp = Blueprint("user", __name__)

@user_bp.route("/")
def index():
    return redirect(url_for("user.login"))

@user_bp.route("/users")
#@login_required
def list_users():
    users = User.get_all()
    return user_view.usuarios(users)

@user_bp.route("/users/create", methods=["GET", "POST"])
#@login_required
def create_user():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        username = request.form["username"]
        password = request.form["password"]
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("El nombre de usuario ya está en uso", "error")
            return redirect(url_for("user.create_user"))
        user = User(first_name, last_name, username, password)
        user.set_password(password)
        user.save()
        flash("Usuario registrado exitosamente", "success")
        return redirect(url_for("user.list_users"))
    return user_view.registro()

@user_bp.route("/users/<int:id>/update", methods=["GET", "POST"])
#@login_required
def update_user(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        user.first_name = first_name
        user.last_name = last_name
        user.update()
        return redirect(url_for("user.list_users"))
    return user_view.actualizar(user)

@user_bp.route("/users/<int:id>/delete")
#@login_required
def delete_user(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    user.delete()
    return redirect(url_for("user.list_users"))

@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.get_user_by_username(username)
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for("user.list_users"))
        else:
            flash("Nombre de usuario o contraseña incorrectos", "error")
    return user_view.login()


@user_bp.route("/logout")
#@login_required
def logout():
    logout_user()
    flash("Sesión cerrada exitosamente", "success")
    return redirect(url_for("user.login"))