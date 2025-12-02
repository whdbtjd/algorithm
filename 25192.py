n = int(input())
cnt = 0
user = set()

for _ in range(n):
    msg = input()

    if msg == "ENTER":
        user.clear()
        continue

    if msg not in user:
        cnt += 1

print(cnt)
