from flask import Flask
from controllers.libro_controller import libro_bp
from flask_swagger_ui import get_swaggerui_blueprint
from database import db

app = Flask(__name__)

SWAGGER_URL = "/api/docs" 
API_URL = "/static/swagger.json" 
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Biblioteca API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(libro_bp, url_prefix="/api")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)