from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class CadastroForm(FlaskForm):
    nome = StringField("Nome")
    submit = SubmitField("Cadastrar")