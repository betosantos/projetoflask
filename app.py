import os
from flask import Flask, render_template, request, jsonify
from datetime import datetime
from models import db, Acesso, User, Location
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa banco
db.init_app(app)

# Cria tabelas
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_location', methods=['POST'])
def save_location():
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')
    if lat is not None and lon is not None:
        loc = Location(latitude=lat, longitude=lon)
        db.session.add(loc)
        db.session.commit()
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

if __name__ == "__main__":
    app.run(debug=True)
