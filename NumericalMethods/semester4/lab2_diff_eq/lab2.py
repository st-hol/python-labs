import math
import matplotlib.pyplot as plt

a = 0.0
b = 2.0
y0 = 0.5
h1 = 0.4
h2 = h1 / 5.0
h3 = h1 / 25.0

def exact_func(x):
    return 1.0 / (1 + math.exp(x ** 2))

def diff_func(x, y):
    return 2 * x * y ** 2 - 2 * x * y

def rkf4_method(xk, yk, h):
    k0 = h * diff_func(xk, yk)
    k1 = h * diff_func(xk + 2.0 / 9 * h, yk + 2.0 / 9 * k0)
    k2 = h * diff_func(xk + h / 3.0, yk + 1.0 / 12 * k0 + 1.0 / 4 * k1)
    k3 = h * diff_func(xk + 3.0 / 4 * h, yk + 69.0 / 128 * k0 - 243.0 / 128 * k1 + 135.0 / 64 * k2)
    k4 = h * diff_func(xk + h, yk - 17.0 / 12 * k0 + 27.0 / 4 * k1 - 27.0 / 5 * k2 + 16.0 / 15 * k3)

    return (yk + 1.0 / 9 * k0 + 9.0 / 20 * k2 + 16.0 / 45 * k3 + 1.0 / 12 * k4)

def hoin_method(xk, yk, h):
    k1 = h * diff_func(xk, yk)
    k2 = h * diff_func(xk + h / 2, yk + k1 / 2)
    k3 = h * diff_func(xk + h, yk - k1 + 2 * k2)

    return yk + 1.0 / 6 * (k1 + 4*k2 + k3)

def calc(h):
    yxk = []
    xk = []
    ykh = []
    yk4 = []

    y = y0
    y2 = y0

    xk.append(a)
    yxk.append(y0)
    ykh.append(y0)
    yk4.append(y0)

    x = a
    i = 1
    while x < b:
        xk.append(x + h)
        yxk.append(exact_func(x + h))
        ykh.append(hoin_method(x, y, h))
        y = ykh[i]
        yk4.append(rkf4_method(x, y2, h))
        y2 = yk4[i]

        x += h
        i += 1

    list = []
    list.append(xk)
    list.append(yxk)
    list.append(ykh)
    list.append(yk4)
    return list




res_h1 = calc(h1)
res_h2 = calc(h2)
res_h3 = calc(h3)

def printTable(res_list, h, e_list, Hoin_or_RK4 = 0):

    if Hoin_or_RK4 == 0:
        print('\t\t\t\t\t\t\t\t\t\t\tВЫЧИСЛЕНИЕ МЕТОДОМ ХОЙНЕ 3-го ПОРЯДКА')
    elif Hoin_or_RK4 == 1:
        print('\t\t\t\t\t\t\t\t\t\t\tВЫЧИСЛЕНИЕ МЕТОДОМ РУНГЕ-КУТТА 4-го ПОРЯДКА')

    print("\t\t\t\t\t\t\t##################### ТАБЛИЦА ПРИ ШАГЕ h =", h,"  #####################")
    print("\t\t\t  xk \t\t\t\t\t  y(xk)  \t\t\t\t  yk  \t\t\t\t\t e = y(xk)-yk \t\t\t\t\t 100*e/yk")
    print("#################################################################################################################################")

    for i in range(len(res_list[0])):
        xk = res_list[0][i]
        y_xk_ = res_list[1][i]
        yk = res_list[2 + Hoin_or_RK4][i]
        e = y_xk_ - yk
        e_ = abs(100*e/yk)
        print("%25.20lf" % xk, "%25.20lf" % y_xk_, "%25.20lf" % yk, "%25.20lf" % e,"%25.20lf" % e_)
        e_list.append(e)





e_list1=[]
e_list2=[]
e_list3=[]

printTable(res_h1, h1, e_list1)
print('\n')
printTable(res_h2, h2, e_list2)
print('\n')
printTable(res_h3, h3, e_list3)
print('\n')


plt.plot(res_h1[0], e_list1, "r", label='e(х) при h1', linewidth='2', alpha=0.4)
plt.plot(res_h2[0], e_list2, "go", label='e(х) при h2', linewidth='2', alpha=0.4)
plt.plot(res_h3[0], e_list3, "b", label='e(х) при h3', linewidth='2', alpha=0.7)
plt.title('График е(х) при разных h')
plt.legend()
plt.xlabel('х', fontsize=30)
plt.ylabel('e', fontsize=30)
plt.show()




e_list1=[]
e_list2=[]
e_list3=[]

printTable(res_h1, h1, e_list1, 1)
print('\n')
printTable(res_h2, h2, e_list2, 1)
print('\n')
printTable(res_h3, h3, e_list3, 1)
print('\n')

# plt.plot(res_h1[0], e_list1, "r", label='e(х) при h1', linewidth='2', alpha=0.4)
# plt.plot(res_h2[0], e_list2, "go", label='e(х) при h2', linewidth='2', alpha=0.4)
# plt.plot(res_h3[0], e_list3, "b", label='e(х) при h3', linewidth='2', alpha=0.7)
# plt.title('График е(х) при разных h')
# plt.legend()
# plt.xlabel('х', fontsize=30)
# plt.ylabel('e', fontsize=30)
# plt.show()












# [print(x) for x in (res_h1)]
# [print(x) for x in (res_h2)]
# [print(x) for x in (res_h3)]




# messages = ['','','','']
#[print(x) for x in (res_h1)]



























