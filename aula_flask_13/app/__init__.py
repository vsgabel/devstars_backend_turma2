from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from config import config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    login_manager.init_app(app)
    Session(app)

    from app.main import main as main_bp
    from app.auth import auth as auth_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app