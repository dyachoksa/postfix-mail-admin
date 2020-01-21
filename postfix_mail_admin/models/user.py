from ..services import db

from .base import BaseModel


class User(BaseModel):
    """Internal user account to access admin panel"""

    __tablename__ = "users"

    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"

    def __str__(self):
        return self.email
