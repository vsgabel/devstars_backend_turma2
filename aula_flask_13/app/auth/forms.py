from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField

class LoginForm(FlaskForm):
    usuario = StringField("Usuário")
    senha = PasswordField("Senha")
    submit = SubmitField("Entrar")