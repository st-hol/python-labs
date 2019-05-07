import math
import matplotlib.pyplot as plt

a = 0.0
b = 2.0
y0 = 0.5
h1 = 0.4
h2 = h1 / 5.0
h3 = h1 / 25.0

def exact_func(x):  # заранее известное решение коши
    return 1.0 / (1.0 + math.exp(x ** 2))

def diff_func(x, y):  # y'=
    return 2 * x * y ** 2 - 2 * x * y

def rkf4_method(xk, yk, h):
    k0 = h * diff_func(xk, yk)
    k1 = h * diff_func(xk + 2.0 / 9 * h, yk + 2.0 / 9 * k0)
    k2 = h * diff_func(xk + h / 3.0, yk + 1.0 / 12 * k0 + 1.0 / 4 * k1)
    k3 = h * diff_func(xk + 3.0 / 4 * h, yk + 69.0 / 128 * k0 - 243.0 / 128 * k1 + 135.0 / 64 * k2)
    k4 = h * diff_func(xk + h, yk - 17.0 / 12 * k0 + 27.0 / 4 * k1 - 27.0 / 5 * k2 + 16.0 / 15 * k3)

    # y_viewSub(k+1) =
    return (yk + 1.0 / 9 * k0 + 9.0 / 20 * k2 + 16.0 / 45 * k3 + 1.0 / 12 * k4)

def hoin_method(xk, yk, h):
    k1 = h * diff_func(xk, yk)
    k2 = h * diff_func(xk + h / 2, yk + k1 / 2)
    k3 = h * diff_func(xk + h, yk - k1 + 2 * k2)

    # y_viewSub(k+1) =
    return yk + 1.0 / 6 * (k1 + 4*k2 + k3)

def calc(h):
    yxk = []  # список для добавления значений точной функции
    xk = []  # список для добавления точек х
    ykh = []  # список для добавления приближенных значений методом MethodHoin
    yk4 = []  # список для добавления приближенных значений методом Рунге-Кутта-Фельберга ІV

    y = y0  # y0 = 0 - початкова умова
    y2 = y0  # y0 = 0 - початкова умова

    xk.append(a)  # добавление точки x0
    yxk.append(y0)  # добавление точки y0
    ykh.append(y0)  # добавление точки y0
    yk4.append(y0)  # добавление точки y0

    x = a
    i = 1
    while x <= b + h:
        xk.append(x + h)  # добавления точек х
        yxk.append(exact_func(x + h))  # добавления значений точной функции
        ykh.append(hoin_method(x, y, h)) # добавление приближенных значений методом Рунге-Кутта-Фельберга ІІІ
        y = ykh[i] # cохранение предидущего значения
        yk4.append(rkf4_method(x, y2, h))  # добавление приближенных значений методом Рунге-Кутта-Фельберга ІV
        y2 = yk4[i] # сохранение предидущего значения

        x += h
        i += 1

    list = []  # динамический список хранящий другие списки
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
# точки Х (с шагом h)
# точки У_точн
# точки У_хойне
# точки У_рк4











































# def calc(h):
#
#             i=0
#             x=0
#             prevY = [0 for i in range(6)]
#
#             list = [] # динамический список хранящий другие списки
#
#             yxk_EXACT = []       # список для добавления значений точной функции
#             xk_FOR_X_AXIS = []        # список для добавления точек х
#             yk_FOR_Y_AXIS = []        # список для добавления точек х
#             y = y0                         # y0 = 0 - початкова умова
#
#             xk_FOR_X_AXIS.append(a)                     # добавление точки x0
#             yxk_EXACT.append(y0)                   # добавление точки y0
#             yk_FOR_Y_AXIS.append(y0)
#
#             #for ( x = a, i=1; x <= b + h; x += h,++i)
#             x = a
#             i = 1
#             while x <= b + h:
#                 xk_FOR_X_AXIS.append(x+h)                                     #  добавления точек х
#                 yxk_EXACT.append(ExactFunction(x+h));                     #  добавления значений точной функции
#                 prevY[0] = Differentialfunction(x,y);
#                 prevY[1] = Differentialfunction(x-h, MethodRungeKuttaFehlberga4(x - 2* h, ExactFunction( x - 2* h ), h));
#                 prevY[2] = Differentialfunction(x - 2 * h, MethodRungeKuttaFehlberga4(x - 3 * h, ExactFunction(x - 3 * h), h));
#                 prevY[3] = Differentialfunction(x - 3 * h, MethodRungeKuttaFehlberga4(x - 4 * h, ExactFunction(x - 4 * h), h));
#                 prevY[4] = Differentialfunction(x - 4 * h, MethodRungeKuttaFehlberga4(x - 5 * h, ExactFunction(x - 5 * h), h));
#                 prevY[5] = Differentialfunction(x - 5 * h, MethodRungeKuttaFehlberga4(x - 6 * h, ExactFunction(x - 6 * h), h));
#                 #yk_FOR_Y_AXIS.Add(MultistepMethod(x+h,y,h,prevY));
#                 #y = yk_FOR_Y_AXIS[i];
#
#                 x += h
#                 i += 1
#
#
#             list.append(xk_FOR_X_AXIS);
#             list.append(yxk_EXACT);
#             list.append(yk_FOR_Y_AXIS);
#
#             return list;
