num = int(input())
ary = list(map(int,input().split()))
ary.sort()

if num % 2 == 0:
    print((ary[0] * ary[num - 1]))
else:
    print(ary[num // 2] ** 2)



