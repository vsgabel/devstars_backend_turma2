import os
from os.path import abspath, dirname, join

basedir = abspath(dirname(__file__)) 

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or "usa algo seguro"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    fullpath = join(basedir, "db.sqlite")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{fullpath}"

class TestingConfig(Config):
    fullpath = join(basedir, "test_db.sqlite")
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{fullpath}"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig
}
