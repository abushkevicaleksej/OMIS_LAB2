import datetime
from model.DefaultSession import DefaultSession


class SessionController:
    def __init__(self):
        self.sessions = []

    def start_session(self, user, page: str):
        new_session = DefaultSession(
            init_session=datetime.datetime.now(),
            end_session=None,
            user=user,
            page=page
        )
        self.sessions.append(new_session)
        print(f"Session started for user: {user.get_login()} on page: {page}")
        return new_session

    def end_session(self, session: DefaultSession):
        session_index = self.sessions.index(session) if session in self.sessions else -1
        if session_index != -1:
            self.sessions[session_index].get_end_session = datetime.datetime.now()
            print(f"Session ended for user: {session.get_user().get_login()}")
            return True
        print("Session not found.")
        return False

    def get_active_sessions(self):
        return [session for session in self.sessions if session.get_end_session() is None]

    def get_sessions_by_user(self, user):
        return [session for session in self.sessions if session.get_user() == user]

    def display_session_details(self, session: DefaultSession):
        if session:
            print(f"Session Details:")
            print(f"  User: {session.get_user().get_login()}")
            print(f"  Page: {session.get_page()}")
            print(f"  Start Time: {session.get_init_session()}")
            print(f"  End Time: {session.get_end_session()}")
        else:
            print("Session not found.")

    def list_all_sessions(self):
        return self.sessions

    def filter_sessions_by_page(self, page: str):
        return [session for session in self.sessions if session.get_page() == page]
