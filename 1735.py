import math

a,b = map(int,input().split())
c,d = map(int,input().split())

y = (b * d) // math.gcd(b,d)
x = a * (y // b) + c * (y // d)

g = math.gcd(x, y)

print(x // g, y // g)
