"""Формируется матрица F следующим образом: если в С количество нулей в ячейках с четной суммой индексов в области 1
 больше, чем произведение чисел по периметру области 2, то поменять в С симметрично области 1 и 2 местами, иначе С и В поменять местами несимметрично.
 При этом матрица А не меняется.
 После чего вычисляется выражение: A T*(F+А)-K* F T .
 Выводятся по мере формирования А, F и все матричные операции последовательно."""


import random
zeroC = 0
multiC = 0
K = int(input("Введите К="))
N = int(input("Введите N="))
n = 1
wall = -1
save = 0
"""формируем матрици размеров N/2 с случайными значением от -10 до 10"""
D =  [[random.randint(-10,10 ) for j in range(N//2)] for i in range(N//2)]
E =  [[random.randint(-10,10 ) for j in range(N//2)] for i in range(N//2)]
C =  [[random.randint(0,0 ) for j in range(N//2)] for i in range(N//2)]
B =  [[random.randint(-10,10 ) for j in range(N//2)] for i in range(N//2)]
G = [ [0]*((N//2)*2) for i in range((N//2)*2) ]
H = [ [0]*((N//2)*2) for i in range((N//2)*2) ]
A = [D[i] + E[i]  for i in range(N//2)]
A += [C[i] + B[i] for i in range(N//2)]
print("матрица A\n",A,"\n\n")

for i in range((N//2)-1,(N//4)-1,-1): #количество нулей в ячейках с четной суммой индексов в области 1
    wall += 1
    for j in range(1+wall , (N//2)-wall-1):

        if  j < i and j > ((N//2) - 1) - i and C[j][i] == 0 and (j+i) % 2 == 0:
            zeroC += 1
wall = -1

print (f'\n\nколичество нулей области 1 {zeroC}')
for i in range(  ( (N//4) + 2 ) + wall, N//2 ):
    wall += 1
    for j in range( ( ( (N//4) -1  ) - wall ),( ( N//4 ) + 1 ) + wall ):

        if j == (i - 1):
            multiC *= C[i][j] * C[i][j-n]
            n += 2
print(f'\n\nпроизведение по периметру треугольника {multiC}')
if zeroC > multiC:

    wall = -1
    for i in range((N // 2) - 1, N // 4, -1):
        wall += 1

        for j in range(1 + wall, (N // 2) - wall - 1):
            if i > j and i > ((N//2)-1)-j:
                save = C[i][j]
                C[i][j]=C[j][i]
                C[j][i]=save

    F = [D[i] + E[i]  for i in range(N//2)]
    F += [C[i] + B[i] for i in range(N//2)]
else:
    F = [D[i] + E[i]  for i in range(N//2)]
    F += [B[i] + C[i] for i in range(N//2)]


print(f'\n\nматрица F   {F}')

"""сложение F+A"""
for i in range(0,N):
    for j in range(0,N):
        G[i][j] = F[i][j] + A[i][j]
print (f'\n\nсложение F+A {G}' )

for i in range(len(A)):
    for j in range(len(F[0])):
        for y in range (len(F)): H[i][j] += A[y][i] * G[y][j]

print (f' \n\nререзультат умножения A^т * (F+A) ,{H} ')

for i in range(len(A)):
    for j in range(len(F[0])):

        H[i][j] = H[i][j] - ( K * F[j][i] )

print(f'\n\nконечный результат {H}')
