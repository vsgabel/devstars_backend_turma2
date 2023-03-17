import os
from flask import Flask, request
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['MAIL_SERVER'] = os.getenv("MAIL_SERVER")
app.config['MAIL_PORT'] = os.getenv("MAIL_PORT")
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = bool(os.getenv("MAIL_USE_TLS"))
app.config['MAIL_USE_SSL'] = bool(os.getenv("MAIL_USE_SSL"))

mail = Mail(app)
from util import enviar_email

@app.route("/email")
def email():
    args = request.args
    assunto = args['assunto']
    remetente = args['remetente']
    destinatario = ['victor.gabel@gmail.com']
    nome = args['nome']

    enviar_email(assunto, remetente, destinatario, 'welcome.html', nome=nome)

    


if __name__ == "__main__":
    app.run(debug=True)
    