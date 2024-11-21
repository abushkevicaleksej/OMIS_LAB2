from controller.AuthController import AuthController
from controller.SessionController import SessionController
from controller.HistoryController import HistoryController
from controller.ReportController import ReportController


class MainController:
    def __init__(self):
        self.__auth_controller = AuthController
        self.__session_controller = SessionController
        self.__history_controller = HistoryController
        self.__report_controller = ReportController
