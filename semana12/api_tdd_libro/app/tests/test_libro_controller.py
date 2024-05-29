def test_get_libros(test_client, auth_headers):
    response = test_client.get("/api/libros", headers=auth_headers)
    assert response.status_code == 200
    assert response.json == []
    
def test_get_libros(test_client, user_headers):
    response = test_client.get("/api/libros", headers=user_headers)
    assert response.status_code == 200
    assert response.json == []

def test_create_libro(test_client, auth_headers):
    data = {"titulo": "Laguna", "autor": "Miguel", "edicion": 2, "disponibilidad": True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers)
    assert response.status_code == 201
    assert response.json["titulo"] == "Laguna"

def test_get_libro(test_client, auth_headers):
    data = {"titulo": "Tinieblas", "autor": "Kevin", "edicion": 3, "disponibilidad": True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    response = test_client.get(f"/api/libros/{libro_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json["titulo"] == "Tinieblas"

def test_get_libro(test_client, user_headers):
    data = {"titulo": "Tinieblas", "autor": "Kevin", "edicion": 3, "disponibilidad": True}
    response = test_client.post("/api/libros", json=data, headers=user_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    response = test_client.get(f"/api/libros/{libro_id}", headers=user_headers)
    assert response.status_code == 200
    assert response.json["titulo"] == "Tinieblas"

def test_update_libro(test_client, auth_headers):
    data = {"titulo": "Tinieblas", "autor": "Kevin", "edicion": 3, "disponibilidad": True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    update_data = {"titulo": "Tinieblas", "autor": "Kevin", "edicion": 2, "disponibilidad": False}
    response = test_client.put(
        f"/api/libros/{libro_id}", json=update_data, headers=auth_headers
    )
    assert response.status_code == 200
    assert response.json["titulo"] == "Angel"
    assert response.json["edicion"] == 3

