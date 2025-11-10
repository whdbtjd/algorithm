n,m = map(int,input().split())
n_set = set()
m_ary = []
ans = 0

for i in range(n):
    n_set.add(input())

for i in range(m):
    m_ary.append(input())

for i in m_ary:
    if i in n_set:
        ans += 1

print(ans)
