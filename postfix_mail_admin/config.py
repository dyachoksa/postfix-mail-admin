import os

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class Config:
    DEBUG = False
    SECRET_KEY = "jjY2fy6yjfkvRgwZZ9HV77SES2tEf4xR"

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE}/app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_RECORD_QUERIES = True
