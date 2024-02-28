import requests

url = "http://localhost:8000/"
# GET consulta a la ruta /lista_estudiantes
ruta_get = url + "lista_estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}

post_response = requests.request(method="POST", 
                                    url=ruta_post, 
                                    json=nuevo_estudiante)
print(post_response.text)

print("#########################")

#Ruta "buscar_nombre" para obtener los nombres que empiecen con la letra 'P'
ruta_Buscar = url + "buscar_nombre"
get_responseP = requests.request(method="GET", url=ruta_Buscar)
print(get_responseP.text)

#Ruta "contar_carreras" para obtener la cantidad de estudiantes por carrera
print("#########################")
ruta_Contar = url + "contar_carreras"
get_responseConteo = requests.request(method="GET", url=ruta_Contar)
print(get_responseConteo.text)

#Ruta "total_estudiantes" para obtener la cantidad total de estudiantes
print("#########################")
ruta_TotalEst = url + "total_estudiantes"
get_responseConteoEst = requests.request(method="GET", url=ruta_TotalEst)
print("Cantidad de estudiantes:", get_responseConteoEst.text)