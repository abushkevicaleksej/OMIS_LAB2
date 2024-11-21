import os.path
import re
from tkinter import *
from tkinter import ttk
import config
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from view.LoginForm import LoginForm
from view.RegistrationForm import RegistrationForm
from view.MainWindow import MainWindow
from controller.AuthController import AuthController
from PIL import Image, ImageTk


class AuthWindow(Tk):
    def __init__(self):
        super().__init__()
        self.controller = AuthController()

        ttk.Style().configure(".", font="helvetica 13", foreground="#004D40", padding=8)

        self.title("My program")
        self.window_width = SCREEN_WIDTH
        self.window_height = SCREEN_HEIGHT

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (self.window_width / 2))
        y_cordinate = int((screen_height / 2) - (self.window_height / 2))

        self.geometry(f"{self.window_width}x{self.window_height}+{x_cordinate}+{y_cordinate}")

        image_path = os.path.join("E:\\BSUIR\\sem5\\omis\\lab 2 Mark Version\\assets", "background.jpg")
        self.background_image = Image.open(image_path)
        self.background_image = self.background_image.resize((self.window_width, self.window_height))
        self.background_image_tk = ImageTk.PhotoImage(self.background_image)
        self.background_label = Label(self, image=self.background_image_tk)
        self.background_label.image = self.background_image_tk
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.login_form = LoginForm(self)
        self.login_form.place(anchor="center")
        self.registration_form = RegistrationForm(self)

        self.show_login_form()
        self.resizable(0, 0)

    def show_login_form(self):
        self.registration_form.pack_forget()
        self.login_form.pack(anchor=CENTER,padx=5, pady=100)

    def show_registration_form(self):
        self.login_form.pack_forget()
        self.registration_form.pack(anchor=CENTER,  padx=5, pady=100)

    def navigate_to_main(self):
        self.destroy()
        MainWindow().mainloop()