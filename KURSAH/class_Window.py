import tkinter

from tkinter import *
from class_Table import *

from tkinter import ttk


class Window(): # окно на котом все рисуется
    def __init__(self):


        self.root = Tk()
        #размеры окна
        self.height = self.root.winfo_screenheight()
        self.width = self.root.winfo_screenwidth()
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False, False)#возможность изменять размер окна
        self.root.title("NAVY")#название программы
        self.canvas = tkinter.Canvas(self.root, height=self.height, width=self.width//2, bg="white")#радар

        self.root.config(bg='#007241')#цвет фона


    def loop(self):
        self.root.mainloop()


    def get_height(self):#get высоты
        return self.height


    def get_width(self):#get ширины
        return self.width


    #отрисовка радара
    def draw_canvas(self,xo,yo,xm,ym,xt,yt):
        self.canvas.delete()


        #наша координаты берется за ноль и от нее выставляются точки остальных объектов

        dot_xm = int(xm) - int(xo)# коорды маяка
        dot_ym = int(ym) - int(yo)

        dot_xt = int(xt) - int(xo) # коорды цели
        dot_yt = int(yt) - int(yo)


        #мы находимся в центре
        self.canvas.create_oval(self.width//4, self.width//4,(self.width//4)+5, (self.width//4)+5, fill="black", outline="#004D40")
        # рисуем маяк
        self.canvas.create_oval((self.width // 4)+dot_xm, (self.width // 4)-dot_ym, ((self.width // 4) + 5)+dot_xm, ((self.width // 4) + 5)-dot_ym,
        fill="green", outline="#004D40")
        #рисуем цель
        self.canvas.create_oval((self.width // 4) + dot_xt, (self.width // 4) - dot_yt,
                                ((self.width // 4) + 5) + dot_xt, ((self.width // 4) + 5) - dot_yt,
                                fill="red", outline="#004D40")

    #инициализация радара
    def init_canvas(self):
        self.canvas.place(x=0,y=0)



win = Window()