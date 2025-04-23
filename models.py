from datetime import datetime
from zoneinfo import ZoneInfo
from db import db


class Usuario(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<Usuario {self.nome}>'
    

class Formcontato(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    assunto = db.Column(db.String(200), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Contato {self.nome}>'
    

class Acesso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(50))
    url = db.Column(db.String(200))
    user_agent = db.Column(db.String(300))
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(ZoneInfo("America/Sao_Paulo")))