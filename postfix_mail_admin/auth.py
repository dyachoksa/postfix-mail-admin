from .models import User


def load_user(user_id: str):
    return User.get(int(user_id))
