
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)



class Acesso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(100))
    rota = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

