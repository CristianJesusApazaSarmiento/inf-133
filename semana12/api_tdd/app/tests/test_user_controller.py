#Testea registro y login

# 
def test_register_user(test_client):
    # Si ya existe el mismo username, dara un error 400
    new_user = {"username": "testuser", "password": "testpassword"}
    response = test_client.post("/api/register", json=new_user)
    assert response.status_code == 201

# Para ver
def test_register_duplicate_user(test_client):
    new_user = {"username": "testuser", "password": "testpassword"}
    response = test_client.post("/api/register", json=new_user)
    # verificamos si se puede registrar
    assert response.status_code == 400
    assert response.json["error"] == "El nombre de usuario ya está en uso"

# Verificamos las credenciales del usuario
def test_login_user(test_client):
    user_credentials = {"username": "testuser", "password": "testpassword"}
    response = test_client.post("/api/login", json=user_credentials)
    assert response.status_code == 200