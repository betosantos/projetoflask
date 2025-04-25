from flask import Blueprint, render_template, redirect, request, session, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import Usuario
from db import db

auth = Blueprint('auth', __name__)



@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        if Usuario.query.filter_by(username=username).first():
            flash('Usuário já existe')
            return redirect(url_for('auth.register'))

        new_user = Usuario(username=username, password=password)
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
            session['id'] = user.id            
            return redirect(url_for('painel'))
        flash('Credenciais inválidas')
    return render_template('login.html')


@auth.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth.login'))
