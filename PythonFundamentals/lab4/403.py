"""
***********************************************************
***             Лабораторна робота №4                  ***
***          з курсу "Основи програмування              ***
***              на скриптових мовах"                   ***
***                   Варіант №7                       ***
***     Виконав:студент Головачук С.В.   Група ТІ-72    ***
***********************************************************
"""
# import numpy as np
import random
N=15
M = [[random.randint(-50,50) for j in range(N)] for i in range(N)]
#print(M)
# Print the matrix
# for row in M:
#     print(row)
[print(row) for row in M]
# indexes=[]
# for r in range(N):
#     for c in range(N):
#         if(M[r][c])==0:
#             indexes.append([r,c])
idx=[[[r,c]  for c in range(N) if M[r][c]==0]for r in range(N)]
#print(idx)
real_idx=[item for item in idx if item]
#print(real_idx)

# print(n_idx)
# print('Indexes of all null elements:')
# [print(row) for row in idx if(row)]
# print(idx)
# for row in idx:
#     if(row):
#         print(row)

if real_idx:
    chc = input('If you want to get index of one Null element, enter "1"\nIf you want to get indexes of all Null element, enter any other key:')
    if chc == '1':
        print('Random Null element index:', random.choice(real_idx))
    else:
        print('All Null elements indexes:', real_idx)
        #[print(row) for row in n_idx if (row)]
else:
    print('No nulls in matrix')





# arr=[]
# N=15
# #A = np.arange(N**2).reshape((N, N))
# Matrix = np.random.randint(30, size=(N,N))
# print(Matrix)
# # arr=np.reshape(Matrix, (1, N*N))[0]
# # print(arr)
# arr = np.array(Matrix).ravel()
# # a =  np.ravel(Matrix).T
# # a = np.array(Matrix).flatten()
# if 0 in arr:
#     choice = input('If you want to get index of one Null element, enter "1"\nIf you want to get indexes of all Null element, enter any other key:')
#     nulls = [index for index, item in enumerate(arr) if item ==0]
#     if choice == '1':
#         print('Random Null element index:', random.choice(nulls))
#     else:
#         print('All Null elements indexes:', nulls)




#
# if 0 in M:
#     chc = input('If you want to get index of one Null element, enter "1"\nIf you want to get indexes of all Null element, enter any other key:')
#     nulls = [index for index, item in enumerate(M) if item ==0]
#     if chc == '1':
#         print('Random Null element index:', random.choice(nulls))
#     else:
#         print('All Null elements indexes:', nulls)


        # choice = input('If you want to enter manually, enter "1"\nIf you want to generate array, enter any other key:')
        # if choice == '1':
        #     # for i in range(N):
        #     #     arr.append(float(input("enter: ")))
        #     arr = list(map(int, input('Enter element separated with spaces').split()))
        # else: