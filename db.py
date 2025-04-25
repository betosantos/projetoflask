from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv()


db = SQLAlchemy()

def init_db(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:AjdObfnXSVPSnIzUmZYpaUCLkPXKZUTr@tramway.proxy.rlwy.net:55888/railway'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)