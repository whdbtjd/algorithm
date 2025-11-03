n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

points.sort(key=lambda p: (p[0], p[1]))

for x, y in points:
    print(x, y)
