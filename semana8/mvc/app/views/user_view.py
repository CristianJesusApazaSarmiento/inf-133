#render_template, Funcion que permite como renderizar la pagina 
from flask import render_template

def usuarios(users):
    return render_template("usuarios.html", users=users)

def registro():
    return render_template("registro.html")

