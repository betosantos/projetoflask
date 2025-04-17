
from app import app
from db import db
from models import Usuario

with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso no Railway!")