from flask import Blueprint

motorista = Blueprint("motorista", __name__)

from app.motorista import routes