from flask import Flask, render_template
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
moment = Moment(app)

@app.route("/")
def index():
    return render_template("index.html", nome="mundo")

@app.route("/horario_atual")
def momento():
    return render_template("momento.html", horario=datetime.now())

@app.route("/<nome>")
def index2(nome: str):
    return render_template("index.html", nome=nome)

if __name__ == "__main__":
    app.run()