import Page


class Website:
    def __init__(self, url: str, pages: [Page]):
        self.__url = url
        self.__pages = pages

    def get_website_url(self):
        return self.__url

    def get_page(self, index):
        return self.__pages[index]

    def get_num_of_page(self):
        return len(self.__pages)
