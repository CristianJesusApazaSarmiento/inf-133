import pytest
# Cuando el usuario se logea se crea el token
# Ahora vamos a crear un token para que los endpoints de "animal" funcionen
from flask_jwt_extended import create_access_token

from app.database import db
from app.run import app

# fixture,
@pytest.fixture(scope="module")
def test_client():
    # Definido en Run.py
    # Configurarlo como TESTING
    app.config["TESTING"] = True
    # La base de datos es temporal, que no se registra en el proyecto
    # Dejara de existir cuando se deje de ejecutar el proyecto
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["JWT_SECRET_KEY"] = "test_secret_key"

    # Levantar un cliente de prueba
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            # Mientras esto este vivo --> yield
            yield testing_client
            db.drop_all()

#Cuando se ejecute pytest, debe ejecutar lo que sigue
@pytest.fixture(scope="module")
# Autorizador de la cabecera
# Lo que genera el token
def auth_headers():
    with app.app_context():
        # El token debe tener la misma estructura que la del login
        access_token = create_access_token(
            identity={"username": "testuser", "roles": '["admin"]'}
        )
        headers = {"Authorization": f"Bearer {access_token}"}
        return headers
    
@pytest.fixture(scope="module")
def user_headers():
    with app.app_context():
        access_token = create_access_token(identity={"username": "Jack", "roles": '["user"]'})
        headers = {"Autorizacion": f"Bearer {access_token}"}
        return headers