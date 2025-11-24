import sys
input = sys.stdin.readline

stack = []

n = int(input())
x = []

for _ in range(n):
    x = list(map(int,input().split()))

    if x[0] == 1:
        stack.append(x[1])
    elif x[0] == 2:
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif x[0] == 3:
        print(len(stack))
    elif x[0] == 4:
        if not stack:
          print(1)
        else:
          print(0)
    else:
        if not stack:
            print(-1)
        else:
            print(stack[-1])



