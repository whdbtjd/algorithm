n = int(input())
cnt = 0
ans = 0

num = list(map(int,input().split()))

for i in range(n):
    cnt = 2
    if num[i] == 2 or num[i] == 3:
        ans += 1
        continue
    elif num[i] == 1:
        continue
    for j in range(2,int(num[i]**0.5) + 1):
        if num[i] % j == 0:
            cnt += 1
            break

    if cnt == 2:
        ans += 1


print(ans)

