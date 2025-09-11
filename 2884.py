# divmod함수 쓰면 더 간단함
(h,m) = map(int,input().split())

total = 60 * h + m

if h == 0 and m < 45:
    h = 23
    m += 15
else:
    total -= 45
    h = total // 60
    m = total % 60

print(f"{h} {m}")


