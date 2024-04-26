from database import db
from datetime import datetime
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    birthdate=db.Column(db.String(50), nullable=False)
    
    def __init__(self, first_name, last_name, email, password, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password= password
        self.birthdate = datetime.strptime(birthdate,"%Y-%m-%d").date()
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @staticmethod
    def get_all():
        return User.query.all()
    
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    
    def update(self):
        db.session.commit()
        
    def delete(self, user):
        db.session.delete(user)
        db.session.commit()
    