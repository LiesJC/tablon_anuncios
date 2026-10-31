import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una-clave-muy-secreta'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bd_anuncios.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False