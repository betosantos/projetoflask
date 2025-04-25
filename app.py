import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash
from dotenv import load_dotenv
from models import Usuario, Formcontato
from db import init_db, db
from auth import auth
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

load_dotenv()

app = Flask(__name__)
app.secret_key = 'sua_chave_ultra_secreta_123456'

init_db(app)

# Configurando o LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# A associação do login_required do Flask-Login
login_manager.login_view = "auth.login"  # Caso o usuário não esteja autenticado, redireciona para o login

# Função para carregar o usuário
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

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




@app.route('/painel')
@login_required
def painel():
    return render_template('painel.html', usuario=current_user)  # O usuário logado é automaticamente acessado via current_user



@app.route('/logout')
def logout():
    logout_user()  # Finaliza a sessão do usuário
    return redirect(url_for('auth.login'))  # Redireciona para a página de login


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
