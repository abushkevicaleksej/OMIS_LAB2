import re
from tkinter import *
from tkinter import ttk
from controller.AuthController import AuthController
import config
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class LoginForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        frame = ttk.Frame(self, borderwidth=1, relief="solid", padding=[8, 10], width=300)
        frame.pack(fill="none", expand=True)

        form_name = ttk.Label(frame, text="Логин", font=("Arial", 14, "bold"))
        form_name.pack(anchor="center", pady=(0, 10))

        name_label = ttk.Label(frame, text="Введите логин:")
        name_label.pack(anchor="nw")
        name_entry = ttk.Entry(frame)
        name_entry.pack(anchor="nw", pady=(0, 10))

        password_label = ttk.Label(frame, text="Введите пароль:")
        password_label.pack(anchor="nw")
        password_entry = ttk.Entry(frame, show="*")
        password_entry.pack(anchor="nw", pady=(0, 10))

        log_button = ttk.Button(
            frame,
            text="Войти",
            command=lambda: parent.navigate_to_main()
        )
        log_button.pack(anchor="center", pady=(30, 30))

        reg_label = ttk.Label(frame, text="Нет аккаунта?", foreground="blue", cursor="hand2")
        reg_label.pack(anchor="nw")
        reg_label.bind("<1>", lambda e: parent.show_registration_form())

        self.place(relx=0.5, rely=0.5, anchor="center")
