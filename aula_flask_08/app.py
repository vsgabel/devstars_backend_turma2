import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

class ContatoForm(FlaskForm):
    remetente = StringField("E-mail")
    assunto = StringField("Assunto")
    mensagem = TextAreaField("Mensagem")
    submit = SubmitField("Enviar")
    
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER")
app.config["MAIL_PORT"] = os.getenv("MAIL_PORT")
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_USE_TLS"] = True #int(os.getenv("MAIL_USE_TLS"))
app.config["MAIL_USE_SSL"] = False #int(os.getenv("MAIL_USE_SSL"))

mail = Mail(app)

def enviar_email(assunto: str, remetente: str, destinatarios: list[str], texto: str):
    msg = Message(assunto)
    msg.sender = remetente
    msg.recipients = destinatarios
    msg.body = texto

    mail.send(msg)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contato', methods=["GET", "POST"])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        assunto = form.assunto.data
        remetente = form.remetente.data
        msg = form.mensagem.data
        enviar_email(assunto, remetente, ['victor.gabel@gmail.com'], msg)
        return f"Sua mensagem foi enviada. Espere um retorno em {remetente}"
    return render_template("contato.html", form=form)

if __name__ == "__main__":
    app.run()