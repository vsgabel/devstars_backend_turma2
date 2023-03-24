import os
from os.path import abspath, dirname, join

basedir = abspath(dirname(__file__)) 
fullpath = join(basedir, "db.sqlite")

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or "usa algo seguro"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{fullpath}"

class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig
}
