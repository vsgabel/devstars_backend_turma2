from flask import Blueprint

carro = Blueprint("carro",__name__)

from app.carro import routes
    
