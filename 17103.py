import sys
input = sys.stdin.readline

case = int(input())
ary = [True] * 1000001
ary[0] = ary[1] = False
i = 2

while i * i <= 1000000:
    if ary[i]:
       for j in range(i * i,1000001,i):
           ary[j] = False

    i += 1

for _ in range(case):
    n = int(input())
    ans = 0

    if n == 4:
        print(1)
        continue
    for i in range(3,n // 2 + 1,2):
        if ary[n - i] and ary[i]:
            ans += 1


    print(ans)



