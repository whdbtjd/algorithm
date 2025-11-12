a,b = map(int,input().split())

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

cnt = 0

for i in set_a:
    if i in set_b:
        cnt += 1

print(len(set_a) - cnt + len(set_b) - cnt)
