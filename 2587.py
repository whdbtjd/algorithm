total_sum = 0
total_mid = []

for _ in range(5):
    n = int(input())
    total_sum += n
    total_mid.append(n)

total_mid.sort()

print(total_sum // 5)
print(total_mid[2])
