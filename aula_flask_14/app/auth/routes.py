from app.auth import auth
from app.auth.forms import LoginForm
from app.models import Usuario
from flask import render_template
from flask_login import login_user

@auth.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usr = form.usuario.data
        pwd = form.senha.data

        u = Usuario.query.filter_by(usuario=usr).first()
        if u.verifica_senha(pwd):
            login_user(u)
            return "Usuário logado"
        return "Usuário ou senha inválidos"
    return render_template("login.html", form=form)
