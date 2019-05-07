print("Armstrong's:")

i=10
while i<=9999:
 if i < 100:
  p=2
 elif i < 1000:
  p=3
 else:
  p=4
 a=i // 1000
 b=(i // 100) % 10
 c=(i // 10) % 10
 d=i%10
 a1 = 1; b1 = 1; c1 = 1; d1 = 1
 j=0
 for j in range(p):
    a1=a1*a
    b1=b1*b
    c1=c1*c
    d1=d1*d

 if a1 + b1 + c1 + d1 == i:
  print(i)
 i+=1