n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

print(round(sum(num)/n))

num.sort()

print(num[n//2])

cnt = [0] * 8001

for i in range(n):
    cnt[num[i] + 4000] += 1

cnt_max = max(cnt)
cnt_max_ary = []

for i in range(n):
    if cnt_max == cnt[i]:
        cnt_max_ary.append(i - 4000)

if len(cnt_max_ary) > 1:
    print(cnt_max_ary[1])
else:
    print(cnt_max_ary[0])


