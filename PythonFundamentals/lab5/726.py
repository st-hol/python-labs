"""
***********************************************************
***             Лабораторна робота №5                  ***
***          з курсу "Основи програмування              ***
***              на скриптових мовах"                   ***
***                   Варіант №7                       ***
***     Виконав:студент Головачук С.В.   Група ТІ-72    ***
***********************************************************
"""
import math

def variantA(x):
    return x*2**x-1
def variants(key, x): #x is parameter for calculating function
    # Returns a key-varianted function for executing task.
    return {
        'а': x*2**x-1,
        'б': x**2-math.sin(5*x),
        'в': 2/3*math.sin(2*x)**2 - 3/4*math.cos(2*x)**2,
        'г': x**3 - 2*x**2 + x - 1,
        'д': (4+x**2)*(math.exp(x) - math.exp(-x)) - 18,
        #'е': x**4 + 0.5*x**3 - 4*x**2 - 3*x - 0.5,
        'ж': x**2 - 1.3*math.log(x+0.5) - 2.8*x + 1.15
    }[key]

def chordeMethod(keyVariant, A,B,eps):
    """
       :param keyVariant:variant name letter, A:left limit, B:right limit, eps:calculation accuracy
       :return: x:root of equatation
       :Tests:
       >>> abs(answers[0] - nsolve(x*2**x-1, x, 0)) < 1e-6
       True
       >>> variants('а', answers[0]) < 1e-6
       True
    """
    x = (A * variants(keyVariant,B) - B * variants(keyVariant,A)) / (variants(keyVariant,B) - variants(keyVariant,A))
    if(variants(keyVariant,A) * variants(keyVariant,B) < 0):
      while(abs(variants(keyVariant,x)) > eps):
        print("\tx: ","%7.7f" % x, "\t\t\t\tf(x): ", variants(keyVariant,x))
        if(variants(keyVariant,A) * variants(keyVariant,x) < 0):
             x = (x * variants(keyVariant,A) - A * variants(keyVariant,x)) / (variants(keyVariant,A) - variants(keyVariant,x))
        else:
            x = (x * variants(keyVariant,B) - B * variants(keyVariant,x)) / (variants(keyVariant,B) - variants(keyVariant,x))
    return x

answers=[]
V=[["а",0,1],["б",0.5,0.6],["в",0,math.pi/4],["г",2.1,2.2],["д",1.2,1.3],["ж",2.1,2.5]]
for v in V:
    print("Варіант: ",v[0],")", "[",v[1],",", v[2],"]")
    answers.append(chordeMethod(v[0], v[1], v[2] , 1e-6))
    print(chordeMethod(v[0], v[1], v[2], 0.001))


from sympy import Symbol,nsolve
x = Symbol('x')

#print("abs",abs(chordeMethod("а",0,1, 1e-6)- nsolve(x*2**x-1, x, 0)))
# f1 = x**3 - 2*x**2 + x - 1
# print(nsolve(f1, x, 0))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


# for i in range(7):
#     print("Варіант: ",V[i][0],")", "[",V[i][1],",", V[i][2],"]")
#     chordeMethod(V[i][0], V[i][1], V[i][2] ,0.01)
#     print('----------------------------------------------------------')

#print(V[6][0])
#chordeMethod(V[6][0],V[6][1], V[6][2] ,0.001)
#chordeMethod(V[6][0], V[6][1], V[6][2] ,0.001)

#
# print("Варіант: ",V[0][0],")")
# chordeMethod(V[0][0],V[0][1], V[0][2] ,0.001)







































# class Polynom(object):
#
#     def __init__(self, ai):
#         self.ai = ai
#
#     def get_polynom(self, x):
#         return sum((k * (x ** z) for z, k in enumerate(self.ai)))
#
#     def chord_method(self, a, b, e):
#         i = 0
#         c = (a * self.get_polynom(b) - b * self.get_polynom(a)) / \
#             (self.get_polynom(b) - self.get_polynom(a))
#         c_prev = 100000
#         while ((abs(c - c_prev) >= e) or abs(self.get_polynom(c)) >= e):
#             # print("#", i, "interval: [" , a, ",", b, "]")
#             print("#", i, "current result = ", c)
#             print(abs(c - c_prev), " > ", e, "   or   ",
#                   abs(self.get_polynom(c)), ">=", e)
#
#             if (self.get_polynom(a) * self.get_polynom(c) <= 0):
#                 b = c
#             else:
#                 a = c
#             c_prev = c
#             c = (a * self.get_polynom(b) - b * self.get_polynom(a)) / \
#                 (self.get_polynom(b) - self.get_polynom(a))
#             i += 1
#         return c
#
#
# def main():
#     pol = Polynom([-4, -2, 1, -3, 1])
#     a = 0.067
#     # a = -2.5
#     b = 5
#     # b = -0.57
#     e = 0.01
#
#     print("====================Chord_method==========================")
#     print(pol.chord_method(a, b, e), '\n')
#
#
#
# if __name__ == '__main__':
#     main()










# import math
# def variantA(x):
#     return x*2**x-1
# def variants(key, x):
#     #return x*2**x-1
#     return {
#         'а': x*2**x-1,
#         'б': x**2-math.sin(5*x),
#         'в': 2/3*math.sin(2*x)**2 - 3/4*math.cos(2*x)**2,
#         'г': x**3 - 2*x**2 + x - 1,
#         'д': (4+x**2)*(math.exp(x) - math.exp(-x)) - 18,
#         'е': x**4 + 0.5*x**3 - 4*x**2 - 3*x - 0.5,
#         'ж': x**2 - 1.3*math.log(x+0.5) - 2.8*x + 1.15,
#     }[key]
#
# def chordeMethod(A,B,eps):
#     x = (A * variantA(B) - B * variantA(A)) / (variantA(B) - variantA(A))
#     if(variantA(A) * variantA(B) < 0):
#       while(abs(variantA(x)) > eps):
#         print("\tx: ","%7.7f" % x, "\t\t\t\tf(x): ", variantA(x))
#         if(variantA(A) * variantA(x) < 0):
#              x = (x * variantA(A) - A * variantA(x)) / (variantA(A) - variantA(x))
#         else:
#             x = (x * variantA(B) - B * variantA(x)) / (variantA(B) - variantA(x))
#
#
# chordeMethod(0, 1 ,0.001)
#
# print(variants('б',2))
















# from numpy import array, arange, sign, polydiv
#
# # precision
# E = 0.01
#
# # var№ 6
# P = array((2, -4, -1, 2))
#
# # derivative
# P1 = array((6, -8, -1))
#
#
# def polynomial(x, p=P):
#     """
#     Get polynomial value
#     :param x: argument
#     :param p: polynomial
#     :return: P(x)
#     """
#
#     value, power = 0, 0
#
#     for i in range(len(p) - 1, -1, -1):
#         value += p[i] * x ** power
#         power += 1
#
#     return value
#
# def chord(a, b, criterion=True):
#     counter, c = 0, 0
#
#     while 1:
#         c_prev = c
#         c = (a * polynomial(b) - b * polynomial(a)) / (polynomial(b) - polynomial(a))
#
#         if polynomial(a) * polynomial(c) <= 0:
#             b = c
#         elif polynomial(b) * polynomial(c) <= 0:
#             a = c
#
#         counter += 1
#         print('iter#', counter, c)
#
#         if criterion:
#             if abs(polynomial(c)) < E:
#                 break
#         else:
#             if abs(c - c_prev) < E:
#                 break
#
#     print(c, ', number of iter: ', counter, sep='')
#
#
#
# print(chord(-2, -0.41), (0.33, 1.65), (1.7, 3))