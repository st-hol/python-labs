import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.linalg import solve


def seidel(A, b, x, n,eps,size):
    x_pr = x[:]
    L = np.tril(A)
    U = A - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print ('Iteration №' + str(i)),
        print(x)
        #print("\n")
        if all(abs(x[i] - x_pr[i]) < eps for i in range(size)):
            break
        x_pr = x[:]
        # if i==n:
        #     print('Solution does not converge')
        #     break
    return x, i

def mainDiag(A, b, size):
    for i in range(size):
        j=i
        #for j in range(size):
        while j <size:
            if(abs(A[i][j])<abs(A[j][i])):
                for k in range(size):
                    tmp = A[i][k]
                    A[i][k] =  A[j][k]
                    A[j][k] = tmp
                tmp = b[i]
                b[i] = b[j]
                b[j] = tmp
            #print(j)
            j+=1
    return A, b

def vector(x):
    for i in range(size):
        sum = 0
        for j in range(size):
            sum = sum + A[i][j]*x[j]
        vect.append(sum-B[i])


'''___MAIN___'''
A = [[-6, 5, 100, 2],[1, 3, 3, 7],[7, 7, 2, 7],[100, 8, 7, 7]]
B = [54, -6, 7, -3]
x = [0, 0, 0,0]

n = 40
eps = 1e-3
size=4

print(mainDiag(A,B,size))
answ = seidel(A, B, x, n,eps,size)
x = answ[0]
print("\n")
print("Вектор розв\'язків x:")
for i in range(size):
    print(str("%15.10f" % x[i]))

vect = []
vector(x)
print('Вектор нев\'язок')
for i in range(size):
    #print(vect[i])
    #print(str("%25.20f" % vect[i]))
    print(str("%15.10f" % vect[i]))
print("\n")
print("\n")

Epsilons=[1e-1,1e-2,1e-3,1e-4,1e-5]
Answers=[]
for i in range(5):
    E = Epsilons[i]
    print("-----------------e="+ str(E) +"------------------------")
    temp = seidel(A, B, x, n,E,size)
    Answers.append(temp[1]+1)
# print(Epsilons)
# print(Answers)


#plt.style.use('ggplot')

plt.plot(Answers, Epsilons, "bo", label='k(e)')
plt.plot(Answers, Epsilons, "b", label='k(e)')
#fig, ax = plt.subplots()
#ax.set(xlim=[0, 6], ylim=[1e-5, 1e-1])
#plt.bar(Epsilons, Answers, label='k(e)')


plt.title('Функція залежності K від E для методу Зейделя')
plt.legend()
plt.xlabel('k', fontsize=30)
plt.ylabel('e', fontsize=30)
plt.show()









# A = np.array([[100, 8, 7, 7],[7, 7, 2, 7],[-6, 5, 100, 2],[1, 3, 3, 7]])
# B = np.array([-3,7,54,-6])
# [-0.16780595  3.60191106  0.40080853 -2.54862183]


#print(solve(A, B))




# print(str("%15.10f" % x[0]))
# print(str("%15.10f" % x[1]))
# print(str("%15.10f" % x[2]))
# print(str("%15.10f" % x[3]))



# def seidel(A, b, x, max_iter,eps):
#     L = np.tril(A)
#     U = A - L
#     x1 = x[:]
#     for __ in range(max_iter):
#         for i in range(n):
#             x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
#             print ('Iteration №' + str(i)),
#             print(x)
#             #print("\n")
#             # if i == 24:
#             #     break
#         if all(abs(x1[i] - x[i]) < eps for i in range(n)):
#             print('FUC21312321321321321321312312312312312312312312312312K')
#             return x
#         x = x1[:]
#     print('Solution does not converge')
#         #return x

# def dominantDiag(A, b, size):
#     i=0
#     j=0
#     k=0
#     while i<size:
#         j = i
#         while j<size:
#             if(abs(A[i][j])<abs(A[j][i])):
#                 while k < size:
#                     tmp = A[i][k]
#                     A[i][k] =  A[j][k]
#                     A[j][k] = tmp
#                     k += 1
#                 tmp = b[i]
#                 b[i] = b[j]
#                 b[j] = tmp
#             j= j+1
#         i= i+1
#     return A, b




# import numpy as np
# from scipy.linalg import solve
#
#
# def jacobi(A, b, x, n):
#     D = np.diag(A)
#     R = A - np.diagflat(D)
#
#     for i in range(n):
#         x = (b - np.dot(R, x)) / D
#         print
#         str(i).zfill(3),
#         print(x)
#     return x
#
#
# '''___Main___'''
#
# A = np.array([[-6.0, 5.0, 100.0, 2.0],[1.0, 3.0, 3.0, 7.0],[7.0, 7.0, 2.0, 7.0],[100.0, 8.0, 7.0, 7.0]])
# b = np.array([54.0, -6.0, 7.0, -3.0])
# x = [1.0, 1.0, 1.0,1.0]
# n = 25
#
# print("\n\ninit"),
# print(x)
# print("")
# x = jacobi(A, b, x, n)
# print("\nSol "),
# print(x)
# print("Act "),
# print(solve(A, b))
# print("\n")






