from flask import Blueprint, render_template
from flask_login import login_required

from ..models import Domain, Mailbox, Alias

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/", endpoint="index")
@login_required
def index_page():
    domains_total = Domain.query.count()
    domains_active = Domain.query.filter(Domain.is_active == True).count()

    mailboxes_total = Mailbox.query.count()
    mailboxes_active = Mailbox.query.filter(Mailbox.is_active == True).count()

    aliases_total = Alias.query.count()
    aliases_active = Alias.query.filter(Alias.is_active == True).count()

    return render_template(
        "index.html",
        stats=[
            {
                "label": "Domains",
                "active": domains_active,
                "total": domains_total,
                "endpoint": "domains",
            },
            {
                "label": "Mailboxes",
                "active": mailboxes_active,
                "total": mailboxes_total,
                "endpoint": "mailboxes",
            },
            {
                "label": "Aliases",
                "active": aliases_active,
                "total": aliases_total,
                "endpoint": "aliases",
            },
        ],
    )
