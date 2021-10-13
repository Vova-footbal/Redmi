import math
a = int(input("Введите а="))
if a>0:
    print(math.sqrt(a))
    print(math.sqrt(a)*(-1))
elif a==0:
          print("x = 0")
else:
    print("EROR 404")
