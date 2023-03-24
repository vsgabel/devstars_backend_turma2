from app import db

class Motorista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(32), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    carros = db.relationship('Carro', backref="dono")
    multas = db.relationship('Multa', backref="motorista")

    def __str__(self):
        return self.nome

class Carro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fabricante = db.Column(db.String(32), nullable=False)
    modelo = db.Column(db.String(16), nullable=False)
    placa = db.Column(db.String(8), nullable=False, unique=True)
    dono_id = db.Column(db.Integer, db.ForeignKey("motorista.id"))
    multas = db.relationship('Multa', backref="carro")

    def __str__(self):
        return f"{self.placa} - {self.fabricante} {self.modelo}"

class Multa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float)
    motivo = db.Column(db.String(32))
    pontos = db.Column(db.Integer)
    gravidade = db.Column(db.Integer)
    motorista_id = db.Column(db.Integer, db.ForeignKey("motorista.id"))
    carro_id = db.Column(db.Integer, db.ForeignKey("carro.id"))