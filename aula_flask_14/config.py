from os import getenv

class Config:
    SECRET_KEY = getenv('SECRET_KEY') or "algo muito seguro"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URI")

config = {
    "development": DevelopmentConfig,

    "default": DevelopmentConfig
}