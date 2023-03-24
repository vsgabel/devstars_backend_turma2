from app import db
from app.motorista.forms import MotoristaForm
from app.models import Motorista
from app.motorista import motorista
from flask import render_template

@motorista.route("/todos")
def todos():
    dados = Motorista.query.all()
    return render_template("motorista_todos.html", dados=dados)

@motorista.route("/novo")
def novo():
    form = MotoristaForm()
    if form.validate_on_submit():
        m = Motorista()
        m.nome = form.nome.data
        m.cpf = form.cpf.data

        db.session.add(m)
        db.session.commit()
        return "Motorista adicionado com sucesso"
    return render_template("motorista_novo.html", form=form)

@motorista.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id: int):
    m = Motorista.query.filter_by(id=id).first()
    form = MotoristaForm(obj=m)
    if form.validate_on_submit():
        m.nome = form.nome.data
        m.cpf = form.cpf.data

        db.session.add(m)
        db.session.commit()
        return f"Motorista adicionado com sucesso"
    return render_template("motorista_novo.html", form=form)
