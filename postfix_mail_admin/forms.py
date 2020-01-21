from flask_wtf import FlaskForm
from wtforms import validators, PasswordField
from wtforms.fields.html5 import EmailField


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[validators.Length(max=150),
                                            validators.Email(),
                                            validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired()])
