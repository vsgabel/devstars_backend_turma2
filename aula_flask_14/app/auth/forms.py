from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class LoginForm(FlaskForm):
    usuario = StringField("Usuário")
    senha = PasswordField("Senha")
    submit = SubmitField("Entrar")