from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class CarroForm(FlaskForm):
    fabricante = StringField('Fabricante', validators=[DataRequired()])
    modelo = StringField('Modelo', validators=[DataRequired()])
    placa = StringField('Placa', validators=[DataRequired(), Length(max=9)])
    motorista = SelectField('Motorista')
    submit = SubmitField('Enviar')