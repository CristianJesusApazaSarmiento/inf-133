def test_get_products_as_user(test_client, user_auth_headers):

    response = test_client.get("/api/productos", headers=user_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_product_as_user(test_client, user_auth_headers):

    data = {"name": "Laptop", "description": "High-end gaming laptop", "price": 1500.0, "stock": 10}
    response = test_client.post("/api/productos", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_get_product_as_user(test_client, user_auth_headers):

    response = test_client.get("/api/productos/1", headers=user_auth_headers)
    assert response.status_code == 200
    assert "name" in response.json
    assert "description" in response.json
    assert "price" in response.json
    assert "stock" in response.json


def test_update_product_as_user(test_client, user_auth_headers):

    data = {"name": "Laptop", "description": "Updated description", "price": 1600.0, "stock": 5}
    response = test_client.put("/api/productos/1", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_delete_product_as_user(test_client, user_auth_headers):

    response = test_client.delete("/api/productos/1", headers=user_auth_headers)
    assert response.status_code == 403