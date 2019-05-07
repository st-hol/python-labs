"""
***********************************************************
***             Лабораторна робота №6                  ***
***          з курсу "Основи програмування              ***
***              на скриптових мовах"                   ***
***                   Варіант №7                       ***
***     Виконав:студент Головачук С.В.   Група ТІ-72    ***
***********************************************************
"""
import math
import numpy as np

#для розрахунку довжини вектора траекторії
def get_vector_len(cord1, cord2):
    return math.sqrt(cord1**2+cord2**2)

def get_vector(x1,y1, x2,y2):
    """ Щоб знайти вектор треба від координат кінця відняти коорд. початку """
    return (x2-x1, y2-y1)

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """
    Returns the angle in radians between vectors 'v1' and 'v2':
            >>> angle_between((1, 0), (0, 1))
            1.5707963267948966
            >>> angle_between((1, 0), (1, 0))
            0.0
            >>> angle_between((1, 0), (-1, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def dogNextCoord(x_cur, y_cur, x_prev, y_prev):
    # цей вектор використовується для обчислення кута між собакою та паралеллю ОХ
    vector_parallel_OX = (x_cur - x_prev, x_prev - x_cur)
#######
    vector_DOG_direction = (x_cur - x_prev, y_cur - y_prev)
    angle = angle_between(vector_parallel_OX, vector_DOG_direction)
    # if int(math.degrees(angle)) >= 90:
    #     angle = int(angle)
    #     angle -= math.radians(75)
    # if math.degrees(angle) <= 40:
    #     angle = int(angle)
    #     angle += math.radians(20)
    # if int(angle) >= np.pi/2:
    #     angle = int(angle)
    #     angle -= np.pi/2

    if math.degrees(angle) <= 0:
        #angle = int(angle)
        angle += math.radians(30)

    print(i, math.degrees(angle))

    dx = 10*math.cos(angle) #швидкість = 10
    dy = 10*math.sin(angle)

    #умова наздогнання собакою зайця -> починають рухатись паралельно
    if y_cur <= 10:
        return [x_cur + 10, y_cur]
    return [x_cur + dx, y_cur - dy]

def rabbitNextCoord(x,y=0):
    return [x+5, y] # швидкість=5


dog_cord = [[0, 50/math.sqrt(2)]]
rabbit_cord = [[50/math.sqrt(2), 0]]

# рахуємо перші дві координати, оскільки за умовою задачі нам даний першопочатковий кут і відстань
# надалі потрібно буде дві останні координати собаки у функцію для визначення кута її повороту
dog_cordX_next = dog_cord[0][0] + 10*math.cos(math.radians(45))
dog_cordY_next = dog_cord[0][1] - 10*math.sin(math.radians(45))
dog_cord.append([dog_cordX_next,dog_cordY_next])
rabbit_cord.append(rabbitNextCoord(rabbit_cord[0][0]))
# print(dog_cord)
# print(rabbit_cord)

# #першопочаткові параметри для першого виклику функції
# dog_prevX = dog_cord[0][0] # Х першої координати
# dog_prevY = dog_cord[0][1] # У першої координати
# dog_curX = dog_cord[1][0] # Х другої координати
# dog_curY = dog_cord[1][1] # У другої координати
#
# rabbit_curX = rabbit_cord[1][0] #перший
# rabbit_curY = rabbit_cord[1][1] #0

i = 0
# поставимо, що одна ітерація = одній секунді погоні
#while dog_cord[-1][1]>=5: #поки остання координата У більше нуля (тобто собака не вийшла на одну лінію з зайцем)
# while abs(dog_cord[i][0]-rabbit_cord[i][0]) > 10:

while i<13:
    dog_cord.append(dogNextCoord(dog_cord[i+1][0],dog_cord[i+1][1],dog_cord[i][0],dog_cord[i][1]))
    rabbit_cord.append(rabbitNextCoord(rabbit_cord[i+1][0], 0))
    i+=1

# print(dog_cord)
# print(rabbit_cord)
[print("Переміщення зайця:",i, rabbit_cord[i],"\t\t\tПереміщення собаки:",i, dog_cord[i]) for i in range(len(dog_cord))]

# вектор ( початок - точка початку рух, кінець - точка руху на 15 секунді)
traject = [dog_cord[-1][0] - dog_cord[0][0], dog_cord[-1][1] - dog_cord[0][1]]
print('Довжина вектора траекторії руху собаки за 15секунд:', get_vector_len(traject[0], traject[1]))
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)

import matplotlib.pyplot as plt

dog = np.array(dog_cord).ravel()
dogX = [dog[i] for i in range(len(dog)) if i%2==0]
dogY = [dog[i] for i in range(len(dog)) if i%2!=0]
plt.plot(dogX, dogY, "g")
# rabbit = np.array(rabbit_cord).ravel()
# rabbitX = [rabbit[i] for i in range(len(dog)) if i%2==0]
# rabbitY = [rabbit[i] for i in range(len(dog)) if i%2!=0]
# plt.plot(rabbitX, rabbitY, "r")
# print(dogX, dogY)

plt.show()


# print(angle_between((0,10/math.sqrt(2)),(10/math.sqrt(2),0)))
# print(math.degrees(angle_between((0,1),(1,0))))
# print(angle_between(get_vector(10/math.sqrt(2),0,0,10/math.sqrt(2)),get_vector(10/math.sqrt(2),0,0,0)))
