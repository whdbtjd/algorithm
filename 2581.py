m = int(input())
n = int(input())

ans = set()

for i in range(m,n + 1):
   if i == 1:
      continue
   for j in range(2,int(i**0.5) + 1):
        if i % j == 0:
            break
   else:
       ans.add(i)

if len(ans) < 1:
    print(-1)
else:
   print(sum(ans))
   print(min(ans))
