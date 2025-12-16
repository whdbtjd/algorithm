import math

n = int(input())

ary = [["*"] * n for _ in range(n)]


def tlqkf(n,x,y):
    if n >= 3:
        idx = n // 3

        for i in range(x + idx,x + 2*idx):
            for j in range(y + idx,y + 2*idx):
               ary[i][j] = " "

        for dx in range(0,n,idx):
           for dy in range(0,n,idx):
               tlqkf(idx,x + dx,y + dy)

tlqkf(n,0,0)

for i in ary:
    print("".join(i))

