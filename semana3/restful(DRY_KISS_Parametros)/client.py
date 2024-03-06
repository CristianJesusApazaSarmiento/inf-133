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

# GET filtrando por nombre con query params
'''ruta_get = url + "estudiantes?nombre=Pedrito"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

print("#### Busqueda por apellido ####")
ruta_get = url + "estudiantes?apellido=Garcia"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

print("### Busqueda por carreras ####")
ruta_get_carrera= url + "estudiantes?carrera=Ingenieria de Sistemas"
get_response_carrera = requests.request(method="GET", url=ruta_get_carrera)
print(get_response_carrera.text)'''

print("#### Busqueda por nombre, apellido y carreras ####")
ruta_get_busqueda= url + "estudiantes?nombre=Pablo&apellido=Escobar&carrera=Administracion"
get_response_busqueda = requests.request(method="GET", url=ruta_get_busqueda)
print(get_response_busqueda.text)