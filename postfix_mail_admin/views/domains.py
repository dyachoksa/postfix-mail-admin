from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required

from ..forms import DomainForm
from ..services import db
from ..models import Domain

domains_blueprint = Blueprint("domains", __name__)


@domains_blueprint.route("/", endpoint="index")
@login_required
def index():
    domains = Domain.query.all()
    return render_template("domains/index.html", domains=domains)


@domains_blueprint.route("/create", endpoint="create", methods=["GET", "POST"])
@login_required
def create():
    form = DomainForm()

    if form.validate_on_submit():
        domain = Domain()
        form.populate_obj(domain)

        db.session.add(domain)
        db.session.commit()

        flash(f"Domain {domain.fqdn} has been successfully created", "success")
        return redirect(url_for(".index"))

    return render_template("domains/create.html", form=form)


@domains_blueprint.route(
    "/<int:domain_id>/edit", endpoint="edit", methods=["GET", "POST"]
)
@login_required
def edit(domain_id):
    domain: Domain = Domain.query.get_or_404(domain_id)
    form = DomainForm(obj=domain)

    if form.validate_on_submit():
        form.populate_obj(domain)

        db.session.add(domain)
        db.session.commit()

        flash(f"Domain {domain.fqdn} has been successfully updated", "success")
        return redirect(url_for(".index"))

    return render_template("domains/edit.html", domain=domain, form=form)


@domains_blueprint.route("/<int:domain_id>/delete", endpoint="delete")
@login_required
def remove(domain_id):
    domain = Domain.query.get_or_404(domain_id)
    db.session.delete(domain)
    db.session.commit()

    flash(f"Domain {domain.fqdn} has been successfully deleted", "success")
    return redirect(url_for(".index"))
