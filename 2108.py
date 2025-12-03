import sys

n = int(sys.stdin.readline())

nums = []
count = [0] * 8001

for _ in range(n):
    x = int(sys.stdin.readline())
    nums.append(x)
    count[x + 4000] += 1


print(round(sum(nums) / n))


nums.sort()
print(nums[n // 2])


max_freq = max(count)

modes = []
for i in range(8001):
    if count[i] == max_freq:
        modes.append(i - 4000)

if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])


print(nums[-1] - nums[0])
