from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    from app.main import main as main_bp
    from app.motorista import motorista as motorista_bp
    from app.carro import carro as carro_bp
    from app.multa import multa as multa_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(motorista_bp, url_prefix="/motorista")
    app.register_blueprint(carro_bp, url_prefix="/carro")
    app.register_blueprint(multa_bp, url_prefix="/multa")
    
    return app