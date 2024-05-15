from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
# Para decoradores
from functools import wraps
import json
#jsonify para las respuestas

def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return fn(*args, **kwargs)
        except Exception as e:
            #No hay token
            return jsonify({"error": str(e)}), 401

    return wrapper
# parametro roles=[] vacio
def roles_required(roles=[]):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                #verifica si el usuario se ha logeado
                verify_jwt_in_request()
                #identity
                current_user = get_jwt_identity()
                #current_user un diccionario
                user_roles = json.loads(current_user.get("roles", []))
                #Conjunto en python: set que se esta haciendo una interseccion
                if not set(roles).intersection(user_roles):
                    #Si no hubiese interseccion
                    return jsonify({"error": "Acceso no autorizado para este rol"}), 403
                return fn(*args, **kwargs)
            except Exception as e:
                return jsonify({"error": str(e)}), 401

        return wrapper

    return decorator