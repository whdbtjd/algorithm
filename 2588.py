x = int(input())
y = list(map(int,input()))[::-1]
ans = 0

for i,j in enumerate(y):
    print(x * j)
    ans += x * j * (10**i)

print(ans)

