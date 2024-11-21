from model.User import User

class DefaultAuthHandler:
    def __init__(self):
        pass

    def handle_login(self, login: str, user: User) -> bool:
        pass

    def handle_login(self, login: str) -> bool:
        pass

    def handle_password(self, password: str, user: User) -> bool:
        pass

    def handle_password(self, password: str) -> bool:
        pass
