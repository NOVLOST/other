import tkinter

from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk

class Window(): # окно на котом все рисуется
    def __init__(self):


        self.root = Tk()
        self.height = self.root.winfo_screenheight()
        self.width = self.root.winfo_screenwidth()
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False, False)
        self.root.title("NAVY")
        self.canvas = tkinter.Canvas(self.root, height=self.height, width=self.width, bg="white")  # отрисовка фона
        self.root.config(bg='#007241')


    def loop(self):
        self.root.mainloop()


    def get_height(self):
        return self.height


    def get_width(self):
        return self.width

    def resize_canvas(self):
        global img , new_img, img_resize



        img = Image.open('table1.png')
        img_resize = img.resize((self.width//2,self.width//2))
        new_img = ImageTk.PhotoImage(img_resize)

        self.canvas.create_image(0, 0, anchor='nw', image=new_img)





        self.canvas.place(x=0, y=0)



win = Window()
