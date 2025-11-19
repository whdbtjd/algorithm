import sys
input = sys.stdin.readline

m,n = map(int,input().split())
ary = [True] * (n + 1)
ary[0] = ary[1] = False

i = 2

while i * i <= n:
    for j in range(i * i, n + 1, i):
        if ary[j]:
            ary[j] = False
    i += 1

for i in range(m,n + 1):
    if ary[i]:
        print(i)
