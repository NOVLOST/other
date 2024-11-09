

import math


from class_Window import *


coordinate_list = [] #данные из файла
table_list = [] #таблицы с целями
index_of_targets = []# индексы целей
headrs = ('Время','Xo', 'Yo', 'Пелинг','Дистанция','X','Y')#заголовки
page = 0 #страницы с таблицами целей
time_list = [] # в нем хранится время в которое были запеленгованы цели
time_selected = [] #выбранное время для передачи на отрисовку целей с таким же временем
label_index_of_target = Label(win.root, text='', fg="black", bg='#007241',
                                      height=2)
case_for_label_index_of_target = []

class Table():

    def __init__(self,i):
        self.target_index = i#индекс цели
    #создание таблицы
    def table_init(self,header,height):
        self.tree = ttk.Treeview(height=height, show="headings",selectmode="extended", columns=header)


        for head in header:#текст заголовков
            self.tree.heading(head, text=head, anchor='center')

        for i in range(1, len(header) + 1):#размеры столбцов
            if i == 5:
                self.tree.column(f"#{i}", stretch=NO, width=80)
            else:
                self.tree.column(f"#{i}", stretch=NO, width=70)

time_tab = Table(0) # таблица для времени
time_tab.table_init('T',15)#инициализируем ее

#чтение файла
#СТРУКТУРА ФАЙЛА:время,х мои ,у мои ,пелинг от меня,х маяка,у маяка,пелинг от маяка,индекс цели.
#ПЕЛИНГ ОТСЧИТЫВАЕМ ОТ 12 ЧАСОВ ПО ЧАСОВОЙ СТРЕЛКЕ!!!
def read_cvs(file_name):
        global coordinate_list

        with open(file_name, 'r') as file:#чтение без записи

            while True:

                coordinate_list = file.readline()#читаем строку
                coordinate_list = coordinate_list.split(',')#разделение строки по запятым



                if len(coordinate_list)==1:#если файл кончился
                    break


                else:#если не кончился

                    if coordinate_list[-1] not in index_of_targets:#добавляем новую цель

                        index_of_targets.append(coordinate_list[-1])#закидываем ее индекс в список

                        table = Table(coordinate_list[-1])#создаем объект таблицы для цели
                        table.table_init(headrs,3)#инициализируем

                        data_tuple = calculation() #расчеты
                        #вставка данных  в таблицу(полследние два не отображаются но храняться это координаты маяка)
                        #первое это время ,вторые два это наши коорды ,затем пелинг от нас ,дистанция,коорды цели
                        table.tree.insert("", END, values=(coordinate_list[0], coordinate_list[1],
                                                           coordinate_list[2], coordinate_list[3],
                                                        data_tuple[0],data_tuple[1], data_tuple[2],coordinate_list[4],coordinate_list[5]))

                        table_list.append(table)# добавляем объект таблицы в список




                    else:#если таблица существует

                        for tab in table_list:#перебираем таблицы
                            if tab.target_index == coordinate_list[-1]:#если строка из файла совпала с индексом таблицы/цели
                                data_tuple = calculation()#вычисления

                                # вставка данных  в таблицу(полследние два не отображаются но храняться это координаты маяка)
                                # первое это время ,вторые два это наши коорды ,затем пелинг от нас ,дистанция,коорды цели
                                tab.tree.insert("", END, values=(coordinate_list[0], coordinate_list[1]
                                                                 ,coordinate_list[2],coordinate_list[3],
                                                                 data_tuple[0],data_tuple[1],data_tuple[2],coordinate_list[4],coordinate_list[5]))

                    # заполнение таблицы времени
                    if coordinate_list[0] not in time_list:
                        time_list.append(coordinate_list[0])
                        time_tab.tree.insert("", END, values=(coordinate_list[0]))






def forward_draw_table():#страница вперед
    global page,label_index_of_target

    if ((page + 2) * 5 ) - len(table_list) < 4:
        page += 1


        coordinate_multiplier = 0.1  # пробел между таблицами

        for i in case_for_label_index_of_target:
            i.place_forget()

        case_for_label_index_of_target.clear()

        for i in range((page-1) * 5, (page ) * 5):
            try:
                table_list[i].tree.place_forget()


            except:
                break

        for i in range(page * 5,(page * 5) + 5):
        # рисуем ее на экране
            try:
                label_index_of_target = Label(win.root, text=f'цель №{table_list[i].target_index}', fg="black",
                                              bg='#007241',
                                              height=2)
                case_for_label_index_of_target.append(label_index_of_target)
                label_index_of_target.place(x=win.width // 2 + 20, y=win.height * coordinate_multiplier - 100)
                table_list[i].tree.place(x=win.width // 2 + 20, y=win.height * coordinate_multiplier - 60)
                coordinate_multiplier += 0.12
            except:
                break

        win.root.update()




def back_draw_table():#рисуем на экране
    global page,label_index_of_target
    if page - 1 >= 0:#проверяем умешаемся ли мы в размер списка

        page -= 1


    coordinate_multiplier = 0.1  # пробел между таблицами

    for i in case_for_label_index_of_target:
        i.place_forget()

    case_for_label_index_of_target.clear()

    for i in range((page+1) * 5,((page + 2) * 5)):
        try:
            table_list[i].tree.place_forget()

        except:
            break

    for i in range(page * 5, (page + 1) * 5):
        # рисуем ее на экране
        try:
            label_index_of_target = Label(win.root, text=f'цель №{table_list[i].target_index}', fg="black", bg='#007241',
                                              height=2)
            case_for_label_index_of_target.append(label_index_of_target)
            label_index_of_target.place(x=win.width // 2 + 20, y=win.height * coordinate_multiplier - 100)
            table_list[i].tree.place(x=win.width // 2 + 20, y=win.height * coordinate_multiplier - 60)

            coordinate_multiplier += 0.12
        except:

            break
    win.root.update()#обновляем экран





def select_time(event):#выбор времени и поиск соответствия в таблице

    time_selected.clear()
    win.canvas.delete('all') #удаляем прошлые объекты
    for i in time_tab.tree.selection():#дабавление в список выбранного времени

        value = time_tab.tree.item(i, option="values")
        time_selected.append(value)
        print(value)

    for time in time_selected:#поиск соответсвия времени в таблице
        for tab in table_list:

            id = tab.tree.get_children("")
            print(id)
            for i in id:

                tab_time = tab.tree.item(i,option = 'values'  )


                if time[0] == tab_time[0]:

                    xo = tab_time[1]#наши коорды
                    yo = tab_time[2]

                    xm = tab_time[-2]#коорды маяка
                    ym = tab_time[-1]

                    xt = round(float(tab_time[-4])) #коорды цели
                    yt = round(float(tab_time[-3]))

                    win.draw_canvas(xo,yo,xm,ym,xt,yt,tab.target_index)#рисуем объекты

def plus_change_scale():


        # без разницы на что ориентироваться в плане числа для определения границы.
    if win.distance_scale + 1 < 20 :

            win.circle_scale += 1
            win.distance_scale += 1
            select_time('e')


def minus_change_scale():

    if win.distance_scale - 1 > 0:

            win.circle_scale -= 1
            win.distance_scale -= 1
            select_time('e')

def call_select_time():

    select_time('e')


#---------------------------------------------------------------------------------------------------
#РАСЧЁТ:происходит по теореме синусов.Для того чтобы найти дистанцию до цели и ее местоположения
#необходимо знать синус двух углов и один катет треугольника.

#ДАНО: координаты маяка и нас,пелинг до цели относительно маяка и нас.

#1.Находим катет от нас до маяка по теореме пифагора (достраиваем прямоугольный треугольник,катеты получаем из разности
# координат маяка и нас например: катет A = xm - x0  )

#2.Далее находим угол маяка : Для этого нужно найти смежный угол в прямоугольном треугольнике находие его через акрсинус
#(закидываем в него синус угла).Теперь отнимает от 180 -(пелинг до цели) - (смежный угол)

#3.Наш синус в треугольнике расчитаваем так: 90 - (синус в прямоугольном треугольнике) + пелинг до цели

#4. теперь находим дистанцию до цели: (Катет * синус нас) / синус маяка.

#5. находим координаты цели : Зная катет и угол можно найти катеты прямоугльного треугольника.
#Для этого найдем угол : 90 - пелинг .Затем по формуле синуса находим катет: A = sin * гипотенуза(дистанция)анологичено
#работаем с cos и находим еще один катет теперь просто складываем их с нашими координатами.

def calculation():

        xo = int(coordinate_list[1])
        yo = int(coordinate_list[2])

        xm = int(coordinate_list[4])
        ym = int(coordinate_list[5])

        leg_a = max(xo,xm) - min(xo,xm)
        leg_b = max(yo, ym) - min(yo, ym)

        #1. наохдим гипотенузу
        hypotenuse = ((leg_a**2) + (leg_b**2))**0.5

        sin_b = (leg_a / hypotenuse)
        #находим смежный угол от маяка в прямоугольном треугольнике
        rigTri_angle_mayak_in_degrees = math.degrees(math.asin(sin_b))


        mayak_peling = int(coordinate_list[6])

        # 2.угол в тругольике относительно маяка
        interior_angel_mayak = 180 -  (mayak_peling + rigTri_angle_mayak_in_degrees)


        sin_a = (leg_b / hypotenuse)

        # 3.находим смежный угол от нас в прямоугольном треугольнике
        rigTri_angle_me_in_degrees = math.degrees(math.asin(sin_a))


        me_peling = int(coordinate_list[3])


        interior_angel_me = (90 -  rigTri_angle_me_in_degrees) + me_peling
        # угол в тругольике относительно нас

        # 4.динтация до цели
        distance_to_target = (hypotenuse * math.sin(math.radians(interior_angel_me))) / math.sin(math.radians(interior_angel_mayak))

        #5.координаты  цели
        y_target_coordinate = (distance_to_target * math.sin(math.radians(90 - me_peling)))
        x_target_coordinate = (distance_to_target * math.cos(math.radians(90 - me_peling)))


        return (round(distance_to_target,2),round(x_target_coordinate,2),round(y_target_coordinate,2))
