from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from ..forms import UserUpdateForm
from ..services import db

users_blueprint = Blueprint("users", __name__)


@users_blueprint.route("/me", endpoint="profile")
@login_required
def profile():
    return render_template("users/profile.html", user=current_user)


@users_blueprint.route("/me/edit", endpoint="edit", methods=["GET", "POST"])
@login_required
def edit():
    user = current_user
    form = UserUpdateForm(obj=user)

    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()

        flash("User has been successfully updated", "success")
        return redirect(url_for(".profile"))

    return render_template("users/edit.html", user=user, form=form)
