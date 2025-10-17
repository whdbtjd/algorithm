n,k = map(int,input().split())

ans = set()

for i in range(1,int(n**0.5)+1):
    if n % i == 0:
        ans.update([i,n // i])

ans = list(ans)
ans = sorted(ans)

if len(ans) < k:
    print(0)
else:
    print(ans[k-1])
