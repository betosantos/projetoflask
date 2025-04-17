import os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)

# Configuração do banco de dados MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:AjdObfnXSVPSnIzUmZYpaUCLkPXKZUTr@tramway.proxy.rlwy.net:55888/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
print(db)

@app.route('/')
def home():    
    return render_template('index.html')


@app.route('/form')
def form(): 
    return render_template('form.html')



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
