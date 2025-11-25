stack = []

while True:
    text = input().rstrip()
    if text == ".":
        break
    ans = True

    for i in text:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack:
                ans = False
                break
            elif stack[-1] == "[":
                ans = False
                break
            else:
                stack.pop()

        if i == "[":
            stack.append(i)
        elif i == "]":
            if not stack:
                ans = False
                break
            elif stack[-1] == "(":
                ans = False
                break
            else:
                stack.pop()

    if stack or not ans:
        print("no")
    else:
        print("yes")

    stack.clear()
