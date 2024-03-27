import requests

url = "http://localhost:8000/tacos"
headers = {'Content-type': 'application/json'}

# GET
print("### Listar todos los tacos ###")
response = requests.get(url)
print(response.json())

# POST
print("### Crear tacos ###")
mi_taco = {
    "base": "Tortilla",
    "guiso": "carnita",
    "toppings": ["lechuga", "tomate"],
    "salsa": "ketchup"
}
mi_taco2 = {
    "base": "Tortilla",
    "guiso": "Tripitas",
    "toppings": ["cebolla", "lechuga"],
    "salsa": "barbacoa"
}
response = requests.post(url, json=mi_taco, headers=headers)
response2 = requests.post(url, json=mi_taco2, headers=headers)
print(response.json())
print(response2.json())

# GET
print("### Listar todos los tacos ###")
response = requests.get(url)
print(response.json())

# PUT
print("### Actualizar taco id 2 ###")
edit_taco = {
    "base": "Tortilla",
    "guiso": "asada",
    "toppings": ["lechuga", "cebolla"],
    "salsa": "ketchup"
}
response = requests.put(url + "/2", json=edit_taco, headers=headers)
print(response.json())

# GET
print("### Listar todos los tacos ###")
response = requests.get(url)
print(response.json())

# DELETE
print("### Eliminar taco por ID 1 ###")
response = requests.delete(url + "/1")
print(response.json())

# GET
print("### Listar todos los tacos ###")
response = requests.get(url)
print(response.json())