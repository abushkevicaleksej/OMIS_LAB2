import datetime

class DefaultAdmin:
    def __init__(self, login: str, password: str, birthdate: datetime,
                 list_of_created_reports=""):
        self.__login = login
        self.__password = password
        self.__birthdate = birthdate
        self.__list_of_creating_reports = list_of_created_reports

    def get_login(self):
        return self.__login

    def get_password(self):
        return self.__password

