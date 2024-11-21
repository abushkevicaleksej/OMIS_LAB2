class Page:
    def __init__(self, id: int, url: str):
        self.__id = id
        self.__url = url

    def get_id(self):
        return self.__id

    def get_page_url(self):
        return self.__url
