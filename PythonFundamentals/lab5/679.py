"""
***********************************************************
***             Лабораторна робота №5                  ***
***          з курсу "Основи програмування              ***
***              на скриптових мовах"                   ***
***                   Варіант №7                       ***
***     Виконав:студент Головачук С.В.   Група ТІ-72    ***
***********************************************************
"""
import numpy as np
n=int(input('Введіть розмірність n:'))
#n=3
np.set_printoptions(precision=1)
m1=np.random.uniform(-n, n, (n, n))

m2=np.random.uniform(-n, n, (n, n))
print('Перший масив\n',m1)
print('Другий масив\n',m2)
max_of_rows_m2=[np.max(m2[row]) for row in range(len(m2))]
print('Максимуми кожної строки другого масиву\n',max_of_rows_m2)

prod_of_rows_m2=[]
prod_tmp = 1
for row in range(n):
    for col in range(n):
        prod_tmp*=m2[row][col]
    prod_of_rows_m2.append(prod_tmp)
    prod_tmp=1
print('Добутки елементів кожної строки другого масиву\n', prod_of_rows_m2)

#завдання а)
A=np.copy(m1)
for row in range(n):
    for col in range(n):
        A[row][col]=(m1[row][col]*max_of_rows_m2[row])

print('Перший масив після обробки завдання а)\n', A)
# завдання б)
B=np.copy(m1)
for col in range(n):
    for row in range(n):
        B[row][col]+=prod_of_rows_m2[col]

print('Перший масив після обробки завдання б)\n', B)


#mm1=[[ m1[i][j]*max_of_rows_m2[i] for j in range(n)] for i in range(n)]
# print(m1)



#maximum_of_rows=[np.max(m1[row] for row in m1 ]
