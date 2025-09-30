ary = []
for i in range(9):
    ary.append(int(input()))

print(max(ary))
print(ary.index(max(ary))+1)
