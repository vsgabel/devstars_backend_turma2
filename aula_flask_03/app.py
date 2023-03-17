from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    lista_alunos = ['Alan', 'Francisco', 'João']
    return render_template('index.html', lista=lista_alunos)

if __name__ == "__main__":
    app.run()