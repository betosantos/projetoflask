import os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from db import db
from models import Usuario
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



@app.route('/')
def home():    
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        novo_usuario = Usuario(nome=nome, email=email)
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('form.html')




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
