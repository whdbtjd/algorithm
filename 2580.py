import sys
input = sys.stdin.readline

ary = [list(map(int, input().split())) for _ in range(9)]
zero = []

for i in range(9):
    for j in range(9):
        if ary[i][j] == 0:
            zero.append((i, j))


def vaild(a, b, num):
    for i in range(9):
        if ary[a][i] == num:
            return False
        if ary[i][b] == num:
            return False

    start = (a // 3) * 3
    end   = (b // 3) * 3

    for i in range(start, start + 3):
        for j in range(end, end + 3):
            if ary[i][j] == num:
                return False

    return True


def dfs(idx):
    if idx == len(zero):
        for row in ary:
            print(*row)
        sys.exit(0)

    a, b = zero[idx]

    for num in range(1, 10):
        if vaild(a, b, num):
            ary[a][b] = num
            dfs(idx + 1)
            ary[a][b] = 0


dfs(0)
