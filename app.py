import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash
from dotenv import load_dotenv
from models import Usuario, Formcontato
from db import init_db, db
from flask_login import LoginManager
from auth import auth
load_dotenv()

app = Flask(__name__)
app.secret_key = 'sua_chave_ultra_secreta_123456'

init_db(app)



app.register_blueprint(auth)



@app.route('/')
def home():        
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



#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        email = request.form['email']
#        senha = request.form['senha']
#        
#        usuario = Usuario.query.filter_by(email=email, senha=senha).first()
#
#        if usuario:            
#            print('Login realizado com sucesso!')
#            return redirect(url_for('painel'))
#        else:
#            print('E-mail ou senha incorretos.')
#    return render_template('login.html')


@app.route('/painel')
def painel():
    if 'usuario' not in session:
        flash('Você precisa estar logado para acessar essa página.', 'warning')
        return redirect(url_for('login'))
    
    return render_template('painel.html', usuario=session['usuario'])



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
