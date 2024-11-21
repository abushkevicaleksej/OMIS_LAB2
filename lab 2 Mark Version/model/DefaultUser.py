from User import User
import datetime


class DefaultUser(User):
    def __init__(self, login: str, password: str, birthdate: datetime, curr_page: str, history: [str]):
        self.__login = login
        self.__password = password
        self.__birthdate = birthdate
        self.__curr_page = curr_page
        self.__history = history

    def get_login(self):
        return self.__login

    def get_password(self):
        return self.__password

    def get_birthdate(self):
        return self.__birthdate

    def get_curr_page(self):
        return self.__curr_page