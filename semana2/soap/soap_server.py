from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
    return "¡Hola, {}!".format(nombre)

def sumaDosNumeros(x,y):
    return "Resultado: {} ".format(x+y)

def cadenaPalindromo(palabra):
    cad=""
    for i in range(len(palabra)-1, -1, -1):
        cad=cad+palabra[i]
    if(cad==palabra):
        return "{}".format(True)
    return "{}".format(False)

dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo": str},
    args={"nombre": str},
)

dispatcher.register_function(
    "SumaDosNumeros",
    sumaDosNumeros,
    returns={"resultado": str},
    args={"x": int, "y":int},
)

dispatcher.register_function(
    "CadenaPalindromo",
    cadenaPalindromo,
    returns={"palindromo ":str},
    args={"palabra": str},
)

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()