import datetime


class DefaultSession:
    def __init__(self, init_session: datetime, end_session: datetime,  page: str):
        self.__init_session = init_session
        self.__end_session = end_session
        self.__page = page

    def get_init_session(self):
        return self.__init_session

    def get_end_session(self):
        return self.__end_session

    def get_page(self):
        return self.__page

