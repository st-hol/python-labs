"""
***********************************************************
***             Лабораторна робота №5                  ***
***          з курсу "Основи програмування              ***
***              на скриптових мовах"                   ***
***                   Варіант №7                       ***
***     Виконав:студент Головачук С.В.   Група ТІ-72    ***
***********************************************************
"""
import random
N = 15
x=[random.uniform(-3,3) for i in range(N)]
y=[random.uniform(-3,3) for i in range(N)]
#print(x,y)
r = [random.uniform(0,10) for i in range(N)]
c=[]
for el in range(N):
    c.append([x[el],y[el]])
#перший елемент - Х, другий - У
# for centre in c:
#     print('{:5.2},{:5.2}'.format(centre[0], centre[1]))
#print(c)

#приймає в якості параметра координати центра С і радіус двох кіл
def isIntersected(c_cur,r_cur,c_next,r_next):
    """
        Determines if two circles intersect.
               :param c_cur:list coordinates of first circle, r_cur:radius of first circle,
                      c_next:list coordinates of second circle,r_next:radius of second circle
               :return: boolean:True if circles intersect, False if not
               :Tests:
               >>> isIntersected([0,0], 1, [0,0], 2)
               True
               >>> isIntersected([0,0], 1, [5,5], 2)
               False
        """
    maxDistanceSquared = r_cur + r_next #radius1+radius2
    maxDistanceSquared *= maxDistanceSquared #(radius1+radius2)^2
    #maxDistanceSquared**=2
    dx = c_cur[0] - c_next[0] #x1-x2
    dy = c_cur[1] - c_next[1] #y1-y2
    currentDistanceSquared = dx * dx + dy * dy #(x1-x2)^2 + (y1-y2)^2
    # currentDistanceSquared = (x1-x2)^2 + (y1-y2)^2
    return currentDistanceSquared < maxDistanceSquared #(x1-x2)^2 + (y1-y2)^2 < (radius1+radius2)^2

#interS = [isIntersected(c[0],r[0],c[i],r[i]) for i in range(N)]

interS = [[isIntersected(c[i],r[i],c[j],r[j]) for i in range(N)]for j in range(N)]
for i in range(15):
    print('Коло №{} C({:5.2},{:5.2}) and R={:.2}, \t{}'.format(i,c[i][0], c[i][1],r[i], interS[i]))

#print(interS)
all_true = [all(row) for row in interS]
#print(all_true)
if all(all_true):
    print('Точка, що налажить всім кругам Сі(Хі,Уі) існує!')
else:
    print('Точка, що налажить всім кругам Сі(Хі,Уі) не існує!')


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)


import matplotlib.pyplot as plt
fig, ax = plt.subplots()
for i in range(N):
    ax.add_patch(plt.Circle((x[i], y[i]), r[i], color=(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)), alpha=0.2))
#Use adjustable='box-forced' to make the plot area square-shaped as well.
ax.set_aspect('equal', adjustable='datalim')
ax.plot() #Causes an autoscale update.
plt.show()






# import matplotlib.pyplot as plt
#  # in points, not data units
# fig, ax = plt.subplots(1, 1)
# ax.scatter(x, y, s=r)
# fig.show()








# def inPolygon(x, y, xp, yp):
#     c = 0
#     for i in range(len(xp)):
#         if (((yp[i] <= y and y < yp[i - 1]) or (yp[i - 1] <= y and y < yp[i])) and \
#                 (x > (xp[i - 1] - xp[i]) * (y - yp[i]) / (yp[i - 1] - yp[i]) + xp[i])): c = 1 - c
#     return c
#
#
#
#
# print(inPolygon(100, 0, (-100, 100, 100, -100), (100, 100, -100, -100)))
#
#
#


# -*- encoding: utf-8 -*-

#
# import numpy as np
#
# def point_in_triangle(p1, p2, p3, p):
#     '''Проверка принадлежности точки p треугольнику,
#      заданному точками (p1, p2, p3).
#     '''
#     e1 = p2 - p1
#     e2 = p3 - p1
#     # Точка внутри треугольника если сумма ее коррдинат в базисе двух сторон меньше 1
#     res = np.dot(np.linalg.pinv(np.vstack([e1, e2]).T), p - p1)
#     if (res >= -4.0e-16).all() and res.sum() <= 1:
#         return True
#     else:
#         return False
#
#
# def estimate_intersection_area(p1i, p2i, p3i, n=100000):
#     cmax = np.max(np.vstack([p1i, p2i, p3i]), axis=0)
#     cmin = np.min(np.vstack([p1i, p2i, p3i]), axis=0)
#     a = np.random.uniform(cmin[0], cmax[0], size=n)
#     b = np.random.uniform(cmin[1], cmax[1], size=n)
#     res = 0
#     # Пробегаем по всем пробным точкам
#     for x, y in zip(a, b):
#         # подсчитываем те, которые принадлежат всем треугольникам сразу
#         if all([point_in_triangle(p1, p2, p3, np.array([x, y])) for p1, p2, p3 in zip(p1i, p2i, p3i)]):
#             res += 1
#     return (cmax[1] - cmin[1]) * (cmax[0] - cmin[0]) * res / float(n)
#
#
# if __name__ == '__main__':
#     p1i = np.array([[0.0, 0.5],
#                     [0.0, 1.0],
#                     [0.0, 2.0]])
#     p2i = np.array([[1.0, 0.0],
#                     [1.0, 0.0],
#                     [1.0, 0.0]])
#     p3i = np.array([[0.0, 0.0],
#                     [0.0, 0.0],
#                     [0.0, 0.0]])
#     # В данном случае задан набор треугольников:
#     # [0,0.5], [1,0], [0,0]
#     # [0,1], [1,0], [0,0]
#     # [0,2], [1,0], [0,0]
#     print('Точное значение площади: 0.25', 'вычисленное:', estimate_intersection_area(p1i, p2i, p3i))






# #def isCollided(x1,y1,radius1, x2,y2, radius2):
#     maxDistanceSquared = radius1 + radius2
#     maxDistanceSquared *= maxDistanceSquared;
#
#     dx = x1 - x2
#     dy = y1 - y2
#
#     currentDistanceSquared = dx * dx + dy * dy
#
#     return currentDistanceSquared < maxDistanceSquared



# for i in range(N):
#     for j in range(N):
#         if ((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]) < (r[i] + r[j]) * (r[i] + r[j])):
#         #if( (x[i] + y[i]) - (x[j] + y[j]) > (r[i] + r[j]) ):
#             print(c[i])


# for(int i=0;i<15;i++)
#      for(int j=i+1;j<15;j++)
#           if(dim(x[i],y[i],x[j],y[j])>r[i]+r[j]) //  dim - функция определяющая растояние между точка на плоскости R*R
#                return false;
# return true;

# есть две ситуации, в которых окружности не пересекаются
# это
# когда расстояние между центрами больше суммы радиусов окружностей
# и
# расстояние между центрами меньше, чем радиус наименьшей окружности (т.е. маленькая окружность болтается внутри большой
