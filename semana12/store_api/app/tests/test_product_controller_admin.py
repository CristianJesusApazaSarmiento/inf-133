import pytest


def test_get_products(test_client, admin_auth_headers):
    response = test_client.get("/api/productos", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_product(test_client, admin_auth_headers):
    data = {
        "name": "Smartphone",
        "description": "Powerful smartphone with advanced features",
        "price": 599.99,
        "stock": 100,
    }
    response = test_client.post("/api/productos", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["name"] == "Smartphone"
    assert response.json["description"] == "Powerful smartphone with advanced features"
    assert response.json["price"] == 599.99
    assert response.json["stock"] == 100


def test_get_product(test_client, admin_auth_headers):
    response = test_client.get("/api/productos/1", headers=admin_auth_headers)
    assert response.status_code == 200
    assert "name" in response.json


def test_get_nonexistent_product(test_client, admin_auth_headers):
    response = test_client.get("/api/productos/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Producto no encontrado"


def test_create_product_invalid_data(test_client, admin_auth_headers):
    data = {"name": "Laptop"}
    response = test_client.post("/api/productos", json=data, headers=admin_auth_headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltan datos requeridos"


def test_update_product(test_client, admin_auth_headers):
    data = {
        "name": "Smartphone Pro",
        "description": "Updated version with improved performance",
        "price": 699.99,
        "stock": 150,
    }
    response = test_client.put("/api/productos/1", json=data, headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json["name"] == "Smartphone Pro"
    assert response.json["description"] == "Updated version with improved performance"
    assert response.json["price"] == 699.99
    assert response.json["stock"] == 150


def test_update_nonexistent_product(test_client, admin_auth_headers):
    data = {
        "name": "Tablet",
        "description": "Portable device with touchscreen interface",
        "price": 299.99,
        "stock": 50,
    }
    response = test_client.put(
        "/api/productos/999", json=data, headers=admin_auth_headers
    )
    assert response.status_code == 404
    assert response.json["error"] == "Producto no encontrado"


def test_delete_product(test_client, admin_auth_headers):
    response = test_client.delete("/api/productos/1", headers=admin_auth_headers)
    assert response.status_code == 204

    response = test_client.get("/api/productos/1", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Producto no encontrado"


def test_delete_nonexistent_product(test_client, admin_auth_headers):
    response = test_client.delete("/api/productos/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Producto no encontrado"