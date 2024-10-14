import tkinter

from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import csv

#NOTE: сделать вывод таблицы по кол-ву целей
#подумать как организовать данные в csv файле и как их обработать.


class Window(): # окно на котом все рисуется
    def __init__(self):


        self.root = Tk()
        self.height = self.root.winfo_screenheight()
        self.width = self.root.winfo_screenwidth()
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False, False)
        self.root.title("NAVY")

        self.root.config(bg='#007241')


    def loop(self):
        self.root.mainloop()


def resize_canvas():
    global img , new_img, img_resize




    img = Image.open('table1.png')
    img_resize = img.resize((win.width//2,win.width//2))
    new_img = ImageTk.PhotoImage(img_resize)

    canvas.create_image(0, 0, anchor='nw', image=new_img)





    canvas.place(x=0, y=0)
class Table():

    def __init__(self):
        self.table_list = []
        self.coor_y_table = (win.height * 0.1, win.height * 0.2, win.height * 0.3)
        self.headrs = ('Время', 'Курс', 'Скорость', 'Дистанция')
        self.coordinate_list = []

    def table_init(self):



        number_target = 1

        for coord in self.coor_y_table:
            table = ttk.Treeview(height=3, show="headings", columns=self.headrs)  # таблица с заказами
            self.table_list.append(table)
            table.column("#1", stretch=NO, width=70)
            table.column("#2", stretch=NO, width=70)
            table.column("#3", stretch=NO, width=70)
            table.column("#4", stretch=NO, width=80)

            self.table_list[-1].place(x=win.width // 2 + 20, y=coord)

            welcome = Label( text=f'ЦЕЛЬ №{number_target}', fg="#003b21",
                            bg='#00AF64', relief=FLAT, bd='1')


            welcome.place(x = win.width//2+20 , y = coord - 25 )


            number_target += 1


        for tab in self.table_list:
            for head in self.headrs:
                tab.heading(head, text=head, anchor='center')

    def read_cvs(self,file_name):

        with open(file_name, 'r') as file:
            self.coordinate_list = file.readline()
            print(self.table_list)




win = Window()
target_table = Table()
canvas = tkinter.Canvas(win.root, height=win.height , width=win.width, bg ="white" )#отрисовка фона

target_table.read_cvs("PELING.csv")


resize_canvas()

target_table.table_init()

win.loop()
