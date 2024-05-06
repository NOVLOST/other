"""ВАРИАНТ 7.Формируется матрица F следующим образом: если в С количество нулевых элементов в нечетных столбцах в области 4 больше
, чем количество нулевых  элементов в четных столбцах в области 1, то поменять в В симметрично области 2 и 3 местами
, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
 После чего вычисляется выражение: ((F*A)– (K * AT) . Выводятся по мере формирования А, F и все матричные операции последовательно."""

import random
sumC4=0
sumC1=0
K=int(input("Введите К="))
N=int(input("Введите N="))
save=0
minus = 0
"""формируем матрици размеров N/2 с случайными значением от -10 до 10"""
D =  [[random.randint(-10,10 ) for j in range(N//2)] for i in range(N//2)]
E =  [[random.randint(-10,10 ) for j in range(N//2)] for i in range(N//2)]
C =  [[random.randint(-10,10 ) for j in range(N//2)] for i in range(N//2)]
B =  [[random.randint(-10,10 ) for j in range(N//2)] for i in range(N//2)]
G = [ [0]*((N//2)*2) for i in range((N//2)*2) ]
H = [ [0]*((N//2)*2) for i in range((N//2)*2) ]
A = [D[i] + E[i]  for i in range(N//2)] #создаем матрицу А добовляя в нее по элементно матрицы D E C B
A += [C[i] + B[i] for i in range(N//2)]
print("матрица A\n",A,"\n\n")


"""если в С количество нулевых элементов в нечетных столбцах в области 4 больше
, чем количество нулевых  элементов в четных столбцах в области 1, то поменять в В симметрично области 2 и 3 местами"""
for i in range(0,N//2,2): # ищем в С количество нулевых элементов в нечетных столбцах в области 4
    for j in range(0,N//2):

        if j < i and j < ((N//2) - 1) - i and C[j][i]==0:
            sumC4 += 1



for i in range(1,N//2,2):# ищем количество нулевых  элементов в четных столбцах в области 1
    for j in range(0,N//2):

        if j < i and j > ((N//2) - 1) - i and C[j][i]==0:
            sumC1 += 1

if sumC4 > sumC1 : # меняем  в В симметрично области 2 и 3 местами

    for i in range((N//2) - 1, N // 4, -1):
        minus = 0
        for j in range(0, N // 2):

            if i > j and i > (N//2) - 1 - j:
                minus += 1
                save = C[i][j]
                C[i][j] = C[i-minus][j-minus]
                C[i - minus][j - minus] = save


    F = [D[i] + E[i]  for i in range(N//2)]
    F += [C[i] + B[i] for i in range(N//2)]

else:
    F = [D[i] + C[i]  for i in range(N//2)]
    F += [E[i] + B[i] for i in range(N//2)]

print(f'\nМатрица F {F}')

for g in range(len(A)):
    for i in range(len(F[0])):
        for k in range(len(F)):G[g][i] += F[g][k] * A[k][i]
print(f'\nF*A  {G}\n')
for g in range(len(A)):
    for i in range(len(A[0])):H[i][g]=A[g][i] * K
print(f'\nAT * K {H}\n',)
for g in range(len(A)):
    for i in range(len(A[0])): G[g][i]=G[g][i]-H[g][i]
print("Конечный результат\n",G,"\n")
