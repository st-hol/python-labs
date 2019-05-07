"""
***********************************************************
***             Лабораторна робота №5                  ***
***          з курсу "Основи програмування              ***
***              на скриптових мовах"                   ***
***                   Варіант №7                       ***
***     Виконав:студент Головачук С.В.   Група ТІ-72    ***
***********************************************************
"""
import numpy as np
m=int(input("Розмірність матриці:"))
n=int(input("Ведіть n:"))
M=np.random.randint(5,size=(m,m))
print("Згенерована матриця:\n",M)

def calcDiag(M):
    """
       :param M:matrix
       :return: integer:sum of diagonal elements
       :Tests:
       >>> calcDiag(M)==M.diagonal().sum()
       True
       >>> calcDiag(M)==M.trace()
       True
    """
    diag_tmp = 0
    for i in range(m):
        diag_tmp += M[i][i]
    return diag_tmp


while(n>=1):
    M_ = np.copy(M)
    for i in range(m):
        for j in range(m):
            M_[i][j] **= n
    print("Слід матриці для степеня <",n,">:", calcDiag(M_))
    print(M_)
    n-=1





#
#
# print("Слід матриці:", calcDiag(M))
# print( M.diagonal().sum())




if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)









# import numpy as np
# m=int(input("Розмірність матриці:"))
# n=int(input("Ведіть дальність проходу (n<size):"))
# M=np.random.randint(5,size=(m,m))
# print(M)
# diag_values=[]
# diag_tmp=0
# #n is depth
# for i in range(n):
#     diag_tmp +=M[i][i]
#     diag_values.append(diag_tmp)
# print("Сліди матриці:",diag_values)




# M_ = np.linalg.matrix_power(M, 2)