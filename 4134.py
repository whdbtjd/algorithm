import sys
input = sys.stdin.readline

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    while True:
        if is_prime(n):
            print(n)
            break
        n += 1
