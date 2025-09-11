x = int(input())
y = list(map(int, input()))[::-1]

ans = 0
for i, d in enumerate(y):
    print(x * d)
    ans += x * d * (10**i)

print(ans)
