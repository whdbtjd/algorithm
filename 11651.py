n = int(input())

xy = [tuple(map(int,input().split())) for i in range(n)]
xy.sort(key = lambda x:(x[1],x[0]))

for x,y in xy:
    print(x,y)
