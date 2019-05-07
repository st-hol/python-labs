import sympy as sp
from scipy import integrate
import math

x = sp.Symbol('x')
def foo(x):
    return math.sin(x**2)+2  -  math.exp(x**2) #f(x) - g(x)

def _rectangle_rule(func, a, b, nseg, frac):
    """Обобщённое правило прямоугольников."""
    dx = 1.0 * (b - a) / nseg
    sum = 0.0
    xstart = a + frac * dx # 0 <= frac <= 1 задаёт долю смещения точки, в которой вычисляется функция, от левого края отрезка dx
    for i in range(nseg):
        sum += func(xstart + i * dx)
    return sum * dx

def midpoint_rectangle_rule(func, a, b, nseg):
    """Правило прямоугольников со средней точкой"""
    return _rectangle_rule(func, a, b, nseg, 0.5)

def trapezoid_rule(func, a, b, rtol = 1e-8, nseg0 = 1):
    """Правило трапеций
       rtol - желаемая относительная точность вычислений
       nseg0 - начальное число отрезков разбиения
       :Tests:
               >>> abs(trapezoid_rule(foo,-1,1) - integrate.quad(foo, -1, 1)[0]) < 1e-6 #графики перескаются в точках -1 и 1
               True
    """
    nseg = nseg0
    old_ans = 0.0
    dx = 1.0 * (b - a) / nseg
    ans = 0.5 * (func(a) + func(b))
    for i in range(1, nseg):
        ans += func(a + i * dx)
    ans *= dx
    err_est = max(1, abs(ans))
    while (err_est > abs(rtol * ans)):
        old_ans = ans
        ans = 0.5 * (ans + midpoint_rectangle_rule(func, a, b, nseg)) # новые точки для уточнения интеграла добавляются ровно в середины предыдущих отрезков
        nseg *= 2
        err_est = abs(ans - old_ans)
    return ans


# проверка - вольфрам
#wolfram --- https://www.wolframalpha.com/input/?i=area+between+y%3Dsin(x%5E2)%2B2,+y%3De%5E(x%5E2)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)














# #http://python-3.ru/page/vychislenie-ploshyshhadi-figury-ogranichennoj-dvumja-krivymi-s-pomoshhju-python#cut
# import math
# n = 500
# # "Цена деления" - расстояние между соседними точками
# dz = 1 / n
# # Количество точек, которые попадают внутрь области
# pts = 0
# # Начальное значение индекса, определяющего столбец точек
# i = 0
# # Внешний оператор цикла. Перебираем столбцы точек
# while i <= n:
#     # x - координата точки
#     x = dz * i
#     # Начальное значение второго индекса для точек столбца
#     j = 0
#     # Внутренний оператор цикла. Перебираем точки
#     # в одном столбце
#     while j <= n:
#         # y - координата точки
#         y = dz * j
#         # Условный оператор: проверяем, попала ли точка
#         # внутрь области
#         if y <= math.sin(x**2)+2 and y >= math.exp(x**2):
#             # Еще одна точка внутри области
#                 pts += 1
#         # Значение второго индекса увеличиваем на единицу
#         j += 1
#     # Значение первого индекса увеличиваем на единицу
#     i += 1
# # Вычисляем площадь фигуры
# S = pts / (n + 1) ** 2
# # Отображаем результат
# print("Площадь фигуры: " + str(S))