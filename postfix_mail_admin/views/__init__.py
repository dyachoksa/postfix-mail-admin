import flask

from .auth import auth_blueprint
from .dashboard import dashboard


def register_blueprints(app: flask.Flask):
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(dashboard)
