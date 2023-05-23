from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def carrega_usuario(usr_id):
    return Usuario.query.get(int(usr_id))

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(32))
    data_nascimento = db.Column(db.Date)
    usuario = db.Column(db.String(32), unique=True)
    senha_hash = db.Column(db.String(128))

    @property
    def senha(self):
        raise AttributeError("Você não pode ler o atributo de senha")

    @senha.setter
    def senha(self, s):
        self.senha_hash = generate_password_hash(s)

    def verifica_senha(self, senha: str) -> bool:
        validacao = check_password_hash(self.senha_hash, senha)
        return validacao