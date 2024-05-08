from flask import Flask

from controllers import user_controller

from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

#Aqui es donde se registran los controladores
app.register_blueprint(user_controller.user_bp)

if __name__ == "__main__":
    #Crea las tablas si no existen
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    