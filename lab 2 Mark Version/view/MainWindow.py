import re
from tkinter import *
import os
from PIL import Image, ImageTk
from tkinter import ttk
import config
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from controller.ReportController import ReportController
from model.Report import Report
from controller.AuthController import AuthController


def create_report_window():
    win = Toplevel()
    curr_time = 0
    curr_date = "22.04.2023"
    win.window_width = 250
    win.window_height = 200
    controller = ReportController()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (win.window_width / 2))
    y_cordinate = int((screen_height / 2) - (win.window_height / 2))

    win.geometry(f"{win.window_width}x{win.window_height}+{x_cordinate}+{y_cordinate}")
    num_label = ttk.Label(win, text="Номер отчета")
    num_in = ttk.Entry(win)
    values = ["Источники трафика", "Установить время посещения", "Выбрать страницу"]
    metrics = ttk.Combobox(win, values=values, state='readonly')
    label = ttk.Label(win, text="Выберите тип метрики")
    btn = ttk.Button(win, text="Добавить")

    num_label.pack(anchor = NW, padx =5, pady=5)
    num_in.pack(anchor = NW, padx =5, pady=5)
    label.pack(anchor=NW, padx=5, pady=5)
    metrics.pack(anchor=NW, padx=5, pady=5)
    btn.pack(anchor=CENTER, padx=5, pady=5)


def update_report_history():
    pass

def create_metrics_window():
    win = Toplevel()
    win.window_width = 250
    win.window_height = 170

    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (win.window_width / 2))
    y_cordinate = int((screen_height / 2) - (win.window_height / 2))

    win.geometry(f"{win.window_width}x{win.window_height}+{x_cordinate}+{y_cordinate}")


    values = ["Источники трафика", "Установить время посещения", "Выбрать страницу"]
    metrics = ttk.Combobox(win,values=values, state = 'readonly')
    label = ttk.Label(win, text="Выберите тип метрики")
    btn = ttk.Button(win, text="Применить", command= process_metrics(metrics.get())) #todo: сюда команду

    label.pack(anchor = NW, padx=5,pady=5)
    metrics.pack(anchor = NW, padx=5,pady=5)
    btn.pack(anchor = CENTER, padx=5,pady=5)

def process_metrics(metrics: str):
    pass



class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        ttk.Style().configure(".", font="helvetica 13", foreground="#004D40", padding=8)
        self.title("My program")
        self.window_width = SCREEN_WIDTH
        self.window_height = SCREEN_HEIGHT

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (self.window_width / 2))
        y_cordinate = int((screen_height / 2) - (self.window_height / 2))

        self.geometry(f"{self.window_width}x{self.window_height}+{x_cordinate}+{y_cordinate}")

        image_path = os.path.join("E:\\BSUIR\\sem5\\omis\\lab 2 Mark Version\\assets", "background1.jpg")
        self.background_image = Image.open(image_path)
        self.background_image = self.background_image.resize((self.window_width, self.window_height))
        self.background_image_tk = ImageTk.PhotoImage(self.background_image)
        self.background_label = Label(self, image=self.background_image_tk)
        self.background_label.image = self.background_image_tk  # Keep a reference to avoid garbage collection
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        report_button = ttk.Button(self.frame, text="Создать отчет", command=create_report_window)
        history_button = ttk.Button(self.frame, text="История отчетов", command= update_report_history)
        metrics_button = ttk.Button(self.frame, text="Информация о метрике", command=create_metrics_window)

        filters = ["По временным меткам"]
        filter_label = ttk.Label(self.frame, text="Выберите фильтр") #todo: сделать дефолт
        filter = ttk.Combobox(self.frame, values = filters, state = 'readonly')
        filter.bind("<<ComboboxSelected>>", print("filter applied"))
        filter_label.pack(anchor = NE, padx=5,pady=5)
        filter.pack(side = "right", padx=5,pady=5)
        report_button.pack(side="left", padx=5, pady=5)
        history_button.pack(side="left", padx=5, pady=5)
        metrics_button.pack(side="left", padx=5, pady=5)
        self.frame.pack(anchor=NW, fill=X, padx=5, pady=5)

        columns = ("id", "date", "type")
        tree = ttk.Treeview(columns=columns, show = "headings")
        tree.pack(fill=BOTH, expand=1)
        tree.heading("id", text = "Номер")
        tree.heading("date", text="Дата создания")
        tree.heading("type", text="Тип метрики")
        self.resizable(0, 0)