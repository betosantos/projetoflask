import os
from flask import Flask, render_template, request, jsonify, url_for, redirect
from datetime import datetime
from models import db, Pessoa
from dotenv import load_dotenv


# Carrega variáveis de ambiente
load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:caconde138@localhost:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa banco
db.init_app(app)


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

    nova_pessoa = Pessoa(
        nome=nome, 
        email=email
    )
    db.session.add(nova_pessoa)
    db.session.commit()

    return redirect(url_for('form'))





if __name__ == "__main__":
    app.run(debug=True)
