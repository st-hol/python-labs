#http://www.cat-in-web.ru/notebook/rasstoyanie-ot-tochki-do-otrezka/

import math
 #Расстояниемеждуточками(x1, y1)и(x2, y2)
def GetDistanceBetweenPoints(x1,y1,x2,y2):
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

 #Является ли угол, противолежащий стороне oppositeLine тупым
def IsObtuseAngle(oppositeLine,a,b):
    cos = (a * a + b * b - oppositeLine * oppositeLine) / (2 * a * b)
    return cos < 0

# Расстояние от точки (x, y) до отрезка AB с координатами A(ax, ay), B(bx, by)
def GetDistanceToSegment(ax,ay,bx,by,x,y):
    """
          :Tests:
          >>> abs(GetDistanceToSegment(0,0,1,1,0,1) - 1*math.sqrt(2)/2) < 1e-3
          True
       """
    if ((ax == x and ay == y) or (bx == x and by == y)):
        return 0
    AB = GetDistanceBetweenPoints(ax, ay, bx, by)
    AC = GetDistanceBetweenPoints(ax, ay, x, y)
    if (AB == 0):
        return AC
    BC = GetDistanceBetweenPoints(bx, by, x, y)
    if IsObtuseAngle(AC, BC, AB):
        return BC
    if IsObtuseAngle(BC, AC, AB):
        return AC
    p = (AC + BC + AB) / 2
    return 2 * math.sqrt(p * (p - AB) * (p - BC) * (p - AC)) / AB

# a)точки квадрата k1,k2,k3,k4
k1_x = -0.5; k1_y = -0.5
k2_x = -0.5; k2_y = 0.5
k3_x = 0.5; k3_y = 0.5
k4_x = 0.5; k4_y = -0.5

# ввод точки
x = float(input("x:"))
y = float(input("y:"))

# поиск расстояния от Точки до каждой стороны
distances_a=[]
distances_a.append( GetDistanceToSegment(k1_x,k1_y, k2_x, k2_y, x, y) )
distances_a.append( GetDistanceToSegment(k2_x,k2_y, k3_x, k3_y, x, y) )
distances_a.append( GetDistanceToSegment(k3_x,k3_y, k4_x, k4_y, x, y) )
distances_a.append( GetDistanceToSegment(k4_x,k4_y, k1_x, k1_y, x, y) )

#print(distances_a)
print("a)", min(distances_a))





# б)точки квадрата k1,k2,k3,k4
k1_x = 0; k1_y = 0
k2_x = 0; k2_y = 1
k3_x = 1; k3_y = 1
k4_x = 1; k4_y = 0

# поиск расстояния от Точки до каждой стороны
distances_b=[]
distances_b.append( GetDistanceToSegment(k1_x,k1_y, k2_x, k2_y, x, y) )
distances_b.append( GetDistanceToSegment(k2_x,k2_y, k3_x, k3_y, x, y) )
distances_b.append( GetDistanceToSegment(k3_x,k3_y, k4_x, k4_y, x, y) )
distances_b.append( GetDistanceToSegment(k4_x,k4_y, k1_x, k1_y, x, y) )

#print(distances)
print("б)", min(distances_b))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)





# # double L=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
# # double PR=(x-x1)*(x2-x1)+(y-y1)*(y2-y1);
# # bool res=true;
# # double cf=PR/L;
# # if(cf<0){ cf=0; res=false; }
# # if(cf>1){ cf=1; res=false; }
# # double xres=x1+cf*(x2-x1);
# # double yres=y1+cf*(y2-y1);
#
# # Есть точка A(x,y).
# # Есть отрезок с началом B(x1,y1) и концом C(x2,y2).
#
# #функция делает отрезок из координат точек начала и координат точек конца и ищет ближайшую точку от заданой(х у)
# #а потом считает длинну перпендикуляра
# def closestPoint(x1,y1,x2,y2,x,y):
#     L=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
#     PR=(x-x1)*(x2-x1)+(y-y1)*(y2-y1)
#     # res=True
#     # cf=PR/L
#     # if(cf<0):
#     #     cf=0
#     #     res=False
#     # if(cf>1):
#     #     cf=1
#     #     res=False
#     # xres=x1+cf*(x2-x1)
#     # yres=y1+cf*(y2-y1)
#
#



#https://ru.stackoverflow.com/questions/721414/%D0%95%D0%B2%D0%BA%D0%BB%D0%B8%D0%B4%D0%BE%D0%B2%D0%B0-%D0%B3%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%8F-%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B5-%D0%BE%D1%82-%D1%82%D0%BE%D1%87%D0%BA%D0%B8-%D0%B4%D0%BE-%D0%BE%D1%82%D1%80%D0%B5%D0%B7%D0%BA%D0%B0
