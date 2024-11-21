import re
from tkinter import *
from tkinter import ttk
from controller.AuthController import AuthController
import config
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class RegistrationForm(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.controller = AuthController()
        self.parent = parent
        self.name_entry = None
        self.password_entry = None
        self.birthdate_entry = None

        frame = ttk.Frame(self, borderwidth=0, padding=[8, 10])
        form_name = ttk.Label(frame, text="Регистрация", font=("Arial", 14, "bold"))
        form_name.pack(anchor=NW)
        name_label = ttk.Label(frame, text="Введите логин")
        name_label.pack(anchor=NW)
        self.name_entry = ttk.Entry(frame)
        self.name_entry.pack(anchor=NW)

        password_label = ttk.Label(frame, text="Введите пароль")
        password_label.pack(anchor=NW)
        self.password_entry = ttk.Entry(frame, show="*")
        self.password_entry.pack(anchor=NW)

        birthdate_label = ttk.Label(frame, text="Введите дату рождения")
        birthdate_label.pack(anchor=NW)
        self.birthdate_entry = ttk.Entry(frame)
        self.birthdate_entry.pack(anchor=NW)

        log_button = ttk.Button(
            frame,
            text="Регистрация",
            command=lambda: parent.navigate_to_main()
        )
        log_button.pack(anchor="center", pady=(30, 30))

        log_label = ttk.Label(frame, text="Уже есть аккаунт?", foreground="blue", cursor="hand2")
        log_label.pack(anchor=NW)
        log_label.bind("<1>", lambda e: parent.show_login_form())

        frame.pack(anchor=CENTER, padx=5, pady=5)

    def register_user(self):
        name = self.name_entry.get()
        password = self.password_entry.get()
        birthdate = self.birthdate_entry.get()
        if self.controller.registration(name, password, birthdate):
            self.parent.navigate_to_main()
        else:
            print("Registration failed")