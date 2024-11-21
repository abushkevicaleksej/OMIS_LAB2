from DefaultAuthHandler import DefaultAuthHandler
from model.User import User

class AuthHandler(DefaultAuthHandler):
    def handle_login(self, login: str, user: User) -> bool:
        pass

    def handle_password(self, password: str, user: User) -> bool:
        pass