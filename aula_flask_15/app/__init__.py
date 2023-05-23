from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    login_manager.init_app(app)

    from app.auth import auth as auth_bp
    from app.pac import pac as pac_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(pac_bp, url_prefix="/pacientes")

    return app