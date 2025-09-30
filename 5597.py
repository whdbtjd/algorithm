ary = [0] * 30

for i in range(28):
    num = int(input())
    ary[num-1] = 1

ans = [x for x,y in enumerate(ary) if y == 0]
print(ans[0]+1)
print(ans[1]+1)

