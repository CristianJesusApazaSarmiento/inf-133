from database import db
from datetime import datetime
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    contraseña = db.Column(db.String(50), nullable=False)
    fecha_de_nacimiento=db.Column(db.Date(), nullable=False)
    
    def __init__(self, first_name, last_name, email, contraseña, fecha_de_nacimiento):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contraseña= contraseña
        self.fecha_de_nacimiento = fecha_de_nacimiento
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @staticmethod
    def get_all():
        return User.query.all()