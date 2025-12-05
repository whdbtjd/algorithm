t = int(input())


for i in range(t):
    word = input().rstrip()
    a = 0
    b = len(word) - 1
    cnt = 0
    while True:
        cnt += 1
        if a >= b:
            break
        elif word[a] != word[b]:
            break
        else:
            a += 1
            b -= 1
            continue

    if a >= b:
        print(1,cnt)
    else:
        print(0,cnt)
