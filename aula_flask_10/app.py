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
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{fullpath}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)