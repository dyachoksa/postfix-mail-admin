import os

from flask import Flask, render_template

from .auth import load_user
from .cli import register_cli
from .services import db, migrate, login_manager
from .views import register_blueprints

try:
    # Dev dependencies
    from flask_debugtoolbar import DebugToolbarExtension
except ImportError:
    DebugToolbarExtension = None

env_name = os.environ.get("FLASK_ENV", "development")

app = Flask(__name__)
app.config.from_object(f"postfix_mail_admin.config.{env_name.title()}Config")

db.init_app(app)
migrate.init_app(app)
login_manager.init_app(app)

if app.debug:
    if DebugToolbarExtension is not None:
        debug_toolbar = DebugToolbarExtension()
        debug_toolbar.init_app(app)

login_manager.user_loader(load_user)

register_blueprints(app)
register_cli(app)
