#ggoogle academy

import math

def f(x):
    C = 1
    return math.tan(x) + C

h = 0.1
x_0 = 1
f_e = 1/math.cos(x_0)**2
MAX_ITER = 30

print("\t\t\t\t\t\t\t##################### TASK   № 1 #####################")
print("\t\t\t  h\t\t\t\t\t   Comput.value\t\t\t\t  Exact value\t\t\t\t\tError")
for i in range(MAX_ITER):
    h /= 2.0
    f_c = (f(x_0 + h) - f(x_0 - h))/(2.0*h)
    print("%25.20lf" % h, "%25.20lf" % f_c, "%25.20lf" % f_e, "%25.20lf" % (f_c - f_e))





#######################################################################################

h = 0.1
print("\t\t\t\t\t\t\t##################### TASK   № 2 #####################")
print("\t\t\t  h\t\t\t\t\t   Comput.value\t\t\t\t  Exact value\t\t\t\t\tError")
for i in range(MAX_ITER):
    h /= 2.0
    f_c = (2.0*(f(x_0 - 2.0*h) - f(x_0 + 2.0*h)) + 16.0*(f(x_0 + h) - f(x_0 - h)))/(24.0*h)
    print("%25.20lf" % h, "%25.20lf" % f_c, "%25.20lf" % f_e, "%25.20lf" % (f_c - f_e))




#######################################################################################

h = 0.1

print("\t\t\t\t\t\t\t##################### TASK   № 3 #####################")
print("\t\t\t  h\t\t\t\t\t   Comput.value\t\t\t\t  Exact value\t\t\t\t\tError")
for i in range(MAX_ITER):
    h /= 2.0
    f_c = (6.0*f(x_0) - 32.0*f(x_0 + h) + 72.0*f(x_0 + 2.0*h) - 96.0*f(x_0 + 3.0*h) + 50.0*f(x_0 + 4.0*h))/(24.0*h)
    print("%25.20lf" % h, "%25.20lf" % f_c, "%25.20lf" % f_e, "%25.20lf" % (f_c - f_e))



#######################################################################################
## 4

h = 0.1
f_e = 2*math.sin(x_0)/math.cos(x_0)**3

print("\t\t\t\t\t\t\t##################### TASK   № 4 #####################")
print("\t\t\t  h\t\t\t\t\t   Comput.value\t\t\t\t  Exact value\t\t\t\t\tError")
for i in range(MAX_ITER):
    h /= 2.0
    f_c = (f(x_0 - h) - 2*f(x_0) + f(x_0+h))/(h**2)
    print("%25.20lf" % h, "%25.20lf" % f_c, "%25.20lf" % f_e, "%25.20lf" % (f_c - f_e))




#######################################################################################
## 5

h = 0.1
f_e = 2*math.sin(x_0)/math.cos(x_0)**3

print("\t\t\t\t\t\t\t##################### TASK   № 5 #####################")
print("\t\t\t  h\t\t\t\t\t   Comput.value\t\t\t\t  Exact value\t\t\t\t\tError")
for i in range(MAX_ITER):
    h /= 2.0
    f_c = (-f(x_0 - 2*h) + 16*f(x_0 - h) - 30*f(x_0) + 16*f(x_0 + h) - f(x_0 + 2*h))/(12*h**2)
    print("%25.20lf" % h, "%25.20lf" % f_c, "%25.20lf" % f_e, "%25.20lf" % (f_c - f_e))