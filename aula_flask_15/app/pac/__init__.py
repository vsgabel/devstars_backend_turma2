from flask import Blueprint

pac = Blueprint("pac", __name__)

from app.pac import routes