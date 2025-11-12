n,m = map(int,input().split())

set_n = set()
ans = set()

for i in range(n):
    set_n.add(input())

for i in range(m):
    name = input()
    if name in set_n:
        ans.add(name)

ans = list(ans)
ans.sort()

print(len(ans))

for i in ans:
     print(i)
