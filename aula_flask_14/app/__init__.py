from config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    db.init_app(app)
    login_manager.init_app(app)

    return app
