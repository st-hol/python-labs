import sympy as sp
from scipy import integrate
import numpy as np
import math

x = sp.Symbol('x')
def f(x):
    return math.cos(x)/x
def trapezial(f, a, b, eps):
    """
        Calculates definite integral by trapezoid method.
               :param f:function, a:lower limit, b:upper limit, eps:tolerance
               :return: int:integral
               :Tests:
               >>> abs(trapezial(f, np.pi/2, np.pi,1e-6) - integrate.quad(f, np.pi/2, np.pi)[0] ) < 1e-3
               True
    """
    answer=(f(a) + f(b))/2 * (b-a) #рахуємо площу суцільної трапеції
    n = 1
    while True: #уточнюємо до eps
        n+=1
        old = answer
        h = (b - a) / n #розділяємо на n трапецій
        answer = (f(a) + f(b))/2 #середня лінія трапеції
        for i in range(1, n):
            answer += f(a + i*h)
        answer *= h
        if abs(old - answer) < eps:
            return answer

print('Використовуючи scipy:',integrate.quad(f, np.pi/2, np.pi))
print('Використовуючи свою функцію:',trapezial(f, np.pi/2, np.pi,1e-6))
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
