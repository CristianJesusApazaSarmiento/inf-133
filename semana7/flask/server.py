#Importa la clase Flask del paquete flask
from flask import Flask, request, jsonify

app = Flask(__name__)

#decorador asociar la ruta a la funcion
@app.route('/') #Por defecto usara GET
def hello_world():
    return 'Hola, mundo'

@app.route('/saludar', methods=['GET'])
def saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parametros de la URL"}),400,
        )
    return jsonify({"mensaje": f"Hola, {nombre}"})

@app.route('/sumar', methods=['GET'])
def sumar():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    if not num1 and not num2:
        return(
            jsonify({"error": f"Se requiere un nombre en los parametros de la URL"}),400,
        )
    return jsonify({"mensaje": f"Suma , {int(num1)+int(num2)}"})

@app.route('/palindromo', methods=['GET'])
def palindromo():
    cadena = request.args.get("cadena")
    print(cadena)
    if not cadena:
        return(
            jsonify({"error": f"Se requiere un nombre en los parametros de la URL"}),400,
        )
    elif cadena != cadena[::-1]:   
        return jsonify({"La cadena es palindromo": cadena})
    return jsonify({"La cadena no es palindromo": cadena})

@app.route('/contar', methods=['GET'])
def contar():
    cadena = request.args.get("cadena")
    vocal = request.args.get("vocal")
    if not cadena and not vocal:
        return(
            jsonify({"error": f"Se requiere un nombre en los parametros de la URL"}),400,
        )
    sumaVocal = cadena.count(vocal)
    return jsonify({"cantidad de vocales": sumaVocal})
#Por defecto iniciara en el puerto 5000
if __name__ == '__main__':
    app.run()