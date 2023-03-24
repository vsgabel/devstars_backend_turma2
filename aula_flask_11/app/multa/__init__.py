from flask import Blueprint

multa = Blueprint('multa',__name__)

from app.multa import routes