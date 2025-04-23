import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from db import db
from models import Usuario, Formcontato, Acesso
load_dotenv()

app = Flask(__name__)

# Configurações do banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:AjdObfnXSVPSnIzUmZYpaUCLkPXKZUTr@tramway.proxy.rlwy.net:55888/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Inicializa o db com o app
db.init_app(app)
# Cria as tabelas
with app.app_context():
    db.create_all()


@app.before_request
def registrar_acesso():
    if request.endpoint not in ('static'):
        novo_acesso = Acesso(
            ip=request.remote_addr,
            url=request.path,
            user_agent=request.headers.get('User-Agent')
        )
        db.session.add(novo_acesso)
        db.session.commit()


@app.route('/')
def home():    
    usuarios = Usuario.query.all()
    #return render_template('index.html', usuarios=usuarios)
    return render_template('base.html')



@app.route('/form', methods=['GET', 'POST'])
def form():
    usuarios = Usuario.query.all()
    print(usuarios)
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        novo_usuario = Usuario(nome=nome, email=email)
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect(url_for('home'))    
    return render_template('form.html', usuarios=usuarios)



@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email =  request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']
        novo_contato = Formcontato(nome=nome, email=email, assunto=assunto, mensagem=mensagem)
        db.session.add(novo_contato)
        db.session.commit()        
        return jsonify({"mensagem": "Mensagem recebida com sucesso!"})




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
