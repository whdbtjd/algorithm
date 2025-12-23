n, m = map(int, input().split())

ary = [False] * (n + 1)
ans = []

def dfs():

    if len(ans) == m:
        print(*ans)
        return


    for i in range(1,n+1):
        if not ary[i]:
           ary[i] = True
           ans.append(i)
           dfs()
           ans.pop()
           ary[i] = False

dfs()