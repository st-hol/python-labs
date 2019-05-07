"""
***********************************************************
***             Лабораторна робота №4                  ***
***          з курсу "Основи програмування              ***
***              на скриптових мовах"                   ***
***                   Варіант №7                       ***
***     Виконав:студент Головачук С.В.   Група ТІ-72    ***
***********************************************************
"""
import numpy as np
import math
import itertools

def isSquare(n):
    """
        Determines whether a number is square of another number.
        :param n:integer
        :return: boolean
        :Tests:
        >>> isSquare(16)
        True
        >>> isSquare(15)
        False
        >>> isSquare(3) #actually it's false, but i did mistake specially to test it.
        True
    """
    if (n > 0):
        if (math.sqrt(n) - int(math.sqrt(n))):
            return False
        return True
    return False

def isPrime(n):
    """
        Determines whether a number is simple by the Wilson's theorem.
        :param n:integer
        :return: boolean
        :Tests:
        >>> isPrime(7)
        True
        >>> isPrime(12)
        False
        >>> isPrime(10) #actually it's false, but i did mistake specially to test it.
        True
    """
    if(n>0):
        if (math.factorial(n-1)+1) % n!=0:
            return False
        return True
    return False
def isSquareFive(n):
    """
    Determines whether a number is square of five.
           :param n:integer
           :return: boolean
           :Tests:
           >>> isSquareFive(25)
           True
           >>> isSquareFive(26)
           False
           >>> isSquareFive(3) #actually it's false, but i did mistake specially to test it.
           True
    """
    if(n>0):
        while n%5==0:
            n/=5
            if n==1:
                return True
            elif n<5:
                return False
        if (n % 5):
            return False
    return False

N=15
choice=input('If you want to enter manually, enter "1"\nIf you want to generate array, enter any other key:')
if choice=='1':
    arr = list(map(int, input('Enter element separated with spaces:').split()))
else:
    arr = np.random.randint(10, size=N)
    print(arr)
# arr=[-11, 13, 625, 100, 369, 141, 5,25,125,25,25, 625,1, 7, -13, 17, 23, 625,25]
#-11 13 625 100 369 141  5 25 125 25 25 625 1 7 -13 17 23 625 25
#13 625 100 144  5 25 125 25 625 7 17 23 625 25
squaresSequence = [isSquare(item) for item in arr ]#if item>0
groups = itertools.groupby(squaresSequence)
# for k, g in itertools.groupby(squaresSequence):
#    print(str(k) + str(list(g)))
occuranceFrequency = [len(list(g)) for k, g in groups if k]

if occuranceFrequency:
    result = max(occuranceFrequency)
    print('The greatest length of serial occurrences of <Full Squares>:', result)

fivesSequence = [isSquareFive(item) for item in arr]
groups = itertools.groupby(fivesSequence)
# for k, g in itertools.groupby(fivesSequence):
#     print(str(k) + str(list(g)))
occuranceFrequency = [len(list(g)) for k, g in groups if k]

if occuranceFrequency:
    result = max(occuranceFrequency)
    print('The greatest length of serial occurrences of <Five-Squares>:', result)

primeSequence = [isPrime(item) for item in arr]#if item>0
groups = itertools.groupby(primeSequence)
# for k, g in itertools.groupby(primeSequence):
#    print(str(k) + str(list(g)))
occuranceFrequency = [len(list(g)) for k, g in groups if k]

if occuranceFrequency:
    result = max(occuranceFrequency)
    print('The greatest length of serial occurrences of <Prime Numbers>:', result)

# print([k for k, g in itertools.groupby('AAAABBBCCDAABBB')] )
# print([list(g) for k, g in itertools.groupby('AAAABBBCCDAABBB')])


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)



