"""
***********************************************************
***             Лабораторна робота №6                  ***
***          з курсу "Основи програмування              ***
***              на скриптових мовах"                   ***
***                   Варіант №7                       ***
***     Виконав:студент Головачук С.В.   Група ТІ-72    ***
***********************************************************
"""
import random
a = [random.uniform(-50, 50) for i in range(25)]
print("a)",a)
b = [random.randint(-20,20) for i in range(30)]
print("б)",b)
v = [random.uniform(0, 40) for i in range(20)]
print("в)",v)
g = [random.randint(0,1000) for i in range(35)]
print("г)",g)
d = [random.randint(1,20) for i in range(27)]
print("д)",d)
n = random.randint(1,30)
e = [random.uniform(-100, 100) for i in range(n)]
print("e)", e)
n = random.randint(1,20)
m = random.randint(1,20)
zhe1 = [random.uniform(-150, 150) for i in range(n)]
zhe2 = [[random.uniform(0, n) for i in range(m)]]
print("ж)", zhe1, zhe2)
two = [2 for i in range(7)]
three = [3 for i in range(8)]
z = two+three
random.shuffle(z)
print("з)",z)
I = [i for i in range(1,13)]
random.shuffle(I)
print("и)",I)
import string
Alphabet = string.ascii_lowercase
k = [random.choice(Alphabet) for i in range(28)]
print("к)",k)
def notIn(lst, key):
    if key not in lst:
        return True
    return False
l = []
while(len(l)<5):
    r = random.choice(Alphabet)
    if notIn(l,r):
        l.append(r)
print("л)",l)