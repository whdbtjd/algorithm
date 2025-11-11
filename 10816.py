n = int(input())
list_n = list(map(int,input().split()))

m = int(input())
list_m = list(map(int,input().split()))

num = dict.fromkeys(list_m,0)
set_m = set(list_m)

for i in list_n:
    if i in set_m:
        num[i] += 1

for i in list_m:
    print(num[i], end=" ")



