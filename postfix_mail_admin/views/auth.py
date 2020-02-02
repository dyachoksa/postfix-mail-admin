from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, logout_user, login_user
from passlib.hash import bcrypt

from ..forms import LoginForm
from ..models import User

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if (
            user is not None
            and user.is_active
            and bcrypt.verify(form.password.data, user.password)
        ):
            login_user(user)
            return redirect(url_for("dashboard.index"))

        flash("Wrong email or password", "warning")

    return render_template("login.html", form=form)


@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
