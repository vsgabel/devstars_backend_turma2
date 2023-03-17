from app import mail
from flask import render_template
from flask_mail import Message

def enviar_email(assunto: str, remetente: str, destinatarios: list[str], template: str, **kwargs):
    msg = Message(assunto, sender=remetente, recipients=destinatarios)
    msg.html = render_template(template, **kwargs)
    mail.send(msg)