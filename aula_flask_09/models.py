from app import db

class Estudante(db.Model):
    __tablename__ = "estudante"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(32), nullable=False)
    data = db.Column(db.String(8))

class Professor(db.Model):
    __tablename__ = "professor"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(32), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)