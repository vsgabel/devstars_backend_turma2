from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.fields import IntegerField, SubmitField
from wtforms.validators import DataRequired

idades = []

class IdadeForm(FlaskForm):
    idade = IntegerField("Idade", validators=[DataRequired()])
    submit = SubmitField("Enviar")

def media(dados: list[int]) -> float:
    soma = 0
    for dado in dados:
        soma += dado
    return soma/len(dados)

def desvio(dados: list[int]) -> float:
    m = media(dados)
    soma = 0
    for dado in dados:
        soma += (dado - m)**2
    soma = soma/len(dados)
    return soma ** 0.5

app = Flask(__name__)
app.config["SECRET_KEY"] = "uma chave muito segura"

@app.route("/", methods=['GET', 'POST'])
def index():
    form = IdadeForm()
    if form.validate_on_submit():
        idade = form.idade.data
        idades.append(idade)
        return render_template("obrigado.html")
    return render_template("index.html", form=form)

@app.route("/resultado")
def resultado():
    if len(idades) == 0:
        d = 0
        m = 0
    else:
        d = desvio(idades)
        m = media(idades)
    return render_template("resultado.html", m=m, d=d)

if __name__ == "__main__":
    app.run()