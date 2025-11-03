n = input()
num = []

for i in n:
    num.append(i)
num.sort()
num.reverse()

for i in num:
    print(i,end="")
