a,b,v = map(int,input().split())

day = a - b

va = v - a

if va % day == 0:
    print(va // day + 1)
elif va % day != 0:
    print(va // day + 2)
