import datetime

import sqlalchemy as sa

from ..services import db


class BaseModel(db.Model):
    """Base model's class"""

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(
        db.Boolean, default=True, nullable=False, server_default=sa.true()
    )
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def __eq__(self, other):
        if isinstance(other, BaseModel):
            return self.get_id() == other.get_id()
        return NotImplemented

    def __ne__(self, other):
        equal = self.__eq__(other)
        if equal is NotImplemented:
            return NotImplemented
        return not equal

    def get_id(self):
        return str(self.id)
