import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

# DELETE elimina todos los estudiantes por la ruta /estudiantes
#ruta_eliminar = url + "estudiantes"
#eliminar_response = requests.request(method="DELETE", 
#                                    url=ruta_eliminar)
#print(eliminar_response.text)

# GET busca a un estudiante por id /estudiantes/{id}
#ruta_filtrar_nombre = url + "estudiantes/1"
#filtrar_nombre_response = requests.request(method="GET", 
#                                url=ruta_filtrar_nombre)
#print(filtrar_nombre_response.text)

# PUT actualiza un estudiante por la ruta /estudiantes
ruta_actualizar = url + "estudiantes"
estudiante_actualizado = {
    "id": 6,
    "nombre": "Juan",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica",
}
put_response = requests.request(
    method="PUT", url=ruta_actualizar, 
    json=estudiante_actualizado
)
print(put_response.text)

# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica"
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

nuevo_estudiante = {
    "nombre": "Pedrito",
    "apellido": "Lopez",
    "carrera": "Ingenieria",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

# Agregar una ruta para mostrar todas las carreras
print("####### CARRERAS #######")
ruta_carrera = url + "carreras"
filtrar_carrera_response = requests.request(method="GET", url=ruta_carrera)
print(filtrar_carrera_response.text)
print("-------------------------")

# Agregar una ruta que devuelva a todos los estudiantes de la carrera de "Economia"
print("####### ESTUDIANTES DE LA CARRERA DE ECONOMIA #######")
ruta_estudiante_economia = url + "economistas"
filtrar_estudiante_economia_response = requests.request(method="GET", url = ruta_estudiante_economia)
print(filtrar_estudiante_economia_response.text)
print("-------------------------")

print("####### AGREGA 2 NUEVOS ESTUDIANTES DE ECONOMIA #######")
ruta_post = url + "estudiantes"
nuevo_estudiante1 = {
    "id": 7,
    "nombre": "Fabricio",
    "apellido": "Castillo",
    "carrera": "Economia"
}

nuevo_estudiante2 = {
    "id": 9,
    "nombre": "Luis",
    "apellido": "Lopez",
    "carrera": "Economia",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante1)
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante2)
print(post_response.text)
print("-------------------------")