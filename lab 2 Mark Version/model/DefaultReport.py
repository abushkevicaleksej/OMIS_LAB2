import datetime
from model.Metrics import Metrics
from model.Admin import Admin
from controller.AuthController import AuthController

class DefaultReport:
    def __init__(self, metrics: [Metrics], admin: Admin, time, date: datetime, num: int):
        self.__metrics = metrics
        self.__admin = Admin
        self.__time_of_creating = time
        self.__date_of_creating = date
        self.__number = num

    def get_metrics(self):
        return self.__metrics

    def set_admin(self, new_admin: Admin):
        self.__admin = new_admin

    def get_admin(self):
        return self.__admin

    def get_num_of_report(self):
        return self.__number

    def get_creating_time(self):
        return self.__time_of_creating

    def get_creating_date(self):
        return self.__date_of_creating



