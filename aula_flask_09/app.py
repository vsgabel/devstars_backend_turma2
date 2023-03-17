from os.path import abspath, dirname, join
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import *

basedir = abspath(dirname(__file__)) #C:\Users\Victor\Documentos\DevStars\backend_2022_02\aula_flask_09

app = Flask(__name__)
app.config["SECRET_KEY"] = "ahkafjsfahjksafhjks"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{join(basedir, 'db.sqlite')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        aluno = Estudante()
        aluno.nome = form.nome.data

        db.session.add(aluno)
        db.session.commit()
        return redirect(url_for("ver_todos"))
    return render_template("cadastro.html", form=form)

@app.route("/todos")
def ver_todos():
    alunos = Estudante.query.all()
    return render_template("todos.html", alunos=alunos)

if __name__ == "__main__":
    app.run(debug=True)