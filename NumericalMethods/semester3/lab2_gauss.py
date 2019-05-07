import numpy as np
#[-0.16780595369349438, 3.6019110621095196, 0.40080852627710395, -2.548621830209482]
#https://prog-cpp.ru/gauss/
#http://mathprofi.ru/metod_gaussa_dlya_chainikov.html
#https://vunivere.ru/work60661/page2
# Нижняя треугольная матрица (или нижнетреугольная матрица) —
# квадратная матрица , у которой все элементы выше главной диагонали равны нулю
B = np.array([54.0, -6.0, 7.0, -3.0])
A = np.array([
        [ -6.0,5.0,100.0,2.0 ],
    	[ 1.0,3.0,3.0,7.0 ],
		[ 7.0,7.0,2.0,7.0 ],
		[ 100.0,8.0,7.0,7.0 ],])
A1 = np.array([
        [ -6.0,5.0,100.0,2.0 ],
    	[ 1.0,3.0,3.0,7.0 ],
		[ 7.0,7.0,2.0,7.0 ],
		[ 100.0,8.0,7.0,7.0 ],])


# np.set_printoptions(precision=3)

# # [A|b]
def gaussElimination(matrix):
    np.asarray(matrix)  # ensure the array
    matrix = matrix.astype(float)  # ensure the datatype is float

    print("the initial matrix:")
    print( matrix)

    if matrix[0, 0] == 0.0:
        raise Exception("matrix row 1 column 1 cannot be zero!")
    n, m = matrix.shape
    #print(  "row:", n, "column:", m)

    # start the elimination phase
    for i in range(0, n):  # row
        for j in range(i + 1, n):
            if matrix[j, i] != 0.0:
                #print("using row ", i, "as pivot and row ", j, "as target")
                #print("використовуючи рядок ", i, "як опорний, а рядок ", j, "як цільовий")
                #print()
                multiplier = matrix[j, i] / matrix[i, i]
                # print matrix[i,k],matrix[k,k],multiplier
                # just to verbose multiplier process
                matrix[j, i:m] = matrix[j, i:m] - multiplier * matrix[i, i:m]
                #print(matrix)

    # start the backsubstitution phase
    x = []
    substractor = 0.0
    for i in range(n - 1, -1, -1):  # row
        # print "i",i #just for debugging
        for j in range(0, n - i):  # column
            # print "j",j #just for debugging
            if j == 0:
                substractor = 0
            else:
                substractor = substractor + matrix[i, m - j - 1] * x[j - 1]

        x.append((matrix[i, m - 1] - substractor) / matrix[i, i])
        # print(matrix)
        # print(x)
        # print "x",x

    return x

#4x5
a=np.array([
        [ -6.0,5.0,100.0,2.0,101.0],
    	[ 1.0,3.0,3.0,7.0,14.0 ],
		[ 7.0,7.0,2.0,7.0,23.0 ],
		[ 100.0,8.0,7.0,7.0,122.0 ],])
# a=np.array([
#         [ -6.0,5.0,100.0,2.0,54.0],
#     	[ 1.0,3.0,3.0,7.0,-6.0 ],
# 		[ 7.0,7.0,2.0,7.0,7.0 ],
# 		[ 100.0,8.0,7.0,7.0,-3.0 ],])

#print('\n Вхідна матриця та вектор розв\'язків : \n', a, '\n')
##first-ouput
#print(np.vectorize("%7.2f".__mod__)(a))
##second-ouput
#print(np.char.mod( "%4.2f", a))
##third-output
# M=np.array(a).ravel()
# c=0
# for i in M:
#     if(c%5==0):
#         print("\n")
#     print('{:10.2f}'.format(i), end='')
#     c+=1
# print("\n")

b = np.array([54.0, -6.0, 7.0, -3.0])
o = np.array([0.0, 0.0, 0.0, 0.0])
n = np.array([0.0, 0.0, 0.0, 0.0])

x=gaussElimination(a)
x.reverse()
## Робимо перевірку, аби знайти нев'язку
for i in range(0,A.shape[0]):
    for j in range(0, A.shape[0]):
        A[i,j] = A[i,j] * x[j]
        o[i] += A[i,j]


print('\n\n Вектор Розв’язкiв X: \n', x)
# for i in range(4):
#     print("%17.7f" % x[i])
#     #print("%17e" % x[i])


np.set_printoptions(suppress=True)
nevyaz=np.absolute(b - o)
print('\n Вектор Нев’язки   [B] - [А] * [X]: \n',nevyaz)
# for i in range(4):
#     print("%17.10f" % nevyaz[i])


# vyazka=np.dot(A1, x)
# #print("\n Вектор Перевiрки    [А] * [X] = [B]:\n", vyazka )
# # for i in range(4):
# #     print("%17.10f" % vyazka[i])












