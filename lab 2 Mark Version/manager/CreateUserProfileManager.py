from model.User import User
from CreateProfileManager import CreateProfileManager


class CreateUserProfileManager(CreateProfileManager):
    def __init__(self, user:User):
        self.__user = user

    def create_profile(self):
        pass

    def save_profile(self):
        pass