import csv
from class_Window import *

coordinate_list = []
table_list = []
tree_list = []
class Table():

    def __init__(self):
        self.headrs = ('Курс', 'Дистанция', 'Скорость', 'Время')
        self.info = []


    def table_init(self):



        coordinate_multiplier= 0.1

        for data in table_list:
            tree = ttk.Treeview(height=3, show="headings", columns=self.headrs)  # таблица c данными целей

            tree.column("#1", stretch=NO, width=70)
            tree.column("#2", stretch=NO, width=80)
            tree.column("#3", stretch=NO, width=70)
            tree.column("#4", stretch=NO, width=70)

            tree.insert("", END, values=(data.info[0][0],data.info[0][1]))

            tree_list.append(tree)

            tree_list[-1].place(x=win.width // 2 + 20, y=win.height * coordinate_multiplier)


            coordinate_multiplier += 0.1






        for tab in tree_list:
            for head in self.headrs:
                tab.heading(head, text=head, anchor='center')

    def read_cvs(self,file_name):
        global coordinate_list
        with open(file_name, 'r') as file:
            coordinate_list = csv.reader(file)
            coordinate_list = list(coordinate_list)

        print(coordinate_list)

        for i in range(0,len(coordinate_list[0]),2):
            table = Table()
            table.info.append((coordinate_list[0][i],coordinate_list[0][i+1]))

            table_list.append(table)
        print(len(table_list))

target_table = Table()