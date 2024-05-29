#Testeo en general 
# test_index recibe un cliente
def test_index(test_client):
    # Realiza un get al index --> "/"
    response = test_client.get("/")
    # Se almacena el cuerpo de la respuesta
    assert response.status_code == 404

# Recibe el cliente de prueba
def test_swagger_ui(test_client):
    response = test_client.get("/api/docs/")
    assert response.status_code == 200
    # Verificar que la cadena este en la respuesta
    # la b nos verifica que si esta en el cuerpo del html
    assert b'id="swagger-ui"' in response.data