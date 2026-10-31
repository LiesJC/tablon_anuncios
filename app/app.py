# app/app.py
from flask import Flask, render_template
from config import Config
from app.extensions import db, migrate, login_manager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    #Registrar Blueprints 
    from app.auth.routes import bp_auth
    from app.usuarios.routes import bp_usuarios
    from app.categorias.routes import bp_categorias
    from app.anuncios.routes import bp_anuncios

    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_usuarios, url_prefix='/usuarios')
    app.register_blueprint(bp_categorias, url_prefix='/categorias')
    app.register_blueprint(bp_anuncios, url_prefix='/anuncios')

    #Ruta principal
    @app.route('/')
    def index():
        return render_template('base.html') 
    return app

@login_manager.user_loader
def load_user(user_id):
    from app.models import Usuario
    return Usuario.query.get(int(user_id))