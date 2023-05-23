from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Enviar')


class CadastroForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    nome = StringField('Nome', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Enviar')

