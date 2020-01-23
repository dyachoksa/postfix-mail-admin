from flask_wtf import FlaskForm
from wtforms import validators, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms_alchemy import model_form_factory

from .services import db
from .models import Domain


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
