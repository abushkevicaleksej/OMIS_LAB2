from DefaultInitSessionManager import DefaultInitSessionManager
from model.User import User
from model.Session import Session


class InitSessionManager(DefaultInitSessionManager):
    def process_init_session(self, user: User, session: Session) -> None:
        pass