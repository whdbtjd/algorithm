import math

n = int(input())

tree = [int(input()) for i in range(n)]
distance = []
ans = 0

for i in range(n-1):
    distance.append(tree[i+1] - tree[i])

g = distance[0]
for i in range(1, len(distance)):
    g = math.gcd(g, distance[i])

for i in range(len(distance)):
    ans += distance[i] // g - 1

print(ans)


