
from class_Table import *
from class_Window import *


#отображение радара

#NOTE: у placeов странные коорды сделаны для того чтобы на разных разрешениях все выглядело ок

read_cvs("PELING.csv")#чтение файла




forward = ttk.Button(win.root,text = "Вперёд",state = tkinter.NORMAL,cursor="top_left_corner",width=6,command=forward_draw_table)#вперед
back = ttk.Button(win.root,text = "Назад",state = tkinter.NORMAL,cursor="top_left_corner",width=6,command=back_draw_table)#назад

win.init_canvas()#инициализация радара

forward.place(x = win.get_width() - (win.get_width() // 3 ) ,y = win.get_height() // 2 + (win.get_height() // 3) )
back.place(x = win.get_width() - (win.get_width() // 3 ) - 100,y =win.get_height() // 2 + (win.get_height() // 3) )
time_tab.tree.place(x = win.get_width() - (win.get_width() // 3 ) - 200,y =win.get_height() // 2 + (win.get_height() // 3)- 250)


win.root.bind('<<TreeviewSelect>>', select_time )# действия по нажатию на кнопку мыши.

win.loop()