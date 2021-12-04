from services.user_service import UserService


class UserController:

    @classmethod
    def get_user(cls):
        user = UserService.get_user()
        return user
