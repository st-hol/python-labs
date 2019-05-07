import numpy as np

def interpolate(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z

n = int(input("кількість відомих точок:"))

#з кроком = 1секунда
x = np.arange(n)
y = np.random.randint(15, 30, size=n)

n=5
h = abs((x[0] - x[-1])/n)

x_=[]
y_=[]
i=x[0]-h
while i<x[-1]+h:
    x_.append(i)
    y_.append(interpolate(x,y,i))
    i += h

print("задані значення температури:", y, "\nна проміжку",x)
print("\nінтерпольовані значення температури:", y_,  "\nна проміжку", x_)

t = float(input("\nшукане t:"))

flag=False
for i in range(len(y_)):
    if abs(y_[i] - t) < 1e-1:
        flag=True
        print("температура", t , "спостерігалася у момент часу", x_[i])

if not flag:
    print("таких температур немає на проміжку")





