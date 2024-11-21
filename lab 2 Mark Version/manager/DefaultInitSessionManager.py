from model.Session import Session
from model.User import User

class DefaultInitSessionManager:
    def __init__(self):
        pass

    def process_init_session(self, user: User, session: Session) -> None:
        pass