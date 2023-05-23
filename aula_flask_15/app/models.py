from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Permissao:
    NENHUM = 0
    VER = 1
    ADICIONAR = 2
    REMOVER = 4

@login_manager.user_loader
def user_loader(id):
    return Usuario.query.get(int(id)) # Usuario.query.filter_by(id=int(id)).first()

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32), nullable=False, unique=True)
    senha_hash = db.Column(db.String(128), nullable=False)
    papel_id = db.Column(db.Integer, db.ForeignKey('papel.id'))
    ativo = db.Column(db.Boolean, default=False)

    @property
    def senha(self):
        return AttributeError("Não pode ver a senha")
    
    @senha.setter
    def senha(self, valor):
        self.senha_hash = generate_password_hash(valor)

    def verifica_senha(self, valor):
        return check_password_hash(self.senha_hash, valor)

class Papel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(16), nullable=False)
    perm = db.Column(db.Integer, nullable=False)
    usuarios = db.relationship('Usuario', backref='papel')

    def __init__(self, **kwargs):
        super(Papel, self).__init__(**kwargs)
        if self.perm is None:
            self.perm = 0
            
    def adicionar_perm(self, permissao: int): #papel.adicionar_perm(Permissao.ver)
        if not self.verifica_perm(permissao):
            self.perm += permissao

    def remover_perm(self, permissao: int):
        if self.verifica_perm(permissao):
            self.perm -= permissao

    def redefinir_perm(self):
        self.perm = 0

    def verifica_perm(self, permissao: int) -> bool:
        return self.perm & permissao == permissao
    
    @staticmethod
    def inserir():
        papeis = {
            "Inativo": [Permissao.NENHUM],
            "Comum": [Permissao.VER],
            "Cadastro": [Permissao.VER, Permissao.ADICIONAR],
            "Admin": [Permissao.VER, Permissao.ADICIONAR, Permissao.REMOVER]
        }
        for nome_papel in papeis:
            papel = Papel.query.filter_by(nome=nome_papel).first()
            if not papel:
                papel = Papel(nome=nome_papel)
            papel.redefinir_perm()
            for perm in papeis[nome_papel]:
                papel.adicionar_perm(perm)
            db.session.add(papel)
        db.session.commit()

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(32), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)