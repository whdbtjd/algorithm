n = int(input())
ary = list(map(int,input().split()))
ops = list(map(int,input().split()))

ans = []

def dfs(a,b):
    if a == n:
        ans.append(b)
        return

    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1
            if i == 0:
                dfs(a+1,b + ary[a])
            elif i == 1:
                dfs(a+1,b - ary[a])
            elif i == 2:
                dfs(a+1, b * ary[a])
            elif i == 3:
                num = abs(b) // abs(ary[a])
                if ary[a] * b < 0:
                    num = -num
                dfs(a+1,num)
            ops[i] += 1

dfs(1,ary[0])
print(max(ans))
print(min(ans))

