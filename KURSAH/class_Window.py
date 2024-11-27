import tkinter

from tkinter import *
from class_Table import *

from tkinter import ttk


class Window():  # окно на котом все рисуется
    def __init__(self):
        self.root = Tk()
        # размеры окна
        self.height = self.root.winfo_screenheight()
        self.width = self.root.winfo_screenwidth()
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False, False)  # возможность изменять размер окна
        self.root.title("NAVY")  # название программы
        self.canvas = tkinter.Canvas(self.root, height=self.height, width=self.width // 2, bg="white")  # радар
        self.circle_scale = 10  # масшаб кружков
        self.distance_scale = 1  # масштаб цели
        self.root.config(bg='#007241')  # цвет фона
        self.label_mayak = Label(self.root, text='Маяк', fg="black", bg='white',
                                 height=2)

        self.label_scale = Label(self.root, text=f'{self.distance_scale}', fg="black", bg='#007241',
                                 height=2)

        self.label_target_name = Label(self.root, text='', fg="black", bg='white',
                                       height=2)

        self.flag_show_name = BooleanVar()

    def loop(self):
        self.root.mainloop()

    def get_height(self):  # get высоты
        return self.height

    def get_width(self):  # get ширины
        return self.width

    # отрисовка радара
    def draw_canvas(self, xo, yo, xm, ym, xt, yt, target_index):
        self.canvas.delete()
        self.label_scale.place_forget()

        # наша координаты берется за ноль и от нее выставляются точки остальных объектов

        dot_xm = (int(xm) - int(xo)) * self.distance_scale  # коорды маяка
        dot_ym = (int(ym) - int(yo)) * self.distance_scale

        dot_xt = (int(xt) - int(xo)) * self.distance_scale  # коорды цели
        dot_yt = (int(yt) - int(yo)) * self.distance_scale

        # мы находимся в центре
        self.canvas.create_oval(self.width // 4, self.width // 4, (self.width // 4) + self.circle_scale,
                                (self.width // 4) + self.circle_scale, fill="black", outline="#004D40")

        # рисуем маяк
        self.canvas.create_oval(((self.width // 4) + dot_xm), ((self.width // 4) - dot_ym),
                                (((self.width // 4) + self.circle_scale) + dot_xm),
                                (((self.width // 4) + self.circle_scale) - dot_ym),
                                fill="green", outline="#004D40")

        # рисуем цель
        self.canvas.create_oval(((self.width // 4) + dot_xt), ((self.width // 4) - dot_yt),
                                (((self.width // 4) + self.circle_scale) + dot_xt),
                                (((self.width // 4) + self.circle_scale) - dot_yt),
                                fill="red", outline="#004D40")

        self.label_scale = Label(self.root, text=f'{self.distance_scale}', fg="black", bg='#007241',
                                 height=2)

        if self.flag_show_name.get() == True:
            self.canvas.create_text(((self.width // 4) + dot_xm, ((self.width // 4) - dot_ym) + 15), text="Маяк",
                                    fill="#004D40")
            self.canvas.create_text(((self.width // 4) + dot_xt, ((self.width // 4) - dot_yt) + 25),
                                    text=f'цель {target_index}', fill="#004D40")

        self.label_scale.place(x=win.get_width() - (win.get_width() // 3) + 240,
                               y=win.get_height() // 2 + (win.get_height() // 3) - 50)

    # инициализация радара
    def init_canvas(self):
        self.canvas.place(x=0, y=0)


win = Window()
