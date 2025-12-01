n = int(input())
cnt = 1
ans = 1

while n + 1 != cnt:
    ans = ans * cnt
    cnt += 1

if n == 0 :
   print(1)
else:
   print(ans)