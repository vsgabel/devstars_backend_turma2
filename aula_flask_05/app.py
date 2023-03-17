from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContatoForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    msg = TextAreaField("Mensagem", validators=[DataRequired()])
    submit = SubmitField("Enviar", validators=[DataRequired()])

app = Flask(__name__)
app.config["SECRET_KEY"] = "uma chave muito segura"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/noticias")
def noticias():
    lista = ["Notícia 1", "Notícia 2", "Notícia 3"]
    return render_template("noticias.html", lista=lista)

@app.route("/contato", methods=["GET", "POST"])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        return render_template("mensagem_enviada.html", nome=nome, email=email)
    return render_template("contato_novo.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)