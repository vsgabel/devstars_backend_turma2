from app.auth import auth
from app.auth.forms import LoginForm
from app.models import Usuario
from flask import render_template, redirect, url_for, session
from flask_login import login_user, logout_user

@auth.route("/login", methods=["GET", "POST"])
def login():
    global usuarios_logados
    form = LoginForm()
    if form.validate_on_submit():
        usr = form.usuario.data
        pwd = form.senha.data

        u = Usuario.query.filter_by(usuario=usr).first()
        if u and u.verifica_senha(pwd):
            login_user(u)
            return redirect(url_for('main.index'))
        else:
            return "Usuário ou senha inválidos"
    return render_template("login.html", form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))