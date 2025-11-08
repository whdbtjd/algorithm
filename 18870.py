n = int(input())
ary = list(map(int, input().split()))

num_ary = sorted(set(ary))

num_dict = {}
idx = 0
for num in num_ary:
    num_dict[num] = idx
    idx += 1

for i in ary:
    print(num_dict[i], end=" ")
