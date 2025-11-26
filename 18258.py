from collections import deque
import sys
input = sys.stdin.readline

q = deque()
n = int(input())

for _ in range(n):
    order = input().split()

    if order[0] == "push":
        q.appendleft(order[1])
    elif order[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.pop())
    elif order[0] == "size":
        print(len(q))
    elif order[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif order[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[-1])
    elif order[0] == "back":
        if not q:
            print(-1)
        else:
            print(q[0])
