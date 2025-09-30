n,m = map(int,input().split())
ary = [0] * n

for _ in range(m):
    i,j,k = map(int,input().split())
    for i in range(i,j+1):
        ary[i-1] = k

print(*ary)


