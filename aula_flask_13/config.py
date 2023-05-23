from os import getenv
from os.path import join, abspath, dirname

basedir = abspath(dirname(__file__))

class Config:
    SECRET_KEY = getenv("SECRET_KEY") or "algo muito seguro"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{join(basedir, 'db.sqlite')}"

config = {
    "default": DevelopmentConfig
}