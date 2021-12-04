from daos.user_dao import UserDAO


class UserService:

    @classmethod
    def get_user(cls):
        user = UserDAO.get_user()

        return user
