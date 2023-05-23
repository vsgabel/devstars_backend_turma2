import os

class Config:
    SECRET_KEY = "ALFAJKF"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")

config = {
    "development": DevelopmentConfig,

    "default": DevelopmentConfig
}