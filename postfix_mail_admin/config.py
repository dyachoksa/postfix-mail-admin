import os

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get(
        "SECRET_KEY", "jjY2fy6yjfkvRgwZZ9HV77SES2tEf4xR"
    )

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{BASE}/app.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_RECORD_QUERIES = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_RECORD_QUERIES = False
