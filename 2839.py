n = int(input())

x = 0
y = 0

ans = 0

while True:
    if n % 5 == 0:
        ans += n // 5
        break
    elif n <= 0:
        ans = -1
        break
    else:
        ans += 1
        n -= 3



print(ans)
