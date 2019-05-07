import numpy as np

def next_gen(arr):
    # кому 2 і більше - народжують інших
    arr1 = arr + 1  # всі виростають на 1 рік

    to_death = np.arange(len(arr1))[arr1 >= 5] # живуть 5 років

    arr2 = np.delete(arr1, to_death)
    parents = arr2 >= 2  # статевозрілі(особи які вже здатні давати нащадків)

    n_p = len(arr2[parents])
    new_born = np.zeros(n_p)  # поставимо, що народилося стільки ж скільки було статевозрілих
    arr3 = np.append(arr2, new_born)
    return arr3

# список - містить вік кожної особи.
# припустимо, спочатку було дві новонароджені особи (вік = 0 < 2 => ще не здатні давати нащадків)
my_arr = np.array([0, 0])


for m in range(10):
    print('Рік:',m,'Статистика віку існуючих тварин:', my_arr)
    my_arr = next_gen(my_arr)

def get_gen_by_year(t):
    my_arr = np.array([0, 0])
    for m in range(t):
        my_arr = next_gen(my_arr)
    return my_arr

n = int(input('Введіть рік:'))
print('Кількість тварин станом на',n,'рік:',len(get_gen_by_year(n)))















# def get_gen_rec(t):
#     if t == 0:
#         return np.array([0, 0])
#     else:
#         return next_gen(get_gen_rec(t - 1))
# print(get_gen_rec(9))












# 1 ітерація = 1 рік

# M = {0: 0, 1: 1}
# def fib(n):
#     if n in M:
#         return M[n]
#     M[n] = fib(n - 1) + fib(n - 2)
#     return M[n]
#
# for i in range(25):
#     print(fib(i))

