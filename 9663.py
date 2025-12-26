n = int(input())

col = [False] * n
ary1 = [False] * (n * 2)
ary2 = [False] * (n * 2)

cnt = 0

def ans(raw):
    global cnt

    if raw == n:
        cnt += 1
        return


    for i in range(n):
        if col[i] or ary1[raw + i] or ary2[raw - i + n]:
            continue

        col[i] = True
        ary1[raw + i] = True
        ary2[raw - i + n] = True
        ans(raw + 1)

        col[i] = False
        ary1[raw + i] = False
        ary2[raw - i + n] = False

ans(0)
print(cnt)