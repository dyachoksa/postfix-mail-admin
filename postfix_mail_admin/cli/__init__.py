import flask

from .users import users_cli


def register_cli(app: flask.Flask):
    app.cli.add_command(users_cli)
