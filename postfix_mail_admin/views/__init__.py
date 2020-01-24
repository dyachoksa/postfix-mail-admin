import flask

from .aliases import aliases_blueprint
from .auth import auth_blueprint
from .dashboard import dashboard
from .domains import domains_blueprint
from .mailboxes import mailboxes_blueprint
from .users import users_blueprint


def register_blueprints(app: flask.Flask):
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(domains_blueprint, url_prefix="/domains")
    app.register_blueprint(mailboxes_blueprint, url_prefix="/mailboxes")
    app.register_blueprint(aliases_blueprint, url_prefix="/aliases")
    app.register_blueprint(users_blueprint, url_prefix="/users")
    app.register_blueprint(dashboard)
