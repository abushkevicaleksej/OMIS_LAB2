from model.Admin import Admin
from CreateProfileManager import CreateProfileManager

class CreateAdminProfileManager(CreateProfileManager):
    def __init__(self, admin: Admin):
        self.__admin = admin

    def create_profile(self):
        pass

    def save_profile(self):
        pass