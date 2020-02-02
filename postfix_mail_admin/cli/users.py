import click
import sqlalchemy.exc
from flask.cli import AppGroup

from ..models import User
from ..services import db

users_cli = AppGroup(
    "users",
    short_help="Manage internal accounts",
    help="Manage internal account to access Postfix Mail admin panel",
)


@users_cli.command("create")
@click.argument("email")
@click.password_option()
def create_user(email: str, password: str):
    """Create a new user account to access admin panel"""
    try:
        user = User(email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        click.secho(f"User {email} has been successfully created", fg="green")
    except sqlalchemy.exc.IntegrityError:
        click.secho(f"User {email} already exists", err=True, fg="red")
    except sqlalchemy.exc.DatabaseError:
        click.secho(f"Database error", err=True, fg="red")
