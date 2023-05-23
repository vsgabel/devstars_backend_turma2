from app.main import main
from app.models import Usuario
from flask import render_template, redirect, url_for
from flask_login import current_user, login_required

@main.route("/")
def index():
    valor = "anônimo"
    if current_user.is_authenticated:
        valor = current_user.nome
    return render_template("index.html", usr=valor)


@main.route("/segredo")
@login_required
def segredo():
    return "Bem-vindo a rota secreta"