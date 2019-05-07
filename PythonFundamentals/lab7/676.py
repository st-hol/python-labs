import numpy as np
X = np.arange(54).reshape(6,9)
print("MATRIX:\n",X)

#перестановка столбцов
X[:,0], X[:,-1] = X[:,-1], X[:,0].copy()
print("MATRIX(swaped cols):\n",X)

#перестановка строк
X[0], X[-1] = X[-1], X[0].copy()
print("MATRIX(swaped rows):\n",X)





# import random
# X = [[random.randint(1,9) for j in range(9)]for i in range(6)]
# [print(i) for i in X]
# print("________")
# X[0], X[-1] = X[-1], X[0]
# [print(i) for i in X]
#
#
# import numpy as np
# X = np.array(X)
#
# X[:,0], X[:,-1] = X[:,-1], X[:,0].copy()
#
# print(X)

#http://progras.ru/33-reshaem-problemy-s-dvumernym-spiskom/