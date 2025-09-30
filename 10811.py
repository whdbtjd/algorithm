n,m = map(int,input().split())

ary = [i+1 for i in range(n)]

for _ in range(m):
    i,j = map(int,input().split())
    ary[i-1:j] = ary[i-1:j][::-1]

print(*ary)
