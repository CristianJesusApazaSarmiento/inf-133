from database import db

class Animal(db.Model):
    __tablename__ = "animals"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Animal.query.all()

    @staticmethod
    def get_by_id(id):
        return Animal.query.get(id)

    def update(self, name=None, species=None, age=None):
        if name is not None:
            self.name = name
        if species is not None:
            self.species = species
        if age is not None:
            self.age = age
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()