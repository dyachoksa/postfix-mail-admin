from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from flask_sqlalchemy import Pagination

from ..forms import AliasForm
from ..services import db
from ..models import Alias

aliases_blueprint = Blueprint("aliases", __name__)


@aliases_blueprint.route("/", endpoint="index")
@login_required
def index():
    pager: Pagination = Alias.query.paginate(per_page=25, max_per_page=50)
    return render_template("aliases/index.html", pager=pager)


@aliases_blueprint.route("/create", endpoint="create", methods=["GET", "POST"])
@login_required
def create():
    form = AliasForm()

    if form.validate_on_submit():
        alias = Alias()
        form.populate_obj(alias)

        db.session.add(alias)
        db.session.commit()

        flash(f"Alias {alias} has been successfully created", "success")
        return redirect(url_for(".index"))

    return render_template("aliases/create.html", form=form)


@aliases_blueprint.route(
    "/<int:alias_id>/edit", endpoint="edit", methods=["GET", "POST"]
)
@login_required
def edit(alias_id):
    alias = Alias.query.get_or_404(alias_id)
    form = AliasForm(obj=alias)

    if form.validate_on_submit():
        form.populate_obj(alias)

        db.session.add(alias)
        db.session.commit()

        flash(f"Alias {alias} has been successfully updated", "success")
        return redirect(url_for(".index"))

    return render_template("aliases/edit.html", alias=alias, form=form)


@aliases_blueprint.route("/<int:alias_id>/delete", endpoint="delete")
@login_required
def remove(alias_id):
    alias = Alias.query.get_or_404(alias_id)

    db.session.delete(alias)
    db.session.commit()

    flash(f"Alias {alias} has been successfully deleted", "success")
    return redirect(url_for(".index"))
