from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    nombre = db.Column(db.String(100))
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(50))
    rol_id = db.Column(db.Integer)

def is_authenticated(self):
    return True

def is_active(self):
    return self.activate

def is_anonymous(self):
    return False

def get_id(self):
    try:
        return unicode(self.id)  # python 2
    except NameError:
        return str(self.id)  # python 3

