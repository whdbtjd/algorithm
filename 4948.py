import sys
input = sys.stdin.readline
n = 1

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    i = 2
    ary = [True] * ((2 * n) + 1)
    ary[0] = ary[1] = False

    while i * i <= 2 * n:
       for j in range(i * i,2 * n + 1,i):
           if ary[j]:
               ary[j] = False
       i += 1

    for i in range(n + 1,2 * n + 1):
        if ary[i]:
            cnt += 1
    print(cnt)

