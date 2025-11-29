from collections import deque

n = int(input())
ary = list(map(int, input().split()))
ary_q = list(map(int,input().split()))
c_n = int(input())
c_q = deque(map(int,input().split()))

q = deque()
ans = []

for i in range(n):
    if ary[i] == 0:
        q.append(ary_q[i])
c_length = len(c_q)

for i in range(c_length):
    q.appendleft(c_q.popleft())

for i in range(c_n):
    print(q.pop(),end = " ")









