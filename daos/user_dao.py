from models.user import User


class UserDAO:

    @classmethod
    def get_user(cls) -> None:

        user_doc = {"name": "許鐸鐙", "age": 26}

        user = User.from_dict(user_doc)

        return user.to_dict()
