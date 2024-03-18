import requests
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Definir la consulta GraphQL simple
query_lista = """
    {
        estudiantes{
            id
            nombre
            apellido
            carrera
        }
    }
"""

# Solicitud POST al servidor GraphQL
print("###Lista de estudiantes###")
response = requests.post(url, json={'query': query_lista})
print(response.text)
print("-----------------------")
# Definir la consulta GraphQL con parametros
query = """
    {
        estudiantePorId(id: 2){
            nombre
        }
    }
"""

# Solicitud POST al servidor GraphQL
print("### Buscar estudiante por ID ###")
response = requests.post(url, json={'query': query})
print(response.text)
print("-----------------------")


query_nombreApellido = """
    {
        estudiantePorNombreApellido(nombre: "Jose", apellido: "Lopez"){
            nombre
            apellido
        }
    }
"""

# Solicitud POST al servidor GraphQL
print("### Buscar estudiante por nombre y apellido ###")
response = requests.post(url, json={'query': query_nombreApellido})
print(response.text)
print("-----------------------")


query_carrera = """
    {
        estudiantePorCarrera(carrera: "Arquitectura"){
            nombre
            
        }
    }
"""

# Solicitud POST al servidor GraphQL
print("### Buscar estudiantes por carrera -Arquitectura- ###")
response = requests.post(url, json={'query': query_carrera})
print(response.text)
print("-----------------------")
# Definir la consulta GraphQL para crear nuevo estudiante
query_crear = """
mutation {
        estudiante1: crearEstudiante(nombre: "Angel", apellido: "Gomez", carrera: "Biologia") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
        estudiante2: crearEstudiante(nombre: "Carlos", apellido: "Huanca", carrera: "Arquitectura"){
            estudiante{
                id
                nombre
                apellido
                carrera
            }
        }
        estudiante3: crearEstudiante(nombre: "Alexia", apellido: "Rodriguez", carrera: "Arquitectura"){
            estudiante{
                id
                nombre
                apellido
                carrera
            }
        }
        estudiante4: crearEstudiante(nombre: "Michael", apellido: "Townley", carrera: "Arquitectura"){
            estudiante{
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
print("### Nuevos estudiantes ###")
response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)
print("-----------------------")


# Lista de todos los estudiantes
print("### Lista de todos los estudiantes ###")
response = requests.post(url, json={'query': query_lista})
print(response.text)
print("-----------------------")

print("### Lista de todos los estudiantes de la carrera de Arquitectura ###")
response = requests.post(url, json={'query': query_carrera})
print(response.text)
print("-----------------------")

# Definir la consulta GraphQL para eliminar un estudiante
#La id esta definida
print("### Eliminar estudiante mediante su ID ###")
query_eliminar = """
mutation {
        deleteEstudiante(id: 3) {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_eliminar})
print(response_mutation.text)
print("-----------------------")

# Lista de todos los estudiantes
print("### Listar a todos los estudiantes ###")
response = requests.post(url, json={'query': query_lista})
print(response.text)
print("-----------------------")

#####
# query para modificar a los estudiantes
print("### Modificar estudiante ###")
query_modificar = """
mutation {
    modificarEstudiante(id: 2, nombre: "Jose", apellido: "Lopez", carrera: "Antropologia") {
        estudiante {
            id
            nombre
            apellido
            carrera
        }
    }
}
"""

response_mutation = requests.post(url, json={'query': query_modificar})
print(response_mutation.text)
print("-----------------------")

# Lista de todos los estudiantes
print("### Listar a todos los estudiantes ###")
response = requests.post(url, json={'query': query_lista})
print(response.text)
print("-----------------------")

print("### Eliminar a todos los estudiantes de una carrera ###")
query_eliminar_por_carrera = """
mutation {
        deleteEstudiantePorCarrera(carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
response_mutation = requests.post(url, json={'query': query_eliminar_por_carrera})
print(response_mutation.text)
print("-----------------------")

# Lista de todos los estudiantes
print("### Listar a todos los estudiantes ###")
response = requests.post(url, json={'query': query_lista})
print(response.text)
print("-----------------------")