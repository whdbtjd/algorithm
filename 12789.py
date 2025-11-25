n = int(input())
order = list(map(int, input().split()))
stack = []
num = 1

for i in order:
    stack.append(i)

    while stack and stack[-1] == num:
        stack.pop()
        num += 1

if num == n + 1:
    print("Nice")
else:
    print("Sad")
