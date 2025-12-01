case = int(input())

for i in range(case):
    n,m = map(int,input().split())

    x = 1
    y = 1
    result = 1

    for i in range(1,n+1):
        result = result * (m - i + 1) // i

    print(result)
