from app import db
from app.carro.forms import CarroForm
from app.models import Carro, Motorista
from app.carro import carro
from flask import render_template

@carro.route("/todos")
def todos():
    dados = Carro.query.all()
    return render_template("carro_todos.html", dados=dados)

@carro.route("/novo", methods=["GET", "POST"])
def novo():
    form = CarroForm()
    motoristas = Motorista.query.all()
    escolhas = []
    for motorista in motoristas:
        escolhas.append((motorista.id, motorista.nome))

    form.motorista.choices = escolhas
    if form.validate_on_submit():
        c = Carro()
        c.modelo = form.modelo.data
        c.placa = form.placa.data
        c.fabricante = form.fabricante.data
        id_motorista = form.motorista.data
        c.dono = Motorista.query.filter_by(id=id_motorista).first()
        
        db.session.add(c)
        db.session.commit()
        return "Carro adicionado com sucesso"
    return render_template("carro_novo.html", form=form)