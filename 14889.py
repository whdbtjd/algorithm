n = int(input())
ary = [list(map(int, input().split())) for _ in range(n)]

check = [False] * n
ans = []

def dfs(idx, cnt):
    if cnt == n // 2:
        start = []
        link = []

        for i in range(n):
            if check[i]:
                start.append(i)
            else:
                link.append(i)

        start_sum = 0
        link_sum = 0

        for i in range(len(start)):
            for j in range(i + 1, len(start)):
                start_sum += ary[start[i]][start[j]] + ary[start[j]][start[i]]
                link_sum += ary[link[i]][link[j]] + ary[link[j]][link[i]]

        ans.append(abs(start_sum - link_sum))
        return

    for i in range(idx, n):
        check[i] = True
        dfs(i + 1, cnt + 1)
        check[i] = False

dfs(0, 0)
print(min(ans))
