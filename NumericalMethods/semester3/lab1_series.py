#/**********************************************************\
#/***             Лабораторна робота №1                 ***\
#/***             з курсу «Чисельні методи»              ***\
#/*** Для ряду f(x) обчислити його наближене значення при***\
#/*** х[0,1] з кроком h=0.05 Обчислення припинити,       ***\
#/*** якщо |ai|<?=0.001 для двох послідовних членів ряду.***\
#/***                 Варіант 7                          ***\

import matplotlib.pyplot as plt
import numpy as np
import math
from mpmath import *
step = 0.05
eps = 0.001
x = 0
sum_coordY = []
temp_coordY = []
temp_coordX = []
#Eilers = [1, 5, 61, 1385, 50521, 2702765, 199360981, 19391512145, 2404879675441, 370371188237525, 69348874393137901, 15514534163557086905, 4087072509293123892361, 1252259641403629865468285, 441543893249023104553682821, 177519391579539289436664789665]
Eilers=[1, 5,61,1385,50521,2702765,199360981,19391512145]

print('\tX\t\t\t\tf(x)\t\t\tf\'(x)\t\t\t%\t\t\tN')
while round(x, 3) <= 1: #підрахунок ряду
    sum = 0
    i = 1

    temp = 1 #шоб хоч один раз зайти в цикл
    while abs(temp) > eps:  #якщо різниця більша eps
        temp = Eilers[i-1]*pow(x, 2*i) / math.factorial(2*i)
        sum += temp
        if round(x,3) == 0.5:   #накопичування точок для графіка при х = 0.5
            temp_coordY.append(temp)
            temp_coordX.append(i)
        i += 1

    sum+=1

    sum_coordY.append(sum)

    if(x==0):
        print(str("%7.2f" % x)+'\t\t\t'+str("%7.3f" % sum)+'\t\t\t'+str("%7.3f" % sec(x))+'\t\t\t'+str("ВИНЯТОК")+'\t\t\t'+str(i-1))
    else:
        print(str("%7.2f" % x)+'\t\t\t'+str("%7.3f" % sum)+'\t\t\t'+str("%7.3f" % sec(x))+'\t\t\t'+str("%7.2f" % ((abs(sum - (sec(x)))/sum*100)))+'\t\t\t'+str(i-1))
    x += step





#побудова графіків
x_coord = np.linspace(0, 1, 21)
y_coord = []
n=0
#blue --- graph for SECANT--f'(x)
for item in range(len(x_coord)):
    n=sec(x_coord[item])
    y_coord.append(n)
# y_coord = np.sin(x_coord)
plt.plot(x_coord, y_coord, "b", lw=5)



#red --- graph for SUM--f(x)
y_coord = np.array(sum_coordY)
# plt.plot(x_coord, y_coord, "r", lw=10, linestyle=':')
plt.plot(x_coord, y_coord, "m", lw=10, linestyle=':')
plt.xlabel('x', fontsize=30)
plt.ylabel('f(x)', fontsize=30)
plt.show()

#green --- graph for a(i)
#для "х"=0.5 -- графік залежності тимчасової суми при певному "і"
y_coord = np.array(temp_coordY)
x_coord = np.array(temp_coordX)
plt.plot(temp_coordX, temp_coordY, "g")
plt.xlabel('i', fontsize=30)
plt.ylabel('a(i)', fontsize=30)
plt.show()