from ..services import db
from .base import BaseModel


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
    )
    name = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Mailbox {self.name}>"
