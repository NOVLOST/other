"""
Задана рекуррентная функция. Область определения функции – натуральные числа.
 Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
  Определить границы применимости рекурсивного и итерационного подхода.
   Результаты сравнительного исследования времени вычисления представить в табличной и графической форме в виде отчета по лабораторной работе.
7.	F(1) = G(1) = 19; F(n) = (-1)n*((3*F(n–1) – 2*G(n–1)), G(n) = (n–1)! + 2*G(n–1), при n >=2"""



import math
import time
import matplotlib.pyplot as plt
import functools

"""n это переменная для значения n"""
n=-1
"""one это переменная для определения знака"""
one=-1
"""k это переменная для выбора режима работы"""
k=-1
timer=[]
timer_rec=[]
"""ans это переменная для ответа пользователя """
ans=1
"""шаг графика"""
step=-1

def rec_f(x):
    global fact
    global one
    if x == 1:
        return 19

    else:
        one *= -1
        return one*(((3*rec_f(x-1)) - (2*rec_g(x-1))))


def rec_g(x):
    global fact
    if x==1:

        return 19

    else:

        return factor(x-1)

"""обертка для кэша"""


"""факториал рекурсивный"""
def factor(n):

    global fact
    if n == 1:

        return 1


    fact[1] = fact[0] * n
    fact[0], fact[1] = fact[1], fact[-1]
    return  factor(n - 1)


"""факториал итерационный"""
def iter_factor(n,fact_iter):


    for i in range(n,n+1): #цикл идет только один раз используя прдеидущее значение

            fact_iter[1] = fact_iter[0] * i
            fact_iter[0],fact_iter[1]=fact_iter[1],fact_iter[-1]



    return fact_iter[1]


"""итерация"""
def it_f(n,fact_iter):
    global one
    global cata_g
    global cata_f

    if n == 1:
        return 19
    for i in range(n,n+1): #цикл идет только один раз используя предидущее значение функции
        one *= -1
        cata_g[1] = iter_factor(i-1,fact_iter)+(2 * cata_g[0])
        cata_f[-1] = (one *( (3 * cata_f[1])-( 2 * cata_g[1] ) ) )
        cata_f[0], cata_f[1] = cata_f[1], cata_f[2]
        cata_g[0], cata_g[1] = cata_g[1], cata_g[2]

    return cata_f[-1]

"""ввод числа n"""
while n < 1:
    print("Введите натуральное число от 1 ")
    n = int(input())
while step<1:
    step=int(input("Введите шаг графика от 1"))
graf = list(range(1, n + 1,step))


"""выбор режима работы программы 0-рекурсия 1-итерация 2-оба"""
while k != 0 and k != 1 and k != 2:
    print("Выберите режим работы 0-рекурсия 1-итерация 2-оба")
    k = int(input())

if (n >=  33 and (k == 0 or k == 2)) or (n >= 5000 and (k == 1 or k == 2)):
    print("работа программы может занять большое время ,вы хотите продолжить? \n 1=да 0=нет")
    ans = int(input())

    while ans != 1 and ans != 0:
        print("работа программы может занять большое время ,вы хотите продолжить? \n 1=да 0=нет")
        ans = int(input())


"""список для факториала """
fact_iter = [1] * (3)
fact = [1] * (3)
"""списки для итерации"""
cata_f = [2] * 3
cata_g = [2] * 3

if k == 0 and ans == 1:

    for i in graf:
        start = time.time()
        res = rec_f(i)
        end = time.time()
        timer.append(end-start)
        rec_times = end - start
        print(i,"№Результат рекурсии ",res,"\nВремя выполнения",end-start,"\n\n")
    """графики"""
    plt.plot(graf, timer, label='рекурсионная функция.')
    plt.legend(loc=2)
    plt.xlabel('Значение n')
    plt.ylabel('Время выполнения (c)')
    plt.show()
if k == 1 and ans == 1:
    for i in graf:
        start = time.time()
        result = it_f(i,fact_iter)
        end = time.time()
        timer.append(end - start)
        iter_times = end - start
        print(i,"№Результат итерации ",result,"\nВремя выполнения",end-start,"\n\n")
    """графики"""
    plt.plot(graf, timer, label='Итерационная функция.')
    plt.legend(loc=2)
    plt.xlabel('Значение n')
    plt.ylabel('Время выполнения (c)')
    plt.show()
if k == 2 and ans == 1:
    for i in graf:
        start = time.time()
        result = it_f(i,fact_iter)
        end = time.time()
        timer.append(end-start)
        start_rec = time.time()
        res = rec_f(i)
        end_rec = time.time()
        timer_rec.append(end_rec-start_rec)
        rec_times = end_rec-start_rec
        iter_times = end-start
        print("\n",i,"№результат рекурсии ", res,"---------результат итерации",result,"-----------время  РЕКУРСИИ ",end_rec-start_rec,"-------время  ИТЕРАЦИИ",end-start)
    """графики"""
    plt.plot(graf, timer, label='Итерационная функция.')
    plt.plot(graf, timer_rec, label='Рекусионная функция.')
    plt.legend(loc=2)
    plt.xlabel('Значение n')
    plt.ylabel('Время выполнения (c)')
    plt.show()
