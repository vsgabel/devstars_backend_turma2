import requests
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)
usrs = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/teste")
def teste():
    escola = "DevStars"
    professor = "Victor"
    alunos = ["Alan", "Gustavo", "João Emanuel", "Francisco"]
    coordenadora = "Lu"

    return render_template("teste.html", escola=escola, professor=professor, alunos=alunos, coordenadora=coordenadora)

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/contato/processar")
def processa_contato():
    dados = request.args
    nome = dados['nome']
    email = dados['email']
    msg = dados['msg']

    return f"O e-mail {email} foi registrado em nome de {nome}"

@app.route("/registro")
def registrar():
    return render_template("registro.html")

@app.route("/registro/processar", methods=['POST'])
def processa_registro():
    dados = request.form
    nome = dados['nome']
    email = dados['email']
    senha = dados['senha']

    usrs[email] = {"nome": nome, "senha": senha}

    return render_template("registro_sucesso.html")

@app.route("/usuarios")
def usuarios():
    return jsonify(usrs)

@app.route("/rio")
def rio():
    url = "https://api.openweathermap.org/data/2.5/weather?q=Rio%20de%20Janeiro&appid=1488a944e8ca18e3249774b86c2216d6&units=metric"
    dados = requests.get(url)
    dados = dados.json()
    temperatura = dados["main"]["temp"]
    return f"{temperatura}"

    
    # retorno apenas da temperatura
@app.route("/taubate")
def taubate():
    url = "https://api.openweathermap.org/data/2.5/weather?q=Taubaté&appid=1488a944e8ca18e3249774b86c2216d6&units=metric"
    resp = requests.get(url)
    dados = resp.json()
    interesse = dados['main']['temp']
    return f'{interesse}'

@app.route("/temperatura/<cidade>")
def temp_cidade(cidade: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=1488a944e8ca18e3249774b86c2216d6&units=metric"
    resp = requests.get(url)
    dados = resp.json()
    temp = dados['main']['temp']
    return redirect(url_for('ver_temp')+f"?cidade={cidade}&temp={temp}")
    # retorno apenas da temperatura

@app.route("/temperatura/ver")
def ver_temp():
    dados = request.args
    cidade = dados['cidade']
    temp = dados['temp']
    return render_template("cidade.html", cidade=cidade, temperatura=temp)
if __name__ == "__main__":
    app.run(debug=True)
