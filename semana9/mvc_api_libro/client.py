import requests

BASE_URL = "http://localhost:5000/api"

headers = {"Content-Type": "application/json"}

url = f"{BASE_URL}/libros"
'''libro_1 = {"titulo": "Calculo I", "autor": "Edgar", "edicion": 2, "disponibilidad": True}
response = requests.post(url, json=libro_1, headers=headers)
print("Creando un nuevo libro:")
print(response.json())

# Crear el segundo animal
libro_2 = {"titulo": "Don Quijote", "autor": "Miguel de Cervantes", "edicion": 1, "disponibilidad":  True}
response = requests.post(url, json=libro_2, headers=headers)
print("\nCreando el segundo libro:")
print(response.json())'''

'''libro_3 = {"titulo": "Cuentos", "autor": "Anton Chevoj", "edicion": 1, "disponibilidad": False}
response = requests.post(url, json=libro_3, headers=headers)
print("\nCreando el tercer libro:")
print(response.json())

libro_4 = {"titulo": "Moby Dick", "autor": "Herman Melville", "edicion": 2, "disponibilidad": False}
response = requests.post(url, json=libro_4, headers=headers)
print("\nCreando el cuarto libro:")
print(response.json())'''

# Obtener la lista de todos los animales
url = f"{BASE_URL}/libros"
response = requests.get(url, headers=headers)
print("\nLista de libros:")
print(response.json())

url = f"{BASE_URL}/libros/1"
response = requests.get(url, headers=headers)
print("\nDetalles del libro con ID 1:")
print(response.json())

url = f"{BASE_URL}/libros/1"
datos_actualizacion = {"titulo": "Calculo II", "autor": "Edgar", "edicion": 3, "disponibilidad": True}
response = requests.put(url, json=datos_actualizacion, headers=headers)
print("\nActualizando el libro con ID 1:")
print(response.json())

url = f"{BASE_URL}/libros/1"
response = requests.delete(url, headers=headers)
print("\nEliminando el libro con ID 1:")
if response.status_code == 204:
    print(f"Libro con ID 1 eliminado con éxito.")
else:
    print(f"Error: {response.status_code} - {response.text}")