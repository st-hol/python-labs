
def thomas_tridiagonal(a, b, c, d, N, C):
    for i in range(10):
        b[i] *= C

    print("\n\n ДАНО СЛАУ:")
    for i in range(10):
        if i == 0:
            print("%10.5f" % b[0], "\t", "%10.5f" % c[0], "\t\t\t\t\t= ", "%10.5f" % d[0])
        elif i != N - 1:
            print("%10.5f" % a[i], "\t", "%10.5f" % b[i], "\t", "%10.5f" % c[i], "\t= ", "%10.5f" % d[i])
        else:
            print("\t\t\t", "%10.5f" % a[i], "\t", "%10.5f" % b[i], "\t= ", "%10.5f" % d[i])

    for i in range(1, 10):
        b[i] = b[i] - a[i] * c[i - 1] / b[i - 1]
        d[i] = d[i] - a[i] * d[i - 1] / b[i - 1]
    print()

    # for i in range(10):
    #     if i == 0:
    #         print("%10.5f" % b[0], "\t", "%10.5f" % c[0], "\t\t\t\t\t= ", "%10.5f" % d[0])
    #     elif i != N - 1:
    #         print(" ", "\t\t\t", "%10.5f" % b[i], "\t", "%10.5f" % c[i], "\t= ", "%10.5f" % d[i])
    #     else:
    #         print("\t\t\t\t\t", " ", "\t\t", "%10.5f" % b[i], "\t= ", "%10.5f" % d[i])

    t = [0 for i in range(N)]
    i = N - 1
    while i >= 0:
        if i == N - 1:
            t[i] = d[i] / b[i]
        else:
            t[i] = (d[i] - c[i] * t[i + 1]) / b[i]
        i -= 1

    i = N - 1
    while i >= 0:
        if i == N - 1:
            t[i] = d[i] / b[i]
        else:
            t[i] = (d[i] - c[i] * t[i + 1]) / b[i]
        i -= 1

    return t


def print_answers(t, N, C):

    print("ОТВЕТЫ ПРИ С = ", C)
    for i in range(N):
        #print("x" + str(i + 1) + " = " + "%10.5f" % t[i])
        print("x" + str(i + 1) + " = " + "%20.16f" % t[i])
        # print("x" + str(i + 1) + " = " + "%e" % t[i])

    print("\n\n############################################################################################################################################################################################################################")


print("############################################################################################################################################################################################################################")
b = []; tmp_b = 3
for iter in range(10):
    b.append(tmp_b)
    tmp_b += 0.1
print("\n\nГЛАВНАЯ ДИАГОНАЛЬ  b = ", b)
b_ = b.copy()
b__ = b.copy()

a=[]; tmp_a = -0.4
a.append(0)
for iter in range(9):
    a.append(tmp_a)
    tmp_a -= 0.2
print("ПОДДИАГОНАЛЬ a = ", a)
a_ = a.copy()
a__ = a.copy()

c = []; tmp_c = 1.0
for iter in range(9):
    c.append(tmp_c)
    tmp_c += 0.1
c.append(0)
c_ = c.copy()
c__ = c.copy()

print("НАДДИАГОНАЛЬ c = ", c)
print("\n\n############################################################################################################################################################################################################################")



############################################################################################################################################################################################
C = 1.0
N = 10
d = [-1.30, -1.67, -2.08, -2.49, -2.90, -3.31, -3.72, -4.13, -4.54, -2.48]
print_answers(thomas_tridiagonal(a, b, c, d, N, C), N, C)
############################################################################################################################################################################################
C = 0.1
N = 10
d_ = [-0.490, -0.554, -0.640, -0.708, -0.758, -0.790, -0.804, -0.800, -0.778, 1.732]
print_answers(thomas_tridiagonal(a_, b_, c_, d_, N, C), N, C)
###########################################################################################################################################################################################################################################
C = 0.001
N = 10
d__ = [-0.40090, -0.43124, -0.48160, -0.51198, -0.52238, -0.51280, -0.48324, -0.43370, -0.36418, 2.19532]
print_answers(thomas_tridiagonal(a__, b__, c__, d__, N, C), N, C)
###########################################################################################################################################################################################################################################






