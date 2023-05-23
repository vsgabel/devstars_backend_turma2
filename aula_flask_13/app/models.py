from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(usr_id):
    return Usuario.query.get(int(usr_id))

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), nullable=False)
    usuario = db.Column(db.String(32), nullable=False)
    senha = db.Column(db.String(32), nullable=False)

    def verifica_senha(self, senha):
        if self.senha == senha:
            return True
        return False