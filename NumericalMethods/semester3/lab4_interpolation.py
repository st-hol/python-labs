import matplotlib.pyplot as plt
import numpy as np
import math

def variant7(x):
    if x<0:
        return -1.3*math.sqrt(abs(x)) + math.sin(x)
    else:
        return math.sqrt(x)+math.sin(x)

def lagranz(x, y, t):
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

a = 0
b = 6
n = 5
H = (b - a) / n
h = (b-a) / (4*n)
X = []
Y = []

for k in range(n+1):
    x = a + k * H
    X.append(x)
    fx = variant7(x)
    Y.append(fx)
# print(X)
# print(Y)

print('\nТаблиця на інтервалі [a, b] з кроком Н\n')
print('\tN \t\t X\t\t   f(x)')
for i in range(len(X)):
    print('\t' + str(i+1)+ '\t' + ("%7.1f" % X[i])+'\t\t'+str("%7.3f" %Y[i]))

# Y_interpolated =[lagranz(X,Y, i) for i in range(len(Y))]
# # print(Y_interpolated)
#
# relative_error = [Y[i]-Y_interpolated[i] for i in range(len(Y))]
# # print(relative_error)
#
# abs_error = [(abs(Y[i]-Y_interpolated[i]))/Y[i]*100 if(Y[i]!=0) else 'Null division ERROR' for i in range(len(Y))]
# # print(abs_error)

print('\n\n')

X_task=[]
Y_task=[]
Y_interpolated_task=[]
p_task = []
pr_task = []
x = a-H
#???
while(x<b+h):
    f1 = variant7(x) # fточн(x)
    f2 = lagranz(X,Y, x) # Lagranz
    p = f1 - f2
    pr = abs((p / f1) * 100)
    X_task.append(x)
    Y_task.append(f1)
    Y_interpolated_task.append(f2)
    p_task.append(p)
    pr_task.append(pr)
    x += h


print('\nТаблиця на інтервалі [a-H, b+H] з кроком h\n')
print('\tN \t\t X\t\t f точн(x) \t\t  f(x) \t\t f точн(x)-f(x) \t\t %')
for i in range(len(X_task)):
    print('\t'+str(i+1)+'\t'+("%7.1f"%X_task[i])+'\t\t'+str("%7.3f"%Y_task[i])+'\t\t\t'+("%7.3f"%Y_interpolated_task[i])+'\t\t\t'+("%7.3f"%p_task[i])+'\t\t\t'+("%7.3f"%pr_task[i]))


plt.plot(X_task,Y_task,'g', linewidth='3', label='f точн(х)')
plt.plot(X_task,Y_interpolated_task, 'r',linewidth='2', label='f(х)')

plt.xlabel('x', fontsize=17)
plt.ylabel('f(x)', fontsize=17)
plt.legend()
plt.grid(True)
plt.show()


#доп завдання (для n20)
n_mytask = 20
H_mytask = (b - a) / n_mytask
h_mytask = (b-a) / (4*n_mytask)
X_mytask=[]
Y_mytask=[]
for k in range(n_mytask+1):
    x = a + k * H_mytask
    X_mytask.append(x)
    fx = variant7(x)
    Y_mytask.append(fx)

print('\n\nДодадкове завдання: 7) Провести розрахунки для n=20. ')
print('\tN \t\t X\t\t   f(x)')
for i in range(len(X_mytask)):
    print('\t' + str(i+1)+ '\t' + ("%7.1f" % X_mytask[i])+'\t\t'+str("%7.3f" %Y_mytask[i]))

plt.plot(X_mytask, Y_mytask,'b', label='f точн(х)')

plt.xlabel('x', fontsize=17)
plt.ylabel('f(x)', fontsize=17)
plt.legend()
plt.grid(True)
plt.show()

def koef_polinom(A,X,Y):
    X1 =[[0 for i in range(6)] for i in range(6)]
    #X1=[[]]
    Y1=[0 for i in range(6)]
    for i in range(n):
        X1[0][i]=pow(X[0],i)
        X1[1][i]=pow(X[1],i)
        X1[2][i]=pow(X[2],i)
        X1[3][i]=pow(X[3],i)
        X1[4][i] = pow(X[4], i)
        X1[5][i] = pow(X[5], i)
        Y1[i]=Y[i]

    for k in range(n):
        AMAX = abs(X1[k][k])
        H = k

        i=k+1
        #for (int i = k + 1; i < n; i++)
        while(i<n):
            if (abs(X1[i][k]) > AMAX):
                AMAX = abs(X1[i][k])
                H = i
            i+=1

        if (H != k):
            j=k
            #for (int j = k; j < n; j++):
            while j < n:
                C = X1[k][j]
                X1[k][j] = X1[H][j]
                X1[H][j]= C
                j += 1

            temp = Y1[k]
            Y1[k] = Y1[H]
            Y1[H] = temp

        for i in range(n):
            if (i != k):
                R =  X1[i][k] / X1[k][k]

                j = k
                # for (int j = k; j < n; j++):
                while j < n:
                    X1[i][j] = X1[i][j] - R * X1[k][j]
                    j+=1
                Y1[i] = Y1[i] - R * Y1[k]
    for i in range(n):
        A.append(Y1[i] /X1[i][i])

    return A

A=[]

# print(koef_polinom(A,X,Y))
#[0.0, 2.564233926599919, -0.7400728141171645, -0.005467378640568845, 0.012324446217821805]



















