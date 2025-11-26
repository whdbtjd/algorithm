from collections import deque

q = deque()
ary = []
n,k = map(int,input().split())

for i in range(1,n + 1):
    q.append(i)

while len(q) > 0:
    num = 1
    while num != k:
        q.append(q.popleft())
        num += 1
    ary.append(q.popleft())

print("<" + ", ".join(map(str, ary)) + ">")

