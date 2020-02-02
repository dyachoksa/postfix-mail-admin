from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from flask_sqlalchemy import Pagination

from ..forms import MailboxForm, MailboxUpdateForm
from ..services import db
from ..models import Mailbox

mailboxes_blueprint = Blueprint("mailboxes", __name__)


@mailboxes_blueprint.route("/", endpoint="index")
@login_required
def index():
    pager: Pagination = Mailbox.query.paginate(per_page=25, max_per_page=50)
    return render_template("mailboxes/index.html", pager=pager)


@mailboxes_blueprint.route(
    "/create", endpoint="create", methods=["GET", "POST"]
)
@login_required
def create():
    form = MailboxForm()

    if form.validate_on_submit():
        mailbox = Mailbox()
        form.populate_obj(mailbox)
        mailbox.set_password(form.data["password"])

        db.session.add(mailbox)
        db.session.commit()

        flash(
            f"Mailbox {mailbox.email} has been successfully created", "success"
        )
        return redirect(url_for(".index"))

    return render_template("mailboxes/create.html", form=form)


@mailboxes_blueprint.route(
    "/<int:mailbox_id>/edit", endpoint="edit", methods=["GET", "POST"]
)
@login_required
def edit(mailbox_id):
    mailbox = Mailbox.query.get_or_404(mailbox_id)
    form = MailboxUpdateForm(obj=mailbox)

    if form.validate_on_submit():
        mailbox.name = form.data["name"]
        mailbox.domain = form.data["domain"]
        mailbox.is_active = form.data["is_active"]
        if len(form.data["password"]) > 0:
            mailbox.set_password(form.data["password"])

        db.session.add(mailbox)
        db.session.commit()

        flash(
            f"Mailbox {mailbox.email} has been successfully updated", "success"
        )
        return redirect(url_for(".index"))

    return render_template("mailboxes/edit.html", mailbox=mailbox, form=form)


@mailboxes_blueprint.route("/<int:mailbox_id>/delete", endpoint="delete")
@login_required
def remove(mailbox_id):
    mailbox = Mailbox.query.get_or_404(mailbox_id)
    mailbox_name = mailbox.email

    db.session.delete(mailbox)
    db.session.commit()

    flash(f"Mailbox {mailbox_name} has been successfully deleted", "success")
    return redirect(url_for(".index"))
