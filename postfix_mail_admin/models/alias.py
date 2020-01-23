from ..services import db
from .base import BaseModel


class Alias(BaseModel):
    """Email forwarding alias"""

    __tablename__ = "aliases"

    domain_id = db.Column(
        db.Integer,
        db.ForeignKey("domains.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    source = db.Column(db.String(150), nullable=False, index=True)
    destination = db.Column(db.String(150), nullable=False)

    def __str__(self):
        return f"{self.source}->{self.destination}"

    def __repr__(self):
        return f"<Alias {self.source} {self.destination}>"

    def __hash__(self):
        return hash((self.id, self.source, self.destination,))
