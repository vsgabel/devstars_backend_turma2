from flask import Blueprint, render_template

main = Blueprint('main',__name__)

from app.main import routes