import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
ans = 10**9

def dfs(idx, cnt):
    global ans

    if cnt == n // 2:
        start = []
        link = []

        for i in range(n):
            if visited[i]:
                start.append(i)
            else:
                link.append(i)

        a = b = 0
        for i in range(n // 2):
            for j in range(i + 1, n // 2):
                a += s[start[i]][start[j]] + s[start[j]][start[i]]
                b += s[link[i]][link[j]] + s[link[j]][link[i]]

        ans = min(ans, abs(a - b))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, cnt + 1)
            visited[i] = False

visited[0] = True
dfs(1, 1)

print(ans)
