from os.path import abspath, dirname, join
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = abspath(dirname(__file__)) 
# basedir = C:\Detran\
# nome = db.sqlite
# fullpath = join(basedir, nome)
# sqlite:///C:\Detran\db.sqlite
fullpath = join(basedir, "db.sqlite")

app = Flask(__name__)
app.config["SECRET_KEY"] = "algo muito seguro"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{fullpath}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *
from forms import MotoristaForm, CarroForm, MultaForm

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/motorista/todos")
def motorista_todos():
    dados = Motorista.query.all()
    return render_template("motorista_todos.html", dados=dados)

@app.route("/carro/todos")
def carro_todos():
    dados = Carro.query.all()
    return render_template("carro_todos.html", dados=dados)

@app.route("/multa/todos")
def multa_todos():
    dados = Multa.query.all()
    return render_template("multa_todos.html", dados=dados)

@app.route("/motorista/novo")
def motorista_novo():
    form = MotoristaForm()
    if form.validate_on_submit():
        motorista = Motorista()
        motorista.nome = form.nome.data
        motorista.cpf = form.cpf.data

        db.session.add(motorista)
        db.session.commit()
        return "Motorista adicionado com sucesso"
    return render_template("motorista_novo.html", form=form)

@app.route("/carro/novo", methods=["GET", "POST"])
def carro_novo():
    form = CarroForm()
    motoristas = Motorista.query.all()
    escolhas = []
    for motorista in motoristas:
        escolhas.append((motorista.id, motorista.nome))

    form.motorista.choices = escolhas
    if form.validate_on_submit():
        carro = Carro()
        carro.modelo = form.modelo.data
        carro.placa = form.placa.data
        carro.fabricante = form.fabricante.data
        id_motorista = form.motorista.data
        carro.dono = Motorista.query.filter_by(id=id_motorista).first()
        
        db.session.add(carro)
        db.session.commit()
        return "Carro adicionado com sucesso"
    return render_template("carro_novo.html", form=form)
    
@app.route("/multa/novo", methods=['GET','POST'])
def multa_novo():
    form = MultaForm()
    form.gravidade.choices = [(0,"Leve"), (1,"Média"), (2,"Grave"), (3,"Gravíssima")]

    # Preencher as escolhas do motorista
    motoristas = Motorista.query.all()
    escolhas = []
    for motorista in motoristas:
        escolhas.append((motorista.id, motorista.nome))
    form.motorista.choices = escolhas

    # Preencher as escolhas do carro
    carros = Carro.query.all()
    escolhas = []
    for carro in carros:
        escolhas.append((carro.id, f"{carro.placa} - {carro.fabricante} {carro.modelo}"))
    form.carro.choices = escolhas

    if form.validate_on_submit():
        multa = Multa()
        multa.valor = form.valor.data
        multa.motivo = form.motivo.data
        multa.pontos = form.pontos.data
        multa.gravidade = form.gravidade.data
        id_motorista = form.motorista.data
        multa.motorista = Motorista.query.filter_by(id=id_motorista).first()
        id_carro = form.carro.data
        multa.carro = Carro.query.filter_by(id=id_carro).first()
        db.session.add(multa)
        db.session.commit()
        return "Multa cadastrada com sucesso"
    return render_template("multa_novo.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)