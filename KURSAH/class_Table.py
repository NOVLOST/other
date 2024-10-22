

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

                        data_tuple = calculation()
                        table.tree.insert("", END, values=(coordinate_list[0], coordinate_list[1],
                                                           coordinate_list[2], coordinate_list[3],
                                                        data_tuple[0],data_tuple[1], data_tuple[2]))

                        table_list.append(table)

                        table_list[-1].tree.place(x=win.width // 2 + 20, y=win.height * coordinate_multiplier)

                        coordinate_multiplier += 0.1

                    else:

                        for tab in table_list:
                            if tab.target_index == coordinate_list[-1]:
                                data_tuple = calculation()
                                tab.tree.insert("", END, values=(coordinate_list[0], coordinate_list[1]
                                                                 ,coordinate_list[2],coordinate_list[3],
                                                                 data_tuple[0],data_tuple[1],data_tuple[2]))
                                print(calculation())





def calculation():
        xo = int(coordinate_list[1])
        yo = int(coordinate_list[2])

        xm = int(coordinate_list[4])
        ym = int(coordinate_list[5])

        leg_a = max(xo,xm) - min(xo,xm)
        leg_b = max(yo, ym) - min(yo, ym)
        print("-------------------\n\n\n",leg_a,leg_b)

        hypotenuse = ((leg_a**2) + (leg_b**2))**0.5
        print(f'hyp = {hypotenuse}')

        sin_b = (leg_a / hypotenuse)

        rigTri_angle_mayak_in_degrees = math.degrees(math.asin(sin_b))

        print("right angle = ",rigTri_angle_mayak_in_degrees)

        mayak_peling = int(coordinate_list[6])
        print("mayak peling  = ",mayak_peling)

        interior_angel_mayak = 180 -  (mayak_peling + rigTri_angle_mayak_in_degrees)

        print("need angel = ",interior_angel_mayak)

        sin_a = (leg_b / hypotenuse)

        print(f"------------------\n\nsin_a = {sin_a}")

        rigTri_angle_me_in_degrees = math.degrees(math.asin(sin_a))

        print(f"rightangle_me = {rigTri_angle_me_in_degrees}")

        me_peling = int(coordinate_list[3])

        print(f'me peling  = {me_peling}')

        interior_angel_me = (90 -  rigTri_angle_me_in_degrees) + me_peling

        print(f'need me angle = {interior_angel_me}')

        print(f'sin me = {math.sin(math.radians(interior_angel_me))}')

        distance_to_target = (hypotenuse * math.sin(math.radians(interior_angel_me))) / math.sin(math.radians(interior_angel_mayak))

        print("distance = ",distance_to_target)

        y_target_coordinate = (distance_to_target * math.sin(math.radians(90 - me_peling)))
        x_target_coordinate = (distance_to_target * math.cos(math.radians(90 - me_peling))) + xo

        print("coordinate finally = ",x_target_coordinate,y_target_coordinate)

        return (round(distance_to_target,2),round(x_target_coordinate,2),round(y_target_coordinate,2))


