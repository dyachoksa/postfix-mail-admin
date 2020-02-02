from passlib.hash import bcrypt

from .base import BaseModel
from ..services import db


class Mailbox(BaseModel):
    """A domain-related mailbox"""

    __tablename__ = "mailboxes"
    __table_args__ = (
        db.UniqueConstraint("domain_id", "name", name="ix_mailboxes_email"),
    )

    domain_id = db.Column(
        db.Integer,
        db.ForeignKey("domains.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        info={"label": "Domain"},
    )
    name = db.Column(db.String(150), nullable=False, info={"label": "Mailbox"})
    password = db.Column(
        db.String(150), nullable=False, info={"label": "Password"},
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Mailbox {self.name}>"

    def __hash__(self):
        return hash((self.id, self.name, self.domain_id))

    @property
    def email(self):
        return f"{self.name}@{self.domain.fqdn}" if self.domain_id else "<none>"

    def set_password(self, value):
        self.password = bcrypt.hash(value)
