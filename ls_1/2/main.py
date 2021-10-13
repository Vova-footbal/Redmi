import math
x=float(input("x="))
y=float(input("y="))
b=float(input("b="))
p=(x+y+b)/2
s=math.sqrt(p*(p-x)*(p-y)*(p-b))
print(s)
input()
