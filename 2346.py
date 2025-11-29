from collections import deque

n = int(input())
move = list(map(int, input().split()))
q = deque()

for i in range(n):
    q.append((i+1, move[i]))

ans = []

while q:
    idx, num = q.popleft()
    ans.append(idx)

    if not q:
        break

    if num > 0:
        q.rotate(-(num-1))
    else:
        q.rotate(-num)

print(*ans)
