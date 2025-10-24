ary = []

x_ans = 0
y_ans = 0

for i in range(3):
    x,y = map(int,input().split())
    ary.append((x,y))

if ary[0][0] == ary[1][0]:
    x_ans = ary[2][0]
elif ary[0][0] == ary[2][0]:
    x_ans = ary[1][0]
else:
    x_ans = ary[0][0]

if ary[0][1] == ary[1][1]:
    y_ans = ary[2][1]
elif ary[0][1] == ary[2][1]:
    y_ans = ary[1][1]
else:
    y_ans = ary[0][1]

print(x_ans,y_ans)








