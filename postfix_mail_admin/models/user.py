from passlib.hash import bcrypt

from .base import BaseModel
from ..services import db


class User(BaseModel):
    """Internal user account to access admin panel"""

    __tablename__ = "users"

    email = db.Column(
        db.String(150), unique=True, nullable=False, info={"label": "Email"}
    )
    password = db.Column(
        db.String(150), nullable=False, info={"label": "Password"},
    )

    def __repr__(self):
        return f"<User {self.email}>"

    def __str__(self):
        return self.email

    def __hash__(self):
        return hash((self.id, self.email,))

    def set_password(self, value):
        self.password = bcrypt.hash(value)
