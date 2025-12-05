n = int(input())

a = 0
b = 1
ans = 0

for i in range(n - 1):
    ans = a + b
    a = b
    b = ans

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    print(ans)

