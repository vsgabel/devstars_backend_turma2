from app import db
from app.multa.forms import MultaForm
from app.models import Multa, Carro, Motorista
from app.multa import multa
from flask import render_template

@multa.route("/todos")
def todos():
    dados = Multa.query.all()
    return render_template("multa_todos.html", dados=dados)
  
@multa.route("/novo", methods=['GET','POST'])
def novo():
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
        m = Multa()
        m.valor = form.valor.data
        m.motivo = form.motivo.data
        m.pontos = form.pontos.data
        m.gravidade = form.gravidade.data
        id_motorista = form.motorista.data
        m.motorista = Motorista.query.filter_by(id=id_motorista).first()
        id_carro = form.carro.data
        m.carro = Carro.query.filter_by(id=id_carro).first()
        db.session.add(m)
        db.session.commit()
        return "Multa cadastrada com sucesso"
    return render_template("multa_novo.html", form=form)