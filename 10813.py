n,m = map(int,input().split())
ary = [i+1 for i in range(n)]

for _ in range(m):
    x,y = map(int,input().split())
    ary[x-1],ary[y-1] = ary[y-1],ary[x-1]

print(*ary)




