import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
print("--------------------------------------------")


# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica",
}
nuevo_estudiante2 = {
    "nombre": "Michael",
    "apellido": "Townley",
    "carrera": "Ingenieria Industrial"
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante2 )
print(post_response.text)
print("--------------------------------------------")

# PUT actualiza un estudiante por la ruta /estudiantes
ruta_actualizar = url + "estudiantes/2"
estudiante_actualizado = {
    "nombre": "Juanito",
    "apellido": "Perez",
    "carrera": "Ingenieria Electronica",
}
put_response = requests.request(method="PUT", url=ruta_actualizar, json=estudiante_actualizado)
ruta_actualizar = url + "estudiantes/3"
estudiante_actualizado2 = {
    "nombre": "Michael",
    "apellido": "Townley",
    "carrera": "Ingenieria Petrolera"
}

put_response = requests.request(method="PUT", url=ruta_actualizar, json=estudiante_actualizado2)
print(put_response.text)
print("--------------------------------------------")

# GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
print("--------------------------------------------")

# GET filtrando por nombre con query params
ruta_get = url + "estudiantes?nombre=Pedrito"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
print("--------------------------------------------")
# GET busca a un estudiante por id /estudiantes/{id}
ruta_filtrar_nombre = url + "estudiantes/3"
filtrar_nombre_response = requests.request(method="GET", url=ruta_filtrar_nombre)
print(filtrar_nombre_response.text)
print("--------------------------------------------")

# DELETE elimina todos los estudiantes por la ruta /estudiantes
ruta_eliminar = url + "estudiantes"
eliminar_response = requests.request(method="DELETE", url=ruta_eliminar)
print(eliminar_response.text)
print("--------------------------------------------")
# GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
print("--------------------------------------------")