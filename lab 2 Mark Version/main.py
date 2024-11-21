import os

os.environ['TCL_LIBRARY'] = r'C:\Users\user\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.path.normpath("E:\BSUIR\\sem5\\omis\lab 2 Mark Version\\assets\\space.jpg")

from controller.MainController import MainController
from view.AuthWindow import AuthWindow


if __name__ == "__main__":
    mc = MainController()
    view = AuthWindow()
    view.mainloop()
    view.bind('<q>', view.destroy())
