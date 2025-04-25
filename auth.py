from flask import Blueprint, render_template, redirect, request, session, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import Usuario
from db import db
from functools import wraps
from flask_login import login_user, logout_user

auth = Blueprint('auth', __name__)



@auth.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']        
        senha = generate_password_hash(request.form['senha'])         
        if Usuario.query.filter_by(email=email).first():
            flash('Usuário já existe')
            return redirect(url_for('auth.registro'))

        new_user = Usuario(nome=nome, email=email, senha=senha)
        db.session.add(new_user)
        db.session.commit()        
        return redirect(url_for('auth.login'))
    return render_template('registro.html')



@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        user = Usuario.query.filter_by(email=email).first()

        if user and check_password_hash(user.senha, senha):
            login_user(user)  
            print('Sucesso!!')
            return redirect(url_for('painel'))              
        else:
            print('Erro')
            return redirect(url_for('auth.login'))  
    return render_template('login.html')



@auth.route('/logout')
def logout():
    logout_user()  # Flask-Login cuida da sessão automaticamente
    return redirect(url_for('auth.login'))  # Redireciona para a página de login


