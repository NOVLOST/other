
import csv
import math
from class_Window import *

coordinate_list = []
table_list = []
index_of_targets = []
coordinate_multiplier= 0.1
headrs = ('Время','Xo', 'Yo', 'Пелинг','Дистанция','X','Y')
class Table():

    def __init__(self,i):
        self.target_index = i

    def table_init(self):
        self.tree = ttk.Treeview(height=3, show="headings", columns=headrs)

        for head in headrs:
            self.tree.heading(head, text=head, anchor='center')

        for i in range(1, len(headrs) + 1):
            if i == 5:
                self.tree.column(f"#{i}", stretch=NO, width=80)
            else:
                self.tree.column(f"#{i}", stretch=NO, width=70)








def read_cvs(file_name):
        global coordinate_list,coordinate_multiplier

        with open(file_name, 'r') as file:

            while True:

                coordinate_list = file.readline()
                coordinate_list = coordinate_list.split(',')
                print(coordinate_list)


                if len(coordinate_list)==1:
                    break


                else:

                    if coordinate_list[-1] not in index_of_targets:

                        index_of_targets.append(coordinate_list[-1])

                        table = Table(coordinate_list[-1])
                        table.table_init()
                        table.tree.insert("", END, values=(coordinate_list[0], coordinate_list[1],coordinate_list[2],coordinate_list[3]))

                        table_list.append(table)

                        table_list[-1].tree.place(x=win.width // 2 + 20, y=win.height * coordinate_multiplier)

                        coordinate_multiplier += 0.1


                    else:

                        for tab in table_list:
                            if tab.target_index == coordinate_list[-1]:
                                tab.tree.insert("", END, values=(coordinate_list[0], coordinate_list[1],coordinate_list[2],coordinate_list[3]))


                        calculation()


def right_triangle(xo,yo,xm,ym):

        leg_a = max(xo,xm) - min(xo,xm)
        leg_b = max(yo, ym) - min(yo, ym)
        print(leg_a,leg_b)

        hypotenuse = ((leg_a**2) + (leg_b**2))**0.5
        print(f'hyp = {hypotenuse}')





def calculation():

        # xo,yo наша координата xm,ym координата маяка
        # sin_po пелинг отновительно нашего коробля sin_pm пелинг относительно маяка
        # side_a сторона треугольника от нас до цели ,side_b от нас до маяка,side_c от маяка до цели

        xo = int(coordinate_list[1])
        yo = int(coordinate_list[2])
        sin_po = math.sin(int(coordinate_list[3]))

        xm = int(coordinate_list[4])
        ym = int(coordinate_list[5])
        sin_pm = int(coordinate_list[6])


        right_triangle(xo,yo,xm,ym)






