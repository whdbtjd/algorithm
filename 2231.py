n = int(input())

for i in range(1, n):
    digits_sum = sum(map(int, str(i)))
    if i + digits_sum == n:
        print(i)
        break
else:
    print(0)
