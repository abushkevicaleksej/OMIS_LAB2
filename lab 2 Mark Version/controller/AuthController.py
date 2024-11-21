from model.Admin import Admin
import datetime


class AuthController:
    def __init__(self):
        self.admin = []

    def add_admin(self, new_admin: Admin):
        self.admin.append(new_admin)

    def get_admin(self):
        if self.admin:
            return self.admin[0]
        else:
            return None

    def auth(self, login, password):
        for admin in self.admin:
            if admin.get_login() == login and admin.get_password() == password:
                print("Successfully auth nigga admin")
                return admin
        print("Unlucky")
        return None

    def registration(self, login: str, password: str, birthdate: datetime) -> bool:
        if any(admin.get_login() == login for admin in self.admin):
            print("Admin with this login already exists.")
            return False

        registered_admin = Admin(login, password, birthdate)
        self.add_admin(registered_admin)
        print("Successfully registered admin.")
        return True


