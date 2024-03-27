from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Base de datos simulada de pizzas
tacos = {
    
}


# Producto: Pizza
class Taco:
    def __init__(self):
        self.base = None
        self.guiso = None
        self.toppings = []
        self.salsa = None

    def __str__(self):
        return f"Base: {self.base}, Guiso: {self.guiso}, Toppings: {', '.join(self.toppings)}, Salsa: {self.salsa}"


# Builder: Constructor de pizzas
class TacoBuilder:
    def __init__(self):
        self.taco = Taco()

    def set_base(self, base):
        self.taco.base = base

    def set_guiso(self, guiso):
        self.taco.guiso = guiso

    def add_topping(self, topping):
        self.taco.toppings.append(topping)
    
    def set_salsa(self, salsa):
        self.taco.salsa = salsa

    def get_taco(self):
        return self.taco


# Director: Pizzería
class Taqueria:
    def __init__(self, builder):
        self.builder = builder

    def create_taco(self, base, guiso, toppings, salsa):
        self.builder.set_base(base)
        self.builder.set_guiso(guiso)
        for topping in toppings:
            self.builder.add_topping(topping)
        self.builder.set_salsa(salsa)
        return self.builder.get_taco()


# Aplicando el principio de responsabilidad única (S de SOLID)
#Manejar todas las acciones de la pizza, la clase PizzaService
class TacoService:
    def __init__(self):
        self.builder = TacoBuilder()
        self.taqueria = Taqueria(self.builder)

    def create_taco(self, post_data):
        base = post_data.get("base", None)
        guiso = post_data.get("guiso", None)
        toppings = post_data.get("toppings", [])
        salsa = post_data.get("salsa", None)

        taco = self.taqueria.create_taco(base, guiso, toppings, salsa)
        tacos[len(tacos) + 1] = taco
        
        return taco

    #Lo esta transformando en un diccionario con el .__dict__
    #
    def read_tacos(self):
        return {index: taco.__dict__ for index, taco in tacos.items()}

    #El get obtiene un key, none, none, []lista vacia
    def update_taco(self, index, post_data):
        if index in tacos:
            taco = tacos[index]
            base = post_data.get("base", None)
            guiso = post_data.get("guiso", None)
            toppings = post_data.get("toppings", [])
            salsa = post_data.get("salsa", None)

            if base:
                taco.base = base
            if guiso:
                taco.guiso = guiso
            if toppings:
                taco.toppings = toppings
            if salsa:
                taco.salsa = salsa

            return taco
        else:
            return None

    #Borrando la pizza por el index, pop para sacar la pizza de la lista
    def delete_taco(self, index):
        if index in tacos:
            return tacos.pop(index)
        else:
            return None

#
class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    #Lectura de la informacion
    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


# Manejador de solicitudes HTTP
#def __init__ el constructor de la clase
class TacoHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.controller = TacoService()
        super().__init__(*args, **kwargs)

    #.__dict__ convertir cualquier cosa en diccionarios
    def do_POST(self):
        if self.path == "/tacos":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.controller.create_taco(data)
            HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    #
    def do_GET(self):
        if self.path == "/tacos":
            response_data = self.controller.read_tacos()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    #Actualizar por ID, 
    #El index se lo envia desde la URL
    #PizzaService, esta instanciado en Controller
    def do_PUT(self):
        if self.path.startswith("/tacos/"):
            index = int(self.path.split("/")[2])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.controller.update_taco(index, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"Error": "Índice de taco no válido"}
                )
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    #Se nos envia el index, despues del / en la ruta
    #PizzaService, se llama controller
    def do_DELETE(self):
        if self.path.startswith("/tacos/"):
            index = int(self.path.split("/")[2])
            deleted_taco = self.controller.delete_taco(index)
            if deleted_taco:
                HTTPDataHandler.handle_response(
                    self, 200, {"message": "Taco eliminada correctamente"}
                )
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"Error": "Índice de taco no válido"}
                )
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})


def run(server_class=HTTPServer, handler_class=TacoHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Iniciando servidor HTTP en puerto {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()