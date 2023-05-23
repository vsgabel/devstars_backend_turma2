from app import db
from app.pac import pac
from app.pac.forms import PacienteForm
from app.models import Paciente, Permissao
from flask import render_template, abort
from flask_login import login_required, current_user
from app.decorators import verificar_permissao, verificar_papel

@pac.route("/lista")
@login_required
# @pode_ver
@verificar_permissao(Permissao.VER)
def lista():
    l = Paciente.query.all()
    return render_template("lista.html", lista=l)

@pac.route("/adicionar", methods=["GET", "POST"])
@login_required
@verificar_permissao(Permissao.ADICIONAR)
def adicionar():
    form = PacienteForm()
    if form.validate_on_submit():
        p = Paciente()
        p.cpf = form.cpf.data
        p.nome = form.nome.data

        db.session.add(p)
        db.session.commit()
        return "Paciente adicionado com sucesso"
    return render_template("adicionar.html", form=form)

@pac.route("/remover/<int:id>")
@login_required
@verificar_permissao(Permissao.REMOVER)
def remover(id: int):
    pa = Paciente.query.get(id)
    if pa:
        # Paciente.query.filter_by(id=id).delete()
        pa.delete()
        db.session.commit()
        return "Paciente removido com sucesso"
    return "Paciente não encontrado"    


def admin():
    if current_user.is_authenticated and current_user.papel.nome == "Admin":
        return "Você é um admin"
    abort(403)

pac.add_url_rule('/admin', 'admin', admin)