from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length

class MotoristaForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired(), Length(min=11, max=11)])
    submit = SubmitField('Enviar')

class CarroForm(FlaskForm):
    fabricante = StringField('Fabricante', validators=[DataRequired()])
    modelo = StringField('Modelo', validators=[DataRequired()])
    placa = StringField('Placa', validators=[DataRequired(), Length(max=9)])
    motorista = SelectField('Motorista')
    submit = SubmitField('Enviar')

class MultaForm(FlaskForm):
    valor = FloatField('Valor')
    motivo = StringField('Motivos')
    pontos = IntegerField('Pontos')
    gravidade = SelectField('Gravidade')
    motorista = SelectField('Motorista')
    carro = SelectField('Carro')
    submit = SubmitField('Enviar')

