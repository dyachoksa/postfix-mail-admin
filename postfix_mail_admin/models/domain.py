from ..services import db
from .base import BaseModel


class Domain(BaseModel):
    """The mail domain"""

    __tablename__ = "domains"

    fqdn = db.Column(
        db.String(150),
        unique=True,
        nullable=False,
        info={"label": "Domain name"},
    )

    mailboxes = db.relationship(
        "Mailbox", lazy=True, backref=db.backref("domain", lazy=False)
    )
    aliases = db.relationship(
        "Alias", lazy=True, backref=db.backref("domain", lazy=False)
    )

    def __str__(self):
        return self.fqdn

    def __repr__(self):
        return f"<Domain {self.fqdn}>"

    def __hash__(self):
        return hash((self.id, self.fqdn,))
