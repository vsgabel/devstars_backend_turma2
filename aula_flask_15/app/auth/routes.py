from app import db
from app.models import Usuario, Papel
from app.auth import auth
from app.auth.forms import LoginForm, CadastroForm
from flask import render_template, redirect, url_for, current_app
from flask_login import login_user, logout_user, login_required, current_user
from app.serializer import Serializer

@auth.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        senha = form.senha.data
        
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.verifica_senha(senha):
            login_user(usuario)
            return "Login efetuado com sucesso"
        return "Usuário ou senha inválidos"
    return render_template("login.html", form=form)

@auth.route("/registro", methods=["GET", "POST"])
def registro():
    form = CadastroForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        senha = form.senha.data
        usuario = Usuario(nome=nome, email=email, senha=senha)
        db.session.add(usuario)
        db.session.commit()
        return "Usuario Cadastrado com Sucesso"
    return render_template("registro.html", form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/gera_token/<int:id>")
def gera_token(id: int):
    token = Serializer.generate_confirmation_token(current_app.config["SECRET_KEY"], id)
    return token

@auth.route("/ativar/<token>")
@login_required
def ativar(token):
    resultado = Serializer.confirm(current_app.config["SECRET_KEY"], current_user.id, token)
    if resultado:
        u = Usuario.query.get(current_user.id)
        u.ativo = True
        u.papel = Papel.query.filter_by(nome="Comum").first()
        db.session.add(u)
        db.session.commit()
        return "Usuário ativado com sucesso"
    return "Houve um erro"