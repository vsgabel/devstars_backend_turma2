from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PacienteForm(FlaskForm):
    cpf = StringField('CPF', validators=[DataRequired()])
    nome = StringField('Nome', validators=[DataRequired()])
    submit = SubmitField('Enviar')
