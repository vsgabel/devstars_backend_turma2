from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField, IntegerField

class MultaForm(FlaskForm):
    valor = FloatField('Valor')
    motivo = StringField('Motivos')
    pontos = IntegerField('Pontos')
    gravidade = SelectField('Gravidade')
    motorista = SelectField('Motorista')
    carro = SelectField('Carro')
    submit = SubmitField('Enviar')