n = int(input("n:"))

import numpy as np
X = np.arange(n**2).reshape(n,n)
print("matrix:\n",X)

tri_upper_diag = np.triu(X)
print("upper triag matrix:\n", tri_upper_diag)

b = np.random.random(n)
print("vector b",b)

prod = np.dot(X,b)
print("X*b = ", prod)