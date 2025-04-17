import os
from flask import Flask, render_template, request, redirect, url_for
from db import db
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave_padrao')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

print("App:", app)
print("DB:", db)

db.init_app(app)  # <-- aqui dá erro se importar Pessoa antes disso

from models import Pessoa  # <-- só importa depois de db.init_app(app)


@app.route('/')
def home():    
    return render_template('index.html')

@app.route('/pessoas')
def index():    
    pessoas = Pessoa.query.all()
    return render_template('index.html', pessoas=pessoas)

@app.route('/form')
def form():
    pessoas = Pessoa.query.all()    
    return render_template('form.html', pessoas=pessoas)

@app.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    email = request.form['email']
    nova_pessoa = Pessoa(nome=nome, email=email)
    db.session.add(nova_pessoa)
    db.session.commit()
    return redirect(url_for('form'))

# Criar tabelas ao subir
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
