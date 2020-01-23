from flask_wtf import FlaskForm
from wtforms import validators, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms_alchemy import model_form_factory, QuerySelectField

from .services import db
from .models import Domain, Mailbox, Alias

BaseModelForm = model_form_factory(FlaskForm)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(cls):
        return db.session


class LoginForm(FlaskForm):
    email = EmailField(
        "Email",
        validators=[
            validators.Length(max=150),
            validators.Email(),
            validators.DataRequired(),
        ],
    )
    password = PasswordField("Password", validators=[validators.DataRequired()])


class DomainForm(ModelForm):
    class Meta:
        model = Domain
        only = ["fqdn", "is_active"]


class MailboxForm(ModelForm):
    class Meta:
        model = Mailbox
        only = ["name", "domain", "password", "is_active"]
        attr_errors = False

    domain = QuerySelectField(
        label="Domain", query_factory=lambda: Domain.query.all()
    )


class MailboxUpdateForm(MailboxForm):
    class Meta:
        validators = {"password": [validators.Optional()]}
        assign_required = False

    password = PasswordField("Password", validators=[validators.Optional()])


class AliasForm(ModelForm):
    class Meta:
        model = Alias
        only = ["domain", "source", "destination", "is_active"]
        attr_errors = False

    domain = QuerySelectField(
        label="Domain", query_factory=lambda: Domain.query.all()
    )
