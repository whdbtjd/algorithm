n = int(input())

for _ in range(n):
    t = input().rstrip()
    stack = []
    ans = True

    for ch in t:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                ans = False
                break
            stack.pop()

    print("YES" if ans and not stack else "NO")
