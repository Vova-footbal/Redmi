money = int(input("summa="))
procent = int(input("procent kakoy="))
for m in range(6):
    money+=money*(procent/100)
    print(money)
