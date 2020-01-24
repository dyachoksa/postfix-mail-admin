from sqlalchemy_utils import PasswordType

from ..services import db

from .base import BaseModel


class User(BaseModel):
    """Internal user account to access admin panel"""

    __tablename__ = "users"

    email = db.Column(
        db.String(150), unique=True, nullable=False, info={"label": "Email"}
    )
    password = db.Column(
        PasswordType(150, schemes=["bcrypt"]),
        nullable=False,
        info={"label": "Password"},
    )

    def __repr__(self):
        return f"<User {self.email}>"

    def __str__(self):
        return self.email

    def __hash__(self):
        return hash((self.id, self.email,))
