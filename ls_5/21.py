import math
a=int(input("Vvedite chislo a="))
b=int(input("Vvedite chislo b="))
c=int(input("Vvedite chislo c="))
d = b**2-4*a*c
if d==0:
    print(x=-b/2*a)
elif d>0:
    x_1=-b+math.sqrt(d)/2*a
    x_2=-b-math.sqrt(d)/2*a
    print(x_1)
    print(x_2)
else:
    print("net x")
